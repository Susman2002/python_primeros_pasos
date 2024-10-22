import time
class QuickSortRecursivo:
    def ordenar(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivote = arr[0]
            menores = [x for x in arr[1:] if x <= pivote]
            mayores = [x for x in arr[1:] if x > pivote]
            return self.ordenar(menores) + [pivote] + self.ordenar(mayores)
class PrincipalQuickSortRecursivo:
    def ejecutar(self):
        # Lista de números desordenada por defecto
        # 10 lista = [64, 34, 25, 12, 22, 11, 90, 88, 45, 67]
        # 15 lista = [64, 34, 25, 12, 22, 11, 90, 88, 45, 67, 55, 62, 17, 7, 89, 17]
        # 25 lista = [34, 67, 90, 25, 12, 76, 33, 88, 19, 52, 8, 11, 55, 49, 22, 98, 64, 23, 89, 17, 75, 45, 13, 29, 100]
        # 20 lista = [34, 67, 90, 25, 12, 76, 33, 88, 19, 52, 8, 11, 55, 49, 22, 98, 64, 23, 89, 17]
        lista = [34, 67, 90, 25, 12, 76, 33, 88, 19, 52, 8, 11, 55, 49, 22, 98, 64, 23, 89, 17, 75, 45, 13, 29, 100, 91, 57, 63, 82, 48]

        print("Lista original:", lista)
        quick_sort = QuickSortRecursivo()
        tiempo = time.perf_counter()  
        lista_ordenada = quick_sort.ordenar(lista.copy())
        tiempo_ejecucion = (time.perf_counter() - tiempo) * 100100 
    
        print("\nQuick Sort Recursivo:")
        print("Lista ordenada:", lista_ordenada)
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.3f}")


if __name__ == "__main__":
    principal = PrincipalQuickSortRecursivo()
    principal.ejecutar()

