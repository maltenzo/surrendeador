# surrendeador
Este proyecto es una aplicacion para farmear el pase de batalla de tft en league of leyends.
# Que hace:
las funcionalidades de este bot se limitan a:
1) Buscar una partida de tft.
2) Encargarse de aceptar la partida y verificar que este dentro.
3) Esperar a que llegue el momento en que uno ya puede rendirse.
4) Rendirse.
5) Contar cuantas partidas lleva jugadas.
6) Buscar otra partida y repetir el proceso.

# Que no hace:
 - jugar o interactuar con los personajes
 - recoger objetos
 - reclamar recompensas

 # Como lo hace:
 Para todas las interacciones con botones (ej buscar partida, aceptar rendirse) conoce las posiciones de los botones, ademas de los colores que indican que debe realizar una accion. Por ejemplo el boton de rendirse permanece opaco hasta que la accion puede realizarse.
 Entonces lo unico que debe hacer es mirar que en las posiciones señalas se encuentren los colores indicados.
 Ahora es configurable desde el menu principal para que sea un poco mas amigable para otros.

 # Problemas que se deberian solucionar:
 - Al completar misiones o recibir recompensas el cliente se comporta de forma no esperada, asi que falla y cambia de estado cuando no deberia (por ej cree que sigue en partida)
 - Luego de jugar mucho tiempo el cliente parece crashear, seria bueno que se encargue de reiniciar el juego
 - Los clicks dentro de la partida de tft no funcionan bien, por alguna razon el click que hace sobre el boton de rendirse muchas veces parece no hacer efecto. (Parece ser que esta relacionado con una limitacion de la libreria del mouse, sobre que no manda eventos que ocurren cuando el click es por hardware.)

#Changelog
