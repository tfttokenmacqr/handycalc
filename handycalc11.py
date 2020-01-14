# ver11 대망의 이미지인식 추가
import pyautogui as pag
import random
import time

# find_button  lt790, 823 rb941 851  wd154 hi28
# accept_button lt884 700 rb1033 726
# setting leftup 1893 873  rightdown 1917 894
# surrender  lt680 854  rb833 888
# sur_accpt  lt770 612 rb945 638    new  lt 776 596   br 943 619
# again lt791 834 rb934 853 width 144 hight 25
# pick lt485 932  rb667 1068  relative 200
# token_get lt902 827 rb1018 849


def loadingFinder():
    try:
        location = pag.locateCenterOnScreen(
            r'C:\Users\whrbd\GoogleDrive\programming\python\handycalc\finder\loadingRock.png', confidence=0.99)
    except TypeError:
        location = (0, 0)

    if location[0] == 0 and location[1] == 0:
        return True
    else:
        return False


def startFinder():
    try:
        location = pag.locateCenterOnScreen(
            r'C:\Users\whrbd\GoogleDrive\programming\python\handycalc\finder\start.png', confidence=0.99)
    except TypeError:
        location = (0, 0)

    if location[0] == 0 and location[1] == 0:
        return True
    else:
        return False


def regameFinder():
    try:
        location = pag.locateCenterOnScreen(
            r'C:\Users\whrbd\GoogleDrive\programming\python\handycalc\finder\button7.png', confidence=0.99)
    except TypeError:
        location = (0, 0)

    if location[0] == 0 and location[1] == 0:
        return True
    else:
        return False


play_time = 0  # 매크로 실행횟수
while True:

    i = 0
    while i < 5:  # 게임찾기버튼
        pag.moveTo(random.uniform(790, 941), random.uniform(
            823, 851), random.uniform(0.8, 0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pag.mouseUp()
        i = i+1

    while loadingFinder():
        print('wait untill accepted')
        pag.moveTo(random.uniform(884+16, 1033),
                   random.uniform(700, 726-15), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()

    while startFinder():
        print("wait untill start")

    print("load complete")
    start2 = time.time()

    while time.time()-start2 < 605:  # 챔피언픽

        pag.moveTo(random.uniform(485, 667), random.uniform(
            932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+200, 667+200),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+400, 667+400),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+600, 667+600),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+800, 667+800),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()

    print("surrender")


# 항복
    # pag.moveTo(random.uniform(1893+2,1917-2),random.uniform(873+2,894-2),random.uniform(0.5,1))
    # pag.mouseDown()
    # time.sleep(random.uniform(0.1,0.3))
    # pag.mouseUp()

    # pag.moveTo(random.uniform(680+2, 741 ),random.uniform(854+2,888-2),random.uniform(0.4,2))
    # pag.mouseDown()
    # time.sleep(random.uniform(0.1,0.25))
    # pag.mouseUp()

    pag.keyDown('enter')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('enter')

    pag.keyDown('/')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('/')

    pag.keyDown('f')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('f')

    pag.keyDown('f')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('f')

    pag.keyDown('enter')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('enter')

    pag.keyDown('enter')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('enter')

    pag.keyDown('/')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('/')

    pag.keyDown('w')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('w')

    pag.keyDown('w')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('w')

    pag.keyDown('enter')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('enter')

    pag.moveTo(random.uniform(900, 943), random.uniform(
        596, 619), random.uniform(0.7, 1.5))
    pag.mouseDown()
    time.sleep(random.uniform(0.1, 0.2))
    pag.mouseUp()

    # pag.moveTo(random.uniform(1893+2,1917-2),random.uniform(873+2,894-2),random.uniform(0.5,1))
    # pag.mouseDown()
    # time.sleep(random.uniform(0.1,0.3))
    # pag.mouseUp()

    while regameFinder():  # 퀘스트깼을때 퀘스트확인버튼
        pag.moveTo(random.uniform(950, 1018-2),
                   random.uniform(827, 849), random.uniform(0.8, 0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pag.mouseUp()


# 다시하기
    pag.moveTo(random.uniform(791, 934), random.uniform(
        834, 853), random.uniform(1, 3.3))
    pag.mouseDown()
    time.sleep(random.uniform(0.08, 0.3))
    pag.mouseUp()

    play_time = play_time+1
    print("play times : ", play_time)
