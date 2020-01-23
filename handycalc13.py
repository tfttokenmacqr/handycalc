# ver13 6등서렌 
# ver13.01 체력이 1남는 경우 죽은 걸로 판단하는 문제 수정
# ver13.02 안나가는 사람을 빨리 죽이기 위한 레벨업 추가
# ver13.03 종료반응성 향상
# ver13.04 판당 시간당토큰개수 추가
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
# level up lt278 931  rb462 992
# password lt931 591  rb988 611


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


def startscreenFinder():
    if pag.pixelMatchesColor(421, 682, (38, 35, 24)):
        return False
    else:
        return True


def isSix(idx):
    if pag.pixelMatchesColor(1853, 679, (22, 24, 33)) and pag.pixelMatchesColor(1853, 752, (22, 24, 33)) and pag.pixelMatchesColor(1836, 747, (22, 24, 33)) and pag.pixelMatchesColor(1836, 673, (22, 24, 33)):
        idx[0] = 1
        return True
    else:
        return False


tokenList = (4, 6, 8, 10)
tokenIdx = [0]

plays = 0  # 매크로 실행횟수
isStart = False
loadtimelist = []
playtimelist = []
tokenGetList = []
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

    print("wait untill start")
    while startFinder():
        x = 1

    loadtime = time.time()-loadtmstart

    print("load complete")
    start2 = time.time()

    while True:  # 챔피언픽

        if time.time()-start2 > 600 and isSix(tokenIdx):
            break
        pag.moveTo(random.uniform(485, 667), random.uniform(
            932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if time.time()-start2 > 600 and isSix(tokenIdx):
            break
        pag.moveTo(random.uniform(485+200, 667+200), random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if time.time()-start2 > 600 and isSix(tokenIdx):
            break
        pag.moveTo(random.uniform(485+400, 667+400),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if time.time()-start2 > 600 and isSix(tokenIdx):
            break
        pag.moveTo(random.uniform(485+600, 667+600),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if time.time()-start2 > 600 and isSix(tokenIdx):
            break
        pag.moveTo(random.uniform(485+800, 667+800),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if time.time()-start2 > 600 and isSix(tokenIdx):
            break
        if time.time()-start2 > 900:
            pag.moveTo(random.uniform(278, 462), random.uniform(931, 992), random.uniform(0.25, 0.75))
            pag.mouseDown()
            time.sleep(random.uniform(0.05, 0.1))
            pag.mouseUp()
        
        if pag.pixelMatchesColor(880, 533, (8, 81, 100)):
            if pag.pixelMatchesColor(1836, 600, (22, 24, 33)) and pag.pixelMatchesColor(1836, 527, (22, 24, 33)) and pag.pixelMatchesColor(1853, (679 - 73), (22, 24, 33)) and pag.pixelMatchesColor(1853, (679 - 73*2), (22, 24, 33)):
                tokenIdx[0] = 2
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("게임오버 4등")
                break
            elif pag.pixelMatchesColor(1836, 600, (22, 24, 33)) and pag.pixelMatchesColor(1853, (679 - 73), (22, 24, 33)):
                tokenIdx[0] = 1
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("게임오버 5등")
                break
            elif pag.pixelMatchesColor(1853, 679, (22, 24, 33)) and pag.pixelMatchesColor(1853, 752, (22, 24, 33)) and pag.pixelMatchesColor(1836, 747, (22, 24, 33)) and pag.pixelMatchesColor(1836, 673, (22, 24, 33)):
                tokenIdx[0] = 1
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("게임오버 6등")
                break
            elif pag.pixelMatchesColor(1853, 752, (22, 24, 33)) and pag.pixelMatchesColor(1836, 747, (22, 24, 33)):
                tokenIdx[0] = 0
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("게임오버 7등")
                break
            else:
                tokenIdx[0] = 0
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("게임오버 8등?")
                break






    

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
    tokenGetList.append(tokenList[tokenIdx[0]])

    loadtmstart = time.time()


    plays = plays+1
    print("플레이 횟수 :", plays)
    print("이번 판 큐+로딩시간 : %imin%isec, 인게임시간 : %imin%isec"  %(loadtime/60, loadtime%60, playtime/60, playtime%60,))
    print("평균 큐+로딩시간 : %imin%isec, 평균 인게임시간 : %imin%isec" %(sum(loadtimelist)/len(loadtimelist)/60, (sum(loadtimelist)/len(loadtimelist))%60, sum(playtimelist)/len(playtimelist)/60, (sum(playtimelist)/len(playtimelist))%60))
    print("총 토큰획득(추정치) :", sum(tokenGetList))
    print("이번 판 시간당 토큰획득 : %.2f" %(tokenList[tokenIdx[0]]/(loadtime + playtime)*3600))
    print("시간당 토큰획득(추정치) : %.2f" %(sum(tokenGetList)/(sum(loadtimelist)+sum(playtimelist))*3600))


    while regameFinder():  # 퀘스트깼을때 퀘스트확인버튼
        pag.moveTo(random.uniform(950, 1018-2),
                   random.uniform(827, 849), random.uniform(0.8, 0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pag.mouseUp()


# 다시하기
    while startscreenFinder():

        pag.moveTo(random.uniform(931, 988), random.uniform(591, 611), random.uniform(1, 3.3))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()

        pag.moveTo(random.uniform(791, 934), random.uniform(834, 853), random.uniform(1, 3.3))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()

    
