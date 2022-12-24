import csv

def bar():
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

def format_task_output(txn):
    print(txn.item_name)
    
katie = {'name': 'katie', 'age': 39}
dustin = {'name': 'dustin', 'age': 37}
people = [katie, dustin]


# write an expression to extract katie's age

def get_katie():
    print(people[0]['age'])

# write an expression to loop over people and print their name and age

def get_age_and_name():
    for p in people:
        print(f"{p['name']}, {p['age']}")

# reformat using f-string



# what is txn.item_name ?
def get_dot_syn():
    print(people[0].age)

class TransactionFileReader():
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            self.records = list(reader)

def read_transactions_file(filepath):
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

records = TransactionFileReader('../transactions.csv').records
records = read_transactions_file('../transactions.csv')

myReader.filepath
myReader.records