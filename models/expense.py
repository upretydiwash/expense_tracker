# track expenses, get user input and save the data into json file as a local database
import json
import sys
from datetime import date
import argparse
from pathlib import Path
from prettytable import PrettyTable


class Expense:

    def __init__(self):
        self.category = ""
        self.amount = 0
        self.description = ""
        self.date = ""
        self.DB_FILE = Path(__file__).resolve().parent.parent / "database" / "expenses.jsonl"

    def get_expense_info(self):
        print("Get the details of the expense: ")
        self.category = input("Category: ")
        self.amount = input("Amount: ")
        self.description = input("Description: ")
        self.date = input("Date: ")

        try:

            validate_fields = {
                "category": self.category,
                "amount": self.amount,
                "description": self.description,
                "date": self.date
            }
            for field, value in validate_fields.items():
                if value is None or not value.strip():
                    raise ValueError(f"The required field {field} is missing")

            # convert user input to integer
            try:
                self.amount = int(self.amount)

            except ValueError as e:
                raise ValueError("Amount must be an integer value")

            try:
                date.fromisoformat(self.date)

            except ValueError as e:
                raise ValueError("Date is not correct or not in correct format 'yyyy-MM-dd'")

        except ValueError as e:
            print(f"Validation error: {e}")
            sys.exit(1)

    def update_json_db(self):
        print('Updating your expense')
        last_record_id = 0
        try:
            with open(self.DB_FILE, "r") as read_file, open(self.DB_FILE, "a") as write_file:
                for line in read_file:
                    if not line.strip():
                        continue

                    data = json.loads(line)
                    last_record_id = data.get('id', 0)

                expense_dict = {
                    "id": last_record_id + 1,
                    "category": self.category,
                    "amount": self.amount,
                    "description": self.description,
                    "date": self.date
                }
                print(expense_dict)
                write_file.write(json.dumps(expense_dict) + "\n")

        except(FileNotFoundError, json.JSONDecodeError):
            print("Something wrong with writing data to the file")
            sys.exit(1)

    def show_expenses(self):
        table = PrettyTable()
        tbl_list = []
        with open(self.DB_FILE, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                data = json.loads(line)
                tbl_list.append(data)

            table.field_names = tbl_list[0].keys()
        for item in tbl_list:
            table.add_row(item.values())
        print(table)

'''
    def run(self):

        parser = argparse.ArgumentParser(description="ExpenseTracker")

        parser.add_argument('option', choices=['add', 'show','delete'])
        args = parser.parse_args()

        if args.option == "add":
            self.get_expense_info()
            self.update_json_db()

        if args.option == "show":
            self.show_expenses()




if __name__ == "__main__":
    app = Expense()
    app.run()
'''