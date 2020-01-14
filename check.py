import pyautogui as pag

while True:
    x,y=pag.position()
    position_str = str(x)+", "+str(y)
    print(position_str)
    
