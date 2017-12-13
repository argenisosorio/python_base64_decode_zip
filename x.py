# -*- coding: utf-8 -*-
"""
Codificar y Decodificar un fichero .zip en un solo script usando base64 en python
"""
import base64 # Importamos la librería base64 de python

# Paso de la codificación

with open("1.zip", "rb") as f: # Leemos el fichero que vamos a codificar.
    bytes = f.read()
    encoded = base64.b64encode(bytes) # Codificamos a base64 el fichero.
    print encoded # Cadena de texto ASCII que es el fichero codificado, imprimimos por pantalla para ver la cadena de caracteres.


# Paso de la decodificación

    decoded = base64.b64decode(encoded) # Decodificamos la cadena de caracteres.
    filename = '2.zip' # Fichero decodificado a partir de la cadena de texto ASCII que es el .zip codificado.
    with open(filename, 'wb') as f: # Asignamos un nombre al nuevo fichero.
        f.write(decoded) # Creamos el fichero y la guardamos en el directorio del script.
