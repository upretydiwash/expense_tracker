import json
import sys
from pathlib import Path
from prettytable import PrettyTable


class Reports:
    DB_FILE = Path(__file__).resolve().parent.parent / "database" / "expenses.jsonl"

    def __init__(self):
        self.year =""
        self.month = ""
        self.total = 0
        self.reference = {
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        }

    def monthly_report(self):

        report_tbl = []
        print("To get the reports year and month should be in YYYY and month should be typed: For example: 2021 March")
        self.year = input("Enter year: ")
        self.month = input("Enter month: ").capitalize()
        month = self.month
        self.month = self.reference.get(self.month)


        try:
            validate_fields = {
                'year': self.year,
                'month': self.month
            }

            for k,v in validate_fields.items():
                if v is None or not v.strip():
                    raise ValueError(f'Required field {k} is missing')

        except ValueError as e:
            print(f'Validation failed becasue of : {e}')
            sys.exit(1)

        try:
            with open(self.DB_FILE, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    if data.get('date')[5:7] == self.month and data.get('date')[0:4] == self.year:
                        report_tbl.append(data)
                        self.total = self.total + int(data.get('amount'))

            # report_tbl.append({'Total':self.total})
            #print(report_tbl)
                table = PrettyTable()

                if len(report_tbl) > 0 :
                    table.field_names = report_tbl[0].keys()

                    for item in report_tbl:
                        table.add_row(item.values())
                    print(table)
                    print(f'Total expense for the month of {self.year}-{month} : {self.total}')

                else:
                    print("No records found for the time period mentioned.")
        except (ValueError,FileNotFoundError) as e:
            print(f"Something wrong with the JSON file: {e}")



#c1 = Reports()
#c1.monthly_report()
