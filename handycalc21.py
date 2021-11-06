import pyautogui
import random
import time
import sys
import ctypes
import subprocess
import urllib.parse
import json
import msvcrt

# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class InputI(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", InputI)]


# Actuals Functions


def press_key(hex_key_code):
    extra = ctypes.c_ulong(0)
    ii_ = InputI()
    ii_.ki = KeyBdInput(0, hex_key_code, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def release_key(hex_key_code):
    extra = ctypes.c_ulong(0)
    ii_ = InputI()
    ii_.ki = KeyBdInput(0, hex_key_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


key_map = {
    'w': 17,
    'e': 18,
    'a': 30,
    's': 31,
    'd': 32,
    'm': 50,
    'p': 25,
    'enter': 28,
    'esc': 1,
    'up': 200,
    'down': 208,
    'left': 203,
    'right': 205,
    'backspace': 14,
    '/': 53,
    '.': 52,
    'g': 34,
    'f': 33,
}


# ==============================체크함수들======================================
def is_client_password_alt():
    if (pyautogui.pixelMatchesColor(766, 449, (1, 10, 19)) and pyautogui.pixelMatchesColor(770, 584, (1, 10, 19))
            and pyautogui.pixelMatchesColor(1147, 462, (1, 10, 19))
            and pyautogui.pixelMatchesColor(1131, 581, (1, 10, 19))):
        print("비밀번호변경 확인창 인식")
        return True
    else:
        return False


def is_client_home():
    if (not pyautogui.pixelMatchesColor(501, 189, (30, 35, 40))
    and pyautogui.pixelMatchesColor(482, 200, (30, 35, 40))):
        print("홈화면 인식")
        return True
    else:
        return False


def is_client_find_game():
    if (pyautogui.pixelMatchesColor(1175, 276, (30, 35, 40))
            and pyautogui.pixelMatchesColor(915, 838, (30, 35, 40))
            and pyautogui.pixelMatchesColor(490, 201, (30, 35, 40))
            and not pyautogui.pixelMatchesColor(940, 850, (30, 35, 40))
            and pyautogui.pixelMatchesColor(380, 840, (1, 10, 19))):
        print("게임찾기 인식")
        return True
    else:
        return False


def is_client_accept_screen():
    if ((not pyautogui.pixelMatchesColor(1000, 794, (92, 91, 87)))
            and pyautogui.pixelMatchesColor(921, 780, (30, 35, 40))
            and pyautogui.pixelMatchesColor(991, 779, (30, 35, 40))):
        print("수락창 인식")
        return True
    else:
        return False


def is_loading_screen():
    if pyautogui.pixelMatchesColor(977, 1072, (0, 11, 19)):
        return True
    else:
        return False


def is_in_game():
    if pyautogui.pixelMatchesColor(1919, 395, (24, 32, 33)) or pyautogui.pixelMatchesColor(1919, 780, (24, 32, 33)):
        print("인게임 인식")
        return True
    else:
        return False


def is_ten_min():
    if time.time() - startTime[0] > 600:
        tokenIdx[0] = 0
        return True
    else:
        return False


def is_achromatic(x, y):
    red, green, blue = pyautogui.pixel(x, y)
    rgb_tuple = (red, green, blue)
    if (rgb_tuple == (0, 0, 0) or rgb_tuple == (240, 240, 240) or rgb_tuple == (205, 205, 205)
            or rgb_tuple == (96, 96, 96) or rgb_tuple == (47, 47, 47) or rgb_tuple == (12, 12, 12)
            or rgb_tuple == (204, 204, 204)):
        return False
    avg_val = (red + green + blue) / 3
    if abs(red - avg_val) <= 0.1 and abs(green - avg_val) <= 0.1 and abs(blue - avg_val) <= 0.1:
        return True
    else:
        return False


def is_six():
    if (is_achromatic(Xserr, Yserr - 72) or is_achromatic(Xserr, Yserr - 72 * 2) or is_achromatic(Xserr, Yserr - 72 * 3)
            or is_achromatic(Xserr, Yserr - 72 * 4) or is_achromatic(Xserr, Yserr - 72 * 5)):
        tokenIdx[0] = 1
        return True
    else:
        return False


def is_four():
    if (is_achromatic(Xserr, Yserr - 72 * 3) or is_achromatic(Xserr, Yserr - 72 * 4)
            or is_achromatic(Xserr, Yserr - 72 * 5)):
        tokenIdx[0] = 2
        return True
    else:
        return False


def is_two():
    if is_achromatic(Xserr, Yserr - 72 * 5):
        tokenIdx[0] = 3
        return True
    else:
        return False


def is_win():
    if pyautogui.pixelMatchesColor(995, 644, (132, 15, 16), 1):
        return True
    else:
        return False


def is_over():
    if pyautogui.pixelMatchesColor(835, 577, (32, 30, 26), 1):
        return True
    else:
        return False


def final_ranking_check():
    if is_two():
        print("1~2등")
        tokenIdx[0] = 3
    elif is_four():
        print("3~4등")
        tokenIdx[0] = 2
    elif is_six():
        print("5~6등")
        tokenIdx[0] = 1


def is_client_regame():
    if ((not pyautogui.pixelMatchesColor(1175, 276, (30, 35, 40)))
            and pyautogui.pixelMatchesColor(917, 844, (30, 35, 40))):
        print("한판더하기 인식")
        return True
    else:
        return False


def is_client_party_ex():
    if (pyautogui.pixelMatchesColor(816, 485, (1, 10, 19)) and pyautogui.pixelMatchesColor(1100, 551, (1, 10, 19))
            and pyautogui.pixelMatchesColor(1097, 489, (1, 10, 19))
            and pyautogui.pixelMatchesColor(817, 550, (1, 10, 19))
            and (not pyautogui.pixelMatchesColor(971, 675, (1, 10, 19)))):
        print("파티제외 인식")
        return True
    else:
        return False


def lessthansixteen():  # 더이상 쓰지 않는 함수
    if time.time() - startTime[0] < 960:
        return True
    elif is_four():
        tokenIdx[0] = 2
        return True
    else:
        return False


def check_button1():  # 게임끝나고 토큰보상 및 퀘스트보상 수락 버튼
    if (pyautogui.pixelMatchesColor(905, 828, (30, 35, 40)) and pyautogui.pixelMatchesColor(1015, 831, (30, 35, 40))
            and pyautogui.pixelMatchesColor(1016, 848, (30, 35, 40))
            and pyautogui.pixelMatchesColor(904, 847, (30, 35, 40))):
        return True
    else:
        return False


# ====================================행동함수들==================================
def current_time():
    print(time.strftime("%I:%M %p", time.localtime(time.time())))


def click(x, y, sleep=0, sec=0.5, times=1, tol=2):
    pyautogui.failSafeCheck()
    if devMode[0] is True:
        return
    pyautogui.moveTo(x + random.uniform(-tol, tol), y + random.uniform(-tol, tol),
                     random.uniform(sec - sec / 4, sec + sec / 4))
    for _ in range(times):
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.08, 0.12))
        pyautogui.mouseUp()
    time.sleep(sleep)


def key_click(key):
    pyautogui.failSafeCheck()
    if devMode[0] is True:
        return
    if key not in key_map or key_map[key] is None:
        return
    key_val = key_map[key]
    press_key(key_val)
    time.sleep(random.uniform(0.05, 0.1))
    release_key(key_val)


def password_alt_ok():
    print("비밀번호변경 확인")
    click(960, 601)
    time.sleep(1)


def home_to_find():
    click(482, 202, times=2, sleep=2)

    click(1037, 487, sleep=2)

    click(860, 849, sleep=2)


def game_find():
    print("게임찾기")
    if onceStart[0] is False:
        loadTimeStart[0] = time.time()

    onceStart[0] = True
    click(866, 837)


def game_accept():
    print('게임수락')
    click(967, 706)
    time.sleep(1)


def game_loading():
    global bot_players
    count = 0
    if hybrid_switch[0] > 0 and load_profile_got[0] is False:
        load_profile1_capture = pyautogui.screenshot(region=(410, 485, 235, 21))
        load_profile2_capture = pyautogui.screenshot(region=(410 + 288, 485, 235, 21))
        load_profile3_capture = pyautogui.screenshot(region=(410 + 288 * 2, 485, 235, 21))
        load_profile4_capture = pyautogui.screenshot(region=(410 + 288 * 3, 485, 235, 21))
        load_profile5_capture = pyautogui.screenshot(region=(410, 485 + 540, 235, 21))
        load_profile6_capture = pyautogui.screenshot(region=(410 + 288, 485 + 540, 235, 21))
        load_profile7_capture = pyautogui.screenshot(region=(410 + 288 * 2, 485 + 540, 235, 21))
        load_profile8_capture = pyautogui.screenshot(region=(410 + 288 * 3, 485 + 540, 235, 21))

        load_profile_imgs = [np.array(load_profile1_capture), np.array(load_profile2_capture),
                             np.array(load_profile3_capture), np.array(load_profile4_capture),
                             np.array(load_profile5_capture), np.array(load_profile6_capture),
                             np.array(load_profile7_capture), np.array(load_profile8_capture)]

        load_profile_grays = [cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) for img in load_profile_imgs]

        players = list(pytesseract.image_to_string(gray, lang='eng+kor', config='--psm 7').replace(' ', '').replace('\n', '')[:-1] for gray in load_profile_grays)

        if hybrid_switch[0] > 0:
            with open("bot_players.json", 'r', encoding="utf8") as bot_players_json:
                bot_players = json.load(bot_players_json)

        log_file = open("log.txt", 'a', encoding="utf8")
        log_file.write(time.strftime("%m.%d. %I:%M %p", time.localtime(time.time()))+'\n')
        if hybrid_switch[0] == 1:
            for player in players:
                log_file.write(player+'\n')
                if player in bot_players and sum(bot_players[player])/len(bot_players[player]) < 660:
                    count += 1
                    print(player)
                    log_file.write(player+'\n')
        elif hybrid_switch[0] == 2:
            for player in players:
                log_file.write(player+'\n')
                if player in bot_players and sum(bot_players[player])/len(bot_players[player]) < 720:
                    count += 1
                    print(player)
                    log_file.write(player+'\n')
        elif hybrid_switch[0] == 3:
            for player in players:
                log_file.write(player+'\n')
                if player in bot_players and sum(bot_players[player])/len(bot_players[player]) < 780:
                    count += 1
                    print(player)
                    log_file.write(player+'\n')

        if 6 <= count:
            mode[0] = 4
            print("2등 set")
            log_file.write("2등 set"+'\n')
        elif 4 <= count <= 5:
            mode[0] = 4
            print("4등 set")
            log_file.write("4등 set"+'\n')
        elif 2 <= count <= 3:
            mode[0] = 3
            print("6등 set")
            log_file.write("6등 set"+'\n')
        elif count <= 1:
            mode[0] = 3
            print("8등 set")
            log_file.write("8등 set"+'\n')
        log_file.close()

        load_profile_got[0] = True

    if devMode[0] is False:
        pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))
    elif devMode[0] is True:
        if int(time.time()) % 2 == 0:
            print("time.time()-startTime[0] :", int(time.time() - startTime[0]))
            print("time.time() - loadTimeStart[0] :", int(time.time() - loadTimeStart[0]))


def game_start():
    if isStart[0] is False:
        startTime[0] = time.time()
        print("게임시작")
        isStart[0] = True
    if loadValIn[0] is False:
        loadTime[0] = time.time() - loadTimeStart[0]
        loadValIn[0] = True

    capture = False

    load_profile_got[0] = False
    print("인게임")
    time.sleep(20)

    while True:  # 챔피언픽

        if is_over():
            game_over()
            break
        if ((mode[0] == 1 and is_ten_min()) or (mode[0] == 2 and is_ten_min() and is_six())
                or (mode[0] == 3 and is_ten_min() and is_four()) or (mode[0] == 4 and is_ten_min() and is_two())):
            if mode[0] == 1:
                pass
            else:
                time.sleep(35)
            game_surrender()
            break
        click(576, 990, tol=30)
        if is_over():
            game_over()
            break
        if ((mode[0] == 1 and is_ten_min()) or (mode[0] == 2 and is_ten_min() and is_six())
                or (mode[0] == 3 and is_ten_min() and is_four()) or (mode[0] == 4 and is_ten_min() and is_two())):
            if mode[0] == 1:
                pass
            else:
                time.sleep(35)
            game_surrender()
            break
        click(778, 988, tol=30)
        if is_over():
            game_over()
            break
        if ((mode[0] == 1 and is_ten_min()) or (mode[0] == 2 and is_ten_min() and is_six())
                or (mode[0] == 3 and is_ten_min() and is_four()) or (mode[0] == 4 and is_ten_min() and is_two())):
            if mode[0] == 1:
                pass
            else:
                time.sleep(35)
            game_surrender()
            break
        click(976, 984, tol=30)
        if is_over():
            game_over()
            break
        if ((mode[0] == 1 and is_ten_min()) or (mode[0] == 2 and is_ten_min() and is_six())
                or (mode[0] == 3 and is_ten_min() and is_four()) or (mode[0] == 4 and is_ten_min() and is_two())):
            if mode[0] == 1:
                pass
            else:
                time.sleep(35)
            game_surrender()
            break
        click(1181, 988, tol=30)
        if is_over():
            game_over()
            break
        if ((mode[0] == 1 and is_ten_min()) or (mode[0] == 2 and is_ten_min() and is_six())
                or (mode[0] == 3 and is_ten_min() and is_four()) or (mode[0] == 4 and is_ten_min() and is_two())):
            if mode[0] == 1:
                pass
            else:
                time.sleep(35)
            game_surrender()
            break
        click(1388, 990, tol=30)
        if is_over():
            game_over()
            break
        if ((mode[0] == 1 and is_ten_min()) or (mode[0] == 2 and is_ten_min() and is_six())
                or (mode[0] == 3 and is_ten_min() and is_four()) or (mode[0] == 4 and is_ten_min() and is_two())):
            if mode[0] == 1:
                pass
            else:
                time.sleep(35)
            game_surrender()
            break

        if time.time() - startTime[0] > 900:
            click(370, 964, tol=10)

        if is_win():
            win()
            break

        if devMode[0] is False:
            pass
        elif devMode[0] is True:
            if int(time.time()) % 2 == 0:
                print("time.time()-startTime[0] :", int(time.time() - startTime[0]))
                print("time.time() - loadTimeStart[0] :", int(time.time() - loadTimeStart[0]))

        if time.time() - startTime[0] > 60 * 18 and capture == False:
            pyautogui.hotkey('alt', 'f10')
            capture = True

        if pyautogui.pixelMatchesColor(1145, 225, (1, 10, 19)):
            time.sleep(5)
            pyautogui.hotkey('alt', 'tab')

def print_token_idx():
    if tokenIdx[0] == 3:
        print("1~2등")
    elif tokenIdx[0] == 2:
        print("3~4등")
    elif tokenIdx[0] == 1:
        print("5~6등")
    elif tokenIdx[0] == 0:
        print("7~8등")


def game_surrender():
    if devMode[0] is True:
        pyautogui.hotkey('alt', 'f1')
        pyautogui.hotkey('win', 'alt', 'prtscr')
    print("항복")

    if is_win() is True:
        tokenIdx[0] = 3
    elif is_over() is True:
        pass
    elif is_two() is True:
        tokenIdx[0] = 3
    elif is_four() is True:
        tokenIdx[0] = 2
    elif is_six() is True:
        tokenIdx[0] = 1

    key_click('enter')
    key_click('.')
    key_click('enter')

    key_click('enter')
    key_click('/')
    key_click('f')
    key_click('f')
    key_click('enter')

    key_click('enter')
    key_click('/')
    key_click('w')
    key_click('w')
    key_click('enter')

    sys.stdout.flush()
    while msvcrt.kbhit():
        msvcrt.getch()

    print_token_idx()

    click(836, 486)

    finishing()


def finishing():
    playTime[0] = time.time() - startTime[0]

    loadTimelist.append(loadTime[0])
    playTimelist.append(playTime[0])
    tokenGetList.append(tokenList[tokenIdx[0]])

    loadTimeStart[0] = time.time()
    isStart[0] = False
    loadValIn[0] = False

    current_time()
    plays[0] += 1
    print("플레이 횟수 :", plays[0])
    print("이번 판 큐+로딩시간 : %imin%isec, \n이번 판 인게임시간 : %imin%isec" % (loadTime[0] / 60,
                                                                   loadTime[0] % 60,
                                                                   playTime[0] / 60, playTime[0] % 60))
    print("평균 큐+로딩시간 : %imin%isec, \n평균 인게임시간 : %imin%isec" % (sum(loadTimelist) / len(loadTimelist) / 60,
                                                               (sum(loadTimelist) / len(loadTimelist)) % 60,
                                                               sum(playTimelist) / len(playTimelist) / 60,
                                                               (sum(playTimelist) / len(playTimelist)) % 60))
    print("총 토큰획득(추정치) :", sum(tokenGetList))
    print("이번 판 시간당 토큰획득 : %.2f" % (tokenList[tokenIdx[0]] / (loadTime[0] + playTime[0]) * 3600))
    print("시간당 토큰획득(추정치) : %.2f" % (sum(tokenGetList) / (sum(loadTimelist) + sum(playTimelist)) * 3600))
    print("재시작 횟수 :", INFloadings[0])
    print("파티제외 횟수 :", partyExcludes[0])
    print("게임오버 횟수 :", overs[0])
    print("게임승리 횟수 :", wins[0])

    if playTime[0] < 500:
        pyautogui.hotkey("alt", "f10")
    
    while True:
        time.sleep(1)
        if pyautogui.pixelMatchesColor(1919, 300, (12, 12, 12)):
            break


def win():
    if devMode[0] is True:
        pyautogui.hotkey('alt', 'f1')
        pyautogui.hotkey('win', 'alt', 'prtscr')
    click(995, 644)
    print("승리")
    tokenIdx[0] = 3
    wins[0] += 1
    finishing()


def game_over():
    if devMode[0] is True:
        pyautogui.hotkey('alt', 'f1')
        pyautogui.hotkey('win', 'alt', 'prtscr')
    click(835, 550)
    print("게임오버")
    overs[0] += 1
    final_ranking_check()
    finishing()


def game_regame():
    global bot_players
    print("한판더하기")
    if hybrid_switch[0] > 0:
        with open("token.txt", 'r', encoding="utf8") as token_txt:
            summoner_token, summoner_name, exceptions = token_txt.read().split('\n')
        exceptions = list(exceptions.replace(' ', '').split(','))
        custom_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": summoner_token
        }

        riot_url1 = "https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/"+urllib.parse.quote(summoner_name)
        res1 = requests.get(riot_url1, headers=custom_headers)
        if res1.status_code != 200:
            click(863, 844)
            time.sleep(1)
            return
        time.sleep(0.05)
        summoner_puuid = res1.json()["puuid"]

        riot_url2 = "https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/" + summoner_puuid + "/ids?count=5"
        res2 = requests.get(riot_url2, headers=custom_headers)
        if res2.status_code != 200:
            click(863, 844)
            time.sleep(1)
            return
        time.sleep(0.05)
        match_ids = res2.json()

        for match_id in match_ids:
            riot_url3 = "https://asia.api.riotgames.com/tft/match/v1/matches/" + match_id
            res3 = requests.get(riot_url3, headers=custom_headers)
            if res3.status_code != 200:
                click(863, 844)
                time.sleep(1)
            time.sleep(0.05)
            res3 = res3.json()

            with open("bot_players.json", 'r', encoding="utf8") as bot_players_json:
                bot_players = json.load(bot_players_json)

            for player in res3["info"]["participants"]:
                if player["time_eliminated"] < 780:
                    riot_url4 = "https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/" + player["puuid"]
                    res4 = requests.get(riot_url4, headers=custom_headers)
                    if res4.status_code != 200:
                        click(863, 844)
                        time.sleep(1)
                    time.sleep(0.05)
                    player_name = res4.json()["name"].replace(' ', '')
                    if (player_name in bot_players
                            and player_name not in exceptions
                            and player["time_eliminated"] not in bot_players[player_name]):
                        bot_players[player_name].append(player["time_eliminated"])
                    elif player_name not in exceptions:
                        bot_players[player_name] = [player["time_eliminated"]]

        with open("bot_players.json", 'w', encoding="utf8") as bot_players_json:
            json.dump(bot_players, bot_players_json, indent=4, ensure_ascii=False)

    click(863, 844)
    time.sleep(1)


def inf_loading():
    print("무한로딩 대응")
    click(1579, 174, sleep=1)

    click(912, 564, sleep=60)

    click(1712, 120, sleep=60)

    subprocess.call("C:\\Riot Games\\League of Legends\\LeagueClient.exe")

    time.sleep(60)
    loadTimeStart[0] = time.time()
    onceStart[0] = False
    INFloadings[0] += 1


def party_ex():
    print("파티제외 대응")
    time.sleep(1)
    click(962, 542 + 3)
    time.sleep(1)

    partyExcludes[0] += 1
    onceStart[0] = False


def button1():
    click(959, 839)


# ==========================메인프레임 구성===================================

def handycalc():
    if is_client_password_alt():
        password_alt_ok()
    elif is_client_home():
        home_to_find()
    elif is_client_party_ex():
        party_ex()
    elif is_client_accept_screen():
        game_accept()
    elif is_client_find_game():
        game_find()
    elif is_loading_screen():
        game_loading()
    elif is_in_game():
        game_start()
    elif check_button1():
        button1()
    elif is_client_regame():
        game_regame()

    else:
        if int(time.time()) % 40 == 0:
            print("알 수 없는 상황")
        if devMode[0] is False:
            pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))
        elif devMode[0] is True:
            if int(time.time()) % 2 == 0:
                print("time.time()-startTime[0] :", int(time.time() - startTime[0]))
                print("time.time() - loadTimeStart[0] :", int(time.time() - loadTimeStart[0]))
        time.sleep(1)
        if onceStart[0] is False:
            loadTimeStart[0] = time.time()
        if loadValIn[0] is False and time.time() - loadTimeStart[0] > 600:
            inf_loading()


def mode_select():
    print("모드를 선택하십시오")
    print("숫자입력 후 엔터")
    print("1. 10분 서렌")
    print("2. 6등 서렌")
    print("3. 4등 서렌")
    print("4. 2등 서렌")
    print("5. 개발자모드On/Off")
    print("6. 모드 설명")
    print("7. 종료")
    print("8. 끝날때까지")
    print("9. hybrid-under11")
    print("10. hybrid-under12")
    print("11. hybrid-under13")
    try:
        mode[0] = int(input())
        if 9 <= mode[0] <= 11:
            hybrid_switch[0] = 0
    except ValueError:
        print("인풋에러, 올바른 값을 입력하시오")
        mode[0] = 0


def mode_demo():
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
5. 게임종료시 스크린샷.

    """)


def dev_switch():
    if devMode[0] is False:
        print("On")
        devMode[0] = True
    else:
        print("Off")
        devMode[0] = False
    mode[0] = 0


# =============================var================================

tokenList = (2, 4, 6, 8, 10)
tokenIdx = [0]
mode = [0]

plays = [0]  # 매크로 실행횟수
onceStart = [False]
loadTimelist = []
playTimelist = []
tokenGetList = []

loadTimeStart = [0.0]
startTime = [0.0]
loadTime = [0.0]
playTime = [0.0]
loadValIn = [False]
isStart = [False]
INFloadings = [0]
partyExcludes = [0]

Xserr = 1870
Yserr = 737

devMode = [False]
overs = [0]
wins = [0]
hybrid_switch = [0]
load_profile_got = [False]
hybrid_imported = [False]


# ============================main===========================================
if __name__ == "__main__":

    while True:
        if mode[0] == 0:
            mode_select()
        elif (mode[0] == 1 or mode[0] == 2 or mode[0] == 3 or mode[0] == 4 or mode[0] == 8
              or (1 <= hybrid_switch[0] <= 3)):
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
6. hybrid 스위치 Off
"""))
                if exmenu == 1:
                    "게임으로 돌아갑니다."
                elif exmenu == 2:
                    print("종료합니다.")
                    time.sleep(2)
                    sys.exit()
                elif exmenu == 3:
                    print("강제로 서렌 합니다.")
                    game_surrender()
                elif exmenu == 4:
                    mode_select()
                elif exmenu == 5:
                    dev_switch()
                elif exmenu == 6:
                    hybrid_switch[0] = 0
                    mode[0] = 0
                else:
                    print("이상한 값 입력. 종료합니다.")
                    time.sleep(2)
                    sys.exit()
        elif mode[0] == 5:
            dev_switch()
        elif mode[0] == 6:
            mode_demo()
            mode_select()
        elif mode[0] == 7:
            print("종료")
            time.sleep(2)
            break
        elif 9 <= mode[0] <= 11:
            if hybrid_imported[0] is False:
                import cv2
                import numpy as np
                import pytesseract
                import requests

                pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
                hybrid_imported[0] = True
            hybrid_switch[0] = mode[0] - 8
            mode[0] = 3
        else:
            print("올바른 값을 입력하십시오.")
            mode[0] = 0
            mode_select()

# =====================================data======================================

    bot_players = []
