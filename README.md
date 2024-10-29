# Juego de La Vida de Conway
<img src="https://ramonaharrison.github.io/images/conway.gif" width="100%">

## ES

## Descripcion:
El Juego de la Vida de Conway es un autómata celular creado por el matemático John Horton Conway en 1970. Es un modelo matemático que simula la vida en una cuadrícula bidimensional donde cada celda puede estar viva o muerta. Las celdas evolucionan en función de reglas simples basadas en el estado de las celdas vecinas. Este código implementa el Juego de la Vida utilizando la biblioteca Pygame y NumPy en Python.

## Desarrolladores:
- Jose Santana [@JoSantana0005](https://github.com/JoSantana0005)
- Alejandro Chavez [@alejandrochmejia](https://github.com/alejandrochmejia)
- Cesar Dominguez [@cesardarizaleta](https://github.com/cesardarizaleta)

## Requisitos:
- Python 3.x
- Numpy
- Pygame

Puedes instalar las dependencias del proyecto utilizando el siguiente comando:
```bash
pip install pygame numpy
```

## Reglas del juego

El estado de cada celda en el tablero se actualiza en cada iteración según las siguientes reglas:

Una celda muerta con exactamente 3 vecinos vivos "revive".
Una celda viva con menos de 2 o más de 3 vecinos vivos "muere".
Una celda viva con 2 o 3 vecinos vivos permanece viva.
Las celdas vecinas se consideran en un entorno de Moore, lo que significa que cada celda tiene 8 vecinos (las celdas adyacentes en horizontal, vertical y diagonal).
  
