# ver17 일시정지 후 게임 재개가 가능한 버전
import pyautogui as pag
import random
import time
import sys

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


def loadingScreenCheck():
    if pag.pixelMatchesColor(203, 187, (20, 20, 27)):
        print("로딩창 인식")
        return True
    else:
        return False


def startedCheck():
    if pag.pixelMatchesColor(1919, 395, (24, 32, 33)):
        print("시작 인식")
        return True
    else:
        return False


def regameScreenCheck():
    if pag.pixelMatchesColor(915, 840, (30, 35, 40)):
        print("한판더하기 인식")
        return True
    else:
        return False


def findgameScreenCheck():
    if pag.pixelMatchesColor(1147, 266, (30, 35, 40)) or pag.pixelMatchesColor(1147, 266, (11, 13, 15)) or pag.pixelMatchesColor(1147, 266, (1, 10, 19)):
        print("게임찾기 인식")
        return True
    else:
        return False


def isSix():
    if pag.pixelMatchesColor(1836, 738, (22, 24, 33)) and pag.pixelMatchesColor(1853, 743, (22, 24, 33)) and pag.pixelMatchesColor(1836, 738-71, (22, 24, 33)) and pag.pixelMatchesColor(1853, 671, (22, 24, 33)):
        tokenIdx[0] = 1
        return True
    else:
        return False


def isTenMin():
    if time.time()-startTime[0] > 600:
        tokenIdx[0] = 0
        return True
    else:
        return False



def lessthansixteen():
    if time.time() - startTime[0] < 960:
        return True
    elif pag.pixelMatchesColor(1836, 738, (22, 24, 33)) and pag.pixelMatchesColor(1853, 743, (22, 24, 33)) and pag.pixelMatchesColor(1836, 738-71, (22, 24, 33)) and pag.pixelMatchesColor(1853, 671, (22, 24, 33)) and pag.pixelMatchesColor(1836, 595, (22, 24, 33)) and pag.pixelMatchesColor(1853, 599, (22, 24, 33)) and pag.pixelMatchesColor(1836, 522, (22, 24, 33)) and pag.pixelMatchesColor(1853, 527, (22, 24, 33)):
        tokenIdx[0] = 2
        return True
    else:
        return False


def passwordAltCheck():
    if pag.pixelMatchesColor(766, 449, (1, 10, 19)) and pag.pixelMatchesColor(770, 584, (1, 10, 19)) and pag.pixelMatchesColor(1147, 462, (1, 10, 19)) and pag.pixelMatchesColor(1131, 581, (1, 10, 19)):
        print("비밀번호변경 확인창 인식")
        return True
    else:
        return False


def acceptScreenCheck():
    if pag.pixelMatchesColor(921, 780, (30, 35, 40)) and pag.pixelMatchesColor(991, 779, (30, 35, 40)):
        print("수락창 인식")
        return True
    else:
        return False


def modeSelect():
    print("모드를 선택하십시오")
    print("1. 10분 서렌")
    print("2. 6등 서렌")
    print("3. 6~4등 서렌")
    print("4. 모드 설명")
    print("5. 종료")
    try:
        mode[0] = int(input())
    except:
        print("인풋에러, 올바른 값을 입력하시오")
        mode[0] = 0


def modeDemo():
    print("""\n\n
1. 10분이 되면 서렌하는 버전. 보통 총로딩시간이 2분이므로 시간당 20개 예상.

    """)
    print("""
2. 6등이 되면 서렌하는 버전. 10분서렌버전 보다 2개 더 많은 6개 토큰을 얻음. 
16분을 넘어서 6등을 하면 10분서렌보다 효율이 떨어짐.
매판 마다 호율이 다르게 나옴. 예상 갯수를 얘기하기에는 데이터가 많지 않음.

    """)
    print("""
3. 6등 서렌버전의 '16분이 넘어서 6등서렌을 하면 10분서렌보다 손해를 보는 부분'을 보완하기 위해 만든 버전. 
16분이 넘어도 6등서렌을 하지 못한 경우 4등이 될때 서렌을 한다. 
이 역시 22분이 넘어서 4등서렌을 할 경우 10분서렌보다 손해를 봄.
일반적인 경우 10분서렌보다 효율이 좋음. 시간당 20~22개 예상. 퀘스트를 깨기에도 좋다.
하지만 계속 플레이시 mmr이 올라가서 자주 게임오버를 당하며 효율이 20으로 떨어짐.
10분 서렌을 하여 mmr을 떨어뜨리고 6~4등서렌하기를 반복하는 것을 추천.

    """)


def gameFind():
    print("게임찾기")
    if not onceStart[0]:
        loadTimeStart[0] = time.time()
    
    onceStart[0] = True
    while True:  # 게임찾기버튼
        if acceptScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        pag.moveTo(random.uniform(790, 941), random.uniform(823, 851), random.uniform(0.8, 0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pag.mouseUp()


def gameAccept():
    print('게임수락')
    while True:
        if loadingScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        pag.moveTo(random.uniform(884+16, 1033), random.uniform(700, 726-15), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()
        


def gameLoading():
    print("로딩")
    while True:
        if startedCheck():
            break

    loadTime[0] = time.time()-loadTimeStart[0]
    loadValIn[0] = True



def gameStart():
    if not isStart[0]:
        startTime[0] = time.time()
        print("로딩 완료")
        isStart[0] = True
    if not loadValIn[0]:
        loadTime[0] = time.time()-loadTimeStart[0]
        loadValIn[0] = True


    while True:  # 챔피언픽

        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isSix() and lessthansixteen()):
            break
        pag.moveTo(random.uniform(485, 667), random.uniform(
            932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isSix() and lessthansixteen()):
            break
        pag.moveTo(random.uniform(485+200, 667+200), random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isSix() and lessthansixteen()):
            break
        pag.moveTo(random.uniform(485+400, 667+400),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isSix() and lessthansixteen()):
            break
        pag.moveTo(random.uniform(485+600, 667+600),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isSix() and lessthansixteen()):
            break
        pag.moveTo(random.uniform(485+800, 667+800),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isSix() and lessthansixteen()):
            break
        if time.time()-startTime[0] > 900:
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

    gameSurrender()


def gameSurrender():
    print("항복")


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
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('enter')
    pag.keyDown('.')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('.')
    pag.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('enter')

    pag.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('enter')

    pag.keyDown('/')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('/')

    pag.keyDown('f')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('f')

    pag.keyDown('f')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('f')

    pag.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('enter')

    pag.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('enter')

    pag.keyDown('/')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('/')

    pag.keyDown('w')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('w')

    pag.keyDown('w')
    time.sleep(random.uniform(0.05, 0.1))
    pag.keyUp('w')

    pag.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
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

    playTime[0] = time.time()-startTime[0]

    loadTimelist.append(loadTime[0])
    playTimelist.append(playTime[0])
    tokenGetList.append(tokenList[tokenIdx[0]])

    loadTimeStart[0] = time.time()
    isStart[0] = False
    loadValIn[0] = False



    plays[0] += 1
    print("플레이 횟수 :", plays[0])
    print("이번 판 큐+로딩시간 : %imin%isec, \n이번 판 인게임시간 : %imin%isec"  %(loadTime[0]/60, loadTime[0]%60, playTime[0]/60, playTime[0]%60,))
    print("평균 큐+로딩시간 : %imin%isec, \n평균 인게임시간 : %imin%isec" %(sum(loadTimelist)/len(loadTimelist)/60, (sum(loadTimelist)/len(loadTimelist))%60, sum(playTimelist)/len(playTimelist)/60, (sum(playTimelist)/len(playTimelist))%60))
    print("총 토큰획득(추정치) :", sum(tokenGetList))
    print("이번 판 시간당 토큰획득 : %.2f" %(tokenList[tokenIdx[0]]/(loadTime[0] + playTime[0])*3600))
    print("시간당 토큰획득(추정치) : %.2f" %(sum(tokenGetList)/(sum(loadTimelist)+sum(playTimelist))*3600))


    while True:  # 퀘스트깼을때 퀘스트확인버튼
        if regameScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        pag.moveTo(random.uniform(950, 1018-2),
                   random.uniform(827, 849), random.uniform(0.8, 0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pag.mouseUp()
        


def gameRegame():
# 다시하기
    print("한판더하기")
    while True:
        if findgameScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        pag.moveTo(random.uniform(791, 934), random.uniform(834, 853), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()



def passwordAltOk():
    print("비밀번호변경 확인")
    pag.moveTo(random.uniform(931, 988), random.uniform(591, 611), random.uniform(0.25, 0.75))
    pag.mouseDown()
    time.sleep(random.uniform(0.05, 0.1))
    pag.mouseUp()
        


def handycalc():
    if passwordAltCheck():
        passwordAltOk()
    elif acceptScreenCheck():
        gameAccept()
    elif findgameScreenCheck():
        gameFind()
    elif loadingScreenCheck():
        gameLoading()
    elif startedCheck():
        gameStart()
    elif regameScreenCheck():
        gameRegame()

    else:
        print("알 수 없는 상황")
        time.sleep(1)

    


tokenList = (4, 6, 8, 10, 12)
tokenIdx = [0]
mode = [0]

plays = [0]  # 매크로 실행횟수
onceStart = [False]
loadTimelist = []
playTimelist = []
tokenGetList = []

loadTimeStart = [0]
startTime = [0]
loadTime = [0]
playTime = [0]
loadValIn = [False]
isStart = [False]


modeSelect()

while True:
    if mode[0] == 1 or mode[0] == 2 or mode[0] == 3:
        try:
            handycalc()
        except pag.FailSafeException:
            exmenu = int(input("""
일시정지. 메뉴를 고르시오.
1. 돌아가기
2. 종료
3. 버그시 강제 서렌
4. 모드 변경
"""))
            if exmenu == 1:
                "게임으로 돌아갑니다."
            elif exmenu == 2:
                print("종료합니다.")
                time.sleep(2)
                sys.exit()
            elif exmenu == 3:
                print("강제로 서렌 합니다.")
                gameSurrender()
            elif exmenu == 4:
                try:
                    mode[0] = int(input("모드를 입력하시오"))
                except:
                    print("인풋에러, 올바른 값을 입력하시오")
                    mode[0] = 0
            else:
                print("이상한 값 입력. 종료합니다.")
                time.sleep(2)
                sys.exit()

    elif mode[0] == 4:
        modeDemo()
        modeSelect()
    elif mode[0] == 5:
        print("종료")
        time.sleep(2)
        break
    elif mode[0] == 0:
        modeSelect()
    else:
        print("올바른 값을 입력하십시오.")
        mode[0] = 0
        modeSelect()

    



