import pyautogui
import time

while True:
    x,y=pyautogui.position()
    position_str = str(x)+", "+str(y)
    pos = pyautogui.position()
    pix = pyautogui.pixel(pos[0], pos[1])
    print(position_str, "|", pix)
    time.sleep(0.1)
    
