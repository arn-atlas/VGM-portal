import csv
from time import sleep
import keyboard as kb
import os

with open(os.path.join(os.getcwd(), "list.csv")) as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    kb.wait('insert')
    for row in reader:
        print(row)
        kb.write(row[0])
        sleep(0.05)
        kb.send('tab')
        sleep(0.05)
        kb.write(row[1])
        sleep(0.05)
        kb.send('tab')
        sleep(0.05)
        kb.write(row[2])
        if len(row[2].split(',')) < 3:
            kb.write("0")
        kb.send('tab')
        sleep(0.2)
        kb.write("Method 2")
        sleep(0.05)
        kb.send('enter')
        sleep(0.2)
        kb.send('tab')
        sleep(0.05)
        kb.send('tab')
        sleep(0.05)
        kb.send('tab')
        sleep(0.05)
