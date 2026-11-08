# KIT COMPLETO DE SUPERVIVENCIA: MATEMÁTICAS
## (Logaritmos, Límites e Indeterminaciones, y Derivadas)

> **Tu manual de rescate para el examen:** Todo el temario explicado en lenguaje claro, con las fórmulas que necesitas, las recetas mecánicas paso a paso y los errores que restan puntos.

---

# BLOQUE 1: LOGARITMOS Y EXPONENCIALES

### 1. ¿Qué es un Logaritmo?
Un logaritmo es una **pregunta sobre una potencia**:
$$\mathbf{\log_{\text{base}}(\text{resultado}) = \text{exponente} \iff \text{base}^{\text{exponente}} = \text{resultado}}$$
> 💡 **La pregunta mágica que debes hacerte siempre:**  
> **"¿A qué número tengo que elevar la base para que me dé el número de dentro?"**
> - $\log_2(8) = \mathbf{3}$ (porque $2^3 = 8$).
> - $\log_3(9) = \mathbf{2}$ (porque $3^2 = 9$).
> - $\log_{10}(1000) = \mathbf{3}$ (si no hay base escrita, es base 10; cuenta los ceros).
> - $\ln(x)$ es el logaritmo neperiano (base $e \approx 2.718$). Las propiedades son exactamente las mismas.

### 2. Lo que está TOTALMENTE PROHIBIDO
- ❌ No existe logaritmo de números negativos ni de cero: $\log(-4) \to$ **ERROR**, $\log(0) \to$ **ERROR**.
- ❌ $\log(A + B) \neq \log A + \log B$ (el logaritmo de una suma **no se separa jamás**).
- ❌ $\frac{\log A}{\log B} \neq \log A - \log B$.

### 3. Las Propiedades de Oro
| Propiedad | Operación dentro | Operación fuera | Ejemplo |
|---|---|---|---|
| **Producto** | $\log(A \cdot B)$ | $\log A + \log B$ | $\log(2x) = \log 2 + \log x$ |
| **Cociente** | $\log(A / B)$ | $\log A - \log B$ | $\log(x / 5) = \log x - \log 5$ |
| **Potencia** | $\log(A^n)$ | $n \cdot \log A$ | $\log(x^4) = 4\log x$ |
| **Raíz** | $\log(\sqrt[n]{A})$ | $\frac{1}{n}\log A$ | $\log(\sqrt{x}) = \frac{1}{2}\log x$ |
| **Base con potencia**| $\log_{b^k}(A)$ | $\frac{1}{k}\log_b(A)$ | $\log_{36}(6) = \log_{6^2}(6) = \frac{1}{2}\log_6(6) = \frac{1}{2}$ |

### 4. El caso del 36 (Números con Varias Bases Primarias)
Si te piden calcular $\log(36)$ sabiendo solo que $\log 2 = a$ y $\log 3 = b$:
- **Factoriza en primos:** $36 = 2^2 \cdot 3^2$.
- **Aplica propiedades:** $\log(36) = \log(2^2 \cdot 3^2) = 2\log(2) + 2\log(3) = \mathbf{2a + 2b}$.
- **Descomposición del 5:** Como $5 = \frac{10}{2}$, entonces $\log(5) = \log(10) - \log(2) = \mathbf{1 - a}$.
- **Con decimales:** $\log(0.36) = \log\left(\frac{36}{100}\right) = \log(36) - \log(100) = \mathbf{2a + 2b - 2}$.

### 5. Ecuaciones Exponenciales con Varias Bases y Exponentes
- **Desglose de potencias:** $2^{x+2} \cdot 3^{x-1} = 48 \implies 4 \cdot 2^x \cdot \frac{3^x}{3} = 48 \implies \frac{4}{3} \cdot 6^x = 48 \implies 6^x = 36 = 6^2 \implies \mathbf{x = 2}$.
- **Exponentes cuadráticos ($x^2$):** $2^{x^2+1} \cdot 3^{x^2-1} = 24 \implies \frac{2}{3} \cdot 6^{x^2} = 24 \implies 6^{x^2} = 36 = 6^2 \implies x^2 = 2 \implies \mathbf{x = \pm\sqrt{2}}$.
- **Bases incompatibles:** $2^{x+1} = 3^{2x-1} \implies$ toma $\ln$ a ambos lados y despeja $x$: $\mathbf{x = \frac{\ln 6}{\ln(4.5)} \approx 1.191}$.

### 6. Receta para Ecuaciones Logarítmicas en 3 Pasos
1. **Agrupa** con las propiedades hasta tener $\log(\dots) = \log(\dots)$.
2. **Tacha** los logaritmos e iguala lo de dentro.
3. **Resuelve** la ecuación y **COMPRUEBA** las soluciones en los logaritmos iniciales: si una solución hace que un argumento sea negativo o cero, **¡se tacha y se descarta obligatoriamente!**

---

# BLOQUE 2: LÍMITES E INDETERMINACIONES

### 1. Regla Cero: ¡Sustituye siempre primero!
Antes de hacer nada, sustituye la $x$ por el valor al que tiende.
- $\frac{0}{k} = \mathbf{0} \quad (k \neq 0)$
- $\frac{k}{\infty} = \mathbf{0}$
- $\frac{k}{0} = \mathbf{\pm\infty}$ *(¡No es indeterminación! Es una asíntota vertical; calcula límites laterales para saber el signo).*

### 2. Recetas de las Indeterminaciones de Examen

| Indeterminación | Tipo de Expresión | Receta Mecánica de Resolución |
|:---|:---|:---|
| $\mathbf{\left[\frac{0}{0}\right]}$ | **Polinomios** ($x \to a$) | **Factoriza** por Ruffini o identidades notables, **tacha el factor común $(x - a)$** arriba y abajo, y vuelve a sustituir. |
| $\mathbf{\left[\frac{0}{0}\right]}$ | **Raíces cuadradas** ($x \to a$) | **Multiplica y divide por el conjugado** $(A + B)$ para romper la raíz con $(A-B)(A+B) = A^2 - B^2$, simplifica y sustituye. |
| $\mathbf{\left[\frac{\infty}{\infty}\right]}$ | **Polinomios / Raíces** ($x \to \infty$) | **Regla de los Grados:**<br>• Si $\text{Grado Arriba} > \text{Grado Abajo} \implies \mathbf{\pm\infty}$<br>• Si $\text{Grado Arriba} < \text{Grado Abajo} \implies \mathbf{0}$<br>• Si $\text{Grado Arriba} = \text{Grado Abajo} \implies \mathbf{\text{Dividir coeficientes líderes}}$ |
| $\mathbf{[\infty - \infty]}$ | **Resta con Raíces** ($x \to \infty$) | **Multiplica y divide por el conjugado** de la expresión con raíces. |
| $\mathbf{\left[1^\infty\right]}$ | **Potencias** ($x \to \infty$) | **Fórmula directa del número $e$:**<br>$$\mathbf{\lim [f(x)]^{g(x)} = e^{\lim g(x) \cdot [f(x) - 1]}}$$ |
| **Jerarquía** | Mezcla de funciones ($x \to \infty$) | **Fuerza de crecimiento:** $\mathbf{\text{Exponencial } (a^x) \gg \text{Polinomio } (x^n) \gg \text{Logaritmo } (\ln x)}$ |

---

# BLOQUE 3: DERIVADAS Y APLICACIONES

### 1. Tabla de Derivadas (con Regla de la Cadena)
> 💡 *Regla: Cuando dentro haya una función $u(x)$, deriva normal y multiplica siempre al final por $u'$ (la derivada de lo de dentro).*

- **Constante:** $(k)' = 0$
- **Identidad:** $(x)' = 1$
- **Potencia:** $(x^n)' = n x^{n-1} \qquad \big([u^n]' = \mathbf{n \cdot u^{n-1} \cdot u'}\big)$
- **Raíz Cuadrada:** $(\sqrt{x})' = \frac{1}{2\sqrt{x}} \qquad \left([\sqrt{u}]' = \mathbf{\frac{u'}{2\sqrt{u}}}\right)$
- **Exponencial $e$:** $(e^x)' = e^x \qquad \big([e^u]' = \mathbf{e^u \cdot u'}\big)$
- **Exponencial $a$:** $(a^x)' = a^x \ln a \qquad \big([a^u]' = \mathbf{a^u \ln a \cdot u'}\big)$
- **Logaritmo:** $(\ln x)' = \frac{1}{x} \qquad \left([\ln u]' = \mathbf{\frac{u'}{u}}\right) \quad \longleftarrow$ *(¡Derivada de dentro entre dentro sin derivar!)*
- **Seno y Coseno:** $(\sin u)' = \cos(u) \cdot u' \qquad (\cos u)' = -\sin(u) \cdot u'$

### 2. Operaciones con Derivadas
- **Producto:** $\mathbf{(u \cdot v)' = u'v + uv'}$
- **Cociente:** $\mathbf{\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}}$

### 3. Recta Tangente a $f(x)$ en $x = a$
> **Fórmula:** $$\mathbf{y - f(a) = f'(a)(x - a)}$$
1. **Punto:** Calcula $f(a)$ para tener las coordenadas $(a, f(a))$.
2. **Pendiente:** Calcula $f'(x)$ y sustituye $x = a$ para obtener $m = f'(a)$.
3. **Ecuación:** Escribe $y - f(a) = m(x - a)$ y despeja la $y$.

### 4. Monotonía (Crecimiento/Decrecimiento) y Extremos Relativos
1. **Deriva e iguala a cero:** $f'(x) = 0$. Las soluciones son los **puntos críticos**.
2. **Recta real y signos:** Coloca los puntos críticos en una recta y prueba un número en cada tramo dentro de $f'(x)$:
   - Si $f'(x) > 0 \implies$ **Creciente** ($\nearrow$)
   - Si $f'(x) < 0 \implies$ **Decreciente** ($\searrow$)
3. **Extremos:**  
   - Si pasa de $\nearrow$ a $\searrow \implies$ **Máximo Relativo**.
   - Si pasa de $\searrow$ a $\nearrow \implies$ **Mínimo Relativo**.
   *(Para hallar la coordenada $y$, sustituye la $x$ en la función original $f(x)$).*

---

# BLOQUE 4: BATERÍA DE ENTRENAMIENTO PARA EL EXAMEN

### Logaritmos y Exponenciales
1. Calcula a mano: $\log_2(64)$ y $\log_3\left(\frac{1}{27}\right)$.
2. Si $\log 2 = a$ y $\log 3 = b$, expresa $\log(36)$ y $\log(180)$.
3. Resuelve: $\log(x + 3) + \log(x - 1) = \log(5)$.
4. Resuelve: $2^{x+2} \cdot 3^{x-1} = 48$.
5. Resuelve: $2^{x^2+1} \cdot 3^{x^2-1} = 24$.

### Límites e Indeterminaciones
6. $\lim_{x \to 2} \frac{x^2 - 4}{x^2 - 3x + 2}$
7. $\lim_{x \to 0} \frac{\sqrt{x+4} - 2}{x}$
8. $\lim_{x \to \infty} \frac{6x^3 - 2x + 1}{2x^3 + 5x^2}$
9. $\lim_{x \to \infty} \left(\sqrt{x^2 + 6x} - x\right)$
10. $\lim_{x \to \infty} \left(\frac{2x+3}{2x-1}\right)^{4x}$

### Derivadas y Aplicaciones
11. Deriva: $f(x) = \ln(x^3 + 4x)$
12. Deriva: $g(x) = \frac{e^{2x}}{x^2 + 1}$
13. Halla la recta tangente a $f(x) = x^2 - 4x + 5$ en $x = 3$.
14. Halla los intervalos de crecimiento y los extremos relativos de $f(x) = x^3 - 3x^2 - 9x + 2$.

---

# SOLUCIONES DE AUTOCORRECCIÓN

1. $\log_2(64) = \mathbf{6}$ ; $\log_3(3^{-3}) = \mathbf{-3}$.
2. $\log(36) = \mathbf{2a + 2b}$ ; $\log(180) = \log(36 \cdot 10/2) = \mathbf{1 + a + 2b}$.
3. $\log((x+3)(x-1)) = \log 5 \implies x^2 + 2x - 8 = 0 \implies \mathbf{x = 2}$ (se descarta $x = -4$).
4. $\frac{4}{3} \cdot 6^x = 48 \implies 6^x = 36 \implies \mathbf{x = 2}$.
5. $\frac{2}{3} \cdot 6^{x^2} = 24 \implies 6^{x^2} = 36 = 6^2 \implies x^2 = 2 \implies \mathbf{x = \pm\sqrt{2}}$.
6. $\left[\frac{0}{0}\right] \implies \lim_{x \to 2} \frac{(x-2)(x+2)}{(x-2)(x-1)} = \frac{2+2}{2-1} = \mathbf{4}$.
7. $\left[\frac{0}{0}\right]$ Conjugado $\implies \lim_{x \to 0} \frac{(x+4)-4}{x(\sqrt{x+4}+2)} = \frac{1}{\sqrt{4}+2} = \mathbf{\frac{1}{4}}$.
8. $\left[\frac{\infty}{\infty}\right]$ Grados iguales (3) $\implies \frac{6}{2} = \mathbf{3}$.
9. $[\infty - \infty]$ Conjugado $\implies \lim_{x \to \infty} \frac{6x}{\sqrt{x^2+6x}+x} = \frac{6x}{2x} = \mathbf{3}$.
10. $\left[1^\infty\right] \implies e^{\lim 4x \cdot \left(\frac{2x+3-(2x-1)}{2x-1}\right)} = e^{\lim \frac{16x}{2x-1}} = \mathbf{e^8}$.
11. $f'(x) = \mathbf{\frac{3x^2 + 4}{x^3 + 4x}}$.
12. Cociente y cadena: $g'(x) = \frac{2e^{2x}(x^2+1) - e^{2x}(2x)}{(x^2+1)^2} = \mathbf{\frac{2e^{2x}(x^2 - x + 1)}{(x^2+1)^2}}$.
13. $f(3) = 9 - 12 + 5 = 2 \implies P(3, 2)$.  
    $f'(x) = 2x - 4 \implies m = f'(3) = 2(3) - 4 = 2$.  
    Recta: $y - 2 = 2(x - 3) \implies \mathbf{y = 2x - 4}$.
14. $f'(x) = 3x^2 - 6x - 9 = 0 \implies x^2 - 2x - 3 = 0 \implies x = -1, \quad x = 3$.  
    - Creciente en $(-\infty, -1) \cup (3, +\infty)$.  
    - Decreciente en $(-1, 3)$.  
    - **Máximo relativo en $(-1, 7)$**; **Mínimo relativo en $(3, -25)$**.
