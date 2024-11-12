import pandas as pd 

#usando la funcion read_csv para leer el archivo CSV, df-> data frame, estructuras de datos bidimensionales
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")
#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordenandode forma descendente
df_orden_descendente = df.sort_values("edad", ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df, df2])

#accediendo a la primer fila con head()
primer_fila = df.head(1)

#accediendo a las  ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales =df.shape
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]

#con desempaquetado queda mejor que hacer el proceso de arriba
filas_y_columnas_totales, columnas_totales = df.shape


#para analisis de datos, obteniendo data estadistica del dataframe
df_info = df.describe()


#accediendo a un elemento especifico del df con loc, se accede a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "edad"]

#accediendo a un elemento especifrico del df con iloc, es decir con los indices, lo mismo que lo anterior pero con iloc
elemento_especifico_loc = df.iloc[2, 2]

#accediendo a todas las filas de una columna
apellidos = df.loc[:,"apellido"]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor a 30
mayor_a_30 = df.loc[df["edad"]>30,:]

print(mayor_a_30)