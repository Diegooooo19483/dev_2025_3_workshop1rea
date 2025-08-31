class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """

    def fibonacci(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        secuencia = [0, 1]
        while len(secuencia) < n:
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]

    def es_primo(self, n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [x for x in range(2, n + 1) if self.es_primo(x)]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n

    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        triangulo = [[1]]
        for _ in range(1, filas):
            prev = triangulo[-1]
            fila = [1]
            for j in range(1, len(prev)):
                fila.append(prev[j - 1] + prev[j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        if n < 0:
            return None
        if n in (0, 1):
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        return n == sum(int(d) ** potencia for d in digitos)

    def es_cuadrado_magico(self, matriz):
        if not matriz or any(len(fila) != len(matriz) for fila in matriz):
            return False
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_objetivo:
                return False
       
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
       
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False
        return True
