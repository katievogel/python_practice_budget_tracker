import csv
import os
from datetime import datetime

headers = ['transaction_date', 'item_name', 'item_category', 'unit_cost', 'total_units', 'total_cost' ]

if not os.path.exists("./transactions.csv"):
    with open("./transactions.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

def add_transaction(transaction_date, item_name, item_category, unit_cost, total_units, total_cost):
    total_cost = float(unit_cost) * float(total_units)
    return {
        'transaction_date': datetime.strptime(transaction_date, "%m-%d-%Y"),
        'item_name': item_name,
        'item_category': item_category.lower(),
        'unit_cost': unit_cost,
        'total_units': total_units,
        'total_cost': total_cost,
        }


def query_all_transactions():
    with open("./transactions.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

#def query_all_txns(): pass
#def format_txns_to_string(): pass
#def connect_to_db(config): pass




def view_account_balance(transaction_date, item_name, item_category, unit_cost, total_units, total_cost, file):
    with open("./transactions.csv", "r") as file:
        reader = csv.DictReader(file)
        expenses = float(0)
        income = float(0)
        profit = float(0)
        for record in reader:
            if record['item_category'] != 'income':
                expenses += float(record['total_cost'])
            else:
                income += float(record['total_cost'])
            profit = income - expenses
        print("Total Expenses: " + str(expenses), "Total Income: " + str(income), "Net Balance: " + str(profit))

def main():
    current_task = ""
    while current_task != "q":
        print("Press [a] to add a transaction, [b] to view the account balance, [v] to view all transactions, or [q] to quit.")
        current_task = input("What would you like to do?")
        if current_task == 'a':
            print("Enter the following transaction information:")
            transaction_date = input('Transaction Date (MM-DD-YYYY):')
            item_name = input('Item Name:')
            item_category = input('Category - Income or Expense?:')
            unit_cost = input('Unit Cost:')
            total_units = input('Total Units:')
            total_cost = float(unit_cost) * float(total_units)
            tx = add_transaction(transaction_date, item_name, item_category, unit_cost, total_units, total_cost)
            with open("./transactions.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writerow(tx)
                
            print(f"The total cost for {item_name} is {float(unit_cost) * float(total_units)}.")
        elif current_task == 'v':
            print("Here is a list of all of the transactions:")
            
            for record in query_all_transactions():
                print(record['transaction_date'],
                    record['item_name'], 
                    record['item_category'], 
                    record['unit_cost'], 
                    record['total_units'], 
                    record['total_cost'])

        elif current_task == 'b':
            print("Here are the balance details:")
            view_account_balance(transaction_date, item_name, item_category, unit_cost, total_units, total_cost, file)
        elif current_task not in ['q', 'a', 'b', 'v']:
            print("Invalid option.")

# main()

if __name__ == '__main__':
    main()