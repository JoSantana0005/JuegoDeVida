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
#Abriendo la ventana
while True:
    py.display.flip()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    #Logica para el juego
        #Creando los cuadros
    for y in range(0,nxC):
        for x in range(0,nyC):
            #Calculando el numero de vecinos cercanos
            vecinosCelda = EstadodeJuego[(x-1)%nxC,(y-1)%nyC] + \
                           EstadodeJuego[(x)%nxC,(y-1)%nyC] + \
                           EstadodeJuego[(x+1)%nxC,(y-1)%nyC] + \
                           EstadodeJuego[(x-1)%nxC,(y)%nyC] + \
                           EstadodeJuego[(x+1)%nxC,(y)%nyC] + \
                           EstadodeJuego[(x-1)%nxC,(y+1)%nyC] + \
                           EstadodeJuego[(x)%nxC,(y+1)%nyC] + \
                           EstadodeJuego[(x+1)%nxC,(y+1)%nyC]

            
            poligonos = [((x)*dimeX,y*dimeY),
                         ((x+1)*dimeX,y*dimeY),
                         ((x+1)*dimeX,(y+1)*dimeY),
                         ((x)*dimeX,(y+1)*dimeY)]
            
            py.draw.polygon(dimesiones,(128,128,128),poligonos,1)
    py.display.flip()