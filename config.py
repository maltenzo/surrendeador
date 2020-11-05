import os
import mouse
import keyboard as kb
from ver_colores import dame_colores
from playsound import playsound as ps

# 0) BUSCAR   = []
# 1) ACEPTAR  = []
# 2) RENDIRSE = []
# 3) SEGURO   = []
# 4) OTRA     = []
# 0_c) COLOR_ACEPTAR  = (0, 0, 0)
# 1_c) COLOR_RENDIRSE = (0, 0, 0)

recording = F"{os.getcwd()}/sonidos/record.mp3"
recorded =  F"{os.getcwd()}/sonidos/recorded.mp3"
dict = {}
def config():
    termine = False
    while(not termine):
            switch()
            if (kb.is_pressed("5")):
                termine = True
    salvar_datos()

def salvar_datos():
    with open(F"{os.getcwd()}/config.txt", "w") as f:
        for key, value  in dict.items():
            print(F"{key}: {value}", file=f, end="\n")

def string_a_tupla(s):
    tupla = []
    numero = ""
    for i in range(0, len(s)):
        if s[i].isnumeric():
            numero=numero+s[i]
        else:
            if("" != numero):
                tupla.append(int(numero))
            numero=""
    return tuple(tupla)
def leer_datos():
    dict = {}
    if os.path.isfile(F"{os.getcwd()}/config.txt"):
        with open(F"{os.getcwd()}/config.txt", "r") as f:
            for line in f:
                words = line.split(": ")
                key = words[0]
                value = words[1]
                dict[key] = string_a_tupla(value)
    else:
        "No hay datos guardados"
    return dict

def switch():
    mouse = mouse()
    if (kb.is_pressed("1")):
        ps(recording)
        while(not mouse.is_pressed("left")):
            x=0
        dict["BUSCAR"] = mouse.get_position()
        ps(recorded)

    elif (kb.is_pressed("2")):
        ps(recording)
        while(not mouse.is_pressed("left")):
            x=0
        dict["COLOR_ACEPTAR"] = dame_colores()
        dict["ACEPTAR"] = mouse.get_position()
        ps(recorded)

    #elif (kb.is_pressed("3")):
    #    ps(recording)
    #    while(not mouse.is_pressed("left")):
    #        x=0
    #    dict["COLOR_RENDIRSE"] = dame_colores()
    #    dict["RENDIRSE"] = mouse.get_position()
    #    ps(recorded)

elif (kb.is_pressed("3")):
        ps(recording)
        while(not mouse.is_pressed("left")):
            x=0
        dict["SEGURO"] = mouse.get_position()
        ps(recorded)

    elif (kb.is_pressed("4")):
        ps(recording)
        while(not mouse.is_pressed("left")):
            x=0
        dict["OTRA"] = mouse.get_position()
        ps(recorded)
