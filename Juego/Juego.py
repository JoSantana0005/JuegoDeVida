#Librerias a utilizar en el proyecto
import pygame as py
import numpy as np
import time

#Inicio pygame
py.init()
#Ancho y Largo de la ventana del juego
witdh,height = 700,500
py.display.set_caption("Juego de la Vida")
dimesiones = py.display.set_mode((witdh,height))
#Color del fondo
bg = 25,25,25
dimesiones.fill(bg)
#Abriendo la ventana
while True:
    py.display.flip()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    #Logica para el juego
        #Creando los cuadros
        