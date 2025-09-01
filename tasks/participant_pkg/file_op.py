import csv
from pathlib import Path

workspace = Path("workspace")
workspace.mkdir(exist_ok=True)
csv_file = workspace / "contact.csv"
