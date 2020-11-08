#control imports
import keyboard
import mouse
import autoit
#image imports
from PIL import Image
import pyscreenshot
import pygetwindow as gw
import ver_colores
#system imports
from time import sleep
import os
import win32gui
import psutil
import win32process


# LeagueClientUx.exe
# Estados: init, searching, waiting, playing
CELESTE = (0, 108, 125)
DORADO = (199, 168, 109)
def mod(a):

    if a < 0:
        return( a*(-1))
    else:
        return a

def casi_iguales(c1, c2):
    return ((mod(c1[0] - c2[0]) <40 ) and (mod(c1[1] - c2[1]) <40) and (mod(c1[2] - c2[2]) <40))

class Bot():
    def __init__(self, dict):
        self.jugadas = 0
        self.state = "init"
        self.dict = dict
        self.client_win = gw.getWindowsWithTitle("League of Legends")[0]

    @property
    def color(self):
        return ver_colores.dame_colores()

    @property
    def window(self):
            return self.client_win

    def screenshot_client(self):
        if not self.window.isActi-ve:
            self.window.active
        return pyscreenshot.grab(bbox = (self.window.topleft[0], self.window.topleft[1], self.window.bottomright[0], self.window.bottomright[1]))

    def  entre(self):
            self.state = "playing"
            img = pyscreenshot.grab()
            width, height = img.size
            pixel_values = list(img.getdata())
            x = self.dict["ACEPTAR"][0]
            y = self.dict["ACEPTAR"][1]
            #print (pixel_values[width*y_aceptar+x_aceptar])
            if pixel_values[width*y+x] == self.dict["PRE-ACEPTAR"] or pixel_values[width*y+x] == self.dict["COLOR_ACEPTAR"]:
                self.state = "searching"
            elif pixel_values[width*y+x] == self.dict["POST-ACEPTAR"] :
                self.state = "waiting"
                #print("entre")
    def partida_encontrada(self):
        res =  False
        mouse.move(self.dict["ACEPTAR"][0], self.dict["ACEPTAR"][1], True, 0)
        if self.dict["COLOR_ACEPTAR"] == self.color:
                res=True
        return res


    def buscar_partida(self):
        mouse.move(self.dict["BUSCAR"][0], self.dict["BUSCAR"][1], True, 0)
        mouse.click("left")
        self.state = "searching"

    def aceptar_partida(self):
        mouse.move(self.dict["ACEPTAR"][0], self.dict["ACEPTAR"][1], True, 0)
        mouse.click("left")
        self.dict["POST-ACEPTAR"] = self.color
        self.state = "waiting"

    def llamar_rendise(self):
        #mouse.move(self.dict["SEGURO"][0], self.dict["SEGURO"][1])
        #self.dict["PRE-SEGURO"] = self.color
            keyboard.send("enter")
            sleep(0.5)
            keyboard.send("/")
            sleep(0.5)
            keyboard.send("f")
            sleep(0.5)
            keyboard.send("f")
            sleep(0.5)
            keyboard.send("enter")
            sleep(0.5)

    def rendirse(self):
        self.llamar_rendise()
        autoit.mouse_click("left",self.dict["SEGURO"][0], self.dict["SEGURO"][1], 1, 1)


    def reiniciar(self):
        self.state = "init"
        self.volver_a_jugar()

    def resolver_recompensas(self):
        mouse.move(981, 767, True, 1)
        while (self.color == (0,1,6)):
            mouse.move(667, 804, True, 1)
            mouse.click()
            mouse.move(981, 767, True, 0)
            sleep(5)

    def volver_a_jugar(self):
        sleep(10)
        self.resolver_recompensas()
        sleep(5)
        mouse.move(self.dict["OTRA"][0], self.dict["OTRA"][1], True, 1)
        mouse.click()
        sleep(5)

    def jugar(self):

        if keyboard.is_pressed("z"):
            while True:
                #agarro el color del cliente cuando no esta el cartel de partida encontrada
                mouse.move(self.dict["ACEPTAR"][0], self.dict["ACEPTAR"][1], True, 0)
                self.dict["PRE-ACEPTAR"] = self.color
                #busco partida
                print("Buscando partida")
                self.buscar_partida()

                while self.state != "playing":
                    if(self.state != "waiting"):
                        while not self.partida_encontrada():
                            pass
                        print("partida encontrada")
                        self.aceptar_partida()
                    self.entre()

                self.jugadas+=1
                sleep(660)
                print("desperte")
                while(self.window == "League of Legends.exe"):
                    self.rendirse()
                self.reiniciar()
                print(self.jugadas)

#########################################################3.0##############################################################################################################

    def buscar_2(self, color, box):
        res = (0,0)
        if not self.window.isActive:
            return res
        #x0 = self.window.topleft[0] + int(self.window.width * 0.45)
        #y0 = self.window.topleft[1] + int(self.window.height* 0.45)
        #top = self.window.bottomright[1]
        #box = (x0, y0, x0+1, top)
        for b in box:
            if b < 0:
                return res
        img = pyscreenshot.grab(bbox = box )

        pixel_values = list(img.getdata())
        for i in range(0, len(pixel_values), 2):
            pixel = pixel_values[i]
            if casi_iguales(color, pixel):
                print(pixel)
                res = (x0, y0 + i)
                break
        return res




    def buscar_partida2(self):
        box =(self.window.topleft[0] + int(self.window.width * 0.45),
        self.window.topleft[1] + int(self.window.height* 0.45),
        self.window.topleft[0] + int(self.window.width * 0.45),
        self.window.bottomright[1])
        pos = self.buscar_2(CELESTE, box)
        if pos == (0,0):
            print("error: No se encontro el cartel de buscar partida")
        else:
            mouse.move(pos[0], pos[1])
            sleep(0.5)
            mouse.click()


    def log_entrada(self):
        while self.window.isActive:
            box =(self.window.topleft[0] + int(self.window.width * 0.45),
            self.window.topleft[1] + int(self.window.height* 0.45),
            self.window.topleft[0] + int(self.window.width * 0.45),
            self.window.bottomright[1])
            pos = self.buscar_2(CELESTE, box)
            if pos == (0,0):
                print("buscando")
            else:
                print("aceptando")
                mouse.move(pos[0], pos[1])
                mouse.click()
                sleep(10)

    def resolver_recompensas(self):
        pos = (0,0)
        box = ()
        pos = self.buscar_2(DORADO, box)
        if pos != (0,0):
            mouse.move(pos[0], pos[1])
            mouse.click()
        sleep(3)

    def jugar2(self):
        if keyboard.is_pressed("z"):
            box =(self.window.topleft[0] + int(self.window.width * 0.45),
            self.window.topleft[1] + int(self.window.height* 0.45),
            self.window.topleft[0] + int(self.window.width * 0.45),
            self.window.bottomright[1])
            while True:
                #Busco el cartel de buscar partida
                self.buscar_partida2()
                sleep(1)
                #En este punto tengo ver si encontre partida
                self.log_entrada()
                #En este punto deberia estar en partida
                print("durmiendo")
                sleep(720)
                print("Despierto")
                while not self.window.isActive:
                    self.rendirse()
                    sleep(8)
                #resolver recompensas
                self.resolver_recompensas()
                self.jugadas += 1
                pos = self.buscar_2(CELESTE, box)
                mouse.move(pos[0], pos[1])
                sleep(0.3)
                mouse.click()
