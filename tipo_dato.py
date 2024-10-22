# string
"""
Conjunto = {1,1,2,2,3,3} 
Lista = [1,1,2,2,3,3]
print(Conjunto)
print(Lista)

numero_decimal = 154
print(type( numero_decimal)) #cuando le pones el type(nombre_de_variable) para que te diga que tipo es esta variable
print(numero_decimal)
numero_decimal=float(numero_decimal)
print(type( numero_decimal)) #cuando le pones el type(nombre_de_variable) para que te diga que tipo es esta variable
print(numero_decimal)

import random
#aleatorio = random.randrange(1, 11)
aleatorio_par= random.randrange(2,21,5)
#print(aleatorio)
print(aleatorio_par)

num = 17
div = 17 % 3
print(div)

print("por cada hora se te paga 40bs")
cantidad_horas = int(input("ingresa la cantidad de horas que trabajaste: "))
total = cantidad_horas * 40
print("su monto total es: ", total)

letras="juanete es muy gracioso pero muy gruñon tambien igual que el SanTos xd"
print(letras[11:50]) #se imprimira desde indice 11 hasta el 50
print(letras[:11]) #este va desde el inicio hasta el 11 no incluye el 11 mismo 
print(letras[11:]) #que va desde el 11 hasta el final

c=55
frace=f"tu debes {c*66:.2f}$" #2f para agregar dos decimales al numero 
print(frace)

mi_cadena = "hola hola"
print(mi_cadena.count("hola"))  # Salida: 2 (porque "hola" aparece dos veces en la cadena)

cadena1 = "12345"
print(cadena1.isnumeric())  # Salida: True

cadena2 = "12345a"
print(cadena2.isnumeric())  # Salida: False

cadena3 = "⅕"  # Fracción
print(cadena3.isnumeric())  # Salida: True

mi_lista = [3, 1, 2,77,99,5,8,]
print(sorted(mi_lista))  # Salida: [1, 2, 3]
"""
texto=" hola juan como estas perro "
mayus=texto.upper()
new_texto=texto.strip()
new_mayus=mayus.strip()
print(new_texto, new_mayus)

