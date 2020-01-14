import pyautogui

while True:
    pos = pyautogui.position()
    pix = pyautogui.pixel(pos[0], pos[1])
    print(pix)
