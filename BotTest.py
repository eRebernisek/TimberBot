import keyboard
import pyautogui
from PIL import ImageGrab
from PIL import Image
from ahk import AHK
import os
import time
from pyscreeze import pixel
from windowcapture import WindowCapture
import cv2 as cv


ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\AutoHotkey.exe')
wincap = WindowCapture('TimbermanVS')
os.system('cls')

esquerda = True
count = 0
tempTelas =[]

def botLoop():
    print("\nStart\n")
    start = True
    global esquerda
    hassTree = False

    pyautogui.press("a")
    pyautogui.press("a")

    while start:

        tela = wincap.get_screenshot()
        tela = tela[...,:3]
        cv.imshow('Tela', tela)

        # processamento()
        
        # move(hassTree)
        hassTree = False

        # start = stop(tela)


    # tela=tela.save("Logs\Tela"+str(count)+".jpg")
    # telaEsquerda=telaEsquerda.save("Logs\imgE"+str(count)+".jpg")
    # telaDireita= telaDireita.save("Logs\imgD"+str(count)+".jpg")

    # salvaTempImg()
    # tempTelas =[]

    log = ""
    log +="hassTree - "+str(hassTree)+"\n"
    log +="esquerda - "+str(esquerda)+"\n"

    with open('Logs\log.txt','w') as arquivo:
                arquivo.write(log)

def processamento():
    global tempTelas
    tela = ImageGrab.grab()
    imgE = (555,750,560,790)
    telaEsquerda = tela.crop(imgE)
    
    imgD = (715,750,720,790)
    telaDireita = tela.crop(imgD)
    
    # telaEsquerda = Image.open(r"C:\Users\machi\Desktop\Python\TimberBot\img2.jpg") 
        
    if esquerda:
        pix_val = list(telaEsquerda.getdata())
        for sets in pix_val:
            value =0
            for x in sets:
                value+=x
            if value/3<10:
                tempTelas.append(telaEsquerda)
                hassTree=True 
    else:
        pix_val = list(telaDireita.getdata())
        for sets in pix_val:
            value =0
            for x in sets:
                value+=x
            if value/3<10:
                tempTelas.append(telaDireita)
                hassTree=True

def move(move):
    global esquerda

    if move:
        esquerda = not esquerda

    if esquerda:
        pyautogui.press("a")
        if move:
            pyautogui.press("a")
    else:
        pyautogui.press("d")
        if move:
            pyautogui.press("d")

def salvaTempImg():
    
    size = len(tempTelas)

    for x in range(11):
        if x>0:
            tempTelas[size-x].save("Logs\Temp\Tela"+str(x)+".jpg")

def stop(tela):
    energy = tela.getpixel((650,365))
    grave2 = tela.getpixel((794,892))
    grave1 = tela.getpixel((532,895))
    
    red = (217,0,17)
    gray = (187,187,187)
    if energy != red or grave1 == gray or grave2 == gray:
        return False
    else:
        return True

os.system('cls')
print("Running")
# pyautogui.displayMousePosition()
time.sleep(3) 
botLoop()
print("End")
# keyboard.on_press_key("space",lambda _:botLoop())
# keyboard.on_press_key("space",lambda _:test())
