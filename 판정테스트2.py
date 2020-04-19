import pyautogui
import time


def isAchromatic(x, y):
    if pyautogui.pixel(x, y) == (16, 24, 27) or pyautogui.pixel(x, y) == (22, 32, 33) or pyautogui.pixel(x, y) == (0, 0, 0) or pyautogui.pixel(x, y) == (240, 240, 240) or pyautogui.pixel(x, y) == (205, 205, 205) or pyautogui.pixel(x, y) == (96, 96, 96):
        return False
    avgVal = (pyautogui.pixel(x, y)[0] + pyautogui.pixel(x, y)[1] + pyautogui.pixel(x, y)[2]) / 3
    if abs(pyautogui.pixel(x, y)[0] - avgVal) <= 2 and abs(pyautogui.pixel(x, y)[1] - avgVal) <= 2 and abs(pyautogui.pixel(x, y)[2] - avgVal) <= 2:
        return True
    else:
        return False



def achromaticPrinter(x, y):
    avgVal = (pyautogui.pixel(x, y)[0] + pyautogui.pixel(x, y)[1] + pyautogui.pixel(x, y)[2]) / 3
    print("%.2f %.2f %.2f | %.2f %.2f %.2f" %(abs(pyautogui.pixel(x, y)[0] - avgVal), abs(pyautogui.pixel(x, y)[1] - avgVal), abs(pyautogui.pixel(x, y)[2] - avgVal), pyautogui.pixel(x, y)[0], pyautogui.pixel(x, y)[1], pyautogui.pixel(x, y)[2]))




def isColor(x, y, rank):
    avgVal = (pyautogui.pixel(x, y - 72 * (8-rank))[0] + pyautogui.pixel(x, y - 72 * (8-rank))[1] + pyautogui.pixel(x, y - 72 * (8-rank))[2]) / 3
    if abs(pyautogui.pixel(x, y - 72 * (8-rank))[0] - avgVal) > val or abs(pyautogui.pixel(x, y - 72 * (8-rank))[1] - avgVal) > val or abs(pyautogui.pixel(x, y - 72 * (8-rank))[2] - avgVal) > val:
        return True
    else:
        print("%i등이 문제" %rank)
        return False


def isSix():
    if isAchromatic(Xserr, Yserr - 72) or isAchromatic(Xserr, Yserr - 72*2) or isAchromatic(Xserr, Yserr - 72*3) or isAchromatic(Xserr, Yserr - 72*4) or isAchromatic(Xserr, Yserr - 72*5):
        
        return True
    else:
        return False




def printer():
    print("8등")
    achromaticPrinter(Xserr, Yserr)
    print("7등")
    achromaticPrinter(Xserr, Yserr - 72)
    print("6등")
    achromaticPrinter(Xserr, Yserr - 72*2)
    print("5등")
    achromaticPrinter(Xserr, Yserr - 72*3)
    print("4등")
    achromaticPrinter(Xserr, Yserr - 72*4)
    print("3등")
    achromaticPrinter(Xserr, Yserr - 72*5)
    print("2등")
    achromaticPrinter(Xserr, Yserr - 72*6)
    print("1등")
    achromaticPrinter(Xserr, Yserr - 72*7)

Xserr = 1870
Yserr = 737
val = 3
input("엔터치면 스타트")
while True:
    printer()
    input("엔터치면 계속")
    