import pytest
from src.geometric.geometric import Geometria

class TestGeometria:
    def setup_method(self):
        self.geometria = Geometria()

    def test_distancia_puntos(self):
        assert round(self.geometria.distancia_puntos(0, 0, 3, 4), 2) == 5
        assert round(self.geometria.distancia_puntos(-1, -1, 2, 3), 2) == 5

    def test_punto_medio(self):
        assert self.geometria.punto_medio(0, 0, 2, 2) == (1, 1)
        assert self.geometria.punto_medio(-1, -3, 3, 1) == (1, -1)

    def test_pendiente_recta(self):
        assert self.geometria.pendiente_recta(1, 1, 4, 7) == 2
        assert self.geometria.pendiente_recta(-1, -2, 2, 4) == 2
        assert self.geometria.pendiente_recta(1, 5, 5, 5) == 0
        with pytest.raises(ZeroDivisionError):
            self.geometria.pendiente_recta(3, 1, 3, 5)

    def test_ecuacion_recta(self):
        assert self.geometria.ecuacion_recta(1, 1, 3, 3) == (2, -2, 0)

    def test_area_triangulo(self):
        assert self.geometria.area_triangulo(10, 5) == 25
        assert self.geometria.area_triangulo(6, 4) == 12

    def test_perimetro_triangulo(self):
        assert self.geometria.perimetro_triangulo(3, 4, 5) == 12

    def test_area_circulo(self):
        assert round(self.geometria.area_circulo(3), 2) == 28.27

    def test_circunferencia_circulo(self):
        assert round(self.geometria.circunferencia_circulo(3), 2) == 18.85

    def test_area_rectangulo(self):
        assert self.geometria.area_rectangulo(4, 5) == 20

    def test_perimetro_rectangulo(self):
        assert self.geometria.perimetro_rectangulo(4, 5) == 18

    def test_area_cuadrado(self):
        assert self.geometria.area_cuadrado(4) == 16

    def test_perimetro_cuadrado(self):
        assert self.geometria.perimetro_cuadrado(4) == 16

    def test_area_poligono_regular(self):
        assert round(self.geometria.area_poligono_regular(3, 10, 2.89), 2) == 43.35
        assert self.geometria.area_poligono_regular(4, 5, 2.5) == 50

    def test_perimetro_poligono_regular(self):
        assert self.geometria.perimetro_poligono_regular(6, 4) == 24

    def test_volumen_cubo(self):
        assert self.geometria.volumen_cubo(3) == 27

    def test_volumen_prisma_rectangular(self):
        assert self.geometria.volumen_prisma_rectangular(2, 3, 4) == 24

    def test_volumen_esfera(self):
        assert round(self.geometria.volumen_esfera(3), 2) == 113.1

    def test_volumen_cilindro(self):
        assert round(self.geometria.volumen_cilindro(3, 5), 2) == 141.37

    def test_volumen_cono(self):
        assert round(self.geometria.volumen_cono(3, 5), 2) == 47.12
