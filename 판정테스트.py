import pyautogui
import time


def isAchromatic(x, y):
    if(pyautogui.pixel(x, y) == (16, 24, 27) or pyautogui.pixel(x, y) == (22, 32, 33) or pyautogui.pixel(x, y) == (0, 0, 0) or pyautogui.pixel(x, y) == (255, 255, 255)):
        return False
    avgVal = (pyautogui.pixel(x, y)[0] + pyautogui.pixel(x, y)[1] + pyautogui.pixel(x, y)[2]) / 3
    if abs(pyautogui.pixel(x, y)[0] - avgVal) <= val and abs(pyautogui.pixel(x, y)[1] - avgVal) <= val and abs(pyautogui.pixel(x, y)[2] - avgVal) <= val:
        return True
    else:
        return False


def isColor(x, y, rank):
    avgVal = (pyautogui.pixel(x, y - 72 * (8-rank))[0] + pyautogui.pixel(x, y - 72 * (8-rank))[1] + pyautogui.pixel(x, y - 72 * (8-rank))[2]) / 3
    if abs(pyautogui.pixel(x, y - 72 * (8-rank))[0] - avgVal) > val or abs(pyautogui.pixel(x, y - 72 * (8-rank))[1] - avgVal) > val or abs(pyautogui.pixel(x, y - 72 * (8-rank))[2] - avgVal) > val:
        return True
    else:
        print("%i등이 문제" %rank)
        return False


def isSix():
    if isAchromatic(1866, 732) and isAchromatic(1866, 657):
        return True
    else:
        return False

def test():
    if isColor(x, y, 8) and isColor(x, y, 7) and isColor(x, y, 6) and isColor(x, y, 5) and isColor(x, y, 4) and isColor(x, y, 3) and isColor(x, y, 2) and isColor(x, y, 1):
        print("pass!")
    else:
        print("fail")

x = 1874
y = 742
val = 10
time.sleep(5)
while True:
    test()