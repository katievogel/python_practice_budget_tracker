import csv

def bar(xx):
    if xx == 1:
        a = 4
        b = xx + a
        print(b)
    c = a + 1
    return c

    # the variable 'xx' is in local scope of function 'bar'

def bat(gg):
    print(xx + 3)

#print(__name__)

def query_print_all_txns():
    with open("./transactions.csv", "r") as file:
        reader = csv.DictReader(file)
        for record in reader:
            print(
                record['transaction_date'],
                record['item_name'], 
                record['item_category'], 
                record['unit_cost'], 
                record['total_units'], 
                record['total_cost']
                )
