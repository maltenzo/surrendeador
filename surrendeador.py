import keyboard
import mouse
from PIL import Image
import pyscreenshot
import pyautogui
from time import sleep
import os
import config
import ver_colores
teclado = keyboard


x = 0
y = 0
# x_buscar = 558
# y_buscar = 750
# x_rendirse = 500
# y_rendirse = 824
# x_aceptar = 622
# y_aceptar = 632
# x_seguro = 718
# y_seguro = 462
# x_otra = 580
# y_otra = 750
# color_aceptar = (163, 217, 225)
# color_rendirse = (69, 124, 121)

buscando_img = 0
encontre = 0
esperando_img = 0


def encontre_partida():
    res = False
    img = pyscreenshot.grab()
    width, height = img.size
    pixel_values = list(img.getdata())
    #print (pixel_values[width*y_aceptar+x_aceptar])
    if pixel_values[width*dict["ACEPTAR"][1]+dict["ACEPTAR"][0]] == dict["COLOR_ACEPTAR"]:
        res = True
        #print("lo encontre")
    return res

def puedo_surrendear():
    res = False
    mydir = "C:\Riot Games\League of Legends\Screenshots"
    while not res:
        filelist = [ f for f in os.listdir(mydir)]
        for f in filelist:
                os.remove(os.path.join(mydir, f))
        keyboard.send("F12", True , True)
        sleep(3)

        img = Image.open("C:\Riot Games\League of Legends\Screenshots\Screen01.png")
        width, height = img.size
        pixel_values = list(img.getdata())
        #print(pixel_values[width*y_rendirse+x_rendirse])
        if pixel_values[width*y_rendirse+x_rendirse] == color_rendirse :
            res = True
            #print("lo encontre")
    return res

def surrendear_2():
    res = False
    img = pyscreenshot.grab()
    width, height = img.size
    pixel_values = list(img.getdata())
    #print (pixel_values[width*y_rendirse+x_rendirse])
    if pixel_values[width*dict["RENDIRSE"][1]+dict["RENDIRSE"][0]] != (0, 0, 0) :
        res = True
        #print("Me rendi")
    return res

def no_entre(dict):
        res = True
        img = pyscreenshot.grab()
        width, height = img.size
        pixel_values = list(img.getdata())
        x = dict["ACEPTAR"][0]
        y = dict["ACEPTAR"][1]
        #print (pixel_values[width*y_aceptar+x_aceptar])
        if pixel_values[width*y+x] != (44, 41, 37) and pixel_values[width*y+x] != dict["COLOR_ACEPTAR"] and pixel_values[width*y+x] != (96, 97, 97):
            res = False
            #print("entre")
        return res

def main(dict):
    #Busco partida
    mouse.move(dict["BUSCAR"][0], dict["BUSCAR"][1], True, 0)
    mouse.click("left")
    #encuentro y acepto la partida
    mouse.move(dict["ACEPTAR"][0], dict["ACEPTAR"][1], True, 0)

    while no_entre(dict):
        if encontre_partida():
            sleep(1)
            mouse.click("left")
    #abro el menu
    print("entre")
    sleep(650)

    while not surrendear_2():
        #memmuevo al rendirse
        if not surrendear_2():
            keyboard.send("esc", True, True)
            mouse.move(dict["RENDIRSE"][0], dict["RENDIRSE"][1], True, 1)
            sleep(1)
            #surrendeo
            mouse.click("left")
            sleep(1)
            pyautogui.click()
        if not surrendear_2():
            #muevo el mouse al estoy seguro y surrendeo
            mouse.move(dict["SEGURO"][0], dict["SEGURO"][1], True, 1)
            sleep(1)
            mouse.click("left")
            sleep(1)
            pyautogui.click()
            sleep(1)
            keyboard.send("esc", True, True)
        sleep(1)


    sleep(60)
    #muevo el mouse a volver a jugar
    mouse.move(dict["OTRA"][0], dict["OTRA"][1], True ,0)
    mouse.click("left")

while True:
    print("1) Correr el programa")
    print("2) Configurar")
    print("3) Ver colores")
    opcion = int(input())
    if opcion == 1:
        partidas = 0
        dict = config.leer_datos()
        while True:
            if teclado.is_pressed("z"):
                main(dict)
                partidas += 1
                print(partidas)
                sleep(3)
            #if partidas == 7:
            #    break
    elif(opcion == 2):
        config.config()
    elif(opcion == 3):
        ver_colores.ver()
