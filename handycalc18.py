import pyautogui as pag
import random
import time
import sys
import ctypes
import subprocess

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


def INFloading():
    pag.moveTo(1579 + random.uniform(-1, 1), 174 + random.uniform(-1, 1), random.uniform(0.8, 0.12))
    pag.mouseDown()
    time.sleep(random.uniform(0.08, 0.12))
    pag.mouseUp()

    time.sleep(1)

    pag.moveTo(912 + random.uniform(-1, 1), 564 + random.uniform(-1, 1), random.uniform(0.8, 0.12))
    pag.mouseDown()
    time.sleep(random.uniform(0.08, 0.12))
    pag.mouseUp()

    time.sleep(60)

    subprocess.call("C:\\Riot Games\\League of Legends\\LeagueClient.exe")

    time.sleep(60)

    while True:
        if passwordAltCheck():
            passwordAltOk()
        if pag.pixelMatchesColor(482, 202, (30, 35, 40)):
            pag.moveTo(482 + random.uniform(-2, 2), 202 + random.uniform(-2, 2), random.uniform(0.8, 0.12))
            pag.mouseDown()
            time.sleep(random.uniform(0.08, 0.12))
            pag.mouseUp()
            pag.mouseDown()
            time.sleep(random.uniform(0.08, 0.12))
            pag.mouseUp()

            time.sleep(1)

            pag.moveTo(1194 + random.uniform(-2, 2), 390 + random.uniform(-2, 2), random.uniform(0.8, 0.12))
            pag.mouseDown()
            time.sleep(random.uniform(0.08, 0.12))
            pag.mouseUp()

            time.sleep(1)

            pag.moveTo(860 + random.uniform(-2, 2), 849 + random.uniform(-2, 2), random.uniform(0.8, 0.12))
            pag.mouseDown()
            time.sleep(random.uniform(0.08, 0.12))
            pag.mouseUp()

            time.sleep(1)

            onceStart[0] = False
            INFloadings[0] += 1
            break




def loadingScreenCheck():
    if pag.pixelMatchesColor(977, 1072, (0, 11, 19)):
        print("????????? ??????")
        return True
    else:
        return False


def startedCheck():
    if pag.pixelMatchesColor(1919, 395, (24, 32, 33)):
        print("?????? ??????")
        return True
    else:
        return False


def regameScreenCheck():
    if pag.pixelMatchesColor(803, 844, (30, 35, 40)):
        print("??????????????? ??????")
        return True
    else:
        return False


def findgameScreenCheck():
    if pag.pixelMatchesColor(1147, 266, (30, 35, 40)) or pag.pixelMatchesColor(1147, 266, (11, 13, 15)) or pag.pixelMatchesColor(1147, 266, (1, 10, 19)):
        print("???????????? ??????")
        return True
    else:
        return False


def isSix():
    if pag.pixelMatchesColor(1836, 738, (22, 24, 33)) and pag.pixelMatchesColor(1854, 743, (22, 24, 33)) and pag.pixelMatchesColor(1836, 738-71, (22, 24, 33)) and pag.pixelMatchesColor(1854, 671, (22, 24, 33)):
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
    elif pag.pixelMatchesColor(1836, 738, (22, 24, 33)) and pag.pixelMatchesColor(1854, 743, (22, 24, 33)) and pag.pixelMatchesColor(1836, 738-71, (22, 24, 33)) and pag.pixelMatchesColor(1854, 671, (22, 24, 33)) and pag.pixelMatchesColor(1836, 595, (22, 24, 33)) and pag.pixelMatchesColor(1854, 599, (22, 24, 33)) and pag.pixelMatchesColor(1836, 522, (22, 24, 33)) and pag.pixelMatchesColor(1854, 527, (22, 24, 33)):
        tokenIdx[0] = 2
        return True
    else:
        return False


def isFour():
    if pag.pixelMatchesColor(1836, 738, (22, 24, 33)) and pag.pixelMatchesColor(1854, 743, (22, 24, 33)) and pag.pixelMatchesColor(1836, 738-71, (22, 24, 33)) and pag.pixelMatchesColor(1854, 671, (22, 24, 33)) and pag.pixelMatchesColor(1836, 595, (22, 24, 33)) and pag.pixelMatchesColor(1854, 599, (22, 24, 33)) and pag.pixelMatchesColor(1836, 522, (22, 24, 33)) and pag.pixelMatchesColor(1854, 527, (22, 24, 33)):
        tokenIdx[0] = 2
        return True
    else:
        return False    


def passwordAltCheck():
    if pag.pixelMatchesColor(766, 449, (1, 10, 19)) and pag.pixelMatchesColor(770, 584, (1, 10, 19)) and pag.pixelMatchesColor(1147, 462, (1, 10, 19)) and pag.pixelMatchesColor(1131, 581, (1, 10, 19)):
        print("?????????????????? ????????? ??????")
        return True
    else:
        return False


def acceptScreenCheck():
    if pag.pixelMatchesColor(921, 780, (30, 35, 40)) and pag.pixelMatchesColor(991, 779, (30, 35, 40)):
        print("????????? ??????")
        return True
    else:
        return False


def finalRankingCheck():
    if pag.pixelMatchesColor(1836, 738, (22, 24, 33)) and pag.pixelMatchesColor(1854, 743, (22, 24, 33)) and pag.pixelMatchesColor(1836, 738-71, (22, 24, 33)) and pag.pixelMatchesColor(1854, 671, (22, 24, 33)) and pag.pixelMatchesColor(1836, 595, (22, 24, 33)) and pag.pixelMatchesColor(1854, 599, (22, 24, 33)) and pag.pixelMatchesColor(1836, 522, (22, 24, 33)) and pag.pixelMatchesColor(1854, 527, (22, 24, 33)):
        print("3~4???")
        tokenIdx[0] = 2
    elif pag.pixelMatchesColor(1836, 738, (22, 24, 33)) and pag.pixelMatchesColor(1854, 743, (22, 24, 33)) and pag.pixelMatchesColor(1836, 738-71, (22, 24, 33)) and pag.pixelMatchesColor(1854, 671, (22, 24, 33)):
        print("5~6???")
        tokenIdx[0] = 1



def modeSelect():
    print("????????? ??????????????????")
    print("1. 10??? ??????")
    print("2. 6??? ??????")
    print("3. 4??? ??????")
    print("4. ?????? ??????")
    print("5. ??????")
    try:
        mode[0] = int(input())
    except:
        print("????????????, ????????? ?????? ???????????????")
        mode[0] = 0


def modeDemo():
    print("""\n\n
1. 10?????? ?????? ???????????? ??????. ?????? ?????????????????? 2???????????? ????????? 10??? ??????.

    """)
    print("""
2. 6?????? ?????? ???????????? ??????. 10??????????????? ?????? 2??? ??? ?????? 4??? ????????? ??????. 
?????????????????? ?????? ????????? ?????? ????????? ????????? ??????.

    """)
    print("""
3. 4?????? ?????? ???????????? ??????. 6?????? ????????????.
mmr??? ????????? ???????????? ????????? ????????? ??????????????? ??????.

    """)


def gameFind():
    print("????????????")
    if not onceStart[0]:
        loadTimeStart[0] = time.time()
    
    onceStart[0] = True
    while True:  # ??????????????????
        if acceptScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        pag.moveTo(random.uniform(790, 941), random.uniform(823, 851), random.uniform(0.8, 0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pag.mouseUp()
        if time.time() - loadTimeStart[0] > 1800:
            INFloading()
            break


def gameAccept():
    print('????????????')
    while True:
        if loadingScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        pag.moveTo(random.uniform(884+16, 1033), random.uniform(700, 726-15), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3, 0.7))
        pag.mouseUp()
        if time.time() - loadTimeStart[0] > 1800:
            INFloading()
            break
        


def gameLoading():
    print("??????")
    while True:
        if startedCheck():
            break

    loadTime[0] = time.time()-loadTimeStart[0]
    loadValIn[0] = True



def gameStart():
    if not isStart[0]:
        startTime[0] = time.time()
        print("?????? ??????")
        isStart[0] = True
    if not loadValIn[0]:
        loadTime[0] = time.time()-loadTimeStart[0]
        loadValIn[0] = True


    while True:  # ????????????

        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pag.moveTo(random.uniform(485, 667), random.uniform(
            932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pag.moveTo(random.uniform(485+200, 667+200), random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pag.moveTo(random.uniform(485+400, 667+400),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pag.moveTo(random.uniform(485+600, 667+600),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        pag.moveTo(random.uniform(485+800, 667+800),
                   random.uniform(932, 1032-50), random.uniform(0.25, 0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.05, 0.1))
        pag.mouseUp()
        if (mode[0] == 1 and isTenMin()) or (mode[0] == 2 and isTenMin() and isSix()) or (mode[0] == 3 and isTenMin() and isFour()):
            break
        if time.time()-startTime[0] > 900:
            pag.moveTo(random.uniform(278, 462), random.uniform(931, 992), random.uniform(0.25, 0.75))
            pag.mouseDown()
            time.sleep(random.uniform(0.05, 0.1))
            pag.mouseUp()

        if pag.pixelMatchesColor(880, 533, (8, 81, 100)):
            if pag.pixelMatchesColor(1836, 600, (22, 24, 33)) and pag.pixelMatchesColor(1836, 527, (22, 24, 33)) and pag.pixelMatchesColor(1854, (679 - 73), (22, 24, 33)) and pag.pixelMatchesColor(1854, (679 - 73*2), (22, 24, 33)):
                tokenIdx[0] = 2
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("???????????? 4???")
                break
            elif pag.pixelMatchesColor(1836, 600, (22, 24, 33)) and pag.pixelMatchesColor(1854, (679 - 73), (22, 24, 33)):
                tokenIdx[0] = 1
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("???????????? 5???")
                break
            elif pag.pixelMatchesColor(1854, 679, (22, 24, 33)) and pag.pixelMatchesColor(1854, 752, (22, 24, 33)) and pag.pixelMatchesColor(1836, 747, (22, 24, 33)) and pag.pixelMatchesColor(1836, 673, (22, 24, 33)):
                tokenIdx[0] = 1
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("???????????? 6???")
                break
            elif pag.pixelMatchesColor(1854, 752, (22, 24, 33)) and pag.pixelMatchesColor(1836, 747, (22, 24, 33)):
                tokenIdx[0] = 0
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("???????????? 7???")
                break
            else:
                tokenIdx[0] = 0
                pag.moveTo(880 + random.uniform(-2, 2), 533 + random.uniform(-2, 2), random.uniform(0.25, 0.75))
                pag.mouseDown()
                time.sleep(random.uniform(0.05, 0.1))
                pag.mouseUp()
                print("???????????? 8????")
                break

    gameSurrender()


def gameSurrender():
    print("??????")


# ??????
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
    finalRankingCheck()
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
    print("????????? ?????? :", plays[0])
    print("?????? ??? ???+???????????? : %imin%isec, \n?????? ??? ??????????????? : %imin%isec"  %(loadTime[0]/60, loadTime[0]%60, playTime[0]/60, playTime[0]%60,))
    print("?????? ???+???????????? : %imin%isec, \n?????? ??????????????? : %imin%isec" %(sum(loadTimelist)/len(loadTimelist)/60, (sum(loadTimelist)/len(loadTimelist))%60, sum(playTimelist)/len(playTimelist)/60, (sum(playTimelist)/len(playTimelist))%60))
    print("??? ????????????(?????????) :", sum(tokenGetList))
    print("?????? ??? ????????? ???????????? : %.2f" %(tokenList[tokenIdx[0]]/(loadTime[0] + playTime[0])*3600))
    print("????????? ????????????(?????????) : %.2f" %(sum(tokenGetList)/(sum(loadTimelist)+sum(playTimelist))*3600))
    print("????????? ?????? :",INFloadings[0])


    while True:  # ?????????????????? ?????????????????????
        if regameScreenCheck():
            break
        if passwordAltCheck():
            passwordAltOk()
        pag.moveTo(981 + random.uniform(-2, 2),
                   838 + random.uniform(-2, 2), random.uniform(0.8, 0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pag.mouseUp()
        


def gameRegame():
# ????????????
    print("???????????????")
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
    print("?????????????????? ??????")
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
        print("??? ??? ?????? ??????")
        time.sleep(1)

    
#=============================var================================

tokenList = (2, 4, 6, 8, 10)
tokenIdx = [0]
mode = [0]

plays = [0]  # ????????? ????????????
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

#============================main===========================================
modeSelect()

while True:
    if mode[0] == 1 or mode[0] == 2 or mode[0] == 3:
        try:
            handycalc()
        except pag.FailSafeException:
            exmenu = int(input("""
????????????. ????????? ????????????.
1. ????????????
2. ??????
3. ????????? ?????? ??????
4. ?????? ??????
"""))
            if exmenu == 1:
                "???????????? ???????????????."
            elif exmenu == 2:
                print("???????????????.")
                time.sleep(2)
                sys.exit()
            elif exmenu == 3:
                print("????????? ?????? ?????????.")
                gameSurrender()
            elif exmenu == 4:
                try:
                    mode[0] = int(input("????????? ???????????????"))
                except:
                    print("????????????, ????????? ?????? ???????????????")
                    mode[0] = 0
            else:
                print("????????? ??? ??????. ???????????????.")
                time.sleep(2)
                sys.exit()

    elif mode[0] == 4:
        modeDemo()
        modeSelect()
    elif mode[0] == 5:
        print("??????")
        time.sleep(2)
        break
    elif mode[0] == 0:
        modeSelect()
    else:
        print("????????? ?????? ??????????????????.")
        mode[0] = 0
        modeSelect()

    



