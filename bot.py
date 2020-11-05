#control imports
import keyboard
import mouse
import autoit
#image imports
from PIL import Image
import pyscreenshot
import ver_colores
#system imports
from time import sleep
import os
import win32gui
import psutil
import win32process



# Estados: init, searching, waiting, playing
class Bot():
    def __init__(self, dict):
        self.jugadas = 0
        self.state = "init"
        self.dict = dict

    @property
    def color(self):
        return ver_colores.dame_colores()

    @property
    def window(self):
            sleep(3)
            w=win32gui
            w.GetWindowText (w.GetForegroundWindow())
            pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
            return (psutil.Process(pid[-1]).name())


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
