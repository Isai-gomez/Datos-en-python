# # list and tuplas
nombre = ['German','Karla','Julian','Roberto','Jose Luis']
#acceder a un solo elemento nobre_list[position]
acceder = nombre[0] # German
#acceder a un conjunto de valores nombre_list[inicio:fin]
acceder = nombre[0:3] #German Karla
nombre[0:3] = ['Perdro','Josefa']
#saltando el numero que indicamos name_list[inicio:fin:saltos]
acceder = nombre[::2]
print(acceder,"con altos")
print(nombre)
nombre[0] = 'Roman'
print(nombre)

Diccionarios nombre_dictionari = {nombre_Llave:valor_nombre} 
album = {'titulo':'end of woourd', 'banda':'u2','year':200,'Cantidad canciones':12}
album['Cantidad canciones'] =13
print(album)

#if of else
while True:
    salir = input('Escribe salir o otra tecla para continuar_ ')
    if salir == 'salir':
        break
    else:
        number = int(input("Escribe un numero_ "))
        var  = 'par' if ( number%2 == 0) else 'impar'
        print(var)

# while True:
#     salir = input('Escribe salir o otra tecla para continuar_ ')
#     if salir == 'salir':
#         break
#     else:
#         number = int(input("Escribe tu edad_ "))
#         var  = 'Mayor' if ( number>17) else 'Menor'
#         print(var)
numero = 0
while numero <=100:
    print(numero)
    numero+=1