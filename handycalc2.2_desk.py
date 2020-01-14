import pyautogui as pag
import random
import time

#find_button  lt790, 823 rb941 851  wd154 hi28
#accept_button lt884 700 rb1033 726
#setting leftup 1893 873  rightdown 1917 894
#surrender  lt680 854  rb833 888
#sur_accpt  lt770 612 rb945 638
#again lt791 834 rb934 853 width 144 hight 25

#pick lt485 932  rb667 1068  relative 200

while True:

    pag.moveTo(random.uniform(790,941),random.uniform(823,851),random.uniform(1.2,2.2))
    pag.mouseDown()
    time.sleep(random.uniform(0.08,0.3))
    pag.mouseUp()

    #time.sleep(3)
    start1=time.time()
    while True:
        pag.moveTo(random.uniform(884,1033),random.uniform(700,726),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()

        if time.time()-start1>120:
            break

    print("in game")
    start2 = time.time()

    while True:
        pag.moveTo(random.uniform(485,667),random.uniform(932,1068),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+200,667+200),random.uniform(932,1068),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+400,667+400),random.uniform(932,1068),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+600,667+600),random.uniform(932,1068),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+800,667+800),random.uniform(932,1068),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        if time.time()-start2>900:
            break


    print("wake up")

    pag.moveTo(random.uniform(1893+2,1917-2),random.uniform(873+2,894-2),random.uniform(0.5,1))
    pag.mouseDown()
    time.sleep(random.uniform(0.1,0.3))
    pag.mouseUp()

    pag.moveTo(random.uniform(680,833),random.uniform(854,888),random.uniform(0.4,2))
    pag.mouseDown()
    time.sleep(random.uniform(0.1,0.25))
    pag.mouseUp()

    pag.moveTo(random.uniform(770,945),random.uniform(612,638),random.uniform(0.7,1.5))
    pag.mouseDown()
    time.sleep(random.uniform(0.12,0.34))
    pag.mouseUp()


    time.sleep(10)

    pag.moveTo(random.uniform(791,934),random.uniform(834,853),random.uniform(1,3.3))
    pag.mouseDown()
    time.sleep(random.uniform(0.08,0.3))
    pag.mouseUp()

    time.sleep(3)
