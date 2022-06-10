import csv
from time import sleep
import keyboard as kb
import os

short_delay = 0.05
long_delay = 0.2

local_dir = os.getcwd()
csv_dir = os.path.join(local_dir, "list.csv")

# Counts number of lines in csv file
with open(csv_dir) as csv_file:
    print(sum(1 for line in csv_file), "containere")

with open(csv_dir) as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    kb.wait('insert')
    for row in reader:
        print(row)
        kb.write(row[0])
        sleep(short_delay)
        kb.send('tab')
        sleep(short_delay)
        kb.write(row[1])
        sleep(short_delay)
        kb.send('tab')
        sleep(short_delay)
        kb.write(row[2])
        kb.send('tab')
        sleep(long_delay)
        kb.write("Method 2")
        sleep(short_delay)
        kb.send('enter')
        sleep(long_delay)
        kb.send('tab')
        sleep(short_delay)
        kb.send('tab')
        sleep(short_delay)
        kb.send('tab')
        sleep(short_delay)
