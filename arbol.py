# -------------------------------
# Tokenizador simple
# -------------------------------
def tokenizar(cadena):
    tokens = []  # lista donde se guardan los tokens
    for ch in cadena.split():  # recorremos cada pedazo de la cadena separado por espacios
        if ch.isdigit():  # si es un número
            tokens.append("num")
        elif ch == "+" or ch == "-":  # si es + o -
            tokens.append("opsuma")
        elif ch == "*" or ch == "/":  # si es * o /
            tokens.append("opmul")
        elif ch == "(":  # si es (
            tokens.append("pari")
        elif ch == ")":  # si es )
            tokens.append("pard")
        else:
            tokens.append("id")  # si no es nada de lo anterior, lo tratamos como identificador
    return tokens  # devolvemos la lista de tokens


# -------------------------------
# Analizador sintáctico recursivo
# -------------------------------
class Parser:
    def __init__(self, grammar):
        self.grammar = grammar  # guarda la gramática, aunque no la usamos directamente
        self.tokens = []  # acá estarán los tokens de entrada
        self.index = 0    # posición actual dentro de los tokens

    def parse(self, tokens):
        self.tokens = tokens  # guardamos los tokens que vamos a analizar
        self.index = 0        # empezamos desde el primer token
        tree = self.E()       # arrancamos la regla principal: E
        if self.index < len(self.tokens):  # si sobran tokens después de analizar
            raise Exception("Error: tokens sobrantes en la entrada")
        return tree           # devolvemos el árbol construido

    # Regla: E -> E opsuma T | T
    def E(self):
        left = self.T()  # primero analizamos un T
        while self._match("opsuma"):  # mientras encontremos + o -
            op = self.tokens[self.index - 1]  # guardamos el operador
            right = self.T()  # analizamos otro T
            left = ("E", op, left, right)  # armamos un nodo del árbol
        return left

    # Regla: T -> T opmul F | F
    def T(self):
        left = self.F()  # primero analizamos un F
        while self._match("opmul"):  # mientras encontremos * o /
            op = self.tokens[self.index - 1]  # guardamos el operador
            right = self.F()  # analizamos otro F
            left = ("T", op, left, right)  # armamos el nodo correspondiente
        return left

    # Regla: F -> id | num | ( E )
    def F(self):
        if self._match("id"):  # si el token es un identificador
            return ("F", "id")
        elif self._match("num"):  # si el token es un número
            return ("F", "num")
        elif self._match("pari"):  # si encontramos (
            expr = self.E()        # analizamos lo que hay dentro de los paréntesis
            if not self._match("pard"):  # verificamos que después venga )
                raise Exception("Error: falta )")
            return ("F", expr)  # devolvemos lo que había dentro de los paréntesis
        else:
            # si el token no corresponde a nada esperado, error
            raise Exception(f"Error: token inesperado {self._peek()}")

    # Función auxiliar: revisa si el token actual es el esperado
    def _match(self, token):
        if self.index < len(self.tokens) and self.tokens[self.index] == token:
            self.index += 1  # avanzamos al siguiente token
            return True
        return False

    # Función auxiliar: devuelve el token actual sin avanzar
    def _peek(self):
        return self.tokens[self.index] if self.index < len(self.tokens) else None


# -------------------------------
# Función para imprimir árbol
# -------------------------------
def imprimir_arbol(nodo, nivel=0):
    if isinstance(nodo, tuple):  # si el nodo es una tupla (no terminal con hijos)
        etiqueta = nodo[0]       # la primera posición es la etiqueta del nodo
        print("  " * nivel + str(etiqueta))  # imprimimos con indentación
        for hijo in nodo[1:]:    # recorremos los hijos del nodo
            imprimir_arbol(hijo, nivel + 1)  # llamada recursiva para cada hijo
    else:
        # si el nodo no es tupla, es un valor simple (terminal)
        print("  " * nivel + str(nodo))


# -------------------------------
# Programa principal
# -------------------------------
def main():
    # Abrimos el archivo con la gramática
    with open("gra.txt", "r") as f:
        grammar = f.read().splitlines()
    print("Gramática cargada:")
    for g in grammar:
        print("  ", g)

    # Pedimos la cadena al usuario
    cadena = input("\nIngrese la cadena (ej: 2 + 3 * 4):\n> ")

    # Convertimos la cadena en tokens
    tokens = tokenizar(cadena)
    print("Tokens:", tokens)

    # Creamos el parser
    parser = Parser(grammar)

    try:
        # Intentamos generar el árbol
        arbol = parser.parse(tokens)
        print("\nÁrbol de sintaxis generado:\n")
        imprimir_arbol(arbol)  # imprimimos el árbol con indentación
    except Exception as e:
        # Si hubo algún problema, lo mostramos
        print("Error de análisis:", e)


# Este if hace que el main solo se ejecute
# si corremos el archivo directamente, no si lo importamos
if __name__ == "__main__":
    main()
