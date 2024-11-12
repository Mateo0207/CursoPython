# cuandos se va añadir algo a ese txt se utiliza 'a'
with open ('archivos\\texto_dalto.txt', 'w', encoding= "UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("jajajaja xd xd xd")
    #agregando 2 lineas con writlines
    archivo.writelines(["hola crack\n","fiera"])
    #agregando otras 2 lineas
    archivo.writelines(["hola crack\n","fiera"]) 
    
    
    #usando un bucle para agregar varias lineas
    for i in range (5):
        archivo.write(f'\n Linea {i+1} agregada ')