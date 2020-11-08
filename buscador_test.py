from PIL import Image
import mouse as m
import pyscreenshot
import pygetwindow as gw
import keyboard as kb
from time import sleep

ACEPTAR = Image.open("imagenes/bot_ac.png")
WINDOW =  gw.getWindowsWithTitle("League of Legends")[0]
def mod(a):

    if a < 0:
        return( a*(-1))
    else:
        return a

def casi_iguales(c1, c2):
    return ((mod(c1[0] - c2[0]) <40 ) and (mod(c1[1] - c2[1]) <40) and (mod(c1[2] - c2[2]) <40))
def buscar_2(color):
    res = (0,0)
    x0 = WINDOW.topleft[0] + int(WINDOW.width * 0.45)
    y0 = WINDOW.topleft[1] + int(WINDOW.height* 0.45)
    top = WINDOW.bottomright[1]
    box = (x0, y0, x0+1, top)
    img = pyscreenshot.grab(bbox = box )

    pixel_values = list(img.getdata())
    for i in range(0, len(pixel_values), 2):
        pixel = pixel_values[i]
        if casi_iguales(color, pixel):
            print(pixel)
            res = (x0, y0 + i)
            break
    return res









def buscar(imagen):
    #WINDOW.activate()
    #sleep(1)
    x0 = int(WINDOW.topleft[0] + WINDOW.width / 2) - 40
    y0 = int(WINDOW.topleft[1] + WINDOW.height * 3/4)
    x1 = x0 + 75
    y1 = y0 + 20
    encontre = False
    while(not encontre):
        box = (x0,y0,x1,y1)
        print(box)
        img = pyscreenshot.grab(bbox = box)
        #encontre = True
        img.save("img1.png")
        if img == ACEPTAR:
            encontre = True
            print("encontre")
        else:
            if y0 == WINDOW.topleft[1] :
                print("F")
                break
            elif x0 == int(WINDOW.topleft[0] + WINDOW.width / 2) :
                x0 = int(WINDOW.topleft[0] + WINDOW.width / 4)
                x1 = x0 + 74
                y0 = y0 + 1
                y1 = y0 + 19
            else:
                x0 += 1
                x1 += 1

ACEPTAR = (10, 188, 175)
CELESTE = (0, 108, 125)#(5, 150, 170)
while True:
    if kb.is_pressed("z"):
        #zwhile True:
            buscar_2(CELESTE)
