import mouse
import keyboard
from PIL import Image
import pyscreenshot
from time import sleep
import os
teclado = keyboard
x = 0
y = 0
x_buscar = 558
y_buscar = 750
x_rendirse = 500
y_rendirse = 824
x_aceptar = 622
y_aceptar = 632
x_seguro = 718
y_seguro = 462
x_otra = 580
y_otra = 750

color_aceptar = (163, 217, 225)
color_rendirse = (69, 124, 121)

buscando_img = 0
encontre = 0
esperando_img = 0


def encontre_partida():
    res = False
    img = pyscreenshot.grab()
    width, height = img.size
    pixel_values = list(img.getdata())
    #print (pixel_values[width*y_aceptar+x_aceptar])
    if pixel_values[width*y_aceptar+x_aceptar] == color_aceptar :
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
    if pixel_values[width*y_rendirse+x_rendirse] != (0, 0, 0) :
        res = True
        #print("Me rendi")
    return res

def no_entre():
        res = True
        img = pyscreenshot.grab()
        width, height = img.size
        pixel_values = list(img.getdata())
        #print (pixel_values[width*y_aceptar+x_aceptar])
        if pixel_values[width*y_aceptar+x_aceptar] != (44, 41, 37) and pixel_values[width*y_aceptar+x_aceptar] != color_aceptar and pixel_values[width*y_aceptar+x_aceptar] != (96, 97, 97):
            res = False
            #print("entre")
        return res

def main():
    #Busco partida
    mouse.move(x_buscar, y_buscar, True, 0)
    mouse.click("left")
    #encuentro y acepto la partida
    mouse.move(x_aceptar, y_aceptar, True, 0)

    while no_entre():
        if encontre_partida():
            sleep(1)
            mouse.click("left")
    #abro el menu
    sleep(650)

    while not surrendear_2():
        #memmuevo al rendirse
        if not surrendear_2():
            keyboard.send("esc", True, True)
            mouse.move(x_rendirse, y_rendirse, True, 1)
            sleep(1)
            #surrendeo
            mouse.click("left")
            sleep(1)
            mouse.click("left")
        if not surrendear_2():
            #muevo el mouse al estoy seguro y surrendeo
            mouse.move(x_seguro, y_seguro, True, 1)
            sleep(1)
            mouse.click("left")
            sleep(1)
            mouse.click("right")
            sleep(1)
            keyboard.send("esc", True, True)
        sleep(1)


    sleep(60)
    #muevo el mouse a volver a jugar
    mouse.move(x_otra, y_otra, True ,0)
    mouse.click("left")

while True:
    if keyboard.is_pressed("z"):
        partidas = 0
        while True:
            main()
            partidas += 1
            print(partidas)
            sleep(3)
            #if partidas == 7:
            #    break
