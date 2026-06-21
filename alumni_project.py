from __future__ import annotations

from dataclasses import dataclass, asdict
import json
from pathlib import Path


DATA_FILE = Path("alumni_data.json")


@dataclass
class Alumni:
    name: str
    graduation_year: int
    department: str
    email: str
    phone: str

    def to_dict(self):
        return asdict(self)


class AlumniManager:
    def __init__(self, file_path: Path = DATA_FILE):
        self.file_path = file_path
        self.alumni: list[Alumni] = []
        self.load_data()

    def load_data(self):
        if not self.file_path.exists():
            return

        try:
            raw_data = json.loads(self.file_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"Warning: {self.file_path} is corrupted. Starting fresh.")
            return

        self.alumni = [
            Alumni(
                name=item["name"],
                graduation_year=int(item["graduation_year"]),
                department=item["department"],
                email=item["email"],
                phone=item["phone"],
            )
            for item in raw_data
        ]

    def save_data(self):
        self.file_path.write_text(
            json.dumps([alumni.to_dict() for alumni in self.alumni], indent=2),
            encoding="utf-8",
        )

    def add_alumni(self, alumni: Alumni):
        self.alumni.append(alumni)
        self.save_data()

    def list_alumni(self):
        return self.alumni

    def search_by_name(self, name: str):
        query = name.strip().lower()
        return [alumni for alumni in self.alumni if query in alumni.name.lower()]

    def delete_alumni(self, name: str):
        before = len(self.alumni)
        self.alumni = [alumni for alumni in self.alumni if alumni.name.lower() != name.lower()]
        if len(self.alumni) != before:
            self.save_data()
            return True
        return False


def display_alumni(alumni_list: list[Alumni]):
    if not alumni_list:
        print("No alumni found.")
        return

    for idx, alumni in enumerate(alumni_list, start=1):
        print(f"{idx}. {alumni.name} | Batch: {alumni.graduation_year} | {alumni.department}")
        print(f"   Email: {alumni.email} | Phone: {alumni.phone}")


def add_alumni_flow(manager: AlumniManager):
    print("\nAdd Alumni")
    name = input("Name: ").strip()
    graduation_year = int(input("Graduation Year: ").strip())
    department = input("Department: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()

    manager.add_alumni(
        Alumni(
            name=name,
            graduation_year=graduation_year,
            department=department,
            email=email,
            phone=phone,
        )
    )
    print("Alumni added successfully.")


def main():
    manager = AlumniManager()

    while True:
        print("\n=== Alumni Project ===")
        print("1. Add Alumni")
        print("2. View All Alumni")
        print("3. Search Alumni by Name")
        print("4. Delete Alumni")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_alumni_flow(manager)
        elif choice == "2":
            print("\nAll Alumni")
            display_alumni(manager.list_alumni())
        elif choice == "3":
            name = input("Search by name: ").strip()
            display_alumni(manager.search_by_name(name))
        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            if manager.delete_alumni(name):
                print("Alumni deleted successfully.")
            else:
                print("Alumni not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
