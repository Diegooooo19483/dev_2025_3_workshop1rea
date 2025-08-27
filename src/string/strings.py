class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto = ''.join(c.lower() for c in texto if c.isalnum())
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        invertida = ""
        for c in texto:
            invertida = c + invertida
        return invertida
    
    def contar_vocales(self, texto):
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        return sum(1 for c in texto if c in vocales)
    
    def contar_consonantes(self, texto):
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for c in texto if c in consonantes)
    
    def es_anagrama(self, texto1, texto2):
        t1 = sorted(c.lower() for c in texto1 if c.isalnum())
        t2 = sorted(c.lower() for c in texto2 if c.isalnum())
        return t1 == t2
    
    def contar_palabras(self, texto):
        return len([p for p in texto.split() if p.strip()])
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayúscula la primera letra de cada palabra,
        conservando los espacios originales.
        """
        resultado = ""
        capitalize_next = True
        for c in texto:
            if c.isspace():
                resultado += c
                capitalize_next = True
            else:
                if capitalize_next:
                    resultado += c.upper()
                    capitalize_next = False
                else:
                    resultado += c
        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados, pero conserva un espacio
        al inicio y al final si existían.
        """
        if not texto:
            return texto
        resultado = []
        prev_space = False
        for c in texto:
            if c == " ":
                if not prev_space:
                    resultado.append(c)
                prev_space = True
            else:
                resultado.append(c)
                prev_space = False
        return "".join(resultado)
    
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] in "+-":
            texto = texto[1:]
        return all(c.isdigit() for c in texto) and len(texto) > 0
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
