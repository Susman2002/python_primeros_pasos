import time
class QuickSortIterativo:
    def ordenar(self, arr):
        stack = [(0, len(arr) - 1)]
        
        while stack:
            start, end = stack.pop()
            if start < end:
                p = self.partition(arr, start, end)
                stack.append((start, p - 1))
                stack.append((p + 1, end))
        return arr
    
    def partition(self, arr, low, high):
        pivote = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivote:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
class PrincipalQuickSortIterativo:
    def ejecutar(self):
        
        lista = [64, 34, 25, 12, 22, 11, 90, 88, 45, 67, 55, 62, 17, 7, 89, 17]
        # 25 lista = [34, 67, 90, 25, 12, 76, 33, 88, 19, 52, 8, 11, 55, 49, 22, 98, 64, 23, 89, 17, 75, 45, 13, 29, 100]
        # 20 lista = [34, 67, 90, 25, 12, 76, 33, 88, 19, 52, 8, 11, 55, 49, 22, 98, 64, 23, 89, 17]

        print("Lista original:", lista)
        
        quick_sort = QuickSortIterativo()
        start_time = time.perf_counter() 
        lista_ordenada = quick_sort.ordenar(lista.copy())
        tiempo_ejecucion = (time.perf_counter() - start_time) * 50000          
        print("\nQuick Sort Iterativo:")
        print("Lista ordenada:", lista_ordenada)
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.3f}")

if __name__ == "__main__":
    principal = PrincipalQuickSortIterativo()
    principal.ejecutar()
