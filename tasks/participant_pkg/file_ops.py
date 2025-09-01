import csv
from pathlib import Path

workspace = Path("workspace")
workspace.mkdir(exist_ok=True)
csv_file = workspace / "contact.csv"

fieldnames = ["Name", "Age","Phone Number", "Track"]

def save_participant(csv_file, participant_dict):
    if type(participant_dict) == dict:
     participant_dict=[participant_dict]
    if csv_file.exist():
        with open(csv_file, "a",newline="", encoding="utf-8") as f:
            write = csv.DictWriter(f, fieldnames=fieldnames )
            write.writeheader()
            write.writerows(participant_dict)
    #    print("Student data written to CSV file!")
    else:
       print(f"{csv_file}, doesn\'t existn Creating it now")
       with open(csv_file, "w", newline="", encoding="utf-8") as f:
           write = csv.DictWriter(f, fieldnames=fieldnames)
           write.writeheader()
           write.writerows(participant_dict)
           

def load_participant(path):
    if path.exist():
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row_number, row in enumerate(reader):
                if row_number == 0: #header row
                    print(f"Headers:{"|".join(row)}")
                    print("-" * 45)
                else:
                    name,age,phone,track = row
                    print(f"{name} {age} {phone} {track}")
    else:
        print("No Participant found yet")

