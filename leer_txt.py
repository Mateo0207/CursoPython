#archivo = open("archivos\\texto_dalto.txt", encoding="UTF-8")  
#print(archivo.read())

archivo_sin_leer = open("archivos\\texto_dalto.txt", encoding="UTF-8")  

#leer archivo completo 
#archivo = archivo_sin_leer.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()

#cerar el archivo, importante cerrarlo para no perder datos, liberar recursos
archivo_sin_leer.close() 
print(linea )


