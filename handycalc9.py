#ver9 10분항복을 못했을 경우 30분게임을 막고 20분 서렌을 하기위해 항복후 설정버튼을 한번더 누르도록 조정
#ver9.1 알수 없는 이유로 큐를 못잡았을 시 친구초대버튼을 누르는 문제수정
import pyautogui as pag
import random
import time
#from PIL import ImageGrab

#find_button  lt790, 823 rb941 851  wd154 hi28
#accept_button lt884 700 rb1033 726
#setting leftup 1893 873  rightdown 1917 894
#surrender  lt680 854  rb833 888
#sur_accpt  lt770 612 rb945 638
#again lt791 834 rb934 853 width 144 hight 25
#pick lt485 932  rb667 1068  relative 200
#token_get lt902 827 rb1018 849

play_time = 0  #매크로 실행횟수
while True:

    i=0
    while i<5:   #게임찾기버튼
        pag.moveTo(random.uniform(790,941),random.uniform(823,851),random.uniform(0.8,0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08,0.12))
        pag.mouseUp()
        i=i+1


    #time.sleep(3)
    start1=time.time()
    while True:    #수락버튼
        pag.moveTo(random.uniform(884+16,1033),random.uniform(700,726-15),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()

        if time.time()-start1>120:
            break

    print("in game")
    start2 = time.time()

    while True:    #챔피언픽

        pag.moveTo(random.uniform(485,667),random.uniform(932,1032-50),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+200,667+200),random.uniform(932,1032-50),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+400,667+400),random.uniform(932,1032-50),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+600,667+600),random.uniform(932,1032-50),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        pag.moveTo(random.uniform(485+800,667+800),random.uniform(932,1032-50),random.uniform(0.25,0.75))
        pag.mouseDown()
        time.sleep(random.uniform(0.3,0.7))
        pag.mouseUp()
        if time.time()-start2>720:
            break


    print("wake up")

    # pag.keyDown('z')
    # time.sleep(random.uniform(0.08,0.3))
    # pag.keyUp('z')
    #
    # now=time.localtime()
    # time="%04d-%02d-%02d-%02dh-%02dm-%02ds"%(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)
    #
    # img=ImageGrab.grab()
    # saveas="{}{}".format(time,'.png')
    # img.save(saveas)
    #
    # start4 = time.time()
    # while time.time()-start4<3:
    #     print("capturing")


#항복
    pag.moveTo(random.uniform(1893+2,1917-2),random.uniform(873+2,894-2),random.uniform(0.5,1))
    pag.mouseDown()
    time.sleep(random.uniform(0.1,0.3))
    pag.mouseUp()

    pag.moveTo(random.uniform(680+2, 741 ),random.uniform(854+2,888-2),random.uniform(0.4,2))
    pag.mouseDown()
    time.sleep(random.uniform(0.1,0.25))
    pag.mouseUp()

    pag.moveTo(random.uniform(900,945),random.uniform(612,638),random.uniform(0.7,1.5))
    pag.mouseDown()
    time.sleep(random.uniform(0.12,0.34))
    pag.mouseUp()

    pag.moveTo(random.uniform(1893+2,1917-2),random.uniform(873+2,894-2),random.uniform(0.5,1))
    pag.mouseDown()
    time.sleep(random.uniform(0.1,0.3))
    pag.mouseUp()



    #time.sleep(30)
    start3 = time.time()
    while True:  #퀘스트깼을때 퀘스트확인버튼
        pag.moveTo(random.uniform(950,1018-2),random.uniform(827,849),random.uniform(0.8,0.12))
        pag.mouseDown()
        time.sleep(random.uniform(0.08,0.12))
        pag.mouseUp()
        if time.time()-start3>30:
            break

#다시하기
    pag.moveTo(random.uniform(791,934),random.uniform(834,853),random.uniform(1,3.3))
    pag.mouseDown()
    time.sleep(random.uniform(0.08,0.3))
    pag.mouseUp()

    time.sleep(3)

    play_time = play_time+1
    print("play times : ",play_time)
