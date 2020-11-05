from bot import Bot
import config
VERSION = "2.0"
while True:
    dict = {}
    choice = int(input("1: Configurar posiciones" + "\n" + "2: Correr Bot" + "\n"))
    if choice == 1:
        config.config()
    elif choice == 2:
        #dict = config.leer_datos()
        if dict == {}:
            print("Configura las posiciones primero")
        #print(dict)
        else:
            bot = Bot(dict)
            while True:
                bot.jugar()
