"""-------------------------EJEMPLOS SIMPLES------------------------
def saludar(nombre):
    return f"Hola, {nombre}!"  # Devuelve el valor

resultado = saludar("Alejandro")
print(resultado)  # Esto imprimirá: Hola, Alejandro!

def saludo(nombre, cargo, antiguedad, sueldo): #le pasamos estos argumentos de todo tipo
    return f"hola {nombre} tu cargo es {cargo} y llevas {antiguedad} años trabajando aqui y en base a tu sueldo de {sueldo} tu bono es de {antiguedad * (sueldo / 6):.3f}" 

p= saludo("Alejandro", "gerente", 5, 2300.68)
print(p)
"""

def evaluar_nota(nota):
    if nota >= 80:
        return "Excelente"
    elif nota >= 51:
        return "Aprobado"
    else:
        return "vete ahora y nunca regreses xd"

m=int(input("ingresa tu nota real: "))
print(evaluar_nota(m))  # Salida: Aprobado








"""----------------AHORA VAMOS A HACER UNA FUNCION QUE USA EL FOR ----------------
def srmd (a): #RECIBE UN PARAMETRO O ARGUMENTO 
    for i in range(1, a+1): #le decimos que el rango de nuneros que debe recorres es 1 hasta a
        n=i*a 
        print(f"{i} X {a} = {n}")  #vamos a mostrar el iterador para mostrar 
        
a=int(input("ingresa un numero por favor: "))        
tabla = srmd(a)
print(tabla)
"""

