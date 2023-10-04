import sys
from time import sleep
import keyboard as kb
from datetime import datetime

args = sys.argv
print(args)
input()

"""
SHORT_DELAY = 0.05
LONG_DELAY = 0.2

def paste_data(text, tabs = 1, delay = SHORT_DELAY):
    print(text)
    if text:
        kb.write(str(text))
        sleep(delay)
    for _ in range(tabs):
        kb.send('tab')
        sleep(delay)

def main():
    args = sys.argv
    data = [a.split("¢") for a in args[1].split("¥")]

    print(data)

    kb.wait('insert')
    for row in data:
        print(row)

        paste_data(row[0])
        paste_data(row[1])
        paste_data(row[2])

        sleep(LONG_DELAY)
        kb.write("Method 2")
        sleep(SHORT_DELAY)
        kb.send('enter')
        sleep(SHORT_DELAY)
        paste_data(None,tabs=3)

if __name__ == '__main__':
    main()
"""