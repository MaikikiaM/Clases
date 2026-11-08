# GUÍA MAESTRA DEFINITIVA DEL PROFESOR: LOGARITMOS, INDETERMINACIONES Y DERIVADAS
## Manual Pedagógico y Técnico Exhaustivo para Examen de Rescate

> **Destinatario:** Profesor / Tutor.  
> **Objetivo:** Guía completa, estructurada y profunda para preparar a una alumna con examen inminente que parte de un bloqueo mental absoluto ("no sé nada").  
> **Estructura del manual:** Cada tema se desarrolla con la misma profundidad pedagógica: intuición en español de la calle, formulación matemática estricta, propiedades y mnemotécnicas, errores que suspenden, tipología de examen resuelta paso a paso y guion verbal para la pizarra.

---

# MÓDULO 0: PSICOLOGÍA DOCENTE Y CRONOGRAMA DE EMERGENCIA

### 1. El diagnóstico de la alumna en pánico
Cuando un alumno dice *"el lunes tengo examen y no sé hacer nada"*, experimenta un colapso por **sobrecarga de símbolos**. Ve logaritmos, límites y derivadas como un laberinto inconexo de fórmulas.  
Tu misión pedagógica no es convertirla en matemática teórica en tres días, sino proporcionarle **algoritmos mecánicos de decisión**. Si sabe reconocer el patrón visual de cada ejercicio y aplicar una receta de 3 pasos, el pánico desaparece de inmediato.

### 2. Cronograma de rescate en 3 sesiones (Fin de semana)
- **Sesión 1 (Viernes / Hoy - 60 min): Logaritmos y Ecuaciones.**  
  *Meta:* Que calcule logaritmos mentalmente en 5 minutos, domine las 4 propiedades y resuelva ecuaciones descartando soluciones negativas.
- **Sesión 2 (Sábado - 75 min): Límites y las 7 Indeterminaciones.**  
  *Meta:* Sustituir siempre primero, dominar el factor $(x-a)$ en $\frac{0}{0}$, el conjugado en raíces, la regla de grados en $\frac{\infty}{\infty}$ y la fórmula del número $e$ en $1^\infty$.
- **Sesión 3 (Domingo - 90 min): Derivadas, Recta Tangente y Extremos.**  
  *Meta:* Dominar la regla de la cadena, resolver la recta tangente en 3 pasos y hacer el estudio de monotonía con la tabla de signos.

---

# TEMA 1: LOGARITMOS Y ECUACIONES EXPONENCIALES

## 1.1. Intuición Pedagógica y Planteamiento Inicial
No arranques la clase con teoría ni escribiendo símbolos raros. Siéntate con ella y abre este diálogo exacto:

> **Profesor:** *"Olvida los apuntes un momento. Respóndeme a esto: ¿cuánto es $2^3$?"*  
> **Alumna:** *"8."*  
> **Profesor:** *"Exacto. En una potencia te doy la base (2) y el exponente (3), y tú calculas el resultado (8). Un logaritmo es exactamente lo mismo pero formulado como una pregunta al revés: te doy la base (2) y el resultado (8), y te pregunto a qué número hay que elevar el 2 para llegar al 8."*

$$\mathbf{\log_2(8) = \,? \quad \longleftrightarrow \quad \text{¿A qué número tengo que elevar el } 2 \text{ para que me dé } 8?}$$

La respuesta es **3**, porque $2^3 = 8$. Por tanto: $\log_2(8) = 3$.

### Ejercicios relámpago de calentamiento (hazlos en la pizarra de viva voz):
- $\log_{10}(100) =$ *"¿A qué elevo 10 para dar 100?"* $\to \mathbf{2}$
- $\log_{10}(1000) =$ *"¿A qué elevo 10 para dar 1000?"* $\to \mathbf{3}$ *(Truco: cuenta los ceros)*
- $\log_3(9) = \mathbf{2}$  (porque $3^2 = 9$)
- $\log_5(25) = \mathbf{2}$ (porque $5^2 = 25$)
- $\log_2(16) = \mathbf{4}$ (porque $2^4 = 16$)

En menos de 5 minutos, la alumna ha resuelto 5 logaritmos de cabeza. Su cerebro asimila que el logaritmo no es un obstáculo insalvable y se abre a aprender.

---

## 1.2. Definición Formal, Notación y Restricciones de Dominio

### Definición y Paso a Forma Exponencial
$$\mathbf{\log_b(a) = c \iff b^c = a}$$

* **$b$ (Base):** El número que se eleva.
* **$a$ (Argumento):** El número de dentro (el resultado de la potencia).
* **$c$ (Logaritmo):** El exponente buscado.

Para despejar o calcular, pasamos a la forma exponencial equivalente: la base elevada al resultado debe ser igual al argumento ($b^c = a$).

### Notaciones que no deben confundirla:
- **Logaritmo decimal:** $\log(x) \equiv \log_{10}(x)$ (si no hay número en la base, es un 10).
- **Logaritmo neperiano o natural:** $\ln(x) \equiv \log_e(x)$ (la base es el número irracional $e \approx 2.71828...$). Se opera **exactamente igual** que cualquier otro logaritmo.

### Las dos líneas rojas de existencia (Pregunta típica de teoría o dominios):
1. **El argumento DEBE ser estrictamente positivo:**  
   $$\text{Para } \log_b(a), \quad \mathbf{a > 0}$$
   - $\log(-5) \to$ **NO EXISTE** en $\mathbb{R}$ (ninguna potencia de base positiva puede dar un resultado negativo).
   - $\log(0) \to$ **NO EXISTE** (tiende a $-\infty$).
2. **La base debe ser positiva y distinta de 1:**  
   $$\mathbf{b > 0, \quad b \neq 1}$$

---

## 1.3. Las Propiedades de Oro y Mnemotécnicas

Explícale que los logaritmos "bajan un escalón" la dificultad de las operaciones matemáticas:
- Multiplicar dentro $\to$ se convierte en **sumar** fuera.
- Dividir dentro $\to$ se convierte en **restar** fuera.
- Elevar a potencia dentro $\to$ se convierte en **multiplicar** fuera.

| # | Propiedad | Traducción Mnemotécnica | Ejemplo Práctico |
|---|---|---|---|
| **1** | $\log_b(1) = 0$ | "¿A qué elevo algo para que dé 1? Al cero." ($b^0 = 1$) | $\log_8(1) = 0, \quad \ln(1) = 0$ |
| **2** | $\log_b(b) = 1$ | "¿A qué elevo $b$ para que dé $b$? Al uno." ($b^1 = b$) | $\log_{10}(10) = 1, \quad \ln(e) = 1$ |
| **3** | $\log_b(A \cdot B) = \log_b A + \log_b B$ | **"El producto dentro es suma fuera"** | $\log(2 \cdot 5) = \log 2 + \log 5$ |
| **4** | $\log_b(A / B) = \log_b A - \log_b B$ | **"La división dentro es resta fuera"** | $\log(x / 7) = \log x - \log 7$ |
| **5** | $\log_b(A^n) = n \cdot \log_b A$ | El exponente pasa multiplicando delante | $\log(x^5) = 5\log x$ |
| **5b**| $\log_b(\sqrt[n]{A}) = \frac{1}{n}\log_b A$ | Las raíces son potencias fraccionarias ($A^{1/n}$) | $\log(\sqrt{x}) = \frac{1}{2}\log x$ |
| **5c**| $\log_{b^k}(A) = \frac{1}{k}\log_b A$ | **Potencia en la base**: sale fuera dividiendo | $\log_{36}(6) = \log_{6^2}(6) = \frac{1}{2}\log_6(6) = \frac{1}{2}$ |
| **6** | $\log_b A = \frac{\ln A}{\ln b} = \frac{\log A}{\log b}$ | **Cambio de base**: logaritmo de arriba entre logaritmo de la base | $\log_3(5) = \frac{\ln 5}{\ln 3} \approx 1.465$ |

---

## 1.4. Errores Habituales de Examen que Deben Evitarse
Márcalos con un recuadro rojo en su cuaderno:
1. ❌ **$\log(A + B) \neq \log A + \log B$** $\implies$ **¡FALSO!** El logaritmo de una suma **no se separa jamás**. Se queda exactamente como $\log(A + B)$.
2. ❌ **$\frac{\log A}{\log B} \neq \log A - \log B$** $\implies$ **¡FALSO!** No confundir la división de dos logaritmos distintos con el logaritmo de una fracción.
3. ❌ **$(\log A)^2 \neq 2\log A$** $\implies$ **¡FALSO!** El exponente pasa multiplicando solo si está **dentro del argumento** ($\log(A^2)$), pero no si eleva a todo el logaritmo.

---

## 1.5. Números Compuestos: El Caso del 36 y Varias Bases
En los exámenes suele caer este ejercicio para comprobar si entienden la descomposición factorial:
> *"Sabiendo que $\log 2 = a$ y $\log 3 = b$, calcula en función de $a$ y $b$: $\log(36)$, $\log(180)$ y $\log(0.36)$."*

### Resolución sistemática:
1. **Descomposición factorial:** $36 = 6^2 = 2^2 \cdot 3^2$.
2. **Aplicar producto a suma y bajar exponentes:**  
   $$\log(36) = \log(2^2 \cdot 3^2) = \log(2^2) + \log(3^2) = 2\log(2) + 2\log(3) = \mathbf{2a + 2b}$$
3. **Descomposición del número 5 mediante $\frac{10}{2}$:**  
   Si piden $\log(180) = \log(36 \cdot 5)$, no conocemos $\log(5)$, pero como $5 = \frac{10}{2}$:  
   $$\log(5) = \log\left(\frac{10}{2}\right) = \log(10) - \log(2) = \mathbf{1 - a}$$  
   Por tanto: $\log(180) = \log(36) + \log(5) = (2a + 2b) + (1 - a) = \mathbf{1 + a + 2b}$.
4. **Con números decimales:**  
   $$\log(0.36) = \log\left(\frac{36}{100}\right) = \log(36) - \log(100) = (2a + 2b) - 2 = \mathbf{2a + 2b - 2}$$

---

## 1.6. Ecuaciones Exponenciales Avanzadas (Con Varias Bases y Exponentes Potenciados)

### Caso 1: Ecuaciones con bases distintas y exponentes desfasados ($x+n$, $x-m$)
$$\mathbf{2^{x+2} \cdot 3^{x-1} = 48}$$
* **Paso 1 (Desglosar potencias para aislar $2^x$ y $3^x$):**  
  Usamos $a^{x+n} = a^x \cdot a^n$ y $a^{x-n} = \frac{a^x}{a^n}$:  
  $$2^x \cdot 2^2 \cdot \frac{3^x}{3^1} = 48 \implies 4 \cdot 2^x \cdot \frac{3^x}{3} = 48$$
* **Paso 2 (Extraer constantes y agrupar bases):**  
  $$\frac{4}{3} \cdot (2^x \cdot 3^x) = 48 \implies \frac{4}{3} \cdot (2 \cdot 3)^x = 48 \implies \frac{4}{3} \cdot 6^x = 48$$
* **Paso 3 (Despejar el bloque con la incógnita):**  
  $$6^x = \frac{48 \cdot 3}{4} = 12 \cdot 3 = 36$$
* **Paso 4 (Igualar exponentes):**  
  $$6^x = 6^2 \implies \mathbf{x = 2}$$

---

### Caso 2: Exponentes Potenciados / Cuadráticos ($x^2$)
$$\mathbf{2^{x^2 + 1} \cdot 3^{x^2 - 1} = 24}$$
* **Paso 1 (Desglosar constantes):**  
  $$2^{x^2} \cdot 2^1 \cdot \frac{3^{x^2}}{3^1} = 24 \implies \frac{2}{3} \cdot (2^{x^2} \cdot 3^{x^2}) = 24 \implies \frac{2}{3} \cdot 6^{x^2} = 24$$
* **Paso 2 (Despejar el bloque $6^{x^2}$):**  
  $$6^{x^2} = \frac{24 \cdot 3}{2} = 36 = 6^2 \implies \mathbf{x^2 = 2}$$
* **Paso 3 (Resolver con doble signo):**  
  $$\mathbf{x = \pm\sqrt{2}}$$

---

### Caso 3: Torre de Exponentes vs Potencia de Potencia
- **Potencia de potencia:** $(2^3)^2 = 2^{3 \cdot 2} = 2^6 = \mathbf{64}$.
- **Torre de potencias:** $2^{3^2} = 2^9 = \mathbf{512}$ *(se opera de arriba a abajo)*.
- **Ecuación en torre:**  
  $$2^{3^{x-1}} = 512 \implies 2^{3^{x-1}} = 2^9 \implies 3^{x-1} = 9 = 3^2 \implies x - 1 = 2 \implies \mathbf{x = 3}$$

---

### Caso 4: Método Universal con Logaritmos (Bases totalmente incompatibles)
$$\mathbf{2^{x+1} = 3^{2x-1}}$$
1. Aplicamos logaritmo neperiano ($\ln$) a ambos lados: $\ln(2^{x+1}) = \ln(3^{2x-1})$.
2. Pasamos los exponentes multiplicando: $(x + 1)\ln(2) = (2x - 1)\ln(3)$.
3. Distributiva: $x\ln(2) + \ln(2) = 2x\ln(3) - \ln(3)$.
4. Agrupar $x$: $\ln(2) + \ln(3) = 2x\ln(3) - x\ln(2) \implies \ln(6) = x(2\ln 3 - \ln 2) = x\ln(9/2)$.
5. Despejar: $\mathbf{x = \frac{\ln(6)}{\ln(4.5)}} \approx \mathbf{1.191}$.

---

## 1.7. Algoritmo para Ecuaciones Logarítmicas
**Ejemplo de examen:** $\log(x + 3) + \log(x - 1) = \log(5)$
1. **Comprimir:** Convierte sumas en productos y restas en cocientes: $\log\big((x + 3)(x - 1)\big) = \log(5)$.
2. **Igualar argumentos:** $(x + 3)(x - 1) = 5 \implies x^2 + 2x - 3 = 5 \implies x^2 + 2x - 8 = 0$.
3. **Resolver ecuación de 2º grado:** $x = \frac{-2 \pm 6}{2} \implies x_1 = 2, \quad x_2 = -4$.
4. **COMPROBACIÓN OBLIGATORIA (Riesgo de penalización de examen):**  
   - Con $x = 2$: $\log(2+3)=\log 5 > 0$ y $\log(2-1)=\log 1 > 0 \implies \mathbf{x = 2 \text{ es VÁLIDA}}$.
   - Con $x = -4$: $\log(-4+3)=\log(-1) \to$ **¡No existe logaritmo de número negativo!** $\implies \mathbf{x = -4 \text{ se DESCARTA}}$.

---

# TEMA 2: LÍMITES E INDETERMINACIONES

## 2.1. Intuición Pedagógica y Concepto de Límite
Explícaselo a la alumna con la idea de aproximación continua:
> *"Un límite no te pregunta qué pasa cuando estás exactamente en el punto, sino **hacia qué valor se aproxima la función cuando la variable se acerca infinitamente a ese valor sin llegar a tocarlo**."*

$$\lim_{x \to a} f(x) = L$$
Significa: "A medida que la $x$ se aproxima al número $a$, el valor de la función $f(x)$ se aproxima al número $L$."

---

## 2.2. El Primer Mandamiento: ¡SUSTITUIR PRIMERO SIEMPRE!
El 30% de los errores en exámenes ocurren porque los alumnos ven una fracción y asumen automáticamente que es una indeterminación rara.  
**Regla:** Antes de aplicar cualquier método, sustituye la $x$ por el valor al que tiende:

### Casos Directos que NO son indeterminación:
- $\frac{0}{k} = \mathbf{0} \quad (k \neq 0)$ (cero caramelos entre 5 personas son 0 caramelos).
- $\frac{k}{\infty} = \mathbf{0}$ (5 caramelos entre toda la población del planeta toca a 0).
- $\frac{\infty}{k} = \mathbf{\pm\infty}$
- $\infty + \infty = \mathbf{+\infty}$
- $k \cdot \infty = \mathbf{\pm\infty}$
- $\frac{k}{0} = \mathbf{\pm\infty} \quad (k \neq 0)$ $\implies$ **NO es indeterminación**, es una **asíntota vertical**. Si es un punto finito, se calculan los límites laterales ($x \to a^+$ y $x \to a^-$) para determinar el signo $(+\infty$ o $-\infty$).

---

## 2.3. Las 7 Indeterminaciones Matemáticas Resueltas Paso a Paso

Las 7 formas indeterminadas son:
$$\left[\frac{0}{0}\right], \quad \left[\frac{\infty}{\infty}\right], \quad [\infty - \infty], \quad [0 \cdot \infty], \quad \left[1^\infty\right], \quad [0^0], \quad [\infty^0]$$

---

### INDETERMINACIÓN 1: $\left[\frac{0}{0}\right]$ en Polinomios ($x \to a$)
* **Por qué ocurre:** Si al sustituir $x = a$ el numerador y el denominador dan 0, significa por el Teorema del Factor que **ambos polinomios tienen como factor común a $(x - a)$**.
* **La Receta:**  
  1. Factorizar numerador y denominador (por Ruffini, factor común o identidades notables $A^2 - B^2 = (A-B)(A+B)$).
  2. Cancelar el factor culpable $(x - a)$ que provocaba el cero arriba y abajo.
  3. Volver a sustituir la $x$.

* **Ejercicio de Examen Resuelto:**  
  $$\lim_{x \to 2} \frac{x^2 - 5x + 6}{x^2 - 4}$$
  - Sustituimos $x = 2$: $\frac{2^2 - 5(2) + 6}{2^2 - 4} = \frac{4 - 10 + 6}{4 - 4} = \left[\frac{0}{0}\right]$.
  - Factorizamos:
    - Numerador: $x^2 - 5x + 6 = (x - 2)(x - 3)$.
    - Denominador (diferencia de cuadrados): $x^2 - 4 = (x - 2)(x + 2)$.
  - Cancelamos $(x - 2)$:  
    $$\lim_{x \to 2} \frac{(x - 2)(x - 3)}{(x - 2)(x + 2)} = \lim_{x \to 2} \frac{x - 3}{x + 2}$$
  - Volvemos a sustituir: $\frac{2 - 3}{2 + 2} = \mathbf{-\frac{1}{4}}$.

---

### INDETERMINACIÓN 2: $\left[\frac{0}{0}\right]$ con Raíces Cuadradas ($x \to a$)
* **Por qué ocurre:** La raíz impide ver el factor $(x - a)$ de forma evidente.
* **La Receta (La técnica del conjugado):**  
  Multiplica y divide toda la fracción por el binomio conjugado (cambiando el signo del medio) para utilizar la identidad notable:  
  $$(A - B)(A + B) = A^2 - B^2$$
  Al elevar al cuadrado, la raíz cuadrada se rompe y el factor $(x - a)$ emerge para ser cancelado.

* **Ejercicio de Examen Resuelto:**  
  $$\lim_{x \to 0} \frac{\sqrt{x + 9} - 3}{x}$$
  - Sustituimos $x = 0$: $\frac{\sqrt{9}-3}{0} = \frac{3-3}{0} = \left[\frac{0}{0}\right]$.
  - El conjugado de $(\sqrt{x+9} - 3)$ es $(\sqrt{x+9} + 3)$. Multiplicamos arriba y abajo:  
    $$\lim_{x \to 0} \frac{(\sqrt{x + 9} - 3)(\sqrt{x + 9} + 3)}{x(\sqrt{x + 9} + 3)}$$
  - En el numerador aplicamos $(A-B)(A+B) = A^2 - B^2$:  
    $$(\sqrt{x + 9})^2 - 3^2 = (x + 9) - 9 = x$$
  - Cancelamos la $x$ del numerador con la del denominador:  
    $$\lim_{x \to 0} \frac{x}{x(\sqrt{x + 9} + 3)} = \lim_{x \to 0} \frac{1}{\sqrt{x + 9} + 3}$$
  - Volvemos a sustituir $x = 0$:  
    $$\frac{1}{\sqrt{0 + 9} + 3} = \frac{1}{3 + 3} = \mathbf{\frac{1}{6}}$$

---

### INDETERMINACIÓN 3: $\left[\frac{\infty}{\infty}\right]$ en Polinomios y Raíces ($x \to \pm\infty$)
* **Intuición:** Cuando $x$ tiende a infinito, los términos de menor grado (como $+3x$ o $-5$) son polvo insignificante comparados con la potencia más alta.
* **La Regla de Oro de los Grados:**  
  Sean $P(x)$ de grado $n$ con coeficiente líder $a_n$, y $Q(x)$ de grado $m$ con coeficiente líder $b_m$:
  $$\lim_{x \to \infty} \frac{P(x)}{Q(x)}$$
  1. Si $\mathbf{\text{grado}(P) > \text{grado}(Q)} \implies \mathbf{\pm\infty}$ *(mira la regla de signos de los coeficientes principales)*.
  2. Si $\mathbf{\text{grado}(P) < \text{grado}(Q)} \implies \mathbf{0}$ *(el denominador crece infinitamente más rápido)*.
  3. Si $\mathbf{\text{grado}(P) = \text{grado}(Q)} \implies \mathbf{\frac{a_n}{b_m}}$ *(se dividen directamente los coeficientes principales)*.

* **Ejemplos instantáneos de examen:**
  - $\lim_{x \to \infty} \frac{5x^3 - 2x + 1}{2x^3 + 7x^2} = \mathbf{\frac{5}{2}}$ (mismo grado, 3 = 3).
  - $\lim_{x \to \infty} \frac{4x^2 + 1}{x^3 - 5} = \mathbf{0}$ (grado 2 < grado 3).
  - $\lim_{x \to \infty} \frac{x^4 - 2}{3x^2 + 1} = \mathbf{+\infty}$ (grado 4 > grado 2).
  - Con raíces: $\lim_{x \to \infty} \frac{\sqrt{4x^2 + 5x}}{3x - 1} = \frac{\sqrt{4}x}{3x} = \mathbf{\frac{2}{3}}$ *(el grado de $\sqrt{x^2}$ es 1)*.

---

### INDETERMINACIÓN 4: Jerarquía de Infinitos
Si mezclan funciones exponenciales, polinómicas y logarítmicas cuando $x \to \infty$, no operes a lo loco. Aplica la escala de fuerza de infinitos:

$$\mathbf{\text{Exponencial } (a^x) \gg \text{Potencia } (x^n) \gg \text{Raíz } (\sqrt[k]{x}) \gg \text{Logaritmo } (\ln x)}$$

- $\lim_{x \to \infty} \frac{\ln(x)}{x^{100}} = \mathbf{0}$ *(la potencia aplasta al logaritmo)*.
- $\lim_{x \to \infty} \frac{x^{500}}{2^x} = \mathbf{0}$ *(la exponencial aplasta a la potencia)*.
- $\lim_{x \to \infty} \frac{3^x}{\ln(x)} = \mathbf{+\infty}$.

---

### INDETERMINACIÓN 5: $[\infty - \infty]$
Aparece principalmente en dos formatos:

#### Tipo A: Resta de fracciones algebraicas
*Receta:* Haz el mínimo común múltiplo para unirlo todo en una sola fracción. Pasará automáticamente a $\left[\frac{0}{0}\right]$ o $\left[\frac{\infty}{\infty}\right]$.

#### Tipo B: Resta con raíces cuando $x \to +\infty$
*Receta:* Multiplica y divide por el conjugado.
* **Ejercicio de Examen Resuelto:**  
  $$\lim_{x \to \infty} \left(\sqrt{x^2 + 4x} - x\right) = [\infty - \infty]$$
  - Multiplicamos y dividimos por el conjugado $(\sqrt{x^2 + 4x} + x)$:  
    $$\lim_{x \to \infty} \frac{(\sqrt{x^2 + 4x} - x)(\sqrt{x^2 + 4x} + x)}{\sqrt{x^2 + 4x} + x} = \lim_{x \to \infty} \frac{(x^2 + 4x) - x^2}{\sqrt{x^2 + 4x} + x} = \lim_{x \to \infty} \frac{4x}{\sqrt{x^2 + 4x} + x}$$
  - Dividimos entre los términos dominantes de grado 1:  
    $$\lim_{x \to \infty} \frac{4x}{x + x} = \lim_{x \to \infty} \frac{4x}{2x} = \mathbf{2}$$

---

### INDETERMINACIÓN 6: $[0 \cdot \infty]$
*Receta:* Transforma el producto en una fracción bajando uno de los dos términos a su inverso:
$$f(x) \cdot g(x) = \frac{f(x)}{\frac{1}{g(x)}} \implies \text{Pasa a } \left[\frac{0}{0}\right] \text{ o } \left[\frac{\infty}{\infty}\right]$$
A partir de ahí, se aplica L'Hôpital o simplificación algebraica.

---

### INDETERMINACIÓN 7: $\left[1^\infty\right]$ (La Fórmula Directa del Número $e$)
Aparece cuando la base tiende a 1 y el exponente tiende a $\infty$.  
> ⚠️ *Advertencia:* $1^\infty$ **NO es 1**, porque la base no es 1 exacto, sino un número que se acerca a 1 mientras la potencia se dispara a infinito.

> 💡 **La Fórmula Mágica de Examen:**  
> Si $\lim_{x \to a} f(x) = 1$ y $\lim_{x \to a} g(x) = \infty$:
> $$\mathbf{\lim_{x \to a} [f(x)]^{g(x)} = e^{\lim_{x \to a} g(x) \cdot [f(x) - 1]}}$$

* **Ejercicio de Examen Resuelto Paso a Paso:**  
  $$\lim_{x \to \infty} \left(\frac{2x + 5}{2x - 1}\right)^{3x}$$
  - Verificamos la indeterminación: Base $\frac{2x}{2x} = 1$, exponente $3(\infty) = \infty \implies \left[1^\infty\right]$.
  - Calculamos el límite del exponente de $e$:  
    $$\lim_{x \to \infty} 3x \cdot \left(\frac{2x + 5}{2x - 1} - 1\right)$$
  - Hacemos la resta dentro del paréntesis con común denominador:  
    $$\frac{2x + 5 - (2x - 1)}{2x - 1} = \frac{2x + 5 - 2x + 1}{2x - 1} = \frac{6}{2x - 1}$$
  - Multiplicamos por $3x$:  
    $$\lim_{x \to \infty} 3x \cdot \left(\frac{6}{2x - 1}\right) = \lim_{x \to \infty} \frac{18x}{2x - 1}$$
  - Grados iguales (1 y 1) $\implies \frac{18}{2} = 9$.
  - Resultado final: $\mathbf{e^9}$.

---

### 2.4. La Regla de L'Hôpital (El atajo de Bachillerato)
Si la alumna ya ha visto derivadas y tiene indeterminaciones $\left[\frac{0}{0}\right]$ o $\left[\frac{\infty}{\infty}\right]$:
$$\mathbf{\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}}$$

> ⚠️ **Error mortal de examen en L'Hôpital:**  
> **NO se deriva como un cociente $\left(\frac{u}{v}\right)'$**. Se hace la derivada del de arriba por un lado y la derivada del de abajo por otro.

---

# TEMA 3: DERIVADAS Y APLICACIONES CLAVE

## 3.1. Intuición Pedagógica de la Derivada
Explícaselo con este paralelismo:
- **En la vida real:** La derivada es un **velocímetro**. No te dice los kilómetros que has recorrido en total, sino a qué velocidad exacta te estás moviendo en este milisegundo concreto.
- **En una gráfica:** La derivada en un punto $x = a$, que se escribe $\mathbf{f'(a)}$, representa la **pendiente de la recta tangente** a la curva en ese punto:
  - Si $f'(a) > 0 \implies$ la curva está subiendo (función **creciente**).
  - Si $f'(a) < 0 \implies$ la curva está cayendo (función **decreciente**).
  - Si $f'(a) = 0 \implies$ la recta tangente es totalmente horizontal (candidato a **máximo o mínimo**).

---

## 3.2. Tabla Maestra de Derivadas con la Regla de la Cadena

> 💡 **Regla de la Cadena (Derivación de Funciones Compuestas):**  
> Cuando dentro de la función haya una expresión $u(x)$ en lugar de una $x$ sola:  
> **Deriva la función exterior evaluada en $u$ y multiplica siempre al final por la derivada de lo de dentro ($u'$).**

| Tipo | Función Simple | Derivada Compuesta (Regla de la Cadena) | Regla Verbal para la Alumna |
|---|---|---|---|
| **Constante** | $f(x) = k \implies f' = 0$ | - | Un número suelto no cambia $\to$ pendiente 0 |
| **Identidad** | $f(x) = x \implies f' = 1$ | - | Pendiente de la recta $y=x$ es 1 |
| **Potencia** | $x^n \implies n x^{n-1}$ | $\mathbf{[u^n]' = n \cdot u^{n-1} \cdot u'}$ | El exponente baja y se resta 1, por $u'$ |
| **Raíz Cuadrada**| $\sqrt{x} \implies \frac{1}{2\sqrt{x}}$ | $\mathbf{[\sqrt{u}]' = \frac{u'}{2\sqrt{u}}}$ | **Derivada de dentro partido de 2 por la raíz** |
| **Exponencial $e$**| $e^x \implies e^x$ | $\mathbf{[e^u]' = e^u \cdot u'}$ | Se queda exactamente igual por $u'$ |
| **Exponencial $a$**| $a^x \implies a^x \ln a$ | $\mathbf{[a^u]' = a^u \ln a \cdot u'}$ | La misma por el logaritmo de la base por $u'$ |
| **Logaritmo $\ln$**| $\ln(x) \implies \frac{1}{x}$ | $\mathbf{[\ln(u)]' = \frac{u'}{u}}$ | **"Derivada de lo de dentro entre lo de dentro sin derivar"** |
| **Logaritmo $\log_a$**| $\log_a(x) \implies \frac{1}{x \ln a}$| $\mathbf{[\log_a(u)]' = \frac{u'}{u \cdot \ln a}}$ | Como el neperiano con $\ln a$ en el denominador |
| **Seno** | $\sin x \implies \cos x$ | $\mathbf{[\sin u]' = \cos(u) \cdot u'}$ | Seno pasa a coseno por $u'$ |
| **Coseno** | $\cos x \implies -\sin x$| $\mathbf{[\cos u]' = -\sin(u) \cdot u'}$ | Coseno pasa a **menos** seno por $u'$ |
| **Tangente** | $\tan x \implies 1 + \tan^2 x$| $\mathbf{[\tan u]' = (1 + \tan^2 u) \cdot u' = \frac{u'}{\cos^2 u}}$ | Secante al cuadrado por $u'$ |

---

## 3.3. Álgebra de Derivadas (Operaciones)

### 1. Derivada de un Producto
$$\mathbf{(u \cdot v)' = u' \cdot v + u \cdot v'}$$
*Mnemotécnica:* **"Derivada del primero por el segundo sin derivar, MÁS el primero sin derivar por la derivada del segundo."**

*Ejemplo:* Deriva $f(x) = x^3 \cdot \ln(x)$
- $u = x^3 \implies u' = 3x^2$
- $v = \ln x \implies v' = \frac{1}{x}$
- $f'(x) = (3x^2) \cdot \ln(x) + (x^3) \cdot \left(\frac{1}{x}\right) = \mathbf{3x^2 \ln(x) + x^2} = x^2(3\ln x + 1)$.

### 2. Derivada de un Cociente
$$\mathbf{\left(\frac{u}{v}\right)' = \frac{u' \cdot v - u \cdot v'}{v^2}}$$
*Mnemotécnica:* **"Derivada del de arriba por el de abajo sin derivar, MENOS el de arriba por derivada del de abajo, todo partido por el de abajo al cuadrado."**

*Ejemplo:* Deriva $f(x) = \frac{e^x}{x^2 + 1}$
- $u = e^x \implies u' = e^x$
- $v = x^2 + 1 \implies v' = 2x$
- $f'(x) = \frac{e^x(x^2 + 1) - e^x(2x)}{(x^2 + 1)^2} = \mathbf{\frac{e^x(x^2 - 2x + 1)}{(x^2 + 1)^2}} = \frac{e^x(x - 1)^2}{(x^2 + 1)^2}$.

---

## 3.4. Las Dos Aplicaciones de Examen (Valen el 50% de la nota)

---

### APLICACIÓN 1: Ecuación de la Recta Tangente en $x = a$
> **La Fórmula Fundamental:**  
> $$\mathbf{y - f(a) = f'(a) \cdot (x - a)}$$

#### El Algoritmo en 3 Pasos:
* **Paso 1 (Hallar la coordenada $y$):** Sustituye $x = a$ en la función original $f(x)$ para obtener $y_0 = f(a)$. El punto de tangencia es $P(a, f(a))$.
* **Paso 2 (Hallar la pendiente $m$):** Calcula la derivada $f'(x)$ y sustituye $x = a$ para obtener la pendiente: $m = f'(a)$.
* **Paso 3 (Montar la ecuación):** Escribe $y - y_0 = m(x - a)$ y despeja la $y$.

#### Ejercicio de Examen Resuelto:
Halla la recta tangente a la curva $f(x) = x^3 - 3x + 2$ en el punto de abscisa $x = 2$.
1. **Punto:** $f(2) = 2^3 - 3(2) + 2 = 8 - 6 + 2 = 4 \implies P(2, 4)$.
2. **Pendiente:**  
   $f'(x) = 3x^2 - 3$  
   $m = f'(2) = 3(2^2) - 3 = 3(4) - 3 = 12 - 3 = 9$.
3. **Ecuación:**  
   $y - 4 = 9(x - 2) \implies y - 4 = 9x - 18 \implies \mathbf{y = 9x - 14}$.

*(Nota: Si piden la recta normal, es la perpendicular: su pendiente es $m_{\text{normal}} = -\frac{1}{f'(a)} = -\frac{1}{9}$).*

---

### APLICACIÓN 2: Monotonía (Crecimiento/Decrecimiento) y Extremos Relativos (Máximos y Mínimos)

#### El Algoritmo en 4 Pasos:
1. **Paso 1: Dominio de la función.** Identifica si hay puntos donde la función no existe (ej. denominadores iguales a cero).
2. **Paso 2: Puntos Críticos.** Deriva la función e iguala a cero:  
   $$\mathbf{f'(x) = 0}$$  
   Las soluciones son los puntos candidatos donde la tangente es horizontal.
3. **Paso 3: Tabla de Signos en la Recta Real.**  
   Coloca en la recta numérica los puntos críticos y los puntos fuera del dominio. Quedará dividida en intervalos. Toma un valor de prueba en cada intervalo y evalúalo en la derivada $f'(x)$:
   - Si $f'(x) > 0 \implies$ Función **Creciente** ($\nearrow$).
   - Si $f'(x) < 0 \implies$ Función **Decreciente** ($\searrow$).
4. **Paso 4: Conclusión de Extremos y Coordenadas.**
   - Si la función pasa de subir a bajar ($\nearrow \searrow$) $\implies$ **Máximo Relativo**.
   - Si la función pasa de bajar a subir ($\searrow \nearrow$) $\implies$ **Mínimo Relativo**.
   - **¡Cuidado!** Para dar las coordenadas del punto $(x, y)$, la $y$ se calcula sustituyendo en la función original $f(x)$, **nunca** en la derivada.

#### Ejercicio de Examen Resuelto:
Determina los intervalos de crecimiento y decrecimiento y los extremos relativos de $f(x) = x^3 - 3x^2 - 9x + 5$.
1. **Dominio:** $\mathbb{R}$ (polinomio).
2. **Derivada e igualación a cero:**  
   $$f'(x) = 3x^2 - 6x - 9$$  
   $$3x^2 - 6x - 9 = 0 \implies x^2 - 2x - 3 = 0 \implies (x - 3)(x + 1) = 0$$  
   Puntos críticos: $\mathbf{x = -1}$ y $\mathbf{x = 3}$.
3. **Intervalos de signo en $f'(x)$:**  
   Los intervalos son $(-\infty, -1)$, $(-1, 3)$ y $(3, +\infty)$.
   - En $x = -2$: $f'(-2) = 3(-2)^2 - 6(-2) - 9 = 12 + 12 - 9 = 15 > 0 \implies$ **Creciente ($\nearrow$)**.
   - En $x = 0$: $f'(0) = -9 < 0 \implies$ **Decreciente ($\searrow$)**.
   - En $x = 4$: $f'(4) = 3(16) - 24 - 9 = 48 - 33 = 15 > 0 \implies$ **Creciente ($\nearrow$)**.
4. **Conclusión:**
   - **Creciente en:** $(-\infty, -1) \cup (3, +\infty)$.
   - **Decreciente en:** $(-1, 3)$.
   - **Máximo relativo en $x = -1$:**  
     $y = f(-1) = (-1)^3 - 3(-1)^2 - 9(-1) + 5 = -1 - 3 + 9 + 5 = 10 \implies \mathbf{\text{Máximo en } (-1, 10)}$.
   - **Mínimo relativo en $x = 3$:**  
     $y = f(3) = 3^3 - 3(3^2) - 9(3) + 5 = 27 - 27 - 27 + 5 = -22 \implies \mathbf{\text{Mínimo en } (3, -22)}$.

---

# MÓDULO 4: SIMULACRO GENERAL DE EXAMEN (6 PROBLEMAS INTEGRADOS)

Plantéale este examen de prueba el domingo:

1. **(Logaritmos):** Resuelve la ecuación: $\log(2x - 1) + \log(x + 2) = 1$.
2. **(Exponenciales con varias bases):** Resuelve: $2^{x+2} \cdot 3^{x-1} = 48$.
3. **(Límites $\frac{0}{0}$ con raíz):** Calcula: $\lim_{x \to 4} \frac{\sqrt{x} - 2}{x^2 - 16}$.
4. **(Límites $1^\infty$ con número $e$):** Calcula: $\lim_{x \to \infty} \left(\frac{3x - 1}{3x + 2}\right)^{2x}$.
5. **(Derivada combinada):** Deriva y simplifica: $f(x) = \frac{\ln(x^2 + 1)}{e^{3x}}$.
6. **(Recta tangente y monotonía):** Dada $f(x) = x^2 - 4x + 3$:  
   a) Halla la ecuación de la recta tangente en $x = 3$.  
   b) Halla su vértice/mínimo relativo indicando crecimiento y decrecimiento.

### Soluciones del Simulacro para Corrección Rápida:
1. $\log((2x-1)(x+2)) = \log(10) \implies 2x^2 + 3x - 12 = 0 \implies x = \frac{-3+\sqrt{105}}{4} \approx 1.81$ (se descarta la raíz negativa).
2. $\frac{4}{3} \cdot 6^x = 48 \implies 6^x = 36 \implies \mathbf{x = 2}$.
3. Conjugado en numerador y diferencia de cuadrados abajo: $\lim_{x \to 4} \frac{x - 4}{(x-4)(x+4)(\sqrt{x}+2)} = \frac{1}{(8)(4)} = \mathbf{\frac{1}{32}}$.
4. Exponente del número $e$: $\lim 2x \cdot \left(\frac{3x-1-(3x+2)}{3x+2}\right) = \lim \frac{-6x}{3x+2} = -2 \implies \mathbf{e^{-2} = \frac{1}{e^2}}$.
5. Cociente y cadena: $f'(x) = \frac{\frac{2x}{x^2+1}e^{3x} - \ln(x^2+1)\cdot 3e^{3x}}{(e^{3x})^2} = \mathbf{\frac{\frac{2x}{x^2+1} - 3\ln(x^2+1)}{e^{3x}}}$.
6. a) $f(3) = 0$, $f'(x) = 2x - 4 \implies m = f'(3) = 2 \implies \mathbf{y = 2x - 6}$.  
   b) $f'(x) = 0 \implies x = 2$. Decrece en $(-\infty, 2)$, crece en $(2, +\infty)$. **Mínimo en $(2, -1)$**.
