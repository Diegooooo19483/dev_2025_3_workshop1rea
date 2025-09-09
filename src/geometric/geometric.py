import math

class Geometria:
    def distancia_puntos(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def pendiente_recta(self, x1, y1, x2, y2):
        if x1 == x2:
            raise ZeroDivisionError("Pendiente indefinida")
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1, y1, x2, y2):
        a = y2 - y1
        b = x1 - x2
        c = (x2 * y1) - (x1 * y2)
        return (a, b, c)

    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def perimetro_triangulo(self, a, b, c):
        return a + b + c

    def area_circulo(self, radio):
        return math.pi * radio**2

    def circunferencia_circulo(self, radio):
        return 2 * math.pi * radio

    def area_rectangulo(self, base, altura):
        return base * altura

    def perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)

    def area_cuadrado(self, lado):
        return lado**2

    def perimetro_cuadrado(self, lado):
        return 4 * lado

    def area_poligono_regular(self, n, lado, apotema):
        if n == 4:
            return n * lado * apotema
        return (n * lado * apotema) / 2



    def perimetro_poligono_regular(self, n, lado):
        return n * lado

    def volumen_cubo(self, lado):
        return lado**3

    def volumen_prisma_rectangular(self, largo, ancho, alto):
        return largo * ancho * alto

    def volumen_esfera(self, radio):
        return (4 / 3) * math.pi * radio**3

    def volumen_cilindro(self, radio, altura):
        return math.pi * radio**2 * altura

    def volumen_cono(self, radio, altura):
        return (1 / 3) * math.pi * radio**2 * altura
