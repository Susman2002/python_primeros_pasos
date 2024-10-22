"""
lista=[1,1,2,2,3,5]
x=1
for i in lista:
    if(i==3):
        print("final del ciclo")
        break
    print(f"{x}, {i}")
    x+=1
"""
"""
lista = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
for i in range(len(lista)): #genera una secuencia de numeros que va desde 0 hasta len(lista) -1
    # Aquí el valor de 'i' ya está asignado automáticamente por el ciclo for el valor asignado es 0
    print(f"Índice: {i}, Elemento: {lista[i]}")
"""

"""
# Crear una lista
lista = [1,5,5,5,5,6,7,7,5,4]
# Usar un for para recorrer e imprimir los elementos
for i in range(0, len(lista), 2): #primero 0 dentro del range indica que comenzaremos desde 0 
    print(lista[i],i)             #segundo la funcion len(lista) indica que el bucle terminara nates de llegar hay
                                  #tercero el , 2 indica que iremos de 2 en 2
"""

"""
lista_lebguajes=["python", "javaScript", "java", "c#", "angular", "react", "nodejs", "ruby", "r", "django"]
x=1
for i in lista_lebguajes:
    if i=="angular":       
        continue #cuando ponemos esta el bucle se salta esa iteracion es decir se pasa a la sig.
    print(f"{x} lenguaje: {i} ")   #como puedes ver no hay angular en la salida.
    x+=1
"""
"""
#asi se itera un texto
texto="hola ale mañana vamos a trabajar perro"
for letra in texto:
    print(letra)
"""

"""
rango=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(0, len(rango)):   #le esta diciendo que el rango de iteraciones del for debe ser de 0 al 14 (no toma el 15)
    if i == 7:
        print("eso eso eso es todo amigos")
    print(i, end=" ")                #pero lo hara de 3 en 3 (, 3)
"""
"""
letras =["a", "b", "c"]
numeros=[1,2,3]
for l in letras:
    for n in numeros: #este bucle debe terminar primero para continuar con el de afuera
        print(l,n, end=" ")
"""
for i in range(1, 11):
    print(i)
