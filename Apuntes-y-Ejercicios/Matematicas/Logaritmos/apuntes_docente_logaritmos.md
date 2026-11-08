# GUÍA MAESTRA DEL PROFESOR: LOGARITMOS (DESDE CERO A EXAMEN)
> **Módulo:** Matemáticas (Bachillerato / 4º ESO)  
> **Objetivo:** Preparación urgente de clase para alumna con examen inminente ("bloqueo total / no sé nada").  
> **Temas cubiertos:** Definición intuitiva y formal, Propiedades de oro, Errores letales, Ecuaciones Logarítmicas y Exponenciales, y Conexión con Indeterminaciones y Derivadas.

---

## 1. ESTRATEGIA PEDAGÓGICA Y PSICOLOGÍA DEL ALUMNO EN PÁNICO

Cuando una alumna dice *"el lunes tengo examen y literal que no sé hacer nada"*, su principal enemigo no son las matemáticas, sino la **ansiedad y la sobrecarga cognitiva**. Se siente abrumada por símbolos que no comprende ($\log, \ln, \lim, \frac{dy}{dx}$).

### Reglas de oro para tu clase de hoy:
1. **Prohibido empezar por fórmulas abstractas:** No abras la clase diciendo *"el logaritmo en base $b$ de $a$ es el exponente..."*. Empieza con un juego mental de potencias sencillas.
2. **Generar confianza en los primeros 5 minutos:** Consigue que en los primeros 5 minutos ella resuelva 4 logaritmos de cabeza. En cuanto vea que es capaz de calcular $\log_2(8) = 3$, el bloqueo inicial desaparece.
3. **Lenguaje claro antes del formalismo:** Toda expresión matemática debe relacionarse con operaciones numéricas simples.
4. **Dividir en bloques de 15 minutos:**
   - **00-10 min:** Intuición y cálculo mental directo.
   - **10-25 min:** Propiedades operativas (suma, resta y exponentes).
   - **25-45 min:** Ecuaciones logarítmicas (método sistemático y comprobación de soluciones).
   - **45-55 min:** Ecuaciones exponenciales usando logaritmos.
   - **55-60 min:** Consolidación: proponerle ejercicios que resuelva de forma autónoma para afianzar el aprendizaje.

---

## 2. LA PREGUNTA MÁGICA: QUÉ ES UN LOGARITMO (INTUICIÓN)

Explícaselo con este diálogo exacto:

> **Profesor:** *"Dime cuánto es $2^3$."*  
> **Alumna:** *"8."*  
> **Profesor:** *"Exacto. Las potencias te dan la base y el exponente, y tú buscas el resultado. Un logaritmo es EXACTAMENTE la misma operación, pero al revés: te da la base y el resultado, y te pregunta el exponente."*

$$\log_2(8) = \,? \quad \longleftrightarrow \quad \text{¿A qué número tengo que elevar el } 2 \text{ para que me dé } 8?$$

Respuesta inmediata: **al 3**, porque $2^3 = 8$. Luego $\log_2(8) = 3$.

### Ejercicios relámpago de calentamiento (hazlos en la pizarra de viva voz):
- $\log_{10}(100) =$ *"¿A qué elevo 10 para que dé 100?"* $\to \mathbf{2}$
- $\log_{10}(1000) =$ *"¿A qué elevo 10 para que dé 1000?"* $\to \mathbf{3}$ (Truco visual: cuenta los ceros).
- $\log_3(9) =$ *"¿A qué elevo 3 para dar 9?"* $\to \mathbf{2}$
- $\log_5(25) = \mathbf{2}$
- $\log_2(16) = \mathbf{4}$

---

## 3. DEFINICIÓN FORMAL Y CONDICIONES DE EXISTENCIA

### 3.1. Definición matemática
$$\log_b(a) = c \iff b^c = a$$

* **$b$ (Base):** Número que se eleva.
* **$a$ (Argumento):** Resultado de la potencia.
* **$c$ (Logaritmo):** El exponente buscado.

**Paso a forma exponencial:**  
Para pasar de logaritmo a potencia o despejar: la base elevada al resultado debe igualar al argumento ($b^c = a$).

### 3.2. Notaciones habituales (que no se líe con las letras)
- **Logaritmo decimal:** $\log(x) \equiv \log_{10}(x)$ (si no hay número abajo, la base es 10).
- **Logaritmo neperiano / natural:** $\ln(x) \equiv \log_e(x)$ (la base es el número $e \approx 2.71828...$). Se aplican **exactamente las mismas propiedades**.

### 3.3. Restricciones obligatorias (¡Pregunta típica de teoría o dominios!)
1. **El argumento debe ser ESTRICTAMENTE POSITIVO:**  
   $$\text{Para } \log_b(a), \quad a > 0$$
   - $\log_2(-4) \to$ **NO EXISTE** (ningún positivo elevado a algo da negativo).
   - $\log_2(0) \to$ **NO EXISTE** (ningún número elevado da 0; tiende a $-\infty$).
2. **La base debe ser positiva y distinta de 1:**  
   $$b > 0, \quad b \neq 1$$

---

## 4. LAS PROPIEDADES DE ORO (Y CÓMO RECORDARLAS)

Para que no las memorice como un robot, relacionalas con las propiedades de las potencias que ya conoce:

| # | Propiedad | Traducción / Mnemotécnica | Ejemplo práctico |
|---|---|---|---|
| **1** | $\log_b(1) = 0$ | "¿A qué elevo algo para que dé 1? Al cero." ($b^0 = 1$) | $\log_7(1) = 0, \quad \ln(1) = 0$ |
| **2** | $\log_b(b) = 1$ | "¿A qué elevo $b$ para que dé $b$? Al uno." ($b^1 = b$) | $\log_{10}(10) = 1, \quad \ln(e) = 1$ |
| **3** | $\log_b(A \cdot B) = \log_b A + \log_b B$ | **"El producto dentro es la suma fuera"** (multiplicar potencias suma exponentes). | $\log(2 \cdot 5) = \log 2 + \log 5$ |
| **4** | $\log_b\left(\frac{A}{B}\right) = \log_b A - \log_b B$ | **"La división dentro es la resta fuera"** (dividir potencias resta exponentes). | $\log\left(\frac{100}{x}\right) = \log 100 - \log x = 2 - \log x$ |
| **5** | $\log_b(A^n) = n \cdot \log_b A$ | **Logaritmo de una potencia**: el exponente baja multiplicando delante del logaritmo. | $\log_2(x^5) = 5\log_2(x)$ |
| **5b**| $\log_b(\sqrt[n]{A}) = \frac{1}{n}\log_b A$ | Las raíces son potencias fraccionarias: $\sqrt[n]{A} = A^{1/n}$. | $\log_3(\sqrt{x}) = \frac{1}{2}\log_3(x)$ |
| **6** | $\log_b A = \frac{\log_c A}{\log_c b}$ | **Cambio de base**: logaritmo de lo de arriba entre logaritmo de la base. | $\log_2(5) = \frac{\ln 5}{\ln 2} \approx 2.32$ |

---

## 5. ERRORES FRECUENTES QUE DEBEN EVITARSE EN EXAMEN

Márcalos en rojo en su libreta:
1. ❌ **$\log(A + B) = \log A + \log B$** $\implies$ **¡FALSO!** El logaritmo de una suma **NO se puede separar**. Se queda como $\log(A+B)$.
2. ❌ **$\frac{\log A}{\log B} = \log A - \log B$** $\implies$ **¡FALSO!** No confundir la resta de logaritmos con la división de dos logaritmos.
3. ❌ **$(\log A)^2 = 2 \log A$** $\implies$ **¡FALSO!** La propiedad de la potencia solo se aplica si el exponente afecta al **argumento interno** ($\log(A^2)$), no si eleva a la función logaritmo completa.

---

## 6. TIPOLOGÍA DE EJERCICIOS DE EXAMEN (RESUELTOS PASO A PASO)

### TIPO 1: Cálculo con potencias negativas y fraccionarias
*Son los primeros que ponen para pillar.*

* **Ejemplo 1A:** $\log_2\left(\frac{1}{16}\right)$  
  *Explicación:* "¿Cómo convierto un 16 del denominador en potencia de 2?". $16 = 2^4$, luego $\frac{1}{16} = 2^{-4}$.  
  $$\log_2(2^{-4}) = -4 \cdot \log_2(2) = -4 \cdot 1 = \mathbf{-4}$$
* **Ejemplo 1B:** $\log_3(\sqrt[5]{27})$  
  *Explicación:* Factorizar y pasar a potencia fraccionaria. $27 = 3^3$, luego $\sqrt[5]{27} = 3^{3/5}$.  
  $$\log_3(3^{3/5}) = \frac{3}{5} \log_3(3) = \mathbf{\frac{3}{5}}$$
* **Ejemplo 1C:** $\log_{\sqrt{2}}(8)$  
  *Explicación:* Plantea la definición: $(\sqrt{2})^x = 8 \implies (2^{1/2})^x = 2^3 \implies 2^{x/2} = 2^3 \implies \frac{x}{2} = 3 \implies \mathbf{x = 6}$.

---

### TIPO 2: Comprimir y Desarrollar expresiones

* **Ejercicio de Comprimir (fundamental para ecuaciones):**  
  Agrupa en un solo logaritmo la expresión:  
  $$E = 2\log(x) - 3\log(y) + \frac{1}{2}\log(z)$$  
  *Paso 1: Subir los coeficientes al exponente del argumento:*  
  $$E = \log(x^2) - \log(y^3) + \log(\sqrt{z})$$  
* **Ejercicio de Desarrollar (El caso de números compuestos como el 36):**  
  ¿Qué pasa si te piden calcular $\log(36)$ sabiendo solo que $\log 2 = a$ y $\log 3 = b$?  
  Aquí 36 contiene "varias bases" primas ($36 = 2^2 \cdot 3^2$ o $6^2 = (2 \cdot 3)^2$).  
  *Paso 1: Descomponer el argumento en factores primos:*  
  $$\log(36) = \log(2^2 \cdot 3^2)$$  
  *Paso 2: Separar productos en sumas y bajar los exponentes de las potencias:*  
  $$\log(36) = \log(2^2) + \log(3^2) = 2\log(2) + 2\log(3) = \mathbf{2a + 2b}$$  
  *El truco maestro del 5 (típico de examen con el 36 o el 180):*  
  Si aparece $\log(180) = \log(36 \cdot 5)$, no conocemos $\log(5)$, pero sabemos que $5 = \frac{10}{2}$:  
  $$\log(5) = \log(10) - \log(2) = 1 - a$$  
  Por tanto: $\log(180) = \log(36) + \log(5) = (2a + 2b) + (1 - a) = \mathbf{1 + a + 2b}$.

---

### TIPO 2B: ¿QUÉ HACER CUANDO LA BASE ES COMPUESTA O UNA POTENCIA? (BASE 36, 6, 4...)

A menudo los alumnos se bloquean cuando la **base** no es un número primo simple, como tener base 36 frente a base 6.

#### 1. La Regla de Oro: La potencia en la base sale dividiendo
Si la base es una potencia ($36 = 6^2$ o $8 = 2^3$), se deduce por cambio de base:
$$\mathbf{\log_{b^k}(A) = \frac{1}{k} \log_b(A)}$$
*(Fíjate en la simetría: el exponente del argumento sale multiplicando arriba; el exponente de la base sale dividiendo abajo).*

* **Ejemplo 1:** $\log_{36}(6) = \log_{6^2}(6) = \frac{1}{2}\log_6(6) = \mathbf{\frac{1}{2}}$  
  *(Comprobación: $36^{1/2} = \sqrt{36} = 6$).*
* **Ejemplo 2:** $\log_{36}(216) = \log_{6^2}(6^3) = \frac{3}{2}\log_6(6) = \mathbf{\frac{3}{2}}$  
  *(Comprobación: $36^{3/2} = (\sqrt{36})^3 = 6^3 = 216$).*
* **Ejemplo 3 (Ecuación con base 6 y base 36):**  
  $$\log_6(x) + \log_{36}(x) = 3$$  
  Pasamos $\log_{36}(x)$ a base 6: $\log_{36}(x) = \frac{1}{2}\log_6(x)$.  
  $$\log_6(x) + \frac{1}{2}\log_6(x) = 3 \implies \frac{3}{2}\log_6(x) = 3 \implies \log_6(x) = 2 \implies \mathbf{x = 6^2 = 36}$$

#### 2. Ecuaciones exponenciales con varias bases que forman 36
* **Caso $2^x \cdot 3^x = 36$:**  
  Como tienen el mismo exponente, agrupamos las bases: $(2 \cdot 3)^x = 36 \implies 6^x = 6^2 \implies \mathbf{x = 2}$.
* **Caso con cambio de variable ($36^x$ y $6^x$):**  
  $$36^x - 7 \cdot 6^x + 6 = 0$$  
  Como $36^x = (6^2)^x = (6^x)^2$, hacemos $t = 6^x$:  
  $$t^2 - 7t + 6 = 0 \implies (t - 6)(t - 1) = 0 \implies t_1 = 6, \quad t_2 = 1$$  
  - $6^x = 6 \implies \mathbf{x = 1}$  
  - $6^x = 1 \implies \mathbf{x = 0}$

#### 3. Ecuaciones con VARIAS BASES Y DIFERENTES EXPONENTES
¿Qué ocurre si tenemos bases distintas (como 2 y 3) y además **exponentes diferentes** (como $x+2$ y $x-1$)?

* **Método 1: Desglose de potencias para unificar bases en 6 o 12 (Si tienen la misma $x$)**  
  > 💡 **La regla:** Separa las constantes con las propiedades de potencias: $a^{x+n} = a^x \cdot a^n$ y $a^{x-n} = \frac{a^x}{a^n}$.
  
  **Ejercicio de Examen Resuelto:**  
  $$2^{x+2} \cdot 3^{x-1} = 48$$
  *Paso 1: Desglosar cada potencia para aislar $2^x$ y $3^x$:*  
  $$2^x \cdot 2^2 \cdot \frac{3^x}{3^1} = 48 \implies 4 \cdot 2^x \cdot \frac{3^x}{3} = 48$$  
  *Paso 2: Extraer las constantes y juntar las bases $(2 \cdot 3)^x = 6^x$:*  
  $$\frac{4}{3} \cdot (2^x \cdot 3^x) = 48 \implies \frac{4}{3} \cdot 6^x = 48$$  
  *Paso 3: Despejar $6^x$:*  
  $$6^x = \frac{48 \cdot 3}{4} = 12 \cdot 3 = 36$$  
  *Paso 4: Reconocer la potencia ($36 = 6^2$):*  
  $$6^x = 6^2 \implies \mathbf{x = 2}$$  
  *(Comprobación instantánea: $2^{2+2} \cdot 3^{2-1} = 2^4 \cdot 3^1 = 16 \cdot 3 = 48 \checkmark$).*

* **Método 2: Método Universal con Logaritmos (Cuando las bases o exponentes no se pueden agrupar)**  
  **Ejercicio de Examen Resuelto:**  
  $$2^{x+1} = 3^{2x-1}$$  
  *Paso 1: Tomar logaritmo neperiano ($\ln$) a ambos miembros:*  
  $$\ln(2^{x+1}) = \ln(3^{2x-1})$$  
  *Paso 2: Bajar los exponentes multiplicando delante del logaritmo:*  
  $$(x + 1)\ln(2) = (2x - 1)\ln(3)$$  
  *Paso 3: Desarrollar los paréntesis (propiedad distributiva):*  
  $$x \ln(2) + \ln(2) = 2x \ln(3) - \ln(3)$$  
  *Paso 4: Agrupar las $x$ a un lado y los términos sin $x$ al otro:*  
  $$\ln(2) + \ln(3) = 2x \ln(3) - x \ln(2)$$  
  *Paso 5: Sacar factor común $x$ y aplicar propiedades de logaritmos:*  
  $$\ln(2 \cdot 3) = x \big(2\ln 3 - \ln 2\big) \implies \ln(6) = x \big(\ln(3^2) - \ln 2\big) = x \ln\left(\frac{9}{2}\right)$$  
  *Paso 6: Despejar $x$:*  
  $$\mathbf{x = \frac{\ln(6)}{\ln(4.5)}} \approx \frac{1.7918}{1.5041} \approx \mathbf{1.191}$$

#### 4. EXPONENTES SIENDO POTENCIADOS (TORRES DE POTENCIAS Y GRADO EN EL EXPONENTE)

Cuando el propio exponente está potenciado o elevado a otra potencia, hay dos trampas que suspenden:

1. **Distinción vital: Potencia de potencia vs Torre de potencias**
   - **Potencia de potencia (con paréntesis):** $(a^b)^c = a^{b \cdot c}$ *(los exponentes se multiplican)*.  
     Ejemplo: $(2^3)^2 = 2^{3 \cdot 2} = 2^6 = 64$.
   - **Torre de potencias (sin paréntesis, exponente potenciado):** $a^{b^c} = a^{(b^c)}$ *(se resuelve de arriba a abajo; $b$ se eleva a $c$)*.  
     Ejemplo: $2^{3^2} = 2^9 = 512$ *(¡completamente diferente de 64!)*.

2. **Ejercicio Maestro: Varias bases combinadas con EXPONENTES CUADRÁTICOS ($x^2$)**
   > **Problema de examen:**  
   > $$2^{x^2 + 1} \cdot 3^{x^2 - 1} = 24$$
   
   *Paso 1: Desglosar las potencias separando la parte cuadrática:*  
   $$2^{x^2} \cdot 2^1 \cdot \frac{3^{x^2}}{3^1} = 24 \implies 2 \cdot 2^{x^2} \cdot \frac{3^{x^2}}{3} = 24$$  
   *Paso 2: Extraer constantes y agrupar las bases $(2 \cdot 3)^{x^2} = 6^{x^2}$:*  
   $$\frac{2}{3} \cdot (2^{x^2} \cdot 3^{x^2}) = 24 \implies \frac{2}{3} \cdot 6^{x^2} = 24$$  
   *Paso 3: Despejar el bloque potenciado $6^{x^2}$:*  
   $$6^{x^2} = \frac{24 \cdot 3}{2} = 12 \cdot 3 = 36$$  
   *Paso 4: Igualar potencias de base 6 ($36 = 6^2$):*  
   $$6^{x^2} = 6^2 \implies \mathbf{x^2 = 2}$$  
   *Paso 5: Resolver la raíz (¡ojo a los dos signos!):*  
   $$\mathbf{x = \pm\sqrt{2}}$$  
   *(Comprobación: $(\pm\sqrt{2})^2 = 2 \implies 2^{2+1} \cdot 3^{2-1} = 2^3 \cdot 3^1 = 8 \cdot 3 = 24 \checkmark$).*

3. **Ejercicio de Torre de Exponentes (Incógnita en la potencia superior):**  
   $$2^{3^{x-1}} = 512$$  
   - Como $512 = 2^9$, igualamos los primeros exponentes: $3^{x-1} = 9$.  
   - Como $9 = 3^2$, igualamos los segundos exponentes: $x - 1 = 2 \implies \mathbf{x = 3}$.

---

### TIPO 3: Ecuaciones Logarítmicas (El ejercicio estrella del examen)

#### Caso A: Igualdad de logaritmos (Estrategia: "Un solo logaritmo a cada lado")
**Resolver:**  
$$\log(x + 3) + \log(x - 1) = \log(5)$$

* **Paso 1 (Comprimir con propiedades):** Suma se convierte en producto:  
  $$\log\big((x + 3)(x - 1)\big) = \log(5)$$
* **Paso 2 (Tachar logaritmos):** Si $\log(A) = \log(B)$, entonces $A = B$:  
  $$(x + 3)(x - 1) = 5$$  
  $$x^2 + 2x - 3 = 5 \implies x^2 + 2x - 8 = 0$$
* **Paso 3 (Resolver la ecuación resultante):**  
  $$x = \frac{-2 \pm \sqrt{4 - 4(1)(-8)}}{2} = \frac{-2 \pm \sqrt{36}}{2} = \frac{-2 \pm 6}{2} \implies x_1 = 2, \quad x_2 = -4$$
* **Paso 4 (¡OBLIGATORIO EN EL EXAMEN! COMPROBACIÓN):**  
  - Para $x_1 = 2$:  
    $\log(2+3) = \log(5) > 0$ y $\log(2-1) = \log(1) = 0 > 0$. **VÁLIDA ($\mathbf{x = 2}$)**.
  - Para $x_2 = -4$:  
    $\log(-4+3) = \log(-1) \to$ **¡No existe logaritmo de negativo!**  
    Por tanto, $x_2 = -4$ se **DESCARTA**.
  > ⚠️ *Dile a tu alumna: "Si no compruebas y tachas la solución negativa en el examen, te quitarán entre 0.5 y 1 punto".*

#### Caso B: Con números sueltos
**Resolver:**  
$$2\log(x) - \log(x + 6) = 0$$  
*Paso 1:* Pasa el negativo al otro lado: $2\log(x) = \log(x + 6)$  
*Paso 2:* Sube el 2 al exponente: $\log(x^2) = \log(x + 6)$  
*Paso 3:* Iguala argumentos: $x^2 = x + 6 \implies x^2 - x - 6 = 0 \implies (x - 3)(x + 2) = 0$.  
*Paso 4:* Posibles soluciones: $x = 3$ y $x = -2$. Comprobando: $\log(-2)$ no existe, por lo que la única solución válida es $\mathbf{x = 3}$.

#### Caso C: Ecuaciones con cambio de variable
**Resolver:**  
$$(\log x)^2 - 3\log x + 2 = 0$$  
*Hacemos $t = \log x$:*  
$$t^2 - 3t + 2 = 0 \implies (t - 1)(t - 2) = 0 \implies t_1 = 1, \quad t_2 = 2$$  
*Deshacemos el cambio:*  
- Si $\log_{10} x = 1 \implies x = 10^1 = \mathbf{10}$  
- Si $\log_{10} x = 2 \implies x = 10^2 = \mathbf{100}$  
Ambas son positivas, por lo que ambas son válidas.

---

### TIPO 4: Ecuaciones Exponenciales resueltas con Logaritmos

Cuando las bases no se pueden igualar fácilmente:  
$$3^x = 7$$  
*Método:* Tomamos logaritmos naturales ($\ln$) a ambos lados:  
$$\ln(3^x) = \ln(7)$$  
*Aplicamos la propiedad de la potencia para bajar el exponente:*  
$$x \cdot \ln(3) = \ln(7) \implies \mathbf{x = \frac{\ln(7)}{\ln(3)}} \approx 1.771$$

---

## 7. EL PUENTE CLAVE: CÓMO CONECTA CON DERIVADAS E INDETERMINACIONES

Tu alumna tiene el examen el lunes e incluye derivadas e indeterminaciones. Hoy dominará los logaritmos, pero debes sembrar la semilla para que cuando vea esos temas no empiece desde cero:

### 7.1. Conexión con DERIVADAS
Los logaritmos tienen la regla de derivación más elegante y fácil:
1. **Derivada elemental:**  
   $$f(x) = \ln(x) \implies f'(x) = \frac{1}{x}$$
2. **Derivada con regla de la cadena:**  
   $$f(x) = \ln\big(u(x)\big) \implies \mathbf{f'(x) = \frac{u'(x)}{u(x)}}$$  
   *Mnemotécnica para la alumna:* **"Derivada de lo de dentro partido por lo de dentro sin derivar"**.  
   *Ejemplo instantáneo:* Si $f(x) = \ln(x^3 + 5x)$, entonces $f'(x) = \frac{3x^2 + 5}{x^3 + 5x}$. ¡Lo aprenden en 10 segundos!
3. **Derivación logarítmica (para funciones elevadas a funciones $u(x)^{v(x)}$):**  
   Se toman logaritmos para bajar el exponente y derivar la expresión resultante como un producto.

### 7.2. Conexión con LÍMITES E INDETERMINACIONES
1. **El comportamiento en los bordes del dominio:**  
   - $\lim_{x \to +\infty} \ln(x) = +\infty$ (pero es la función que más lento crece de todas: las potencias le ganan siempre).
   - $\lim_{x \to 0^+} \ln(x) = -\infty$ (se va a menos infinito cuando se acerca a cero por la derecha).
2. **Indeterminación $1^\infty$ (El número $e$):**  
   Nace directamente de la definición del logaritmo y la base $e$:  
   $$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$$  
   La fórmula rápida de resolución: $\lim [f(x)]^{g(x)} = e^{\lim g(x) \cdot (f(x) - 1)}$.
3. **Regla de L'Hôpital con logaritmos:**  
   Indeterminaciones del tipo $0 \cdot \infty$, $0^0$, $\infty^0$ y $1^\infty$ se transforman aplicando logaritmos para convertir potencias en productos y bajarlas al cociente $\frac{0}{0}$ o $\frac{\infty}{\infty}$.

---

## 8. GUION TEMPORIZADO DE LA CLASE DE HOY (60 MINUTOS)

```
[00:00 - 05:00] DESCOMPRESIÓN Y JUEGO MENTAL
- "No mires el libro. Olvídate de los apuntes 5 minutos."
- "¿Cuánto es 2^3? Bien. Ahora: ¿a qué número elevo el 2 para que dé 8? Eso es un logaritmo."
- Hacer 5 cálculos orales de log2 y log10.

[05:00 - 15:00] DEFINICIÓN FORMAL Y LAS RESTRICCIONES
- Escribir log_b(a) = c <=> b^c = a (definición y paso a potencia exponencial).
- Las dos alarmas rojas: argumento > 0 siempre, base > 0 y != 1.
- Escribir ln(x) y explicar que es log en base e, nada más.

[15:00 - 30:00] LAS PROPIEDADES BÁSICAS Y ERRORES FRECUENTES
- Presentar: suma -> producto, resta -> cociente, potencia (bajada de exponente).
- Mostrar los errores frecuentes: ¡El logaritmo de una suma no se separa!
- Ejercicio guiado de comprimir una expresión con x, y, z.

[30:00 - 45:00] ECUACIONES LOGARÍTMICAS
- Resolver juntos el Ejercicio Tipo 3A (agrupar, quitar logaritmos, ecuación de 2º grado).
- ENFATIZAR: Descartar la solución que dé argumento negativo.

[45:00 - 55:00] ECUACIONES EXPONENCIALES
- Resolver 2^x = 5 tomando ln a ambos lados.

[55:00 - 60:00] CONSOLIDACIÓN Y VICTORIA MORAL
- Ponerle 2 ejercicios: uno de calcular y una ecuación sencilla.
- Dejarla que los resuelva sola con su chuleta delante.
- Felicitación y fijar la siguiente sesión: "El próximo día hacemos indeterminaciones y derivadas usando lo que ya sabes de hoy".
```
