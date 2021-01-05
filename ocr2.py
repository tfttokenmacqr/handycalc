import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import pytesseract
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
input("엔터치면 3초뒤 시작")
time.sleep(3)

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

# plt.figure(figsize=(12, 10))
# plt.imshow(load_profile1, cmap="gray")
# plt.show()
# plt.figure(figsize=(12, 10))
# plt.imshow(load_profile2, cmap="gray")
# plt.show()
# plt.figure(figsize=(12, 10))
# plt.imshow(load_profile3, cmap="gray")
# plt.show()
# plt.figure(figsize=(12, 10))
# plt.imshow(load_profile4, cmap="gray")
# plt.show()
# plt.figure(figsize=(12, 10))
# plt.imshow(load_profile5, cmap="gray")
# plt.show()
# plt.figure(figsize=(12, 10))
# plt.imshow(load_profile6, cmap="gray")
# plt.show()
# plt.figure(figsize=(12, 10))
# plt.imshow(load_profile7, cmap="gray")
# plt.show()
# plt.figure(figsize=(12, 10))
# plt.imshow(load_profile8, cmap="gray")
# plt.show()

# player1 = pytesseract.image_to_string(load_profile1, lang='eng+kor', config='--psm 7')
# print(player1.replace(' ', '').replace('\n', '')[:-1])
# player2 = pytesseract.image_to_string(load_profile2, lang='eng+kor', config='--psm 7')
# print(player2.replace(' ', '').replace('\n', '')[:-1])
# player3 = pytesseract.image_to_string(load_profile3, lang='eng+kor', config='--psm 7')
# print(player3.replace(' ', '').replace('\n', '')[:-1])
# player4 = pytesseract.image_to_string(load_profile4, lang='eng+kor', config='--psm 7')
# print(player4.replace(' ', '').replace('\n', '')[:-1])
# player5 = pytesseract.image_to_string(load_profile5, lang='eng+kor', config='--psm 7')
# print(player5.replace(' ', '').replace('\n', '')[:-1])
# player6 = pytesseract.image_to_string(load_profile6, lang='eng+kor', config='--psm 7')
# print(player6.replace(' ', '').replace('\n', '')[:-1])
# player7 = pytesseract.image_to_string(load_profile7, lang='eng+kor', config='--psm 7')
# print(player7.replace(' ', '').replace('\n', '')[:-1])
# player8 = pytesseract.image_to_string(load_profile8, lang='eng+kor', config='--psm 7')
# print(player8.replace(' ', '').replace('\n', '')[:-1])

print(players)

input("엔터치면 종료")
