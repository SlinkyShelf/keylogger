from time import sleep, time
from pynput import keyboard, mouse
from datetime import date
import os 

day = date.today()
charsperline = 1

logpath = "./logs/"+str(day)+".txt"

# if os.path.exists(logpath):
#     open(logpath, "x")


writer = ""
with open(logpath, "a") as w:
    writer = w

if not writer:
    quit()

currentcharcount = 0
currentline = ""
def onkeypress(keyevent):
    try:
        if keyevent.char == "s":
            writer.close()
            quit()

        global currentcharcount
        global currentline
        key = keyevent.char
        if currentcharcount+len(key) > charsperline:
            currentcharcount = 0
            print("writeline", currentline)
            writer.write(currentline)
            currentline = ""

        currentline += key
        currentcharcount += len(key)

    except:
        _ = ""


listener = keyboard.Listener(on_press = onkeypress)
listener.start()

while True:
    sleep(1)