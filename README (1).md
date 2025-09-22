# Proyecto: Árbol de Sintaxis en Python

En este caso lo que hicimos fue crear un programa en **Python** que recibe una gramática (`gra.txt`) y una cadena de prueba, y luego nos imprime el árbol de sintaxis.  

La idea es que podamos escribir expresiones como `2 + 3 * 4` y ver cómo se arma el árbol según las reglas de la gramática.

---

## Archivos principales

- `gra.txt`: acá está la gramática que usamos.
- `arbol.py`: el programa en Python que lee la gramática, pide la cadena y arma el árbol.
- `README.md`: este archivo que estás leyendo.

---

## Cómo usarlo

1. Guardás la gramática en un archivo `gra.txt`. En este caso se ve así:

   ```
   E -> E opsuma T | T
   T -> T opmul F | F
   F -> id | num | pari E pard
   ```

2. Ejecutás el programa:

   ```bash
   python arbol.py
   ```

3. Ahora podés escribir expresiones normales, por ejemplo:

   ```
   2 + 3 * 4
   ( 2 + 3 ) * 4
   2 + 3 - 4
   ```

   El programa se encarga de transformar esos números y operadores en los tokens que entiende la gramática (`num`, `opsuma`, `opmul`, etc.).

---

## Ejemplos

Acá te dejo unas capturas de cómo se ve en consola:

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

## Cosas a tener en cuenta

- Acá los números se convierten en `num`, y los operadores en `opsuma`, `opmul`, etc.
- Si escribís algo raro que no está en la gramática, el programa te avisa con un error.
- Podés probar con distintas cadenas y ver cómo cambia la estructura del árbol.

---

## Próximos pasos

Si querés mejorar la visual, se podría armar el árbol con ramas ASCII (`├──`, `└──`) o incluso exportarlo a una imagen con librerías gráficas. Pero por ahora funciona todo con puro texto.
