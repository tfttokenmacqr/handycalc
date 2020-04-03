import pyautogui
import time
#1862 660

def isAchromatic(x, y):
    if(pyautogui.pixel(x, y) == (16, 24, 27) or pyautogui.pixel(x, y) == (22, 32, 33) or pyautogui.pixel(x, y) == (0, 0, 0) or pyautogui.pixel(x, y) == (255, 255, 255)):
        return False
    avgVal = (pyautogui.pixel(x, y)[0] + pyautogui.pixel(x, y)[1] + pyautogui.pixel(x, y)[2]) / 3
    if abs(pyautogui.pixel(x, y)[0] - avgVal) <= 20 and abs(pyautogui.pixel(x, y)[1] - avgVal) <= 20 and abs(pyautogui.pixel(x, y)[2] - avgVal) <= 20:
        return True
    else:
        return False


def isSix():
    if isAchromatic(1866, 732) and isAchromatic(1866, 657):
        return True
    else:
        return False



time.sleep(5)
while True:
    print(isSix())