# coleccion de multiples datos de un mismo tipo en una misma variable. jaja
"""
frutas =["juanete", "nuskis", "rata", "jimbo", "flaco", "gordo", 55, 15.66] 
numero_E= len(frutas)
print("el numero de elementos es:", numero_E)

#              1         2        3       4        5        6     7     8    
frutas = ["juanete", "nuskis", "rata", "jimbo", "flaco", "gordo", 55, 15.66]
numero_E = len(frutas)
print("el numero de elementos es:", numero_E)
print(frutas[0]) #que muestre el primer elemento de la lista
print(frutas[0:4]) # que muestre de la posicion cero a la 4(excepto la 4)
print(frutas[:3]) #desde el comienzo hasta el 3
print(frutas[4:]) #desde el 4 hasta el final

#              8         7        6       5        4        3     2     1  
frutas = ["juanete", "nuskis", "rata", "jimbo", "flaco", "gordo", 55, 15.66]
print(frutas[-7])  #tomara justo en la posicion en la que este
print(frutas[2:-2]) 
print(frutas[:-3])

frutas = ["juanete", "nuskis", "rata", "jimbo", "flaco", "gordo", 55, 15.66]
que=input("a quien buscas: ")
if que in frutas:
    print("si esta ")
else:
    print("no se encuentra")

#              0        1         2       3        4        5      6     7  
nombres = ["juanete", "nuskis", "rata", "jimbo", "flaco", "gordo", 55, 15.66]
nombres.append("serch")#es lo mismo que el insert solo que este o inserta al final de la lista
apellidos=["ochoa", "santos"]
nombres.extend(apellidos) #agregar cualquier tipo de coleccion a otra lista tuplas, listas, etc
segundos_nombre=('Nata','gabi','ange')#tuplas
nombres.extend(segundos_nombre)
apellidos_maternis={"maidana": "pitu"}#diccionario auque aqui solo agrega el primero
nombres.extend(apellidos_maternis)
print(nombres)
"""
#              0          1        2       3        4        5        6        7  
#nombres = ["juanete", "nuskis55", "rata", "jimbo", "flaco55", "gordo", "Pandas", 55]
"""
nombres.remove(nombres[4]) #le estamos dando el numero del elemento que queremos eliminar
nombres.remove('gordo')#le decimos textual cual queremos eliminar
nombres.pop()#elimina el ultimo elemento
nombres.pop(0)#elimina el numero de la posicion que le especifiquemos
print(nombres)
"""

"""         recorrer un array con un for     
for i in range(len(nombres)): #le decimos que este for tiene que ir de i(0) hasta el len(nombres)(osea 7)
    print(f"{i+1}. {nombres[i]} ------- ", end=" ") #usamos las f para poder imprimir mejor.
"""

#nombres = ["juanete", "nuskis55", "rata", "jimbo", "flaco55", "gordo", "Pandas", 55]
#[print(i) for i in nombres]    


"""        ver si hay un elemento en la lista usando for      
                #en este caso todas son de tipo string para que funcione.
nombres = ["juanete", "nuskis55", "rata", "jimbo", "flaco55", "gordo", "Pandas"] 
lista= [] #importante es que la lista en la que vayas a buscar elementos sea del mismo tipo.  
for i in nombres:
    if "55" in i:
        lista.append(i) #en caso de que se cumpla la condicion se agrega el elemnto a la lista[] 
print(lista)
""" 


"""        ver si hay un elemento en la lista usando for     
                #en este caso todas son de tipo int para que funcione.
nombres = [12,55,99,12,155,195,88,65,55,845,55] 
lista= [] #importante es que la lista en la que vayas a buscar elementos sea del mismo tipo.  
for i in nombres:#el tipo int no es iterable.
    if i==55:
        lista.append(i) #en caso de que se cumpla la condicion se agrega el elemnto a la lista[] 
print(lista)
 """ 
 
"""              METODO DE ORDENAMIENTO descendente       
num=[4,8,9,1,18,6,55,7]
num.sort(reverse=True) #este es el metodo de ordenamiento de forma inversa
print(num) #en el caso de que sean strings los ordenara alfabeticamente.
 """

dias=["lunes", "martes", "miercoles_ xd"]
semana=dias.copy()
semanaC=semana.reverse()
print(dias + semana)

 
 
 
 