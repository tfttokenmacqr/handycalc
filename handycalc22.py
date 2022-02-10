import pyautogui
import random
import time
import sys
import ctypes
import subprocess
import msvcrt

# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# 키 입력을 위한 부분. pyautogui의 내장함수로는 게임 내에서의 키 입력이 되지않는다.
# direct x key code에 맞는 입력을 주어야 함

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


# 입력값은 direct x keycode 검색하여 참조
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


class HandyCalc:
    def __init__(self):
        self.mode = 0
        self.tokenList = [0.1, 0.15]
        self.tokenIdx = 0

        self.plays = 0  # 매크로 실행횟수
        self.onceStart = False
        self.loadTimelist = []
        self.playTimelist = []
        self.tokenGetList = []

        self.loadTimeStart = 0.0
        self.startTime = 0.0
        self.loadTime = 0.0
        self.playTime = 0.0
        self.loadValIn = False
        self.isStart = False
        self.INFloadings = 0
        self.partyExcludes = 0

        self.Xserr = 1870
        self.Yserr = 737

        self.devMode = False
        self.overs = 0
        self.wins = 0

    # ==============================체크함수들======================================
    def is_client_password_alt(self):
        """
        패스워드를 변경하시오 창이 떳는지 확인
        """
        if (pyautogui.pixelMatchesColor(766, 449, (1, 10, 19)) and pyautogui.pixelMatchesColor(770, 584, (1, 10, 19))
                and pyautogui.pixelMatchesColor(1147, 462, (1, 10, 19))
                and pyautogui.pixelMatchesColor(1131, 581, (1, 10, 19))):
            print("비밀번호변경 확인창 인식")
            return True
        else:
            return False

    def is_client_home(self):
        """
        홈 화면인지 확인
        """
        if (not pyautogui.pixelMatchesColor(501, 189, (30, 35, 40))
                and pyautogui.pixelMatchesColor(482, 200, (30, 35, 40))):
            print("홈화면 인식")
            return True
        else:
            return False

    def is_client_find_game(self):
        """
        게임찾기 대기실인지 확인
        """
        if (pyautogui.pixelMatchesColor(1175, 276, (30, 35, 40))
                and pyautogui.pixelMatchesColor(915, 838, (30, 35, 40))
                and pyautogui.pixelMatchesColor(490, 201, (30, 35, 40))
                and not pyautogui.pixelMatchesColor(940, 850, (30, 35, 40))
                and pyautogui.pixelMatchesColor(380, 840, (1, 10, 19))):
            print("게임찾기 인식")
            return True
        else:
            return False

    def is_client_accept_screen(self):
        """
        게임 큐가 잡히고 수락 확인창이 떳는지 확인
        """
        if ((not pyautogui.pixelMatchesColor(1000, 794, (92, 91, 87)))
                and pyautogui.pixelMatchesColor(921, 780, (30, 35, 40))
                and pyautogui.pixelMatchesColor(991, 779, (30, 35, 40))):
            print("수락창 인식")
            return True
        else:
            return False

    def is_loading_screen(self):
        """
        게임로딩창인지 확인
        """
        if pyautogui.pixelMatchesColor(977, 1072, (0, 11, 19)):
            return True
        else:
            return False

    def is_in_game(self):
        """
        게임이 시작됐는지 확인
        """
        if pyautogui.pixelMatchesColor(1919, 395, (24, 32, 33)) or pyautogui.pixelMatchesColor(1919, 780, (24, 32, 33)):
            print("인게임 인식")
            return True
        else:
            return False

    def is_ten_min(self):
        """
        게임이 시작되고 10분이 지났는지 확인
        """
        if time.time() - self.startTime > 600:
            self.tokenIdx = 0
            return True
        else:
            return False

    def is_achromatic(self, x, y):
        """
        x, y 지점의 픽셀값이 흑백인지 확인
        """
        red, green, blue = pyautogui.pixel(x, y)
        rgb_tuple = (red, green, blue)

        # 밑에는 몇몇 예외로 하는 값들
        if (rgb_tuple == (0, 0, 0) or rgb_tuple == (240, 240, 240) or rgb_tuple == (205, 205, 205)
                or rgb_tuple == (96, 96, 96) or rgb_tuple == (47, 47, 47) or rgb_tuple == (12, 12, 12)
                or rgb_tuple == (204, 204, 204)):
            return False
        avg_val = (red + green + blue) / 3
        if abs(red - avg_val) <= 0.1 and abs(green - avg_val) <= 0.1 and abs(blue - avg_val) <= 0.1:
            return True
        else:
            return False

    def is_six(self):
        """
        현재 남은 사람이 6명 이하 인지(등수가 6등 이상 인지) 확인
        """
        if (self.is_achromatic(self.Xserr, self.Yserr - 72) or
                self.is_achromatic(self.Xserr, self.Yserr - 72 * 2) or
                self.is_achromatic(self.Xserr, self.Yserr - 72 * 3) or
                self.is_achromatic(self.Xserr, self.Yserr - 72 * 4) or
                self.is_achromatic(self.Xserr, self.Yserr - 72 * 5)):
            self.tokenIdx = 0
            return True
        else:
            return False

    def is_four(self):
        """
        현재 남은 사람이 4명 이하 인지(등수가 4등 이상 인지) 확인
        """
        if (self.is_achromatic(self.Xserr, self.Yserr - 72 * 3) or
                self.is_achromatic(self.Xserr, self.Yserr - 72 * 4) or
                self.is_achromatic(self.Xserr, self.Yserr - 72 * 5)):
            self.tokenIdx = 1
            return True
        else:
            return False

    def is_two(self):
        """
        현재 남은 사람이 2명 이하 인지(등수가 2등 이상 인지) 확인
        """
        if self.is_achromatic(self.Xserr, self.Yserr - 72 * 5):
            self.tokenIdx = 1
            return True
        else:
            return False

    def is_win(self):
        """
        승리했는지 확인
        """
        if pyautogui.pixelMatchesColor(995, 644, (132, 15, 16), 1):
            return True
        else:
            return False

    def is_over(self):
        """
        패배로 게임이 끝났는지 확인
        """
        if (pyautogui.pixelMatchesColor(835, 577, (32, 30, 26), 1) or
                pyautogui.pixelMatchesColor(1155, 552, (46, 40, 33))):
            return True
        else:
            return False

    def final_ranking_check(self):
        """
        마지막 등수 체크
        """
        if self.is_two():
            print("1~2등")
            self.tokenIdx = 1
        elif self.is_four():
            print("3~4등")
            self.tokenIdx = 1
        elif self.is_six():
            print("5~6등")
            self.tokenIdx = 0

    def is_client_regame(self):
        """
        게임 종료 후 통계창(한판 더 하기 버튼이 있는)인지 확인
        """
        if ((not pyautogui.pixelMatchesColor(1175, 276, (30, 35, 40)))
                and pyautogui.pixelMatchesColor(917, 844, (30, 35, 40))):
            print("한판더하기 인식")
            return True
        else:
            return False

    def is_client_party_ex(self):
        """
        파티에서 제외되었습니다. 라는 경고창이 떴는지 확인
        """
        if (pyautogui.pixelMatchesColor(816, 485, (1, 10, 19)) and pyautogui.pixelMatchesColor(1100, 551, (1, 10, 19))
                and pyautogui.pixelMatchesColor(1097, 489, (1, 10, 19))
                and pyautogui.pixelMatchesColor(817, 550, (1, 10, 19))
                and (not pyautogui.pixelMatchesColor(971, 675, (1, 10, 19)))):
            print("파티제외 인식")
            return True
        else:
            return False

    def lessthansixteen(self):
        """
        인게임시간이 16분 이전인지 확인
        더이상 쓰지 않는 함수
        """
        if time.time() - self.startTime < 960:
            return True
        elif self.is_four():
            self.tokenIdx = 1
            return True
        else:
            return False

    def is_reword_get_button(self):
        """
        게임끝나고 토큰보상 및 퀘스트보상 수락 창이 떴는지 확인
        """
        if (pyautogui.pixelMatchesColor(905, 828, (30, 35, 40)) and pyautogui.pixelMatchesColor(1015, 831, (30, 35, 40))
                and pyautogui.pixelMatchesColor(1016, 848, (30, 35, 40))
                and pyautogui.pixelMatchesColor(904, 847, (30, 35, 40))):
            return True
        else:
            return False

    # ====================================행동함수들==================================
    def current_time(self):
        """
        현재시각 날짜 출력
        """
        print(time.strftime("%I:%M %p", time.localtime(time.time())))

    def click(self, x, y, sleep:float=0, sec=0.5, times=1, tol=2):
        """
        x, y좌표를 클릭.
        sleep은 클릭 후 쉬는 시간
        sec는 마우스커서를 좌표위치까지 이동하는데 걸리는 시간
        times는 클릭 횟수
        tol는 클릭좌표 오차범위
        """
        pyautogui.failSafeCheck()
        if self.devMode is True:
            return
        pyautogui.moveTo(x + random.uniform(-tol, tol), y + random.uniform(-tol, tol),
                         random.uniform(sec - sec / 4, sec + sec / 4))
        for _ in range(times):
            pyautogui.mouseDown()
            time.sleep(random.uniform(0.08, 0.12))
            pyautogui.mouseUp()
        time.sleep(sleep)

    def key_click(self, key: str):
        """
        키보드 클릭
        어떤 키를 클릭할 지
        key_click('입력하고자 하는키') 형식으로 사용
        입력가능 키 종류는 key_map 딕셔너리 참조
        """
        pyautogui.failSafeCheck()
        if self.devMode is True:
            return
        if key not in key_map or key_map[key] is None:
            return
        key_val = key_map[key]
        press_key(key_val)
        time.sleep(random.uniform(0.05, 0.1))
        release_key(key_val)

    def password_alt_ok(self):
        """
        비밀번호 변경 하라는 창 확인버튼 클릭
        """
        print("비밀번호변경 확인")
        self.click(960, 601)
        time.sleep(1)

    def home_to_find(self):
        """
        홈화면에서부터 큐 대기화면까지 이동하는 과정
        """
        self.click(482, 202, times=2, sleep=2)

        self.click(1037, 487, sleep=2)

        self.click(860, 849, sleep=2)

    def game_find(self):
        """
        게임찾기 버튼 클릭
        """
        print("게임찾기")
        if self.onceStart is False:
            self.loadTimeStart = time.time()

        self.onceStart = True
        self.click(866, 837)

    def game_accept(self):
        """
        큐잡히고 게임 수락 버튼 클릭
        """
        print('게임수락')
        self.click(967, 706)
        time.sleep(1)

    def game_loading(self):
        """
        게임 로딩중 할 활동
        """
        if self.devMode is False:
            pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))
        elif self.devMode is True:
            if int(time.time()) % 2 == 0:
                print("time.time()-startTime[0] :", int(time.time() - self.startTime))
                print("time.time() - loadTimeStart[0] :", int(time.time() - self.loadTimeStart))

    def game_start(self):
        """
        게임 시작하고 하는 행동
        """
        if self.isStart is False:
            self.startTime = time.time()
            print("게임시작")
            self.isStart = True
        if self.loadValIn is False:
            self.loadTime = time.time() - self.loadTimeStart
            self.loadValIn = True

        capture = False

        print("인게임")
        time.sleep(20)

        while True:  # 챔피언픽

            if self.is_over():
                self.game_over()
                break
            if ((self.mode == 1 and self.is_ten_min()) or (self.mode == 2 and self.is_ten_min() and self.is_six())
                    or (self.mode == 3 and self.is_ten_min() and self.is_four()) or (self.mode == 4 and self.is_ten_min() and self.is_two())):
                if self.mode == 1:
                    pass
                else:
                    time.sleep(35)
                self.game_surrender()
                break
            self.click(576, 990, tol=30)
            if self.is_over():
                self.game_over()
                break
            if ((self.mode == 1 and self.is_ten_min()) or (self.mode == 2 and self.is_ten_min() and self.is_six())
                    or (self.mode == 3 and self.is_ten_min() and self.is_four()) or (self.mode == 4 and self.is_ten_min() and self.is_two())):
                if self.mode == 1:
                    pass
                else:
                    time.sleep(35)
                self.game_surrender()
                break
            self.click(778, 988, tol=30)
            if self.is_over():
                self.game_over()
                break
            if ((self.mode == 1 and self.is_ten_min()) or (self.mode == 2 and self.is_ten_min() and self.is_six())
                    or (self.mode == 3 and self.is_ten_min() and self.is_four()) or (self.mode == 4 and self.is_ten_min() and self.is_two())):
                if self.mode == 1:
                    pass
                else:
                    time.sleep(35)
                self.game_surrender()
                break
            self.click(976, 984, tol=30)
            if self.is_over():
                self.game_over()
                break
            if ((self.mode == 1 and self.is_ten_min()) or (self.mode == 2 and self.is_ten_min() and self.is_six())
                    or (self.mode == 3 and self.is_ten_min() and self.is_four()) or (self.mode == 4 and self.is_ten_min() and self.is_two())):
                if self.mode == 1:
                    pass
                else:
                    time.sleep(35)
                self.game_surrender()
                break
            self.click(1181, 988, tol=30)
            if self.is_over():
                self.game_over()
                break
            if ((self.mode == 1 and self.is_ten_min()) or (self.mode == 2 and self.is_ten_min() and self.is_six())
                    or (self.mode == 3 and self.is_ten_min() and self.is_four()) or (self.mode == 4 and self.is_ten_min() and self.is_two())):
                if self.mode == 1:
                    pass
                else:
                    time.sleep(35)
                self.game_surrender()
                break
            self.click(1388, 990, tol=30)
            if self.is_over():
                self.game_over()
                break
            if ((self.mode == 1 and self.is_ten_min()) or (self.mode == 2 and self.is_ten_min() and self.is_six())
                    or (self.mode == 3 and self.is_ten_min() and self.is_four()) or (self.mode == 4 and self.is_ten_min() and self.is_two())):
                if self.mode == 1:
                    pass
                else:
                    time.sleep(35)
                self.game_surrender()
                break

            if time.time() - self.startTime > 900:
                self.click(370, 964, tol=10)

            if self.is_win():
                self.win()
                break

            if self.devMode is False:
                pass
            elif self.devMode is True:
                if int(time.time()) % 2 == 0:
                    print("time.time()-startTime[0] :", int(time.time() - self.startTime))
                    print("time.time() - loadTimeStart[0] :", int(time.time() - self.loadTimeStart))

            if self.devMode is True and time.time() - self.startTime > 60 * 18 and capture is False:
                pyautogui.hotkey('alt', 'f10')
                capture = True

    def print_token_idx(self):
        """
        현재 등수 출력
        """
        if self.tokenIdx == 1:
            print("1~4등")
        elif self.tokenIdx == 0:
            print("5~8등")

    def game_surrender(self):
        """
        항복 실행
        """
        if self.devMode is True:
            pyautogui.hotkey('alt', 'f1')
            pyautogui.hotkey('win', 'alt', 'prtscr')
        print("항복")

        if self.is_win() is True:
            self.tokenIdx = 1
        elif self.is_over() is True:
            pass
        elif self.is_two() is True:
            self.tokenIdx = 1
        elif self.is_four() is True:
            self.tokenIdx = 1
        elif self.is_six() is True:
            self.tokenIdx = 0

        self.key_click('enter')
        self.key_click('.')
        self.key_click('enter')

        self.key_click('enter')
        self.key_click('/')
        self.key_click('f')
        self.key_click('f')
        self.key_click('enter')

        self.key_click('enter')
        self.key_click('/')
        self.key_click('w')
        self.key_click('w')
        self.key_click('enter')

        # 특정 시스템에서 프로그램이 멈추는 문제에 대하여 해결책
        sys.stdout.flush()
        while msvcrt.kbhit():
            msvcrt.getch()

        self.click(836, 486, sleep=1.5)
        self.click(836, 486)

        self.finishing()

    def finishing(self):
        """
        게임 종료 후 마무리 결과 출력
        토큰 계산식은 
        https://support-leagueoflegends.riotgames.com/hc/ko/articles/4409463089811-%EB%A6%AC%EA%B7%B8-%EC%98%A4%EB%B8%8C-%EB%A0%88%EC%A0%84%EB%93%9C-2021-%EC%97%B0%EB%AF%B8%EB%B3%B5
        이곳을 참조
        """
        self.playTime = time.time() - self.startTime

        self.loadTimelist.append(self.loadTime)
        self.playTimelist.append(self.playTime)
        self.tokenGetList.append(self.tokenList[self.tokenIdx] * (self.playTime / 60))

        self.loadTimeStart = time.time()
        self.isStart = False
        self.loadValIn = False

        self.current_time()
        self.plays += 1
        print("플레이 횟수 :", self.plays)
        print("이번 판 큐+로딩시간 : %imin%isec, \n이번 판 인게임시간 : %imin%isec" % (self.loadTime / 60, self.loadTime % 60,
                                                                       self.playTime / 60, self.playTime % 60))
        print("평균 큐+로딩시간 : %imin%isec, \n평균 인게임시간 : %imin%isec" %
              (sum(self.loadTimelist) / len(self.loadTimelist) / 60,
               (sum(self.loadTimelist) / len(self.loadTimelist)) % 60,
               sum(self.playTimelist) / len(self.playTimelist) / 60,
               (sum(self.playTimelist) / len(self.playTimelist)) % 60))
        print("총 토큰획득(추정치) : %i" % (sum(self.tokenGetList)))
        print("이번 판 시간당 토큰획득 : %.2f" %
              (self.tokenList[self.tokenIdx] * (self.playTime / 60) / (self.loadTime + self.playTime) * 3600))
        print("시간당 토큰획득(추정치) : %.2f" %
              (sum(self.tokenGetList) / (sum(self.loadTimelist) + sum(self.playTimelist)) * 3600))
        print("재시작 횟수 :", self.INFloadings)
        print("파티제외 횟수 :", self.partyExcludes)
        print("게임오버 횟수 :", self.overs)
        print("게임승리 횟수 :", self.wins)

        if self.devMode is True and self.playTime < 500:
            pyautogui.hotkey("alt", "f10")

        while True:
            time.sleep(1)
            if not self.is_in_game():
                return

    def win(self):
        """
        승리했을때 확인버튼 클릭
        """
        if self.devMode is True:
            pyautogui.hotkey('alt', 'f1')
            pyautogui.hotkey('win', 'alt', 'prtscr')
        self.click(995, 644)
        print("승리")
        self.tokenIdx = 1
        self.wins += 1
        self.finishing()

    def game_over(self):
        """
        패배했을때 확인버튼 클릭
        """
        if self.devMode is True:
            pyautogui.hotkey('alt', 'f1')
            pyautogui.hotkey('win', 'alt', 'prtscr')
        self.click(835, 550)
        print("게임오버")
        self.overs += 1
        self.final_ranking_check()
        self.finishing()

    def game_regame(self):
        """
        게임종료 후 통계창에서 한판더하기 클릭
        """
        self.click(863, 844)
        time.sleep(1)

    def inf_loading(self):
        """
        가끔 큐잡을때 큐는 안잡히면서 시간만 계속가는 경우가 생기는데
        그 경우 이것을 실행하여 롤 클라이언트를 종료하고 재시작
        롤이 c드라이브 기본폴더에 설치되어 있어야 한다.
        혹은 자신의 설치폴더 위치로 대체해야한다.
        """
        print("무한로딩 대응")
        self.click(1579, 174, sleep=1)

        self.click(912, 564, sleep=60)

        subprocess.call("C:\\Riot Games\\League of Legends\\LeagueClient.exe")

        time.sleep(60)
        self.loadTimeStart = time.time()
        self.onceStart = False
        self.INFloadings += 1

    def party_ex(self):
        """
        파티에서 제외되었습니다 경고문 확인버튼 클릭
        """
        print("파티제외 대응")
        time.sleep(1)
        self.click(962, 542 + 3)
        time.sleep(1)

        self.partyExcludes += 1
        self.onceStart = False

    def reword_get_button(self):
        """
        게임 종료 후 보상 받는 버튼 클릭
        """
        self.click(959, 839)

    # ==========================메인프레임 구성===================================

    def handycalc(self):
        """
        메인 시작 함수
        계속 돌면서 상황을 파악하고 그에 맞는 행동을 한다
        """
        if self.is_client_password_alt():
            self.password_alt_ok()
        elif self.is_client_home():
            self.home_to_find()
        elif self.is_client_party_ex():
            self.party_ex()
        elif self.is_client_accept_screen():
            self.game_accept()
        elif self.is_client_find_game():
            self.game_find()
        elif self.is_loading_screen():
            self.game_loading()
        elif self.is_in_game():
            self.game_start()
        elif self.is_reword_get_button():
            self.reword_get_button()
        elif self.is_client_regame():
            self.game_regame()

        else:
            if int(time.time()) % 40 == 0:
                print("알 수 없는 상황")
            if self.devMode is False:
                pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))
            elif self.devMode is True:
                if int(time.time()) % 40 == 0:
                    print("time.time()-self.startTime :", int(time.time() - self.startTime))
                    print("time.time() - self.loadTimeStart :", int(time.time() - self.loadTimeStart))
            time.sleep(1)
            if self.onceStart is False:
                self.loadTimeStart = time.time()
            if self.loadValIn is False and time.time() - self.loadTimeStart > 600:
                self.inf_loading()

    def mode_select(self):
        """
        모드선택 화면
        """
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
        try:
            self.mode = int(input())
        except ValueError:
            print("인풋에러, 올바른 값을 입력하시오")
            self.mode = 0

    def mode_demo(self):
        """
        각 모드 설명
        """
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

    def dev_switch(self):
        """
        개발자 모드로 변경
        """
        if self.devMode is False:
            print("On")
            self.devMode = True
        else:
            print("Off")
            self.devMode = False
        self.mode = 0
        
    def main(self):
        """
        메인함수
        """
        while True:
            if self.mode == 0:
                self.mode_select()
            elif self.mode == 1 or self.mode == 2 or self.mode == 3 or self.mode == 4 or self.mode == 8:
                try:
                    self.handycalc()
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
                        self.game_surrender()
                    elif exmenu == 4:
                        self.mode_select()
                    elif exmenu == 5:
                        self.dev_switch()
                    else:
                        print("이상한 값 입력. 종료합니다.")
                        time.sleep(2)
                        sys.exit()
            elif self.mode == 5:
                self.dev_switch()
            elif self.mode == 6:
                self.mode_demo()
                self.mode_select()
            elif self.mode == 7:
                print("종료")
                time.sleep(2)
                break
            else:
                print("올바른 값을 입력하십시오.")
                self.mode = 0
                self.mode_select()


# ============================main===========================================
if __name__ == "__main__":
    handy_calc = HandyCalc()
    handy_calc.main()
