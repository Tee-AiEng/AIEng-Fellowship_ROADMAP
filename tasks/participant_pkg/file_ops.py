import csv
from pathlib import Path

workspace = Path("participant_pkg")
csv_file = workspace / "contact.csv"

def save_participant(path, participant_dict):
    header = list(participant_dict.keys())
    rows =  list(participant_dict.values())
    if path.exist():
        with open(path, "a",newline="", encoding="ut-8") as f:
            write = csv.DictWriter(f, fieldnames=header )
            write.writeheader()
            write.writerow(rows)
    print("Student data written to CSV file!")

def load_participant(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row_number, row in enumerate(reader):
            if row_number == 0: #header row
                print(f"Headers:{"|".join(row)}")
                print("-" * 45)
            else:
                name,age,phone,track = row
                

