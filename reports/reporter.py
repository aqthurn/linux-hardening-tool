import json
from datetime import datetime
import os
os.makedirs("reports", exist_ok=True)

def save_json(results):
    data = {"scan_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "results": results,
            "summary": {
                "total_pass": len([r for r in results if r["status"] == "PASS"]),
                "total_fail": len([r for r in results if r["status"] == "FAIL"]),
                "total_error": len([r for r in results if r["status"] == "ERROR"])
            },
            }
    with open("reports/results.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
       