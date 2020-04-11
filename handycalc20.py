import pyautogui
import random
import time
import sys
import ctypes
import subprocess





#==============================체크함수들======================================


def loadingScreenCheck():
    if pyautogui.pixelMatchesColor(977, 1072, (0, 11, 19)):
        print("로딩창 인식")
        return True
    else:
        return False


def startedCheck():
    if pyautogui.pixelMatchesColor(1919, 395, (24, 32, 33)):
        print("시작 인식")
        return True
    else:
        return False


def regameScreenCheck():
    if pyautogui.pixelMatchesColor(803, 844, (30, 35, 40)):
        print("한판더하기 인식")
        return True
    else:
        return False


def findgameScreenCheck():
    if pyautogui.pixelMatchesColor(1147, 266, (30, 35, 40)) or pyautogui.pixelMatchesColor(1147, 266, (11, 13, 15)) or pyautogui.pixelMatchesColor(1147, 266, (1, 10, 19)):
        print("게임찾기 인식")
        return True
    else:
        return False


def isSix():
    if isAchromatic(Xserr, Yserr - 72) or isAchromatic(Xserr, Yserr - 72*2) or isAchromatic(Xserr, Yserr - 72*3) or isAchromatic(Xserr, Yserr - 72*4) or isAchromatic(Xserr, Yserr - 72*5):
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



def isAchromatic(x, y):
    if(pyautogui.pixel(x, y) == (16, 24, 27) or pyautogui.pixel(x, y) == (22, 32, 33) or pyautogui.pixel(x, y) == (0, 0, 0) or pyautogui.pixel(x, y) == (255, 255, 255)) or pyautogui.pixel(x, y) == (240, 240, 240) or pyautogui.pixel(x, y) == (205, 205, 205) or pyautogui.pixel(96, 96, 96):
        return False
    avgVal = (pyautogui.pixel(x, y)[0] + pyautogui.pixel(x, y)[1] + pyautogui.pixel(x, y)[2]) / 3
    if abs(pyautogui.pixel(x, y)[0] - avgVal) <= 2 and abs(pyautogui.pixel(x, y)[1] - avgVal) <= 2 and abs(pyautogui.pixel(x, y)[2] - avgVal) <= 2:
        return True
    else:
        return False




def lessthansixteen():
    if time.time() - startTime[0] < 960:
        return True
    elif isFour():
        tokenIdx[0] = 2
        return True
    else:
        return False


def isFour():
    if isAchromatic(Xserr, Yserr - 72*3) or isAchromatic(Xserr, Yserr - 72*4) or isAchromatic(Xserr, Yserr - 72*5):
        tokenIdx[0] = 2
        return True
    else:
        return False    


def passwordAltCheck():
    if pyautogui.pixelMatchesColor(766, 449, (1, 10, 19)) and pyautogui.pixelMatchesColor(770, 584, (1, 10, 19)) and pyautogui.pixelMatchesColor(1147, 462, (1, 10, 19)) and pyautogui.pixelMatchesColor(1131, 581, (1, 10, 19)):
        print("비밀번호변경 확인창 인식")
        return True
    else:
        return False


def acceptScreenCheck():
    if pyautogui.pixelMatchesColor(921, 780, (30, 35, 40)) and pyautogui.pixelMatchesColor(991, 779, (30, 35, 40)):
        print("수락창 인식")
        return True
    else:
        return False


def finalRankingCheck():
    if isFour():
        print("3~4등")
        tokenIdx[0] = 2
    elif isSix():
        print("5~6등")
        tokenIdx[0] = 1


def partyExCheck():
    if pyautogui.pixelMatchesColor(842, 498, (1, 10, 19)) and pyautogui.pixelMatchesColor(1090, 541, (1, 10, 19)):
        return True
    else:
        return False


def isWin():
    if pyautogui.pixelMatchesColor(995, 644, (132, 15, 16), 1):
        return True
    else:
        return False


def isOver():
    if pyautogui.pixelMatchesColor(890, 534, (8, 85, 106), 1):
        return True
    else:
        return False




#====================================행동함수들==================================
def currentTime():
    print(time.strftime("%I:%M %p", time.localtime(time.time())))
    

def click(x, y, sleep = 0, sec = 0.5, times = 1, tol  = 2):
    pyautogui.moveTo(x+random.uniform(-tol, tol), y+random.uniform(-tol, tol), random.uniform(sec - 0.02, sec + 0.02))
    for _ in range(times):
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pyautogui.mouseUp()
    time.sleep(sleep)

def startToFind():
    click(482, 202, times = 2, sleep = 1)

    click(1194, 390, sleep=1)

    click(860, 849, sleep=1)



def INFloading():
    click(1579, 174, sleep=1)

    click(912, 564, sleep=60)

    subprocess.call("C:\\Riot Games\\League of Legends\\LeagueClient.exe")

    time.sleep(60)

    while True:
        if passwordAltCheck():
            passwordAltOk()
        if pyautogui.pixelMatchesColor(482, 202, (30, 35, 40)):
            startToFind()

            onceStart[0] = False
            INFloadings[0] += 1
            break



def modeSelect():
    print("모드를 선택하십시오")
    print("1. 10분 서렌")
    print("2. 6등 서렌")
    print("3. 4등 서렌")
    print("4. 모드 설명")
    print("5. 종료")
    try:
        mode[0] = int(input())
    except:
        print("인풋에러, 올바른 값을 입력하시오")
        mode[0] = 0


def modeDemo():
    print("""\n\n
1. 10분이 되면 서렌하는 버전. 보통 총로딩시간이 2분이므로 시간당 10개 예상.

    """)
    print("""
2. 6등이 되면 서렌하는 버전. 10분서렌버전 보다 2개 더 많은 4개 토큰을 얻음. 
다른사람들이 언제 나가는 지에 따라서 효율이 변함.

    """)
    print("""
3. 4등이 되면 서렌하는 버전. 6개의 토큰보상.
mmr이 올라갈 것이라는 우려가 있으며 확인된바는 없음.

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
        if partyExCheck():
            partyEx()
            break
        pyautogui.moveTo(random.uniform(790, 941), random.uniform(823, 851), random.uniform(0.8, 0.12))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pyautogui.mouseUp()
        if time.time() - loadTimeStart[0] > 1800:
            INFloading()
            break


def gameAccept():
    print('게임수락')
    while True:
        if loadingScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        if partyExCheck():
            partyEx()
            break
        pyautogui.moveTo(random.uniform(884+16, 1033), random.uniform(700, 726-15), random.uniform(0.25, 0.75))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pyautogui.mouseUp()
        if time.time() - loadTimeStart[0] > 1800:
            INFloading()
            break
        


def gameLoading():
    print("로딩")
    while True:
        if startedCheck():
            break

    loadTime[0] = time.time()-loadTimeStart[0]
    loadValIn[0] = True



def partyEx():
    time.sleep(10)
    pyautogui.moveTo(962 + random.uniform(-2, 2), 542 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.mouseUp()
            
            
    pyautogui.moveTo(482 + random.uniform(-2, 2), 202 + random.uniform(-2, 2), random.uniform(0.8, 0.12))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.08, 0.12))
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.08, 0.12))
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.moveTo(1194 + random.uniform(-2, 2), 390 + random.uniform(-2, 2), random.uniform(0.8, 0.12))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.08, 0.12))
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.moveTo(860 + random.uniform(-2, 2), 849 + random.uniform(-2, 2), random.uniform(0.8, 0.12))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.08, 0.12))
    pyautogui.mouseUp()

    time.sleep(1)
    partyExcludes[0] += 1
    onceStart[0] = False


def finishing():
    playTime[0] = time.time()-startTime[0]

    loadTimelist.append(loadTime[0])
    playTimelist.append(playTime[0])
    tokenGetList.append(tokenList[tokenIdx[0]])

    loadTimeStart[0] = time.time()
    isStart[0] = False
    loadValIn[0] = False


    currentTime()
    plays[0] += 1
    print("플레이 횟수 :", plays[0])
    print("이번 판 큐+로딩시간 : %imin%isec, \n이번 판 인게임시간 : %imin%isec"  %(loadTime[0]/60, loadTime[0]%60, playTime[0]/60, playTime[0]%60,))
    print("평균 큐+로딩시간 : %imin%isec, \n평균 인게임시간 : %imin%isec" %(sum(loadTimelist)/len(loadTimelist)/60, (sum(loadTimelist)/len(loadTimelist))%60, sum(playTimelist)/len(playTimelist)/60, (sum(playTimelist)/len(playTimelist))%60))
    print("총 토큰획득(추정치) :", sum(tokenGetList))
    print("이번 판 시간당 토큰획득 : %.2f" %(tokenList[tokenIdx[0]]/(loadTime[0] + playTime[0])*3600))
    print("시간당 토큰획득(추정치) : %.2f" %(sum(tokenGetList)/(sum(loadTimelist)+sum(playTimelist))*3600))
    print("재시작 횟수 :",INFloadings[0])
    print("파티제외 횟수 :",partyExcludes[0])


    while True:  # 퀘스트깼을때 퀘스트확인버튼
        if regameScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        if partyExCheck():
            partyEx()
            break
        pyautogui.moveTo(981 + random.uniform(-2, 2),
                   838 + random.uniform(-2, 2), random.uniform(0.8, 0.12))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pyautogui.mouseUp()


def gameStart():
    if not isStart[0]:
        startTime[0] = time.time()
        print("로딩 완료")
        isStart[0] = True
    if not loadValIn[0]:
        loadTime[0] = time.time()-loadTimeStart[0]
        loadValIn[0] = True


    while True:  # 챔피언픽

        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pyautogui.moveTo(random.uniform(485, 667), random.uniform(
            932, 1032-50), random.uniform(0.25, 0.75))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pyautogui.moveTo(random.uniform(485+200, 667+200), random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pyautogui.moveTo(random.uniform(485+400, 667+400),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pyautogui.moveTo(random.uniform(485+600, 667+600),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pyautogui.moveTo(random.uniform(485+800, 667+800),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        if time.time()-startTime[0] > 900:
            pyautogui.moveTo(random.uniform(278, 462), random.uniform(931, 992), random.uniform(0.25, 0.75))
            pyautogui.mouseDown()
            time.sleep(random.uniform(0.05, 0.1))
            pyautogui.mouseUp()

        if isWin():
            win()
        if isOver():
            gameOver()

    gameSurrender()


def gameSurrender():
    print("항복")



    pyautogui.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('enter')
    pyautogui.keyDown('.')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('.')
    pyautogui.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('enter')

    pyautogui.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('enter')

    pyautogui.keyDown('/')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('/')

    pyautogui.keyDown('f')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('f')

    pyautogui.keyDown('f')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('f')

    pyautogui.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('enter')

    pyautogui.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('enter')

    pyautogui.keyDown('/')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('/')

    pyautogui.keyDown('w')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('w')

    pyautogui.keyDown('w')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('w')

    pyautogui.keyDown('enter')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('enter')

    pyautogui.moveTo(random.uniform(900, 943), random.uniform(
        596, 619), random.uniform(0.7, 1.5))
    finalRankingCheck()
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.1, 0.2))
    pyautogui.mouseUp()



    finishing()



def win():
    pyautogui.moveTo(995 + random.uniform(-2, 2), 644 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.mouseUp()
    print("승리")
    tokenIdx[0] = 3
    finishing()
        

def gameOver():
    pyautogui.moveTo(890 + random.uniform(-2, 2), 534 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.mouseUp()
    print("게임오버")
    finalRankingCheck()
    finishing()

def gameRegame():
# 다시하기
    print("한판더하기")
    while True:
        if findgameScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        pyautogui.moveTo(random.uniform(791, 934), random.uniform(834, 853), random.uniform(0.25, 0.75))
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.mouseUp()



def passwordAltOk():
    print("비밀번호변경 확인")
    pyautogui.moveTo(random.uniform(931, 988), random.uniform(591, 611), random.uniform(0.25, 0.75))
    pyautogui.mouseDown()
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.mouseUp()
        


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
        pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))
        time.sleep(1)

    
#=============================var================================

tokenList = (2, 4, 6, 8, 10)
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
INFloadings = [0]
partyExcludes = [0]

Xserr = 1876
Yserr = 737

#============================main===========================================
modeSelect()

while True:
    if mode[0] == 1 or mode[0] == 2 or mode[0] == 3:
        try:
            handycalc()
        except pyautogui.FailSafeException:
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

    



