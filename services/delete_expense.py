import argparse
import os
from pathlib import Path
import sys
import json


class DeleteExpense:
    def __init__(self):
        self.id = 0
        self.DB_FILE = Path(__file__).resolve().parent.parent / "database" / "expenses.jsonl"

    def delete_expense(self):
        self.id = input("Enter the expense id you want to remove:")
        try:
            if self.id is None or not self.id:
                raise ValueError("Need to be a valid value")

            try:
                self.id = int(self.id)

            except ValueError:
                raise ValueError("Entered ID should be an integer")

        except ValueError as e:
            print(f"Cannot use the given id: {e}")
            sys.exit(1)

        try:
            temp_file = Path(__file__).resolve().parent.parent / "database" / "temp_expenses.jsonl"
            with open(self.DB_FILE, "r", encoding="utf-8") as file, open(temp_file, "w", encoding="utf-8") as temp:
                for line in file:
                    if not line.strip():
                        continue
                    record = json.loads(line)

                    if record.get("id") != self.id:
                        temp.write(line)

            os.replace(temp_file, self.DB_FILE)

        except (FileNotFoundError, json.JSONDecodeError):
            raise FileNotFoundError("File was not found")

