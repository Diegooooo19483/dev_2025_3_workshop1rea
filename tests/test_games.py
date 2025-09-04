import pytest
from src.games.games import Games

class TestGames:
    def setup_method(self):
        self.games = Games()
    
    def test_piedra_papel_tijera(self):
        # Test empates
        assert self.games.piedra_papel_tijera("piedra", "piedra") == "empate"
        assert self.games.piedra_papel_tijera("papel", "papel") == "empate"
        assert self.games.piedra_papel_tijera("tijera", "tijera") == "empate"
        
        # Test victorias de jugador1
        assert self.games.piedra_papel_tijera("piedra", "tijera") == "jugador1"
        assert self.games.piedra_papel_tijera("papel", "piedra") == "jugador1"
        assert self.games.piedra_papel_tijera("tijera", "papel") == "jugador1"
        
        # Test victorias de jugador2
        assert self.games.piedra_papel_tijera("tijera", "piedra") == "jugador2"
        assert self.games.piedra_papel_tijera("piedra", "papel") == "jugador2"
        assert self.games.piedra_papel_tijera("papel", "tijera") == "jugador2"
        
        # Test con mayúsculas y minúsculas mixtas
        assert self.games.piedra_papel_tijera("PIEDRA", "tijera") == "jugador1"
        assert self.games.piedra_papel_tijera("Papel", "PIEDRA") == "jugador1"
        
        # Test con valores inválidos
        assert self.games.piedra_papel_tijera("piedra", "invalid") == "invalid"
        assert self.games.piedra_papel_tijera("invalid", "papel") == "invalid"
    
    def test_adivinar_numero_pista(self):
        # Correcto
        assert self.games.adivinar_numero_pista(50, 50) == "correcto"
        assert self.games.adivinar_numero_pista(1, 1) == "correcto"
        assert self.games.adivinar_numero_pista(100, 100) == "correcto"
        
        # Muy alto
        assert self.games.adivinar_numero_pista(50, 75) == "muy alto"
        assert self.games.adivinar_numero_pista(10, 20) == "muy alto"
        assert self.games.adivinar_numero_pista(1, 99) == "muy alto"
        
        # Muy bajo
        assert self.games.adivinar_numero_pista(50, 25) == "muy bajo"
        assert self.games.adivinar_numero_pista(100, 1) == "muy bajo"
        assert self.games.adivinar_numero_pista(20, 10) == "muy bajo"
        
        # Negativos
        assert self.games.adivinar_numero_pista(-10, -5) == "muy alto"
        assert self.games.adivinar_numero_pista(-10, -15) == "muy bajo"
        assert self.games.adivinar_numero_pista(-10, -10) == "correcto"
        
        # Casos límite
        assert self.games.adivinar_numero_pista(0, 1) == "muy alto"
        assert self.games.adivinar_numero_pista(0, -1) == "muy bajo"
    
    def test_ta_te_ti_ganador(self):
        # Filas
        tablero_fila1 = [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_fila1) == "X"
        
        tablero_fila2 = [[" ", " ", " "], ["O", "O", "O"], ["X", "X", " "]]
        assert self.games.ta_te_ti_ganador(tablero_fila2) == "O"
        
        tablero_fila3 = [["O", "X", "O"], ["X", "O", "X"], ["X", "X", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_fila3) == "X"
        
        # Columnas
        tablero_col1 = [["X", "O", "O"], ["X", "O", "X"], ["X", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_col1) == "X"
        
        tablero_col2 = [["X", "O", "X"], [" ", "O", "X"], ["X", "O", " "]]
        assert self.games.ta_te_ti_ganador(tablero_col2) == "O"
        
        tablero_col3 = [["X", "O", "O"], ["X", "X", "O"], [" ", " ", "O"]]
        assert self.games.ta_te_ti_ganador(tablero_col3) == "O"
        
        # Diagonales
        tablero_diag1 = [["X", "O", "O"], ["O", "X", "O"], ["X", "O", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_diag1) == "X"
        
        tablero_diag2 = [["X", "O", "O"], ["X", "O", "X"], ["O", "X", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_diag2) == "O"
        
        # Empate
        tablero_empate = [["X", "O", "X"], ["O", "O", "X"], ["O", "X", "O"]]
        assert self.games.ta_te_ti_ganador(tablero_empate) == "empate"
        
        # Continúa (corregido)
        tablero_continua = [["X", "O", " "], [" ", " ", "O"], ["O", " ", "X"]]
        assert self.games.ta_te_ti_ganador(tablero_continua) == "continua"
        
        # Vacío
        tablero_vacio = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        assert self.games.ta_te_ti_ganador(tablero_vacio) == "continua"
    
    def test_generar_combinacion_mastermind(self):
        colores = ["rojo", "azul", "verde", "amarillo"]
        
        combinacion = self.games.generar_combinacion_mastermind(4, colores)
        assert len(combinacion) == 4
        for color in combinacion:
            assert color in colores
        
        combinacion2 = self.games.generar_combinacion_mastermind(6, colores)
        assert len(combinacion2) == 6
        
        combinacion3 = self.games.generar_combinacion_mastermind(1, colores)
        assert len(combinacion3) == 1
        assert combinacion3[0] in colores
        
        colores_limitados = ["rojo", "azul"]
        combinacion4 = self.games.generar_combinacion_mastermind(3, colores_limitados)
        assert len(combinacion4) == 3
        for color in combinacion4:
            assert color in colores_limitados
        
        combinacion5 = self.games.generar_combinacion_mastermind(0, colores)
        assert len(combinacion5) == 0
        
        combinaciones = []
        for _ in range(10):
            comb = self.games.generar_combinacion_mastermind(4, colores)
            combinaciones.append(tuple(comb))
        assert len(set(combinaciones)) >= 1
    
    def test_validar_movimiento_torre_ajedrez(self):
        tablero_vacio = [[" " for _ in range(8)] for _ in range(8)]
        
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 7, tablero_vacio) == True
        assert self.games.validar_movimiento_torre_ajedrez(4, 2, 4, 6, tablero_vacio) == True
        assert self.games.validar_movimiento_torre_ajedrez(7, 7, 7, 0, tablero_vacio) == True
        
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 7, 0, tablero_vacio) == True
        assert self.games.validar_movimiento_torre_ajedrez(2, 4, 6, 4, tablero_vacio) == True
        assert self.games.validar_movimiento_torre_ajedrez(7, 3, 1, 3, tablero_vacio) == True
        
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 1, 1, tablero_vacio) == False
        assert self.games.validar_movimiento_torre_ajedrez(3, 3, 5, 5, tablero_vacio) == False
        
        assert self.games.validar_movimiento_torre_ajedrez(4, 4, 4, 4, tablero_vacio) == False
        
        tablero_con_piezas = [[" " for _ in range(8)] for _ in range(8)]
        tablero_con_piezas[0][3] = "P"
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 7, tablero_con_piezas) == False
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 2, tablero_con_piezas) == True
        assert self.games.validar_movimiento_torre_ajedrez(0, 4, 0, 7, tablero_con_piezas) == True
        
        tablero_con_piezas2 = [[" " for _ in range(8)] for _ in range(8)]
        tablero_con_piezas2[3][0] = "R"
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 7, 0, tablero_con_piezas2) == False
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 2, 0, tablero_con_piezas2) == True
        
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 0, 8, tablero_vacio) == False
        assert self.games.validar_movimiento_torre_ajedrez(0, 0, 8, 0, tablero_vacio) == False
        assert self.games.validar_movimiento_torre_ajedrez(-1, 0, 0, 0, tablero_vacio) == False
        assert self.games.validar_movimiento_torre_ajedrez(0, -1, 0, 0, tablero_vacio) == False
