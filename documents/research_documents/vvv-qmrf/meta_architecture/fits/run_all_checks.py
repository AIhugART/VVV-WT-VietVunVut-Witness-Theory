"""Run all PP-4 sanity checks."""
import sys
sys.path.insert(0, ".")

from utils.qm_standard import run_sanity_checks as qm_checks
from utils.k9a_predictor import run_sanity_checks as k9a_checks
from utils.k9e_predictor import run_sanity_checks as k9e_checks

all_results = {}
all_results.update(qm_checks())
all_results.update(k9a_checks())
all_results.update(k9e_checks())

print("=" * 65)
print("PP-4 SANITY CHECK REPORT")
print("=" * 65)

all_pass = True
for cid in sorted(all_results.keys()):
    info = all_results[cid]
    status = info["status"]
    if status != "PASS":
        all_pass = False
    desc = info["description"]
    desc = desc.replace("→", "->").replace("√", "sqrt").replace("β", "beta").replace("≠", "!=").replace("Σ", "Sum").replace("δ", "delta")
    desc = desc.encode("ascii", errors="replace").decode("ascii")
    print(f"  CHECK {cid}: {status:4s}  {desc}")
    if status == "FAIL":
        print(f"           Expected: {info['expected']}")
        print(f"           Computed: {info['computed']}")

print()
if all_pass:
    n = len(all_results)
    print(f"  All {n} sanity checks PASS.")
    print("  Python infrastructure is ready for Phase 10.")
else:
    fails = [k for k, v in all_results.items() if v["status"] == "FAIL"]
    print(f"  {len(fails)} checks FAIL: {', '.join(fails)}")
    print("  Phase 10 cannot begin until resolved.")
