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


#Abriendo la ventana
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    #Logica para el juego
    #Copiamos el estado actual del juego
    nuevoEstado = np.copy(EstadodeJuego)
    dimesiones.fill(bg)
    time.sleep(0.1)
    #Creando los cuadros
    for y in range(0,nxC):
        for x in range(0,nyC):
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