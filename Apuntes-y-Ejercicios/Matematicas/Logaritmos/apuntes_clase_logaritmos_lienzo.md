# Hoja 1: Concepto de Logaritmo como Inversa de la Potencia y Comparación Gráfica

### 1.1 Comportamiento Gráfico: Potencia vs. Logaritmo
En la pizarra se introduce la relación funcional comparando el crecimiento de tres funciones clave:
* **Función identidad:** $y = x$ (bisectriz del primer cuadrante).
* **Función potencial / cuadrática:** $y = x^2$. Crece muy rápidamente a medida que aumenta $x$ (la curva se dispara hacia arriba).
* **Función logarítmica:** $y = \log_{10}(x)$. Es la función inversa de la exponencial; a medida que avanza en el eje $X$, su tasa de crecimiento disminuye progresivamente (crece de forma sumamente lenta).

### 1.2 La Potencia y su Inversa: El Logaritmo
Toda potencia relaciona una base, un exponente y un resultado:
$$b^a = c$$

* **Ejemplo base en clase:**
  $$2^3 = 8$$
  Donde **$2$** es la base, **$3$** es el exponente y **$8$** es el resultado de la potencia.

* **Traducción a Logaritmo:**
  El logaritmo invierte la pregunta: dados la base y el resultado, busca el exponente al que hay que elevar:
  $$\mathbf{\log_2(8) = 3}$$
  * Base: $2$ (número en subíndice inferior).
  * Argumento: $8$ (número dentro del logaritmo).
  * Resultado: $3$ (las veces que hay que multiplicar la base por sí misma para obtener el argumento).

### 1.3 Notación Neperiana y Decimal
* **Número de Euler ($e$):** Número irracional $e \approx 2.718...$
* **Logaritmo Neperiano / Natural:**
  $$\ln(x) \equiv \log_e(x)$$

### 1.4 Primeros Cálculos Mentales Directos
* **Cálculo con potencias de 10:**
  $$\log_{10}(1000) = x \iff 10^x = 1000$$
  Como $1000$ tiene 3 ceros ($10 \cdot 10 \cdot 10 = 1000$):
  $$\mathbf{x = 3}$$

* **Extensión a 10.000:**
  $$\log_{10}(10000) = \mathbf{4}$$

* **Cálculo con base 5:**
  $$\log_5(25) = x \iff 5^x = 25$$
  Dado que $5^1 = 5$ y $5^2 = 25$:
  $$\mathbf{x = 2}$$

<div class="page-break"></div>

# Hoja 2: Descomposición Factorial, Notación Formal y Logaritmos Directos

### 2.1 El Método de la Descomposición en Factores Primos
Para bases mayores a 2 (como base 4), se descompone el argumento sucesivamente en factores primos y se agrupan en potencias de la base buscada:

* **Ejemplo 1: $\log_4(16) = 2$**
  $$\begin{array}{r|l}
  16 & 2 \\
  8 & 2 \to 2 \cdot 2 = 4 \\
  4 & 2 \\
  2 & 2 \to 2 \cdot 2 = 4 \\
  1 &
  \end{array} \implies 16 = 4^2 \implies \mathbf{\log_4(16) = 2}$$

* **Ejemplo 2: $\log_4(64) = 3$**
  $$64 = 2^6 = (2^2)^3 = 4^3 \implies \text{Se obtienen 3 grupos de 4} \implies \mathbf{\log_4(64) = 3}$$

* **Caso no entero (números no potencias exactas):**
  $$\log_4(60) = \text{No da un número entero limpio; requiere calculadora o aproximación decimal.}$$

### 2.2 Relación Fundamental (Definición de Logaritmo)
$$\mathbf{\log_b(a) = c \iff b^c = a}$$

### 2.3 Batería de Ejercicios Resueltos Oralmente
* $\log_{10}(1000000) = \mathbf{6}$ (6 ceros $\to 10^6$).
* $\log_5(125) = \mathbf{3}$ ($5^3 = 125$).
* $\log_2(128) = \mathbf{7}$ ($2^7 = 128$).

### 2.4 Propiedad de Inversa Inmediata con la Base
* En base 10: $\log_{10}(x) = c \implies 10^c = x$.
* En base $e$ (neperiano):
  $$\ln(x) = c \iff \log_e(x) = c$$
  $$\mathbf{\ln(e^7) = 7}$$
  *(Elevar $e$ a la 7 en base $e$ devuelve directamente el exponente 7).*

<div class="page-break"></div>

# Hoja 3: Restricciones de Existencia y Dominio del Logaritmo

### 3.1 Prohibición 1: No Existen Logaritmos de Números Negativos
$$\mathbf{\log_{10}(-4) \to \nexists \quad (\text{No Existe})}$$

* **Demostración de imposibilidad:**
  Buscamos un valor $x$ tal que:
  $$10^x = -4$$
  - Si probamos exponentes negativos: $10^{-3} = \frac{1}{10^3} = \frac{1}{1000} = 0.001 \neq -4$ (los exponentes negativos generan fracciones positivas, nunca números negativos).
  - Si probamos $x = 0$: $10^0 = 1 > 0$.
  - Si probamos exponentes positivos: $10^7 = 10.000.000 > 0$.
* **Conclusión matemática:** Para cualquier base $b > 0$, la potencia $b^x > 0$ es estrictamente positiva para cualquier valor real de $x$. Por tanto:
  $$\mathbf{b^x \neq \text{número negativo}}$$

### 3.2 Prohibición 2: No Existe el Logaritmo de Cero
$$\mathbf{\log_2(0) \to \nexists \quad (\text{No Existe})}$$

* **Demostración de imposibilidad:**
  $$2^x = 0$$
  - $2^0 = 1 \neq 0$.
  - $1000^0 = 1 \neq 0$.
* No existe ningún exponente real que haga que una base positiva se anule. A medida que $x \to -\infty$, $2^x \to 0$, pero nunca llega a valer 0.

### 3.3 Dominio de la Función Logarítmica
De las dos restricciones anteriores se deduce formalmente el dominio:
$$\text{Para } f(x) = \log(x) \implies \mathbf{\text{Dom}(f) = (0, +\infty)}$$
* El intervalo es **abierto en 0** (con paréntesis) porque el 0 no está incluido.
* El infinito siempre lleva paréntesis.

### 3.4 Contexto en Ecuaciones
Se ilustra la transición desde una ecuación algebraica polinómica:
$$3x^2 + 4x + 5 = 0$$
hacia una ecuación con logaritmos integrados:
$$\log(x) + 3x^2 + 4x + 5 = 0$$
donde la condición de existencia previa exige que cualquier solución deba cumplir obligatoriamente $x > 0$.

<div class="page-break"></div>

# Hoja 4: Propiedades Operativas y la Advertencia de Potencias

### 4.1 Formulario de Propiedades Fundamentales
En la pizarra se formalizan las reglas operatorias para trabajar con logaritmos:

1. **Logaritmo de la unidad:**
   $$\mathbf{\log_b(1) = 0 \iff b^0 = 1}$$
2. **Logaritmo de la propia base:**
   $$\mathbf{\log_b(b) = 1 \iff b^1 = b}$$
3. **Logaritmo de un producto:**
   $$\mathbf{\log_b(A \cdot B) = \log_b(A) + \log_b(B)}$$
4. **Logaritmo de un cociente:**
   $$\mathbf{\log_b\left(\frac{A}{B}\right) = \log_b(A) - \log_b(B)}$$
5. **Logaritmo de una potencia:**
   $$\mathbf{\log_b(A^n) = n \cdot \log_b(A)}$$
   *(El exponente del argumento pasa multiplicando delante del logaritmo).*
6. **Logaritmo de una raíz:**
   $$\mathbf{\log_b(\sqrt[n]{A}) = \log_b(A^{1/n}) = \frac{1}{n} \cdot \log_b(A)}$$
7. **Fórmula del Cambio de Base:**
   $$\mathbf{\log_b(A) = \frac{\log_c(A)}{\log_c(b)} = \frac{\ln(A)}{\ln(b)}}$$

### 4.2 La Advertencia Crítica: Posición del Exponente
En clase se resalta el error más común en exámenes entre exponente del argumento y exponente de la función:
$$\mathbf{\log_b(A^n) \neq (\log_b A)^n}$$

* En $\log_b(A^n)$, el exponente $n$ afecta **únicamente al argumento $A$**, por lo que **sí** pasa multiplicando delante:
  $$\log_b(A^n) = n \cdot \log_b(A)$$
* En $(\log_b A)^n$, el exponente eleva a **todo el logaritmo**, por lo que **no** se puede pasar multiplicando delante:
  $$(\log_b A)^n \neq n \cdot \log_b A$$

<div class="page-break"></div>

# Hoja 5: Demostración Numérica de Errores y Exponentes Negativos

### 5.1 Desmontando Falsas Propiedades con Números
Se demuestra numéricamente por qué ciertas expresiones habituales son incorrectas:

* **Error 1: Resta de logaritmos vs. División de logaritmos**
  $$\mathbf{\frac{\log A}{\log B} \neq \log A - \log B}$$
  $$\mathbf{\log\left(\frac{A}{B}\right) \neq \frac{\log A}{\log B}}$$

* **Comprobación numérica realizada en la pizarra:**
  Tomando base 2 con los números $2$ y $4$:
  $$\log_2\left(\frac{2}{4}\right) = \log_2(2) - \log_2(4) = 1 - 2 = \mathbf{-1}$$
  Mientras que si se dividen los logaritmos:
  $$\frac{\log_2(2)}{\log_2(4)} = \frac{1}{2} = \mathbf{0.5}$$
  Dado que $-1 \neq 0.5$, queda demostrado que la división de logaritmos no equivale al logaritmo de una fracción.

### 5.2 Ejercicios con Exponentes Negativos y Fracciones
* **Ejercicio 1: Logaritmo de una fracción en base 2**
  $$\log_2\left(\frac{1}{16}\right)$$
  - Método 1 (por propiedad de cociente):
    $$\log_2(1) - \log_2(16) = 0 - 4 = \mathbf{-4}$$
  - Método 2 (por potencia negativa):
    $$\frac{1}{16} = \frac{1}{2^4} = 2^{-4} \implies \log_2(2^{-4}) = -4 \cdot \log_2(2) = \mathbf{-4}$$

* **Ejercicio 2: Logaritmo de una fracción en base 3**
  $$\log_3\left(\frac{1}{27}\right)$$
  - Como $27 = 3^3$, entonces $\frac{1}{27} = \frac{1}{3^3} = 3^{-3}$:
    $$\log_3\left(\frac{1}{27}\right) = \log_3(3^{-3}) = -3 \cdot \log_3(3) = -3 \cdot 1 = \mathbf{-3}$$

<div class="page-break"></div>

# Hoja 6: Raíces Fraccionarias y Ecuaciones con Bases Radicales

### 6.1 Logaritmo de una Raíz Fraccionaria
$$\mathbf{\log_3(\sqrt[5]{27})}$$
1. Se extrae la raíz como exponente fraccionario hacia fuera mediante la propiedad:
   $$\log_3(\sqrt[5]{27}) = \frac{1}{5} \log_3(27)$$
2. Se descompone el argumento en base 3 ($27 = 3^3$):
   $$\frac{1}{5} \log_3(3^3) = \frac{1}{5} \cdot 3 \cdot \log_3(3) = \frac{3}{5} \cdot 1 = \mathbf{\frac{3}{5}}$$

---

### 6.2 Ecuación con Base Radical: $\log_{\sqrt{2}}(8) = x$
Se plantea la ecuación para determinar a qué exponente $x$ hay que elevar la base $\sqrt{2}$ para obtener $8$:

* **Paso 1: Aplicar la definición de logaritmo:**
  $$(\sqrt{2})^x = 8$$
* **Paso 2: Transformar la raíz en potencia fraccionaria:**
  $$\sqrt{2} = 2^{1/2} \implies (2^{1/2})^x = 2^{x/2}$$
* **Paso 3: Expresar el segundo miembro en base 2:**
  $$8 = 2^3 \implies 2^{x/2} = 2^3$$
* **Paso 4 (Método por logaritmos):**
  Tomando $\log_2$ en ambos lados:
  $$\log_2(2^{x/2}) = \log_2(2^3) \implies \frac{x}{2} \cdot \log_2(2) = 3 \cdot \log_2(2)$$
  Como $\log_2(2) = 1$:
  $$\frac{x}{2} = 3 \implies \mathbf{x = 6}$$

---

### 6.3 Ecuación Análoga: $\log_{\sqrt{3}}(27) = x$
Se plantea el mismo procedimiento con base $\sqrt{3}$:
* **Paso 1:** $(\sqrt{3})^x = 27$
* **Paso 2:** $3^{x/2} = 27$
* **Paso 3:** Tomando logaritmos en base 3:
  $$\log_3(3^{x/2}) = \log_3(27)$$
  $$\frac{x}{2} \cdot \log_3(3) = \log_3(27)$$

*(Continúa en la Hoja 7).*

<div class="page-break"></div>

# Hoja 7: Conclusión del Ejercicio con Raíces y Cierre de Sesión

### 7.1 Resolución Final de $\log_{\sqrt{3}}(27)$
Continuando el desarrollo de la Hoja 6:
$$\frac{x}{2} \cdot \log_3(3) = \log_3(27)$$

1. Se descompone $27 = 3^3$:
   $$\frac{x}{2} \cdot \log_3(3) = \log_3(3^3) = 3 \cdot \log_3(3)$$
2. Como $\log_3(3) = 1$:
   $$\frac{x}{2} \cdot 1 = 3 \cdot 1$$
   $$\frac{x}{2} = 3 \implies \mathbf{x = 6}$$

* **Comprobación:**
  $$(\sqrt{3})^6 = (3^{1/2})^6 = 3^{6/2} = 3^3 = 27 \quad \checkmark$$

### 7.2 Repaso de Potencias Directas
* $7^2 = 49 \implies \log_7(49) = 2$.
* Recordatorio de $\log(A \cdot B) = \log A + \log B$.

### 7.3 Fórmula Final de Cambio de Base (Destacada)
Al cierre de la sesión, se enfatiza la fórmula del cambio de base como herramienta indispensable cuando la base no es amigable:

$$\mathbf{\log_b(A) = \frac{\log_c(A)}{\log_c(b)}}$$

* Permite calcular en cualquier calculadora estándar usando logaritmos decimales o neperianos:
  $$\log_7(50) = \frac{\ln(50)}{\ln(7)} \approx \frac{3.912}{1.946} \approx 2.01$$
