import pyautogui as pag
import random
import time

#find_button  lt790, 823 rb941 851  wd154 hi28
#accept_button lt884 700 rb1033 726
#setting leftup 1893 873  rightdown 1917 894
#surrender  lt680 854  rb833 888
#sur_accpt  lt770 612 rb945 638
#again lt791 834 rb934 853 width 144 hight 25


x=0
y=0

while not((x>=790 and x<=941) and (y>=823 and y<=851)):
    try:
        x,y=pag.locateCenterOnScreen('find_button.PNG')
    except:
        print("waiting find_button")
        print(x,y)
#print("done")
x,y=pag.locateCenterOnScreen('find_button.PNG')
pag.moveTo(x+random.uniform(-154/2,154/2),y+random.uniform(-28/2,28/2),random.uniform(1.2,2.2))
pag.mouseDown()
time.sleep(random.uniform(0.08,0.3))
pag.mouseUp()

#time.sleep(3)
while not((x>=884 and x<=1033) and (y>=700 and y<=726)):
    try:
        x,y=pag.locateCenterOnScreen('accept_button.PNG')
    except:
        print("waiting accept_button")
        print(x,y)
x,y=pag.locateCenterOnScreen('accept_button.PNG')
pag.moveTo(x+random.uniform(-100/2,101/2),y+random.uniform(-30/2,30/2),random.uniform(0.8,1.9))
pag.mouseDown()
time.sleep(random.uniform(0.08,0.2))
pag.mouseUp()

print("sleeping 15mins")
time.sleep(random.uniform(963, 978))

pag.moveTo(random.unifom(1893,1917),random.uniform(873,894),random.uniform(0.5,1))
pag.mouseDown()
time.sleep(random.uniform(0.1,0.3))
pag.mouseUp()

pag.moveTo(random.unifom(680,833),random.uniform(854,888),random.uniform(0.4,2))
pag.mouseDown()
time.sleep(random.uniform(0.1,0.25))
pag.mouseUp()

pag.moveTo(random.unifom(770,945),random.uniform(612,638),random.uniform(0.7,1.5))
pag.mouseDown()
time.sleep(random.uniform(0.12,0.34))
pag.mouseUp()

while not((x>=791 and x<=934) and (y>=834 and y<=853)):
    try:
        x,y=pag.locateCenterOnScreen('accept_button.PNG')
    except:
        print("waiting accept_button")
        print(x,y)
#time.sleep(10)

x,y=pag.locateCenterOnScreen('accept_button.PNG')
pag.moveTo(x+random.uniform(-144/2,144/2),y+random.uniform(-25/2,25/2),random.uniform(1,3.3))
pag.mouseDown()
time.sleep(random.uniform(0.08,0.3))
pag.mouseUp()
