import time, os, random

pid = os.getpid()
filepath = './new_transactions.csv'
file = open(filepath, 'w')
while True:
    time.sleep(.001)
    file.write(str(pid) + '\n')
    if random.randint(1,3000) == 1:
        file.flush()