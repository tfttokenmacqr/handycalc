import pyautogui


def is_achromatic(x, y):
    red, green, blue = pyautogui.pixel(x, y)
    rgb_tuple = (red, green, blue)
    if (rgb_tuple == (0, 0, 0) or rgb_tuple == (240, 240, 240) or rgb_tuple == (205, 205, 205)
            or rgb_tuple == (96, 96, 96) or rgb_tuple == (47, 47, 47) or rgb_tuple == (12, 12, 12)
            or rgb_tuple == (204, 204, 204)):
        return False
    avg_val = (red + green + blue) / 3
    if abs(red - avg_val) <= 0.1 and abs(green - avg_val) <= 0.1 and abs(blue - avg_val) <= 0.1:
        return True
    else:
        return False


def is_six():
    if (is_achromatic(Xserr, Yserr - 72) or is_achromatic(Xserr, Yserr - 72 * 2) or is_achromatic(Xserr, Yserr - 72 * 3)
            or is_achromatic(Xserr, Yserr - 72 * 4) or is_achromatic(Xserr, Yserr - 72 * 5)):
        tokenIdx[0] = 1
        return True
    else:
        return False


def debug():
    print("7등자리", pyautogui.pixel(Xserr, Yserr - 72))
    print("6등자리", pyautogui.pixel(Xserr, Yserr - 72 * 2))
    print("5등자리", pyautogui.pixel(Xserr, Yserr - 72 * 3))
    print("4등자리", pyautogui.pixel(Xserr, Yserr - 72 * 4))
    print("3등자리", pyautogui.pixel(Xserr, Yserr - 72 * 5))


Xserr = 1870
Yserr = 737
tokenIdx = [0]

input("엔터치면 작동")
debug()
input("엔터치면 종료")


