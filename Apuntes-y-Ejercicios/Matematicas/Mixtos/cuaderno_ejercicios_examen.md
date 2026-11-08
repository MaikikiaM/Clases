# CUADERNO DE ENTRENAMIENTO PRÁCTICO PARA EXAMEN
> **Temas:** Logaritmos y Ecuaciones Exponenciales · Límites e Indeterminaciones · Derivadas y Aplicaciones  
> **Nivel:** 1º Bachillerato / Preparación EVAU

---

## BLOQUE 1: LOGARITMOS Y POTENCIAS

### 1.1. Cálculo manual directo (sin calculadora)
Calcula el valor exacto de cada logaritmo aplicando la definición:
1. $\log_2(64)$
2. $\log_3\left(\frac{1}{27}\right)$
3. $\log_5(\sqrt[4]{125})$
4. $\log_{\sqrt{2}}(16)$

### 1.2. Desarrollo con números compuestos y cambio de base
5. Sabiendo que $\log 2 \approx 0.301$ y $\log 3 \approx 0.477$ (en base 10), calcula aplicando propiedades:
   - a) $\log(36)$
   - b) $\log(180)$ *(pista: descompón $5 = 10/2$)*
   - c) $\log(0.75)$
6. Comprime en un único logaritmo la siguiente expresión:
   $$E = 2\ln(x) - \frac{1}{3}\ln(y) + 3\ln(z)$$

### 1.3. Ecuaciones logarítmicas
Resuelve y comprueba obligatoriamente la validez de las soluciones:
7. $\log(x) + \log(x + 3) = 1$
8. $2\log(x) - \log(x + 6) = 0$
9. $(\log x)^2 - 4\log x + 3 = 0$ *(mediante cambio de variable $t = \log x$)*

### 1.4. Ecuaciones exponenciales avanzadas
10. $2^{x+2} \cdot 3^{x-1} = 48$ *(desglose de potencias y unificación de bases)*
11. $2^{x^2 + 1} \cdot 3^{x^2 - 1} = 24$ *(exponentes cuadráticos)*
12. $3^{2x-1} = 7^x$ *(resolución mediante logaritmos neperianos)*

---

## BLOQUE 2: LÍMITES E INDETERMINACIONES

### 2.1. Sustitución y primeras indeterminaciones racionales
13. $\lim_{x \to 3} \frac{x^2 - 1}{x + 2}$ *(sustitución directa)*
14. $\lim_{x \to 2} \frac{x^2 - 5x + 6}{x^2 - 4}$ *($[0/0]$ en cociente de polinomios)*
15. $\lim_{x \to 1} \frac{x^3 - 3x + 2}{x^2 - 1}$ *($[0/0]$ con factorización por Ruffini)*

### 2.2. Indeterminaciones con radicales y conjugados
16. $\lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x}$ *($[0/0]$ multiplicando por el conjugado)*
17. $\lim_{x \to 3} \frac{x - 3}{\sqrt{x + 1} - 2}$ *($[0/0]$ con radical en denominador)*
18. $\lim_{x \to \infty} \left(\sqrt{x^2 + 6x} - x\right)$ *($[\infty - \infty]$ con conjugado)*

### 2.3. Indeterminaciones en el infinito y número $e$
19. $\lim_{x \to \infty} \frac{4x^3 - 2x + 7}{5x^3 + 3x^2 - 1}$ *($[\infty/\infty]$ por comparación de grados)*
20. $\lim_{x \to \infty} \frac{\sqrt{9x^2 + 4x}}{2x - 1}$ *($[\infty/\infty]$ con radicales dominantes)*
21. $\lim_{x \to \infty} \left(1 + \frac{4}{x}\right)^{3x}$ *($[1^\infty]$ tipo número $e$)*
22. $\lim_{x \to \infty} \left(\frac{x + 3}{x - 1}\right)^{2x + 5}$ *($[1^\infty]$ con fórmula general)*

---

## BLOQUE 3: DERIVADAS Y APLICACIONES

### 3.1. Cálculo de funciones derivadas (regla de la cadena)
Calcula la derivada simplificada de cada función:
23. $f(x) = (3x^2 - 5x + 1)^4$
24. $f(x) = \sqrt{x^3 + 2x}$
25. $f(x) = e^{x^2 - 3x}$
26. $f(x) = \ln(x^4 + 3x^2 + 2)$
27. $f(x) = x^2 \cdot e^{2x}$ *(derivada de un producto)*
28. $f(x) = \frac{2x - 1}{x^2 + 3}$ *(derivada de un cociente)*

### 3.2. Recta tangente a una curva en un punto
29. Halla la ecuación de la recta tangente a la curva $f(x) = x^2 - 4x + 1$ en el punto de abscisa $x_0 = 3$.
30. Halla la ecuación de la recta tangente a la curva $f(x) = \frac{x + 2}{x - 1}$ en el punto de abscisa $x_0 = 2$.

### 3.3. Monotonía y extremos relativos (máximos y mínimos)
31. Dada la función $f(x) = x^3 - 3x^2 - 9x + 5$:
   - a) Determina los intervalos de crecimiento y decrecimiento.
   - b) Halla las coordenadas exactas $(x, y)$ de sus máximos y mínimos relativos.

---

# SOLUCIONARIO COMPLETO PASO A PASO

## BLOQUE 1: LOGARITMOS Y POTENCIAS

**1. $\log_2(64)$:**  
¿A qué potencia elevo 2 para obtener 64? $64 = 2^6 \implies \log_2(2^6) = \mathbf{6}$.

**2. $\log_3\left(\frac{1}{27}\right)$:**  
$27 = 3^3 \implies \frac{1}{27} = 3^{-3} \implies \log_3(3^{-3}) = \mathbf{-3}$.

**3. $\log_5(\sqrt[4]{125})$:**  
$125 = 5^3 \implies \sqrt[4]{125} = 5^{3/4} \implies \log_5(5^{3/4}) = \mathbf{\frac{3}{4}}$.

**4. $\log_{\sqrt{2}}(16)$:**  
Definición: $(\sqrt{2})^x = 16 \implies (2^{1/2})^x = 2^4 \implies 2^{x/2} = 2^4 \implies \frac{x}{2} = 4 \implies \mathbf{x = 8}$.

**5. Sabiendo $\log 2 \approx 0.301$ y $\log 3 \approx 0.477$:**  
- a) $\log(36) = \log(2^2 \cdot 3^2) = 2\log 2 + 2\log 3 = 2(0.301) + 2(0.477) = 0.602 + 0.954 = \mathbf{1.556}$.
- b) $\log(180) = \log(36 \cdot 5) = \log 36 + \log\left(\frac{10}{2}\right) = \log 36 + \log 10 - \log 2 = 1.556 + 1 - 0.301 = \mathbf{2.255}$.
- c) $\log(0.75) = \log\left(\frac{3}{4}\right) = \log 3 - \log(2^2) = \log 3 - 2\log 2 = 0.477 - 0.602 = \mathbf{-0.125}$.

**6. Comprimir expresión:**  
Subir coeficientes a los exponentes:  
$E = \ln(x^2) - \ln(y^{1/3}) + \ln(z^3) = \ln\left(\frac{x^2 \cdot z^3}{\sqrt[3]{y}}\right)$.

**7. $\log(x) + \log(x + 3) = 1$:**  
- Agrupar: $\log\big(x(x + 3)\big) = \log(10) \implies x^2 + 3x = 10 \implies x^2 + 3x - 10 = 0$.  
- Factorizar: $(x + 5)(x - 2) = 0 \implies x_1 = 2, \quad x_2 = -5$.  
- Comprobación: para $x = -5$, $\log(-5)$ no existe (se descarta). Para $x = 2$, ambos argumentos son positivos.  
  **Solución única válida:** $\mathbf{x = 2}$.

**8. $2\log(x) - \log(x + 6) = 0$:**  
- Trasponer y subir exponente: $\log(x^2) = \log(x + 6) \implies x^2 - x - 6 = 0$.  
- Raíces: $(x - 3)(x + 2) = 0 \implies x_1 = 3, \quad x_2 = -2$.  
- Comprobación: $\log(-2)$ no existe.  
  **Solución única válida:** $\mathbf{x = 3}$.

**9. $(\log x)^2 - 4\log x + 3 = 0$:**  
- Cambio $t = \log x \implies t^2 - 4t + 3 = 0 \implies (t - 1)(t - 3) = 0 \implies t_1 = 1, \quad t_2 = 3$.  
- Deshacer cambio: $\log_{10} x = 1 \implies \mathbf{x = 10}$; $\log_{10} x = 3 \implies \mathbf{x = 1000}$.  
  Ambas soluciones son positivas y válidas.

**10. $2^{x+2} \cdot 3^{x-1} = 48$:**  
- Desglosar potencias: $2^x \cdot 2^2 \cdot \frac{3^x}{3^1} = 48 \implies 4 \cdot \frac{1}{3} \cdot (2 \cdot 3)^x = 48$.  
- Despejar $6^x$: $\frac{4}{3} \cdot 6^x = 48 \implies 6^x = \frac{48 \cdot 3}{4} = 36$.  
- Como $36 = 6^2 \implies \mathbf{x = 2}$.

**11. $2^{x^2 + 1} \cdot 3^{x^2 - 1} = 24$:**  
- Desglosar: $2 \cdot 2^{x^2} \cdot \frac{3^{x^2}}{3} = 24 \implies \frac{2}{3} \cdot (2 \cdot 3)^{x^2} = 24$.  
- Despejar: $6^{x^2} = \frac{24 \cdot 3}{2} = 36 = 6^2 \implies x^2 = 2 \implies \mathbf{x = \pm\sqrt{2}}$.

**12. $3^{2x-1} = 7^x$:**  
- Tomar logaritmo neperiano: $\ln(3^{2x-1}) = \ln(7^x) \implies (2x - 1)\ln 3 = x \ln 7$.  
- Desarrollar y agrupar $x$: $2x \ln 3 - \ln 3 = x \ln 7 \implies x(2\ln 3 - \ln 7) = \ln 3$.  
- Despejar: $\mathbf{x = \frac{\ln 3}{\ln(9/7)}} \approx \mathbf{4.37}$.

---

## BLOQUE 2: LÍMITES E INDETERMINACIONES

**13. $\lim_{x \to 3} \frac{x^2 - 1}{x + 2}$:**  
Sustitución directa: $\frac{3^2 - 1}{3 + 2} = \mathbf{\frac{8}{5}}$.

**14. $\lim_{x \to 2} \frac{x^2 - 5x + 6}{x^2 - 4}$:**  
Sustituyendo da $\left[\frac{0}{0}\right]$.  
Factorizando: $\frac{(x - 2)(x - 3)}{(x - 2)(x + 2)} = \frac{x - 3}{x + 2}$.  
Límite: $\frac{2 - 3}{2 + 2} = \mathbf{-\frac{1}{4}}$.

**15. $\lim_{x \to 1} \frac{x^3 - 3x + 2}{x^2 - 1}$:**  
Sustituyendo da $\left[\frac{0}{0}\right]$.  
Factorizando numerador por Ruffini con raíz $1$: $x^3 - 3x + 2 = (x - 1)(x^2 + x - 2) = (x - 1)^2(x + 2)$.  
Denominador: $x^2 - 1 = (x - 1)(x + 1)$.  
Simplificando: $\lim_{x \to 1} \frac{(x - 1)(x + 2)}{x + 1} = \frac{0 \cdot 3}{2} = \mathbf{0}$.

**16. $\lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x}$:**  
Sustituyendo da $\left[\frac{0}{0}\right]$.  
Multiplicando por el binomio conjugado:  
$$\frac{(\sqrt{x + 4} - 2)(\sqrt{x + 4} + 2)}{x(\sqrt{x + 4} + 2)} = \frac{(x + 4) - 4}{x(\sqrt{x + 4} + 2)} = \frac{x}{x(\sqrt{x + 4} + 2)} = \frac{1}{\sqrt{x + 4} + 2}$$  
Límite: $\frac{1}{\sqrt{4} + 2} = \mathbf{\frac{1}{4}}$.

**17. $\lim_{x \to 3} \frac{x - 3}{\sqrt{x + 1} - 2}$:**  
Multiplicando por $(\sqrt{x + 1} + 2)$:  
$$\frac{(x - 3)(\sqrt{x + 1} + 2)}{(x + 1) - 4} = \frac{(x - 3)(\sqrt{x + 1} + 2)}{x - 3} = \sqrt{x + 1} + 2$$  
Límite: $\sqrt{3 + 1} + 2 = 2 + 2 = \mathbf{4}$.

**18. $\lim_{x \to \infty} \left(\sqrt{x^2 + 6x} - x\right)$:**  
Indeterminación $[\infty - \infty]$. Multiplicando y dividiendo por $(\sqrt{x^2 + 6x} + x)$:  
$$\frac{(x^2 + 6x) - x^2}{\sqrt{x^2 + 6x} + x} = \frac{6x}{\sqrt{x^2 + 6x} + x}$$  
Dividiendo numerador y denominador entre $x$:  
$$\frac{6}{\sqrt{1 + \frac{6}{x}} + 1} \xrightarrow{x \to \infty} \frac{6}{1 + 1} = \mathbf{3}$$

**19. $\lim_{x \to \infty} \frac{4x^3 - 2x + 7}{5x^3 + 3x^2 - 1}$:**  
Cociente de polinomios con idéntico grado (3): límite = cociente de coeficientes líderes = $\mathbf{\frac{4}{5}}$.

**20. $\lim_{x \to \infty} \frac{\sqrt{9x^2 + 4x}}{2x - 1}$:**  
El término dominante del numerador es $\sqrt{9x^2} = 3x$.  
El término dominante del denominador es $2x$.  
Límite = $\frac{3x}{2x} = \mathbf{\frac{3}{2}}$.

**21. $\lim_{x \to \infty} \left(1 + \frac{4}{x}\right)^{3x}$:**  
Indeterminación $[1^\infty]$. Aplicando la fórmula $e^{\lim g(x)(f(x) - 1)}$:  
$$e^{\lim_{x \to \infty} 3x \cdot \frac{4}{x}} = e^{12} = \mathbf{e^{12}}$$

**22. $\lim_{x \to \infty} \left(\frac{x + 3}{x - 1}\right)^{2x + 5}$:**  
Base tiende a 1, exponente a $\infty \implies [1^\infty]$.  
$$f(x) - 1 = \frac{x + 3}{x - 1} - 1 = \frac{x + 3 - (x - 1)}{x - 1} = \frac{4}{x - 1}$$  
Exponente: $\lim_{x \to \infty} (2x + 5) \cdot \frac{4}{x - 1} = \lim_{x \to \infty} \frac{8x + 20}{x - 1} = 8$.  
Resultado: $\mathbf{e^8}$.

---

## BLOQUE 3: DERIVADAS Y APLICACIONES

**23. $f(x) = (3x^2 - 5x + 1)^4$:**  
$$f'(x) = 4(3x^2 - 5x + 1)^3 \cdot \frac{d}{dx}(3x^2 - 5x + 1) = \mathbf{4(3x^2 - 5x + 1)^3(6x - 5)}$$

**24. $f(x) = \sqrt{x^3 + 2x}$:**  
$$f'(x) = \frac{1}{2\sqrt{x^3 + 2x}} \cdot (3x^2 + 2) = \mathbf{\frac{3x^2 + 2}{2\sqrt{x^3 + 2x}}}$$

**25. $f(x) = e^{x^2 - 3x}$:**  
$$f'(x) = e^{x^2 - 3x} \cdot (2x - 3) = \mathbf{(2x - 3)e^{x^2 - 3x}}$$

**26. $f(x) = \ln(x^4 + 3x^2 + 2)$:**  
$$f'(x) = \frac{u'(x)}{u(x)} = \mathbf{\frac{4x^3 + 6x}{x^4 + 3x^2 + 2}}$$

**27. $f(x) = x^2 \cdot e^{2x}$:**  
Regla del producto $(u \cdot v)' = u'v + uv'$:  
$$f'(x) = 2x \cdot e^{2x} + x^2 \cdot (2e^{2x}) = \mathbf{2x(1 + x)e^{2x}}$$

**28. $f(x) = \frac{2x - 1}{x^2 + 3}$:**  
Regla del cociente $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:  
$$f'(x) = \frac{2(x^2 + 3) - (2x - 1)(2x)}{(x^2 + 3)^2} = \frac{2x^2 + 6 - 4x^2 + 2x}{(x^2 + 3)^2} = \mathbf{\frac{-2x^2 + 2x + 6}{(x^2 + 3)^2}}$$

**29. Recta tangente a $f(x) = x^2 - 4x + 1$ en $x_0 = 3$:**  
1. Punto de tangencia: $y_0 = f(3) = 3^2 - 4(3) + 1 = 9 - 12 + 1 = -2 \implies P(3, -2)$.  
2. Pendiente: $f'(x) = 2x - 4 \implies m = f'(3) = 2(3) - 4 = 2$.  
3. Ecuación punto-pendiente: $y - (-2) = 2(x - 3) \implies y + 2 = 2x - 6 \implies \mathbf{y = 2x - 8}$.

**30. Recta tangente a $f(x) = \frac{x + 2}{x - 1}$ en $x_0 = 2$:**  
1. Punto de tangencia: $y_0 = f(2) = \frac{4}{1} = 4 \implies P(2, 4)$.  
2. Pendiente: $f'(x) = \frac{1(x - 1) - (x + 2)(1)}{(x - 1)^2} = \frac{-3}{(x - 1)^2} \implies m = f'(2) = \frac{-3}{(2 - 1)^2} = -3$.  
3. Ecuación punto-pendiente: $y - 4 = -3(x - 2) \implies y - 4 = -3x + 6 \implies \mathbf{y = -3x + 10}$.

**31. Monotonía y extremos de $f(x) = x^3 - 3x^2 - 9x + 5$:**  
1. Derivada: $f'(x) = 3x^2 - 6x - 9$.  
2. Puntos críticos: $3(x^2 - 2x - 3) = 0 \implies (x - 3)(x + 1) = 0 \implies x_1 = -1, \quad x_2 = 3$.  
3. Intervalos de signo de $f'(x)$:  
   - En $(-\infty, -1)$: $f'(-2) = 3(4) - 6(-2) - 9 = 15 > 0 \implies$ **Creciente en $(-\infty, -1)$**.  
   - En $(-1, 3)$: $f'(0) = -9 < 0 \implies$ **Decreciente en $(-1, 3)$**.  
   - En $(3, \infty)$: $f'(4) = 3(16) - 24 - 9 = 15 > 0 \implies$ **Creciente en $(3, \infty)$**.  
4. Extremos relativos:  
   - En $x = -1$: la función cambia de creciente a decreciente $\implies$ **Máximo relativo**.  
     $f(-1) = (-1)^3 - 3(-1)^2 - 9(-1) + 5 = -1 - 3 + 9 + 5 = 10 \implies \mathbf{\text{Máximo en } (-1, 10)}$.  
   - En $x = 3$: la función cambia de decreciente a creciente $\implies$ **Mínimo relativo**.  
     $f(3) = 3^3 - 3(3^2) - 9(3) + 5 = 27 - 27 - 27 + 5 = -22 \implies \mathbf{\text{Mínimo en } (3, -22)}$.
