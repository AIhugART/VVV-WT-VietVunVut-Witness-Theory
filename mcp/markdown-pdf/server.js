// Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

import { execFile } from "node:child_process";
import { existsSync, realpathSync, statSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const execFileAsync = promisify(execFile);
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, "..", "..");
const repoRealPath = realpathSync.native(repoRoot);
const exportScriptPath = path.join(repoRoot, "scripts", "export-md-to-pdf.ps1");

function isInsideRepo(candidatePath) {
  const relativePath = path.relative(repoRealPath, candidatePath);
  return relativePath === "" || (!relativePath.startsWith("..") && !path.isAbsolute(relativePath));
}

function assertInsideRepo(candidatePath, rawPath) {
  if (!isInsideRepo(candidatePath)) {
    throw new Error(`Path must stay inside repository: ${rawPath}`);
  }
}

function resolveRepoPath(rawPath) {
  const resolvedPath = path.isAbsolute(rawPath)
    ? path.resolve(rawPath)
    : path.resolve(repoRoot, rawPath);
  const relativePath = path.relative(repoRoot, resolvedPath);

  if (relativePath.startsWith("..") || path.isAbsolute(relativePath)) {
    throw new Error(`Path must stay inside repository: ${rawPath}`);
  }

  return resolvedPath;
}

function resolveExistingParent(targetPath) {
  let parentPath = path.dirname(targetPath);

  while (!existsSync(parentPath)) {
    const nextParent = path.dirname(parentPath);
    if (nextParent === parentPath) {
      throw new Error(`No existing parent directory found for output_path: ${targetPath}`);
    }
    parentPath = nextParent;
  }

  if (!statSync(parentPath).isDirectory()) {
    throw new Error(`Output parent path is not a directory: ${parentPath}`);
  }

  return parentPath;
}

function assertOutputTargetInsideRepo(outputFullPath) {
  const outputParentPath = resolveExistingParent(outputFullPath);
  assertInsideRepo(realpathSync.native(outputParentPath), outputFullPath);

  if (existsSync(outputFullPath)) {
    assertInsideRepo(realpathSync.native(outputFullPath), outputFullPath);
  }
}

function buildChildPath() {
  const pathEntries = [];

  if (process.env.LOCALAPPDATA) {
    pathEntries.push(path.join(process.env.LOCALAPPDATA, "Pandoc"));
    pathEntries.push(path.join(process.env.LOCALAPPDATA, "Programs", "MiKTeX", "miktex", "bin", "x64"));
  }

  pathEntries.push(process.env.Path ?? process.env.PATH ?? "");
  return pathEntries.filter(Boolean).join(path.delimiter);
}

function validateExportPaths(inputPath, outputPath) {
  const inputFullPath = resolveRepoPath(inputPath);
  const outputFullPath = resolveRepoPath(outputPath);

  if (path.extname(inputFullPath).toLowerCase() !== ".md") {
    throw new Error("input_path must point to a Markdown .md file.");
  }

  if (path.extname(outputFullPath).toLowerCase() !== ".pdf") {
    throw new Error("output_path must point to a PDF .pdf file.");
  }

  if (!existsSync(inputFullPath)) {
    throw new Error(`Input Markdown file not found: ${inputFullPath}`);
  }

  assertInsideRepo(realpathSync.native(inputFullPath), inputPath);
  assertOutputTargetInsideRepo(outputFullPath);

  return { inputFullPath, outputFullPath };
}

const server = new McpServer({
  name: "vvv-qmrf-markdown-pdf",
  version: "0.1.0",
});

server.registerTool(
  "export_markdown_to_pdf",
  {
    description: "Exports a repository Markdown file to PDF through the local Pandoc PowerShell pipeline.",
    inputSchema: {
      input_path: z.string().describe("Markdown file path inside the repository, e.g. history.md"),
      output_path: z.string().describe("PDF output path inside the repository, e.g. exports/history.pdf"),
      engine: z.enum(["latex", "weasyprint"]).default("latex").describe("PDF engine to use"),
    },
  },
  async ({ input_path, output_path, engine }) => {
    try {
      if (!existsSync(exportScriptPath)) {
        throw new Error(`Export script not found: ${exportScriptPath}`);
      }

      const { inputFullPath, outputFullPath } = validateExportPaths(input_path, output_path);
      const childPath = buildChildPath();
      const { stdout, stderr } = await execFileAsync(
        "powershell.exe",
        [
          "-NoLogo",
          "-NoProfile",
          "-NonInteractive",
          "-File",
          exportScriptPath,
          inputFullPath,
          outputFullPath,
          "-Engine",
          engine,
        ],
        {
          cwd: repoRoot,
          shell: false,
          timeout: 600_000,
          maxBuffer: 10 * 1024 * 1024,
          windowsHide: true,
          env: {
            ...process.env,
            Path: childPath,
            PATH: childPath,
          },
        },
      );

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(
              {
                success: true,
                pdf_path: outputFullPath,
                stdout: stdout.trim(),
                stderr: stderr.trim(),
              },
              null,
              2,
            ),
          },
        ],
      };
    } catch (error) {
      return {
        isError: true,
        content: [
          {
            type: "text",
            text: JSON.stringify(
              {
                success: false,
                error: error instanceof Error ? error.message : String(error),
                stdout: typeof error?.stdout === "string" ? error.stdout.trim() : "",
                stderr: typeof error?.stderr === "string" ? error.stderr.trim() : "",
              },
              null,
              2,
            ),
          },
        ],
      };
    }
  },
);

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("vvv-qmrf-markdown-pdf MCP server running on stdio");
