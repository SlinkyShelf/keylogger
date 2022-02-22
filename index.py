from time import sleep, time
from pynput import keyboard, mouse
from datetime import date
from os.path import exists
import atexit
import sys

day = date.today()
charsperline = 100

listener = ""
stop = False

logpath = "./logs/"+str(day)+".txt"


currentcharcount = 0
currentline = ""

if exists(logpath):


    line = ""
    for line in open(logpath):
        pass
    # currentline = line
    currentcharcount = len(line)

print(currentline+".")
print(currentcharcount)

def saveline():
    global currentcharcount
    global currentline

    writer = open(logpath, "a")
    if currentcharcount >= charsperline:
        writer.write(currentline+"\n")
    else:
        writer.write(currentline)
    writer.close()
    currentcharcount = 0
    currentline = ""

def onkeypress(keyevent):
    try:
        if keyevent == keyboard.Key.f9:
            listener.stop()

        global currentcharcount
        global currentline
        key = keyevent.char
        print(currentline+".")
        print(currentcharcount)
        if currentcharcount+len(key) > charsperline:
            saveline()
            

        currentline += key
        currentcharcount += len(key)

    except:
        pass

atexit.register(saveline)

listener = keyboard.Listener(on_press=onkeypress)
listener.start()
listener.join()