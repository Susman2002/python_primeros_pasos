"""
tuplas=("moto", "moto", "alex", "marty")
print(tuplas)
print(type(tuplas))
list_Tupla= list(tuplas)#transformamos a lista la tupla
print(list_Tupla)
print(type(list_Tupla))
"""
#DESEMPAQUETAMIENTO
tuplas=("moto", "moto", "alex", "marty")
(a,b,c,d)=tuplas #le asigna una variable a todos los elementos dela tupla
print(b, d)
