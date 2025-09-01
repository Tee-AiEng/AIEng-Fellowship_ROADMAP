student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subject": "Chemistry",
    "is_full_time": True
}
from pathlib import Path
import csv
workspace = Path("workspace")
workspace.mkdir(exist_ok=True)
csv_file = workspace / "details.csv"

fieldname = ["name","age","department", "subject","is_full_time"]

with open(csv_file,"w",newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow(student)