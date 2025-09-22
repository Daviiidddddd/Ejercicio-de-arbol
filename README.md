# Proyecto: Árbol de Sintaxis en Python
## David Castellanos

En este caso lo que se hizo fue crear un programa en **Python** que recibe una gramática (`gra.txt`) y una cadena de prueba, y luego nos imprime el árbol de sintaxis.  

La idea es que podamos escribir expresiones como `2 + 3 * 4` y ver cómo se arma el árbol según las reglas de la gramática.

---

## Archivos principales

- `gra.txt`: acá está la gramática que usamos.
- `arbol.py`: el programa en Python que lee la gramática, pide la cadena y arma el árbol.
- `README.md`: es el README.

---

## Cómo usarlo

1. Se pone y se guarda la gramática en un archivo `gra.txt`. En este caso se ve así:

   ```
   E -> E opsuma T | T
   T -> T opmul F | F
   F -> id | num | pari E pard
   ```

2. Luego se ejecuta el programa de Python:

   ```bash
   python arbol.py
   ```

3. Ahora podemos escribir expresiones normales, en este caso se usaron las del ejemplo del archivo pero igual podrian variar:

   ```
   2 + 3 * 4
   ( 2 + 3 ) * 4
   2 + 3 - 4
   ```

   El programa se encarga de transformar esos números y operadores en los tokens que entiende la gramática (`num`, `opsuma`, `opmul`, etc.).

---

## Ejemplos

Asi se ve una vez ya ejecutado

### Ejemplo 1
Expresión: `2 + 2 * 4`

![Ejemplo 1](foto%201%20arbol.png)

---

### Ejemplo 2
Expresión: `2 + 3 - 4`

![Ejemplo 2](foto%202%20arbol.png)

---

### Ejemplo 3
Expresión: `2 + 3 * ( 4 - 5 )`

![Ejemplo 3](foto%203%20arbol.png)

---

## Fin

---
