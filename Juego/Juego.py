#Librerias a utilizar en el proyecto
import pygame as py
import numpy as np
import time

#Inicio pygame
py.init()
#Ancho y Largo de la ventana del juego
witdh,height = 700,500
py.display.set_caption("Juego de la vida")
py.display.set_mode((witdh,height))