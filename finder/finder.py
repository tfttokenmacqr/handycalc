import pyautogui
import time
#r'C:\Users\whrbd\GoogleDrive\programming\python\handycalc\finder\




while True:
    try:
        location = pyautogui.locateCenterOnScreen(r'C:\Users\whrbd\GoogleDrive\programming\python\handycalc\finder\button7.png')
    except TypeError:
        location = (0, 0)
    print(location)
    print(location[0])