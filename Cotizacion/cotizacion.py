'''Lee un archivo CSV utilizando la biblioteca pandas, realiza algunas operaciones sobre los datos y devuelve un DataFrame que resume las cotizaciones en términos 
de mínimo, máximo y media. Aquí hay una breve explicación de lo que debería devolver el código:

    pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0) carga el archivo CSV especificado ('H:\Pandas\Cotizacion\cotizacion.csv') en un DataFrame. Se asume que el archivo CSV utiliza punto y coma (;) como separador de campos, coma (,) como separador decimal y el índice de la primera columna (columna 0).

    pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media']) crea un nuevo DataFrame que contiene tres filas: 'Mínimo', 'Máximo' y 'Media'. Cada fila contiene los valores mínimos, máximos y promedio de todas las columnas en el DataFrame df original.'''



import pandas as pd

def resumen_cotizaciones(fichero):
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
    resumen = pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])
    print(resumen)


resumen_cotizaciones('H:\Pandas\Cotizacion\cotizacion.csv')