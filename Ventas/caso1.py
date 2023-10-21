#importamos la libreria pandas
import pandas as pd

#pedimos informacion de los años de ventas al usuario
inicio = int(input('Introduce el año inicial: '))
fin = int(input('Introduce el año final: '))

#Creamos el diccionario ventas
ventas = {}

#Mediante un ciclo For vamos rellenando las ventas de cada  año
for i in range(inicio, fin+1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
ventas = pd.Series(ventas)
print('Ventas\n', ventas)
print('Ventas con descuento\n', ventas*0.9)