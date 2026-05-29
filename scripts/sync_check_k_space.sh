#!/usr/bin/env bash
# sync_check_k_space.sh — Verify K_Space_Axiomatization.md peer copies are in sync
# PEER-SYNC rule (2026-05-24): both files must match structurally.
# Run before committing changes to either copy.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CANONICAL="$REPO_ROOT/documents/research_documents/meta_architecture/K_Space_Axiomatization.md"
CLASS_C="$REPO_ROOT/documents/research_documents/project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo "=== K_Space_Axiomatization.md PEER-SYNC CHECK ==="
echo "Canonical:  $CANONICAL"
echo "Class C:    $CLASS_C"
echo ""

# Check files exist
for f in "$CANONICAL" "$CLASS_C"; do
    if [ ! -f "$f" ]; then
        echo -e "${RED}MISSING: $f${NC}"
        exit 1
    fi
done

# Check for K5_prospective
echo "--- K5_prospective ---"
if grep -q 'K5_prospective' "$CANONICAL"; then
    echo -e "${GREEN}Canonical: K5_prospective PRESENT${NC}"
else
    echo -e "${RED}Canonical: K5_prospective MISSING${NC}"
fi
if grep -q 'K5_prospective' "$CLASS_C"; then
    echo -e "${GREEN}Class C:   K5_prospective PRESENT${NC}"
else
    echo -e "${RED}Class C:   K5_prospective MISSING${NC}"
fi

# Check for T8
echo ""
echo "--- T8 Bridge Theorem ---"
if grep -q '### T8 ' "$CANONICAL"; then
    echo -e "${GREEN}Canonical: T8 PRESENT${NC}"
else
    echo -e "${RED}Canonical: T8 MISSING${NC}"
fi
if grep -q '### T8 ' "$CLASS_C"; then
    echo -e "${GREEN}Class C:   T8 PRESENT${NC}"
else
    echo -e "${RED}Class C:   T8 MISSING${NC}"
fi

# Check for T8-H1/H3/H4
echo ""
echo "--- T8 substructures ---"
for sub in "T8-H1" "T8-H3" "T8-H4"; do
    c1=$(grep -c "$sub" "$CANONICAL" || true)
    c2=$(grep -c "$sub" "$CLASS_C" || true)
    if [ "$c1" -gt 0 ] && [ "$c2" -gt 0 ]; then
        echo -e "${GREEN}$sub: both copies present${NC}"
    elif [ "$c1" -gt 0 ]; then
        echo -e "${RED}$sub: canonical only${NC}"
    elif [ "$c2" -gt 0 ]; then
        echo -e "${RED}$sub: Class C only${NC}"
    else
        echo -e "${RED}$sub: MISSING from both${NC}"
    fi
done

# Check PEER-SYNC headers
echo ""
echo "--- PEER-SYNC headers ---"
if grep -q 'PEER-SYNC' "$CANONICAL"; then
    echo -e "${GREEN}Canonical: PEER-SYNC header PRESENT${NC}"
else
    echo -e "${YELLOW}Canonical: PEER-SYNC header MISSING${NC}"
fi
if grep -q 'PEER-SYNC' "$CLASS_C"; then
    echo -e "${GREEN}Class C:   PEER-SYNC header PRESENT${NC}"
else
    echo -e "${YELLOW}Class C:   PEER-SYNC header MISSING${NC}"
fi

# Line count comparison
echo ""
echo "--- Size comparison ---"
canonical_lines=$(wc -l < "$CANONICAL")
classc_lines=$(wc -l < "$CLASS_C")
diff_lines=$((canonical_lines - classc_lines))
echo "Canonical: $canonical_lines lines"
echo "Class C:   $classc_lines lines"
echo "Delta:     $diff_lines lines"
if [ "${diff_lines#-}" -gt 50 ]; then
    echo -e "${RED}WARNING: Line delta > 50 — likely drift. Review before commit.${NC}"
elif [ "${diff_lines#-}" -gt 10 ]; then
    echo -e "${YELLOW}CAUTION: Line delta > 10 — minor drift possible.${NC}"
else
    echo -e "${GREEN}Line counts within 10 — likely in sync.${NC}"
fi

# Final verdict
echo ""
echo "=== VERDICT ==="
issues=0
grep -q 'K5_prospective' "$CANONICAL" || issues=$((issues+1))
grep -q 'K5_prospective' "$CLASS_C" || issues=$((issues+1))
grep -q '### T8 ' "$CANONICAL" || issues=$((issues+1))
grep -q '### T8 ' "$CLASS_C" || issues=$((issues+1))
grep -q 'PEER-SYNC' "$CANONICAL" || issues=$((issues+1))
grep -q 'PEER-SYNC' "$CLASS_C" || issues=$((issues+1))

if [ "$issues" -eq 0 ]; then
    echo -e "${GREEN}PASS: Both copies in sync. Safe to commit.${NC}"
    exit 0
else
    echo -e "${RED}FAIL: $issues sync issue(s) detected. Sync before commit.${NC}"
    echo "Run: git diff --stat -- $CANONICAL $CLASS_C"
    exit 1
fi
