class Data:
    
    
    def invertir_lista(self, lista):
        
        inicio = 0
        fin = len(lista) - 1

        while inicio < fin:
            lista[inicio], lista[fin] = lista[fin], lista[inicio]
            inicio += 1
            fin -= 1

        return lista
    
    def buscar_elemento(self, lista, elemento):
        
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        resultado = []
        for elemento in lista:
            if not any(isinstance(e, type(elemento)) and e == elemento for e in resultado):
                resultado.append(elemento)
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        
        i, j = 0, 0
        resultado = []

        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
    
    def rotar_lista(self, lista, k):
        
        if not lista:
            return lista
        
        n = len(lista)
        k = k % n

        resultado = [] 

        for i in range(n - k, n):
            resultado.append(lista[i])
        
        for i in range(0,n - k):
            resultado.append(lista[i])

        return resultado
    

    def encuentra_numero_faltante(self, lista):
        
        n = len(lista) + 1
        suma_total = n * (n + 1) // 2
        suma_lista = sum(lista)
        return suma_total - suma_lista
        
    
    def es_subconjunto(self, conjunto1, conjunto2):
        
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        
        pila = []
        def push(elemento):
            pila.append(elemento)
        def pop():
            if not pila:
                return None
            return pila.pop()
        def peek():
            if not pila:
                return None
            return pila[-1]
        def is_empty():
            return len(pila) == 0
        return {
            'push': push,
            'pop': pop,
            'peek': peek,
            'is_empty': is_empty
        }
    
    def implementar_cola(self):
        
        cola = []
        def enqueue(elemento):
            cola.append(elemento)
        def dequeue():
            if not cola:
                return None
            return cola.pop(0)
        def peek():
            if not cola:
                return None
            return cola[0]
        def is_empty():
            return len(cola) == 0
        return {
            'enqueue': enqueue,
            'dequeue': dequeue,
            'peek': peek,
            'is_empty': is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0
        transpuesta = [ [0] * filas for _ in range(columnas) ]

        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i] = matriz[i][j]
        return transpuesta