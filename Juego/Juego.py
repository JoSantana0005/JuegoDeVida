#Librerias a utilizar en el proyecto
import pygame as py
import numpy as np
import time

#Inicio pygame
py.init()

#Ancho y Largo de la ventana del juego
witdh,height = 890,500
py.display.set_caption("Juego de la Vida")
dimesiones = py.display.set_mode((witdh,height))

#Color del fondo
bg = 25,25,25
dimesiones.fill(bg)

#Numeros de celdas
nxC,nyC = 50,50

#Dimesiones de la celda
dimeX = witdh/nxC
dimeY = height/nyC
#Estado de las celdas. Vivas = 1; Muertas = 0
EstadodeJuego = np.zeros((nxC,nyC))
#Automata movil
EstadodeJuego[21,21] = 1
EstadodeJuego[22,22] = 1
EstadodeJuego[22,23] = 1
EstadodeJuego[21,23] = 1
EstadodeJuego[20,23] = 1
#Automata estatico
EstadodeJuego[5,5] = 1
EstadodeJuego[5,6] = 1
EstadodeJuego[6,5] = 1
EstadodeJuego[6,6] = 1
#Autoamta nave
EstadodeJuego[10,10] = 1
EstadodeJuego[10,11] = 1
EstadodeJuego[10,12] = 1
EstadodeJuego[11,9] = 1
EstadodeJuego[11,13] = 1
#automata mariposa
EstadodeJuego[15,15] = 1
EstadodeJuego[15,16] = 1
EstadodeJuego[15,17] = 1
EstadodeJuego[16,14] = 1
EstadodeJuego[16,18] = 1
EstadodeJuego[17,15] = 1
EstadodeJuego[17,16] = 1
EstadodeJuego[17,17] = 1
#automata planeador
EstadodeJuego[25,25] = 1
EstadodeJuego[25,26] = 1
EstadodeJuego[25,27] = 1
EstadodeJuego[26,25] = 1
EstadodeJuego[27,26] = 1
#automata marciano
EstadodeJuego[30,30] = 1
EstadodeJuego[30,31] = 1
EstadodeJuego[30,32] = 1
EstadodeJuego[31,30] = 1
EstadodeJuego[31,31] = 1
EstadodeJuego[31,32] = 1
EstadodeJuego[32,30] = 1
EstadodeJuego[32,31] = 1
EstadodeJuego[32,32] = 1
#automata pentadecathlon
EstadodeJuego[35,35] = 1
EstadodeJuego[35,36] = 1
EstadodeJuego[35,37] = 1
EstadodeJuego[36,35] = 1
EstadodeJuego[36,36] = 1
EstadodeJuego[36,37] = 1
EstadodeJuego[37,35] = 1
EstadodeJuego[37,36] = 1
EstadodeJuego[37,37] = 1
EstadodeJuego[35,38] = 1
EstadodeJuego[36,38] = 1
EstadodeJuego[37,38] = 1
#automata parpadeador
EstadodeJuego[40,40] = 1
EstadodeJuego[40,41] = 1
EstadodeJuego[40,42] = 1
#automata parpadeador
EstadodeJuego[45,45] = 1
EstadodeJuego[45,46] = 1

#Control de la ejecucion del juego
ejecucion = False
#Abriendo la ventana
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        elif event.type == py.KEYDOWN:
            ejecucion = not ejecucion
        mouseClick = py.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX,posY = py.mouse.get_pos()
            celX,celY = int(np.floor(posX/dimeX)),int(np.floor(posY/dimeY))
            EstadodeJuego[celX,celY] = not EstadodeJuego[celX,celY]
    #Logica para el juego
    #Copiamos el estado actual del juego
    nuevoEstado = np.copy(EstadodeJuego)
    dimesiones.fill(bg)
    time.sleep(0.1)
    #Creando los cuadros
    for y in range(0,nxC):
        for x in range(0,nyC):
            if not ejecucion:
                #Calculando el numero de vecinos cercanos
                vecinosCelda = EstadodeJuego[(x-1) % nxC,(y-1) % nyC] + \
                               EstadodeJuego[(x) % nxC,(y-1) % nyC] + \
                               EstadodeJuego[(x+1) % nxC,(y-1) % nyC] + \
                               EstadodeJuego[(x-1) % nxC,(y) % nyC] + \
                               EstadodeJuego[(x+1) % nxC,(y) % nyC] + \
                               EstadodeJuego[(x-1) % nxC,(y+1) % nyC] + \
                               EstadodeJuego[(x) % nxC,(y+1) % nyC] + \
                               EstadodeJuego[(x+1) % nxC,(y+1) % nyC]
                #Reglas del juego de la vida

                #Regla 1: Una celula muerta con exactamente 3 vecinos vivos, "revive"
                if EstadodeJuego[x,y] == 0 and vecinosCelda == 3:
                    nuevoEstado[x,y] = 1
                #Regla 2: Una celula viva con menos de 2 o mas de 3 vecinos vivas, "Muere"
                elif EstadodeJuego[x,y] == 1 and (vecinosCelda < 2 or vecinosCelda > 3):
                    nuevoEstado[x,y] = 0

            poligonos = [((x)*dimeX,(y)*dimeY),
                             ((x+1)*dimeX,(y)*dimeY),
                             ((x+1)*dimeX,(y+1)*dimeY),
                             ((x)*dimeX,(y+1)*dimeY)]
            #Pintando las celdas
            if nuevoEstado[x,y] == 0:
                py.draw.polygon(dimesiones,(128,128,128),poligonos,1)
            else:
                py.draw.polygon(dimesiones,(255,255,255),poligonos,0)
    #Actualizando el estado del juego
    EstadodeJuego = np.copy(nuevoEstado)
    py.display.flip()