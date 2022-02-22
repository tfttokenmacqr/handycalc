import pyautogui
import random
import time
import sys
import ctypes
import subprocess
import msvcrt
from enum import IntEnum

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


# 열거용 클래스
class Mode(IntEnum):
    Base = 0
    TenMin = 1
    SixthPlace = 2
    FourthPlace = 3
    SecondPlace = 4
    ToTheEnd = 5
    DevSwitch = 6
    ModeDescription = 7
    Exit = 8


class HandyCalc:
    mode = Mode.Base
    token_list = [0.1, 0.15]
    token_idx = 0

    plays = 0  # 매크로 실행횟수
    once_start = False
    load_time_list = []
    play_time_list = []
    token_get_list = []

    load_time_start = 0.0
    start_time = 0.0
    load_time = 0.0
    play_time = 0.0
    load_val_in = False
    is_start = False
    inf_loadings = 0
    party_excludes = 0

    x_surr = 1870
    y_surr = 737

    dev_mode = False
    overs = 0
    wins = 0

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
        if time.time() - HandyCalc.start_time > 600:
            HandyCalc.token_idx = 0
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
        if (self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72) or
                self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72 * 2) or
                self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72 * 3) or
                self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72 * 4) or
                self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72 * 5)):
            HandyCalc.token_idx = 0
            return True
        else:
            return False

    def is_four(self):
        """
        현재 남은 사람이 4명 이하 인지(등수가 4등 이상 인지) 확인
        """
        if (self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72 * 3) or
                self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72 * 4) or
                self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72 * 5)):
            HandyCalc.token_idx = 1
            return True
        else:
            return False

    def is_two(self):
        """
        현재 남은 사람이 2명 이하 인지(등수가 2등 이상 인지) 확인
        """
        if self.is_achromatic(HandyCalc.x_surr, HandyCalc.y_surr - 72 * 5):
            HandyCalc.token_idx = 1
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
            HandyCalc.token_idx = 1
        elif self.is_four():
            print("3~4등")
            HandyCalc.token_idx = 1
        elif self.is_six():
            print("5~6등")
            HandyCalc.token_idx = 0

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
        if time.time() - HandyCalc.start_time < 960:
            return True
        elif self.is_four():
            HandyCalc.token_idx = 1
            return True
        else:
            return False

    def is_reword_get_button(self):
        """
        게임끝나고 토큰보상 및 퀘스트보상 수락 창이 떴는지 확인
        """
        if ((pyautogui.pixelMatchesColor(905, 828, (30, 35, 40)) and
             pyautogui.pixelMatchesColor(1015, 831, (30, 35, 40)) and
             pyautogui.pixelMatchesColor(1016, 848, (30, 35, 40)) and
             pyautogui.pixelMatchesColor(904, 847, (30, 35, 40)))
                or
                (pyautogui.pixelMatchesColor(905, 828, (28, 33, 38)) and
                 pyautogui.pixelMatchesColor(1015, 831, (28, 33, 38)) and
                 pyautogui.pixelMatchesColor(1016, 848, (28, 33, 38)) and
                 pyautogui.pixelMatchesColor(904, 847, (28, 33, 38)))):
            return True
        else:
            return False

    def is_surrender_condition(self):
        """
        항복 조건인지 확인
        """
        if self.is_ten_min():
            return True
        else:
            return False

    # ====================================행동함수들==================================
    def current_time(self):
        """
        현재시각 날짜 출력
        """
        print(time.strftime("%I:%M %p", time.localtime(time.time())))

    def click(self, x, y, sleep: float = 0, sec=0.5, times=1, tol=2):
        """
        x, y좌표를 클릭.
        sleep은 클릭 후 쉬는 시간
        sec는 마우스커서를 좌표위치까지 이동하는데 걸리는 시간
        times는 클릭 횟수
        tol는 클릭좌표 오차범위
        """
        pyautogui.failSafeCheck()
        if HandyCalc.dev_mode is True:
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
        if HandyCalc.dev_mode is True:
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
        if HandyCalc.once_start is False:
            HandyCalc.load_time_start = time.time()

        HandyCalc.once_start = True
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
        if HandyCalc.dev_mode is False:
            pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))
        elif HandyCalc.dev_mode is True:
            if int(time.time()) % 2 == 0:
                print("time.time()-startTime[0] :", int(time.time() - HandyCalc.start_time))
                print("time.time() - loadTimeStart[0] :", int(time.time() - HandyCalc.load_time_start))

    def game_start(self):
        """
        게임 시작하고 하는 행동
        """
        if HandyCalc.is_start is False:
            HandyCalc.start_time = time.time()
            print("게임시작")
            HandyCalc.is_start = True
        if HandyCalc.load_val_in is False:
            HandyCalc.load_time = time.time() - HandyCalc.load_time_start
            HandyCalc.load_val_in = True

        capture = False

        print("인게임")
        time.sleep(20)

        while True:  # 챔피언픽

            for i in range(4):
                if self.is_win():
                    self.win()
                    return
                if self.is_over():
                    self.game_over()
                    return
                if self.is_surrender_condition():
                    if HandyCalc.mode == Mode.TenMin:
                        pass
                    else:
                        time.sleep(35)
                    self.game_surrender()
                    return

                self.click(576 + i * 200, 990, tol=30)

            if time.time() - HandyCalc.start_time > 900:
                self.click(370, 964, tol=10)

            if HandyCalc.dev_mode is False:
                pass
            elif HandyCalc.dev_mode is True:
                if int(time.time()) % 2 == 0:
                    print("time.time()-startTime[0] :", int(time.time() - HandyCalc.start_time))
                    print("time.time() - loadTimeStart[0] :", int(time.time() - HandyCalc.load_time_start))

            if HandyCalc.dev_mode is True and time.time() - HandyCalc.start_time > 60 * 18 and capture is False:
                pyautogui.hotkey('alt', 'f10')
                capture = True

    def print_token_idx(self):
        """
        현재 등수 출력
        """
        if HandyCalc.token_idx == 1:
            print("1~4등")
        elif HandyCalc.token_idx == 0:
            print("5~8등")

    def game_surrender(self):
        """
        항복 실행
        """
        if HandyCalc.dev_mode is True:
            pyautogui.hotkey('alt', 'f1')
            pyautogui.hotkey('win', 'alt', 'prtscr')
        print("항복")

        if self.is_win() is True:
            HandyCalc.token_idx = 1
        elif self.is_over() is True:
            pass
        elif self.is_two() is True:
            HandyCalc.token_idx = 1
        elif self.is_four() is True:
            HandyCalc.token_idx = 1
        elif self.is_six() is True:
            HandyCalc.token_idx = 0

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
        HandyCalc.play_time = time.time() - HandyCalc.start_time

        HandyCalc.load_time_list.append(HandyCalc.load_time)
        HandyCalc.play_time_list.append(HandyCalc.play_time)
        HandyCalc.token_get_list.append(HandyCalc.token_list[HandyCalc.token_idx] * (HandyCalc.play_time / 60))

        HandyCalc.load_time_start = time.time()
        HandyCalc.is_start = False
        HandyCalc.load_val_in = False

        self.current_time()
        HandyCalc.plays += 1
        print("플레이 횟수 :", HandyCalc.plays)
        print("이번 판 큐+로딩시간 : %imin%isec, \n이번 판 인게임시간 : %imin%isec" %
              (HandyCalc.load_time / 60, HandyCalc.load_time % 60, HandyCalc.play_time / 60, HandyCalc.play_time % 60))
        print("평균 큐+로딩시간 : %imin%isec, \n평균 인게임시간 : %imin%isec" %
              (sum(HandyCalc.load_time_list) / len(HandyCalc.load_time_list) / 60,
               (sum(HandyCalc.load_time_list) / len(HandyCalc.load_time_list)) % 60,
               sum(HandyCalc.play_time_list) / len(HandyCalc.play_time_list) / 60,
               (sum(HandyCalc.play_time_list) / len(HandyCalc.play_time_list)) % 60))
        print("총 토큰획득(추정치) : %i" % (sum(HandyCalc.token_get_list)))
        print("이번 판 시간당 토큰획득 : %.2f" %
              (HandyCalc.token_list[HandyCalc.token_idx] * (HandyCalc.play_time / 60) /
               (HandyCalc.load_time + HandyCalc.play_time) * 3600))
        print("시간당 토큰획득(추정치) : %.2f" %
              (sum(HandyCalc.token_get_list) / (sum(HandyCalc.load_time_list) + sum(HandyCalc.play_time_list)) * 3600))
        print("재시작 횟수 :", HandyCalc.inf_loadings)
        print("파티제외 횟수 :", HandyCalc.party_excludes)
        print("게임오버 횟수 :", HandyCalc.overs)
        print("게임승리 횟수 :", HandyCalc.wins)

        if HandyCalc.dev_mode is True and HandyCalc.play_time < 500:
            pyautogui.hotkey("alt", "f10")

        while True:
            time.sleep(1)
            if not self.is_in_game():
                return

    def win(self):
        """
        승리했을때 확인버튼 클릭
        """
        if HandyCalc.dev_mode is True:
            pyautogui.hotkey('alt', 'f1')
            pyautogui.hotkey('win', 'alt', 'prtscr')
        self.click(995, 644)
        print("승리")
        HandyCalc.token_idx = 1
        HandyCalc.wins += 1
        self.finishing()

    def game_over(self):
        """
        패배했을때 확인버튼 클릭
        """
        if HandyCalc.dev_mode is True:
            pyautogui.hotkey('alt', 'f1')
            pyautogui.hotkey('win', 'alt', 'prtscr')
        self.click(835, 550)
        print("게임오버")
        HandyCalc.overs += 1
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
        HandyCalc.load_time_start = time.time()
        HandyCalc.once_start = False
        HandyCalc.inf_loadings += 1

    def party_ex(self):
        """
        파티에서 제외되었습니다 경고문 확인버튼 클릭
        """
        print("파티제외 대응")
        time.sleep(1)
        self.click(962, 542 + 3)
        time.sleep(1)

        HandyCalc.party_excludes += 1
        HandyCalc.once_start = False

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
            if HandyCalc.dev_mode is False:
                pyautogui.moveTo(230, 800, random.uniform(0.8, 1.2))
            elif HandyCalc.dev_mode is True:
                if int(time.time()) % 40 == 0:
                    print("time.time()-HandyCalc.startTime :", int(time.time() - HandyCalc.start_time))
                    print("time.time() - HandyCalc.loadTimeStart :", int(time.time() - HandyCalc.load_time_start))
            time.sleep(1)
            if HandyCalc.once_start is False:
                HandyCalc.load_time_start = time.time()
            if HandyCalc.load_val_in is False and time.time() - HandyCalc.load_time_start > 600:
                self.inf_loading()

    def mode_select(self):
        """
        모드선택 화면
        """
        print("모드를 선택하십시오")
        print("숫자입력 후 엔터누르면 5초 후 동작")
        print("1. 10분 서렌")
        print("2. 6등 서렌")
        print("3. 4등 서렌")
        print("4. 2등 서렌")
        print("5. 끝날때까지")
        print("6. 개발자모드On/Off")
        print("7. 사용설명")
        print("8. 종료")
        try:
            HandyCalc.mode = int(input())
            time.sleep(5)
        except ValueError:
            print("인풋에러, 올바른 값을 입력하시오")
            HandyCalc.mode = Mode.Base

    def user_guide(self):
        """
        사용법 설명
        """
        print("""\n\n
# 우선 본 매크로의 일시정지 방법은 마우스 커서를 화면의 네 모서리 중 한 곳으로 옮기는 것 입니다.

본 프로그램의 실행 창이 오른쪽 화면을 가리도록 하지 마십시오(롤 클라이언트 기준 오른쪽).
특히 플레이어들의 순위를 표시하는 부분을 가리면 안됩니다.

각 모드 설명:      

""")
        print("""\n\n
1. 10분이 되면 서렌하는 버전.

""")
        print("""
2. 6등이 되면 서렌하는 버전.

""")
        print("""
3. 4등이 되면 서렌하는 버전.

""")
        print("""
4. 2등이 되면 서렌하는 버전.

""")
        print("""
5. 승리하거나 체력이 0 이하가 될 때까지.

""")

    def dev_switch(self):
        """
        개발자 모드로 변경
        """
        if HandyCalc.dev_mode is False:
            print("On")
            HandyCalc.dev_mode = True
        else:
            print("Off")
            HandyCalc.dev_mode = False
        HandyCalc.mode = Mode.Base


# END OF HandyCalc


class HandyCalcSixthPlace(HandyCalc):
    """
    6등이면 서렌하는 모드용 클래스
    """
    def is_surrender_condition(self):
        """
        항복 조건인지 확인
        """
        if self.is_ten_min() and self.is_six():
            return True
        else:
            return False


class HandyCalcFourthPlace(HandyCalc):
    """
    4등이면 서렌하는 모드용 클래스
    """
    def is_surrender_condition(self):
        """
        항복 조건인지 확인
        """
        if self.is_ten_min() and self.is_four():
            return True
        else:
            return False


class HandyCalcSecondPlace(HandyCalc):
    """
    2등이면 서렌하는 모드용 클래스
    """
    def is_surrender_condition(self):
        """
        항복 조건인지 확인
        """
        if self.is_ten_min() and self.is_two():
            return True
        else:
            return False


class HandyCalcToTheEnd(HandyCalc):
    """
    끝날때까지 하는 모드용 클래스
    """
    def is_surrender_condition(self):
        """
        항복 조건인지 확인
        """
        return False


class HandyCalcLite(HandyCalc):
    """
    저해상도용 클래스
    """
    pass


def change_mode(handycalc: HandyCalc):
    if handycalc.mode == Mode.SixthPlace:
        return HandyCalcSixthPlace()
    elif handycalc.mode == Mode.FourthPlace:
        return HandyCalcFourthPlace()
    elif handycalc.mode == Mode.SecondPlace:
        return HandyCalcSecondPlace()
    elif handycalc.mode == Mode.ToTheEnd:
        return HandyCalcToTheEnd()


def main():
    """
    메인함수
    """
    handycalc = HandyCalc()

    while True:
        if handycalc.mode == Mode.Base:
            handycalc.mode_select()
        elif (handycalc.mode == Mode.TenMin or handycalc.mode == Mode.SixthPlace or
              handycalc.mode == Mode.FourthPlace or handycalc.mode == Mode.SecondPlace or
              handycalc.mode == Mode.ToTheEnd):
            handycalc = change_mode(handycalc)
            try:
                handycalc.handycalc()
            except pyautogui.FailSafeException:
                ex_menu = int(input("""
일시정지. 메뉴를 고르시오.
1. 돌아가기
2. 종료
3. 버그시 강제 서렌
4. 모드 변경
5. 개발자모드On/Off

숫자 입력 후 엔터누르면 5초뒤 동작
"""))
                time.sleep(5)
                if ex_menu == 1:
                    "게임으로 돌아갑니다."
                elif ex_menu == 2:
                    print("종료합니다.")
                    time.sleep(2)
                    sys.exit()
                elif ex_menu == 3:
                    print("강제로 서렌 합니다.")
                    handycalc.game_surrender()
                elif ex_menu == 4:
                    handycalc.mode_select()
                    handycalc = change_mode(handycalc)
                elif ex_menu == 5:
                    handycalc.dev_switch()
                else:
                    print("이상한 값 입력. 종료합니다.")
                    time.sleep(2)
                    sys.exit()
        elif handycalc.mode == Mode.DevSwitch:
            handycalc.dev_switch()
        elif handycalc.mode == Mode.ModeDescription:
            handycalc.user_guide()
            handycalc.mode_select()
        elif handycalc.mode == Mode.Exit:
            print("종료")
            time.sleep(2)
            break
        else:
            print("올바른 값을 입력하십시오.")
            handycalc.mode = Mode.Base
            handycalc.mode_select()


# ============================main===========================================
if __name__ == "__main__":
    main()
