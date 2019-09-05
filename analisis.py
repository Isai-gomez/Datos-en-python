#!/usr/bin/python
file = open('palabras.txt','r')
contenedor = "" 
for linea in file:
	contenedor = contenedor + file.readline()
	print(linea.strip().upper())
print(contenedor,linea,"\n")
file.close()
