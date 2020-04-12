import pyautogui
import random
import time
import sys
import ctypes
import subprocess





#==============================체크함수들======================================
def isClientPasswordAlt():
    if pyautogui.pixelMatchesColor(766, 449, (1, 10, 19)) and pyautogui.pixelMatchesColor(770, 584, (1, 10, 19)) and pyautogui.pixelMatchesColor(1147, 462, (1, 10, 19)) and pyautogui.pixelMatchesColor(1131, 581, (1, 10, 19)):
        print("비밀번호변경 확인창 인식")
        return True
    else:
        return False


def isClientHome():
    if not pyautogui.pixelMatchesColor(501, 189, (30, 35, 40)) and pyautogui.pixelMatchesColor(482, 200, (30, 35, 40)):
        print("홈화면 인식")
        return True
    else:
        return False


def isClientFindGame():
    if (not pyautogui.pixelMatchesColor(920, 852, (92, 91, 87))) and pyautogui.pixelMatchesColor(1144, 276, (30, 35, 40)) and pyautogui.pixelMatchesColor(915, 838, (30, 35, 40)) and pyautogui.pixelMatchesColor(490, 201, (30, 35, 40)):
        print("게임찾기 인식")
        return True
    else:
        return False


def isClientAcceptScreen():
    if (not pyautogui.pixelMatchesColor(1000, 794, (92, 91, 87))) and pyautogui.pixelMatchesColor(921, 780, (30, 35, 40)) and pyautogui.pixelMatchesColor(991, 779, (30, 35, 40)):
        print("수락창 인식")
        return True
    else:
        return False


def isLoadingScreen():
    if pyautogui.pixelMatchesColor(977, 1072, (0, 11, 19)):
        if devMode[0] == True:
            print("로딩창 인식")
        return True
    else:
        return False


def isInGame():
    if pyautogui.pixelMatchesColor(1919, 395, (24, 32, 33)):
        print("인게임 인식")
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
    if pyautogui.pixel(x, y) == (16, 24, 27) or pyautogui.pixel(x, y) == (22, 32, 33) or pyautogui.pixel(x, y) == (0, 0, 0) or pyautogui.pixel(x, y) == (240, 240, 240) or pyautogui.pixel(x, y) == (205, 205, 205) or pyautogui.pixel(x, y) == (96, 96, 96):
        return False
    avgVal = (pyautogui.pixel(x, y)[0] + pyautogui.pixel(x, y)[1] + pyautogui.pixel(x, y)[2]) / 3
    if abs(pyautogui.pixel(x, y)[0] - avgVal) <= 2 and abs(pyautogui.pixel(x, y)[1] - avgVal) <= 2 and abs(pyautogui.pixel(x, y)[2] - avgVal) <= 2:
        return True
    else:
        return False



def isSix():
    if isAchromatic(Xserr, Yserr - 72) or isAchromatic(Xserr, Yserr - 72*2) or isAchromatic(Xserr, Yserr - 72*3) or isAchromatic(Xserr, Yserr - 72*4) or isAchromatic(Xserr, Yserr - 72*5):
        tokenIdx[0] = 1
        return True
    else:
        return False



def isFour():
    if isAchromatic(Xserr, Yserr - 72*3) or isAchromatic(Xserr, Yserr - 72*4) or isAchromatic(Xserr, Yserr - 72*5):
        tokenIdx[0] = 2
        return True
    else:
        return False


def isTwo():
    if isAchromatic(Xserr, Yserr - 72*5):
        tokenIdx[0] = 3
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


def finalRankingCheck():
    if isTwo():
        print("1~2등")
        tokenIdx[0] = 3
    elif isFour():
        print("3~4등")
        tokenIdx[0] = 2
    elif isSix():
        print("5~6등")
        tokenIdx[0] = 1


def isClientRegame():
    if (not pyautogui.pixelMatchesColor(1144, 276, (30, 35, 40))) and pyautogui.pixelMatchesColor(917, 844, (30, 35, 40)):
        print("한판더하기 인식")
        return True
    else:
        return False


def isClientPartyEx():
    if pyautogui.pixelMatchesColor(842, 498, (1, 10, 19)) and pyautogui.pixelMatchesColor(1090, 541, (1, 10, 19)):
        print("파티제외 인식")
        return True
    else:
        return False


def lessthansixteen(): #더이상 쓰지 않는 함수
    if time.time() - startTime[0] < 960:
        return True
    elif isFour():
        tokenIdx[0] = 2
        return True
    else:
        return False





#====================================행동함수들==================================
def currentTime():
    print(time.strftime("%I:%M %p", time.localtime(time.time())))
    
def click(x, y, sleep = 0, sec = 0.5, times = 1, tol  = 2):
    pyautogui.moveTo(x+random.uniform(-tol, tol), y+random.uniform(-tol, tol), random.uniform(sec - sec/4, sec + sec/4))
    for _ in range(times):
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pyautogui.mouseUp()
    time.sleep(sleep)

def keyClick(string):
    pyautogui.keyDown(string)
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp(string)


def passwordAltOk():
    print("비밀번호변경 확인")
    click(960, 601)



def homeToFind():
    click(482, 202, times = 2, sleep = 1)

    click(1194, 390, sleep=1)

    click(860, 849, sleep=1)



def gameFind():
    print("게임찾기")
    if onceStart[0] == False:
        loadTimeStart[0] = time.time()
    
    onceStart[0] = True
    click(866, 837)


def gameAccept():
    print('게임수락')
    click(967, 706)
    time.sleep(1)


def gameLoading():
    pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))


def gameStart():
    if isStart[0] == False:
        startTime[0] = time.time()
        print("게임시작")
        isStart[0] = True
    if loadValIn[0]  == False:
        loadTime[0] = time.time()-loadTimeStart[0]
        loadValIn[0] = True
    print("인게임")


    while True:  # 챔피언픽

        if isOver():
            gameOver()
            break
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()) or (mode[0] == 4 and isTenMin() and isTwo()):
            gameSurrender()
            break
        click(576, 990, tol=30)
        if isOver():
            gameOver()
            break
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()) or (mode[0] == 4 and isTenMin() and isTwo()):
            gameSurrender()
            break
        click(778, 988, tol=30)
        if isOver():
            gameOver()
            break
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()) or (mode[0] == 4 and isTenMin() and isTwo()):
            gameSurrender()
            break
        click(976, 984, tol=30)
        if isOver():
            gameOver()
            break
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()) or (mode[0] == 4 and isTenMin() and isTwo()):
            gameSurrender()
            break
        click(1181, 988, tol=30)
        if isOver():
            gameOver()
            break
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()) or (mode[0] == 4 and isTenMin() and isTwo()):
            gameSurrender()
            break
        click(1388, 990, tol=30)
        if isOver():
            gameOver()
            break
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()) or (mode[0] == 4 and isTenMin() and isTwo()):
            gameSurrender()
            break
        
        if time.time()-startTime[0] > 900:
            click(370, 964, tol=10)

        if isWin():
            win()
            break

    



def gameSurrender():
    print("항복")

    keyClick('enter')
    keyClick('.')
    keyClick('enter')

    keyClick('enter')
    keyClick('/')
    keyClick('f')
    keyClick('f')
    keyClick('enter')

    keyClick('enter')
    keyClick('/')
    keyClick('w')
    keyClick('w')
    keyClick('enter')

    finalRankingCheck()

    click(922, 608)

    finishing()



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
    print("게임오버 횟수 :", overs[0])
    print("게임승리 횟수 :", wins[0])
    time.sleep(10)






def win():
    click(995, 644)
    print("승리")
    tokenIdx[0] = 3
    wins[0] += 1
    finishing()
        

def gameOver():
    click(890, 534)
    print("게임오버")
    overs[0] += 1
    finalRankingCheck()
    finishing()


def gameRegame():
    print("한판더하기")
    click(863, 844)



def INFloading():
    print("무한로딩 대응")
    click(1579, 174, sleep=1)

    click(912, 564, sleep=60)

    subprocess.call("C:\\Riot Games\\League of Legends\\LeagueClient.exe")

    time.sleep(60)
    onceStart[0] = False
    INFloadings[0] += 1



def partyEx():
    print("파티제외 대응")
    time.sleep(10)
    click(962, 542)
            
    click(482, 202, sleep=1, times=2)

    click(1194, 390, 1)

    click(860, 849, 1)

    partyExcludes[0] += 1
    onceStart[0] = False




    

#==========================메인프레임 구성===================================

def handycalc():
    if isClientPasswordAlt():
        passwordAltOk()
    elif isClientPartyEx():
        partyEx()
    elif isClientHome():
        homeToFind()
    elif isClientAcceptScreen():
        gameAccept()
    elif isClientFindGame():
        gameFind()
    elif isLoadingScreen():
        gameLoading()
    elif isInGame():
        gameStart()
    elif isClientRegame():
        gameRegame()

    else:
        if devMode[0] == False:
            if int(time.time())%40 == 0:
                print("알 수 없는 상황")
        else:
            print("알 수 없는 상황")
        pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))
        time.sleep(1)


def modeSelect():
    print("모드를 선택하십시오")
    print("숫자입력 후 엔터")
    print("1. 10분 서렌")
    print("2. 6등 서렌")
    print("3. 4등 서렌")
    print("4. 2등 서렌")
    print("5. 개발자모드On/Off")
    print("6. 모드 설명")
    print("7. 종료")
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
    print("""
4. 2등이 되면 서렌하는 버전. 8개의 토큰보상.

    """)
    print("""
5. 로그 출력이 지저분해짐.

    """)


def devSwitch():
    if devMode[0] == False:
        print("On")
        devMode[0] == True
    else:
        print("Off")
        devMode[0] == False
    
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

devMode = [False]
overs = [0]
wins = [0]
#============================main===========================================


while True:
    if mode[0] == 0:
        modeSelect()
    elif mode[0] == 1 or mode[0] == 2 or mode[0] == 3 or mode[0] == 4:
        try:
            handycalc()
        except pyautogui.FailSafeException:
            exmenu = int(input("""
일시정지. 메뉴를 고르시오.
1. 돌아가기
2. 종료
3. 버그시 강제 서렌
4. 모드 변경
5. 개발자모드On/Off
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
                modeSelect()
            elif exmenu == 5:
                devSwitch()
            else:
                print("이상한 값 입력. 종료합니다.")
                time.sleep(2)
                sys.exit()
    elif mode[0] == 5:
        devSwitch()
    elif mode[0] == 6:
        modeDemo()
        modeSelect()
    elif mode[0] == 7:
        print("종료")
        time.sleep(2)
        break
    else:
        print("올바른 값을 입력하십시오.")
        mode[0] = 0
        modeSelect()

    



