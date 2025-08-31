import math
from collections import Counter

class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        if not numeros:
            return 0
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        mitad = n // 2
        if n % 2 == 0:  
            return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
        else:  # impar
            return numeros_ordenados[mitad]
    
    def moda(self, numeros):
        if not numeros:
            return None  
        conteo = Counter(numeros)
        max_freq = max(conteo.values())
        for num in numeros:  
            if conteo[num] == max_freq:
                return num
    
    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0
        if len(numeros) == 1:
            return 0
        mu = self.promedio(numeros)
        var = sum((x - mu) ** 2 for x in numeros) / len(numeros)
        return math.sqrt(var)
    
    def varianza(self, numeros):
        if not numeros:
            return 0
        if len(numeros) == 1:
            return 0
        mu = self.promedio(numeros)
        return sum((x - mu) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)
