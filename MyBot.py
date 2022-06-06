import keyboard
import pyautogui
from PIL import ImageGrab
from ahk import AHK
import os
import time

from pyscreeze import pixel


ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\AutoHotkey.exe')
os.system('cls')

def botLoop():
    print("\rStart\r")
    start = True
    checkTree()
    
def checkTree():  
    global esquerda

    if esquerda:
        x = 530
    else:
        x = 730
    checkTela(x)

def checkTela(x):
    global esquerda
    global log
    print("Esquerda")
    tela = ImageGrab.grab()

    for y in range(730,780 ):
        area = tela.getpixel((x, y))
        
        
        pixels=[]
        pixels.append(area)
        
        if area != (7,186,147):
            
            hasTree = False

            if area == (0,0,0):
                os.system('cls')
                if esquerda:
                    log +="\nTree Left"
                    pyautogui.press("d")
                    esquerda = False
                    checkTree()
                else:
                    log +="\nTree Right"
                    pyautogui.press("a")
                    esquerda = True
                    checkTree()
            

        else:
            os.system('cls')
            print("Stop")
            with open('log.txt','w') as arquivo:
                arquivo.write(log)
            return
    
    os.system('cls')
    myStr = ""
    for pixel in pixels:
        myStr = myStr + str(pixel) + ","
    log+="\n"+myStr

    if esquerda:
        pyautogui.press("a")
        checkTela(x)
    else:
        pyautogui.press("d")
        checkTela(x)
    
def test():
    print("Teste")
    pyautogui.press("a")
    time.sleep(1)
    pyautogui.press("d")

esquerda = True
log=""
keyboard.on_press_key("space",lambda _:botLoop())
# keyboard.on_press_key("space",lambda _:test())

os.system('cls')
print("Running")
pyautogui.displayMousePosition()
time.sleep(10)
print("End")

# x 530
# y 430-510

# pyautogui.displayMousePosition()
