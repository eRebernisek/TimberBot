from PIL import ImageGrab
import pyautogui, time

left_track = []
right_track = []

side = "left"

left_point =(430,900,570,720)
right_point = (570,471,590,556)
replayBtn = (482,801)

def replay():
    pyautogui.click(replayBtn)
    time.sleep(2)

def init():
    replay()
    global left_init, right_init
    left_init = ImageGrab.grab(left_point)
    right_init = ImageGrab.grab(right_point)

    # left_init.save('left.jpg')
    # right_init.save('right.jpg')

    left_track.append(True)
    right_track.append(True)

def getTrack():
    look_left= ImageGrab.grab(left_point)
    look_right= ImageGrab.grab(right_point)

    left_track.append(look_left==left_init)
    right_track.append(look_right==right_init)

    # print('l',left_track)
    # print('r',right_track)


def cut():
    global side
    l,r = left_track.pop(0),right_track.pop(0)
    if l and r : #양쪽에 나무가 없다.
        pyautogui.press(side)
    elif l : #왼쪽에만 나무가 없고 오른쪽이 있다.
        pyautogui.press('left')
        side='left'
    else :
        pyautogui.press('right')
        side='right'

init()
while True:
    getTrack() #트랙분석
    cut() #판단 후 자르기