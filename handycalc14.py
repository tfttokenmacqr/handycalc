# ver14 무한로딩 대응버전 12버전 베이스
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
    if pag.pixelMatchesColor(130, 650, (18, 19, 19)):
        return False
    else:
        return True


def startFinder():
    if pag.pixelMatchesColor(1919, 395, (24, 32, 33)):
        return False
    else:
        return True


def regameFinder():
    if pag.pixelMatchesColor(915, 840, (30, 35, 40)):
        return False
    else:
        return True

def infQueueREstart():
    x = 1


plays = 0  # 매크로 실행횟수
isStart = False
loadtimelist = []
playtimelist = []
restarts = 0
while True:

    if not isStart:
        loadtmstart = time.time()
    
    isStart = True

    i = 0
    while i < 5:  # 게임찾기버튼
        pag.moveTo(random.uniform(790, 941), random.uniform(
            823, 851), random.uniform(0.8, 0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pag.mouseUp()
        i = i+1

    print('wait untill accepted')
    while loadingFinder():

        pag.moveTo(random.uniform(884+16, 1033),
                   random.uniform(700, 726-15), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()
        if time.time()-loadtmstart > 600:
            break

    if startFinder():
        restarts = restarts + 1
        infQueueREstart()
        continue
        
        

    print("wait untill start")
    while startFinder():
        x = 1

    loadtime = time.time()-loadtmstart

    print("load complete")
    start2 = time.time()

    while time.time()-start2 < 600:  # 챔피언픽

        pag.moveTo(random.uniform(485, 667), random.uniform(
            932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+200, 667+200), random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
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
    pag.keyDown('.')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('.')
    pag.keyDown('enter')
    pag.PAUSE = random.uniform(0.05, 0.1)
    pag.keyUp('enter')

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

    playtime = time.time()-start2

    loadtimelist.append(loadtime)
    playtimelist.append(playtime)

    loadtmstart = time.time()

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

    plays = plays+1
    print("플레이 횟수 :", plays)
    print("이번 판 큐+로딩시간 : %imin%isec, 인게임시간 : %imin%isec"  %(loadtime/60, loadtime%60, playtime/60, playtime%60,))
    print("평균 큐+로딩시간 : %imin%isec, 평균 인게임시간 : %imin%isec" %(sum(loadtimelist)/len(loadtimelist)/60, (sum(loadtimelist)/len(loadtimelist))%60, sum(playtimelist)/len(playtimelist)/60, (sum(playtimelist)/len(playtimelist))%60))
    print("총 토큰획득(추정치) :", plays*4)
    print("시간당 토큰획득(추정치) : %.2f" %(plays*4/(sum(loadtimelist)+sum(playtimelist))*3600))
    if restarts > 0:
        print("무한로딩 재시작 횟수 :", restarts)

