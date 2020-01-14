import pyautogui as pag
import time


def loadingFinder():
    try:
        location = pag.locateCenterOnScreen(
            r'C:\Users\whrbd\GoogleDrive\programming\python\handycalc\finder\loadingRock.png', confidence=0.99)
    except TypeError:
        location = (0, 0)

    print('loading')
    print(location)


def startFinder():
    try:
        location = pag.locateCenterOnScreen(
            r'C:\Users\whrbd\GoogleDrive\programming\python\handycalc\finder\start.png', confidence=0.99)
    except TypeError:
        location = (0, 0)

    print('start')
    print(location)


def regameFinder():
    try:
        location = pag.locateCenterOnScreen(
            r'C:\Users\whrbd\GoogleDrive\programming\python\handycalc\finder\regame.png', confidence=0.99)
    except TypeError:
        location = (0, 0)

    print('regame')
    print(location)
