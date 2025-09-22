# -------------------------------
# Tokenizador simple
# -------------------------------
def tokenizar(cadena):
    tokens = []
    for ch in cadena.split():
        if ch.isdigit():
            tokens.append("num")
        elif ch == "+" or ch == "-":
            tokens.append("opsuma")
        elif ch == "*" or ch == "/":
            tokens.append("opmul")
        elif ch == "(":
            tokens.append("pari")
        elif ch == ")":
            tokens.append("pard")
        else:
            tokens.append("id")  # cualquier otro se asume como identificador
    return tokens


# -------------------------------
# Analizador sintáctico recursivo
# -------------------------------
class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tokens = []
        self.index = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.index = 0
        tree = self.E()
        if self.index < len(self.tokens):
            raise Exception("Error: tokens sobrantes en la entrada")
        return tree

    def E(self):
        left = self.T()
        while self._match("opsuma"):
            op = self.tokens[self.index - 1]
            right = self.T()
            left = ("E", op, left, right)
        return left

    def T(self):
        left = self.F()
        while self._match("opmul"):
            op = self.tokens[self.index - 1]
            right = self.F()
            left = ("T", op, left, right)
        return left

    def F(self):
        if self._match("id"):
            return ("F", "id")
        elif self._match("num"):
            return ("F", "num")
        elif self._match("pari"):
            expr = self.E()
            if not self._match("pard"):
                raise Exception("Error: falta )")
            return ("F", expr)
        else:
            raise Exception(f"Error: token inesperado {self._peek()}")

    def _match(self, token):
        if self.index < len(self.tokens) and self.tokens[self.index] == token:
            self.index += 1
            return True
        return False

    def _peek(self):
        return self.tokens[self.index] if self.index < len(self.tokens) else None


# -------------------------------
# Función para imprimir árbol
# -------------------------------
def imprimir_arbol(nodo, nivel=0):
    if isinstance(nodo, tuple):
        etiqueta = nodo[0]
        print("  " * nivel + str(etiqueta))
        for hijo in nodo[1:]:
            imprimir_arbol(hijo, nivel + 1)
    else:
        print("  " * nivel + str(nodo))


# -------------------------------
# Programa principal
# -------------------------------
def main():
    # Leer gramática
    with open("gra.txt", "r") as f:
        grammar = f.read().splitlines()
    print("Gramática cargada:")
    for g in grammar:
        print("  ", g)

    # Entrada del usuario
    cadena = input("\nIngrese la cadena (ej: 2 + 3 * 4):\n> ")

    tokens = tokenizar(cadena)
    print("Tokens:", tokens)

    parser = Parser(grammar)

    try:
        arbol = parser.parse(tokens)
        print("\nÁrbol de sintaxis generado:\n")
        imprimir_arbol(arbol)
    except Exception as e:
        print("Error de análisis:", e)


if __name__ == "__main__":
    main()
