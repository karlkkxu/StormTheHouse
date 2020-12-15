import pyautogui
import keyboard
import mss
import time

#http://www.bngames.com/games/storm-the-house-3/full_screen.html
#125%

#screencoords
topLeft   = (270, 710)
topRight  = (1390, 710)
botLeft   = (270, 1050)
botRight  = (1390, 1050)


monitor = {
    "top": topLeft[1] ,
    "left": topLeft[0] ,
    "width": topRight[0] - topLeft[0] ,
    "height": botLeft[1] - topLeft[1]
}

pyautogui.PAUSE = 0.0
screenCaps = mss.mss()

safeZone = []

def in_safeZone(i, j):
    global safeZone
    for x,y in safeZone:
        if (abs(i - x) + abs(j - y)) < 60:
            return True
    
    return False

def shoot(img):
    global monitor, safeZone

    for x in range(img.width - 1, 0, -5):
        for y in range(img.height - 1, 0, -5):
            if img.pixel(x,y)[0] == 0 and img.pixel(x,y)[1] == 0 and img.pixel(x,y)[2] == 0:
                if in_safeZone(monitor["left"] + x , monitor["top"] + y) == False:
                    pyautogui.click(monitor["left"] + x , monitor["top"] + y)
                    pyautogui.click(monitor["left"] + x , monitor["top"] + y)
                    safeZone.append((monitor["left"] + x , monitor["top"] + y))



while keyboard.is_pressed('q') == False:
    for x in range(0, 30, 1):
        img = screenCaps.grab(monitor)
        shoot(img)
        safeZone = []
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')

