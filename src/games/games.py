import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        opciones = ["piedra", "papel", "tijera"]
        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"
        if jugador1 == jugador2:
            return "empate"
        if (jugador1 == "piedra" and jugador2 == "tijera") or \
           (jugador1 == "papel" and jugador2 == "piedra") or \
           (jugador1 == "tijera" and jugador2 == "papel"):
            return "jugador1"
        return "jugador2"

    def ta_te_ti_ganador(self, tablero):
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]
        for fila in tablero:
            for celda in fila:
                if celda == " ":
                    return "continua"
        return "empate"

    def validar_movimiento_torre_ajedrez(self, x1, y1, x2, y2, tablero):
        if not (0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8):
            return False
        if x1 == x2 and y1 == y2:
            return False
        if x1 != x2 and y1 != y2:
            return False
        if x1 == x2:
            paso = 1 if y2 > y1 else -1
            for y in range(y1 + paso, y2, paso):
                if tablero[x1][y] != " ":
                    return False
        else:
            paso = 1 if x2 > x1 else -1
            for x in range(x1 + paso, x2, paso):
                if tablero[x][y1] != " ":
                    return False
        return True

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento < numero_secreto:
            return "muy bajo"
        else:
            return "muy alto"

    def generar_combinacion_mastermind(self, longitud, colores):
        return [random.choice(colores) for _ in range(longitud)]
