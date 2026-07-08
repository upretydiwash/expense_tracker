from models.expense import Expense
from services.delete_expense import DeleteExpense
from utils.reports import Reports
import argparse

exp = Expense()
dlt = DeleteExpense()
rprt = Reports()


parser = argparse.ArgumentParser(description="Expense tracker app")
parser.add_argument('option',choices=['add','list','remove','report'])
args = parser.parse_args()

if args.option == "add":
    exp.get_expense_info()
    exp.update_json_db()

if args.option == "list":
    exp.show_expenses()

if args.option == "remove":
    dlt.delete_expense()

if args.option == "report":
    rprt.monthly_report()



