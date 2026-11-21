# Apuntes Maestros de Cálculo Integral

> **Tipos de integrales, métodos de resolución y más de 85 ejemplos resueltos paso a paso**  
> Desde primitivas inmediatas hasta aplicaciones geométricas e integrales impropias.

---

## Índice General de Contenidos

1. [Concepto de Primitiva, Propiedades e Integrales Inmediatas](#1-concepto-de-primitiva-propiedades-e-integrales-inmediatas)
2. [Integrales Casi Inmediatas (Regla de la Cadena Inversa)](#2-integrales-casi-inmediatas-regla-de-la-cadena-inversa)
3. [Integración por Cambio de Variable (Sustitución)](#3-integración-por-cambio-de-variable-sustitución)
4. [Integración por Partes](#4-integración-por-partes)
5. [Integrales Racionales $\int \frac{P(x)}{Q(x)}\,dx$](#5-integrales-racionales)
6. [Integrales Trigonométricas](#6-integrales-trigonométricas)
7. [Integral Definida, Regla de Barrow y Teorema Fundamental](#7-integral-definida-regla-de-barrow-y-teorema-fundamental)
8. [Aplicaciones Geométricas: Cálculo de Áreas y Volúmenes](#8-aplicaciones-geométricas-cálculo-de-áreas-y-volúmenes)
9. [Ampliación: Integrales Impropias Básicas](#9-ampliación-integrales-impropias-básicas)
10. [Mapa Maestro de Decisión y los 10 Errores Letales](#10-mapa-maestro-de-decisión-y-los-10-errores-letales)

---

## 1. Concepto de Primitiva, Propiedades e Integrales Inmediatas

### 1.1. ¿Qué es integrar? Primitiva y constante de integración $+C$

Integrar es la operación inversa de derivar. Dada una función $f(x)$, buscamos otra función $F(x)$, llamada **primitiva** (o antiderivada) de $f(x)$, tal que su derivada devuelva la función original:

$$F(x) \text{ es primitiva de } f(x) \iff F'(x) = f(x)$$

**¿Por qué aparece siempre $+C$?** Como la derivada de cualquier constante $C \in \mathbb{R}$ es $0$, si $F(x)$ es una primitiva de $f(x)$, entonces $F(x) + C$ también lo es, porque $(F(x) + C)' = F'(x) + 0 = f(x)$. A la familia de todas las primitivas (curvas desplazadas verticalmente) se la llama **integral indefinida**:

$$\int f(x)\,dx = F(x) + C, \qquad C \in \mathbb{R}$$

### 1.2. Propiedades de linealidad y prohibiciones absolutas

* **Integral de una suma o resta:** $\displaystyle \int [f(x) \pm g(x)]\,dx = \int f(x)\,dx \pm \int g(x)\,dx$.
* **Sacar constantes multiplicativas:** $\displaystyle \int k \cdot f(x)\,dx = k \cdot \int f(x)\,dx \quad (k \in \mathbb{R})$.

**Prohibiciones absolutas al integrar:**
* ❌ **NO existe regla del producto:** $\int f(x)\cdot g(x)\,dx \neq \left(\int f(x)\,dx\right)\cdot\left(\int g(x)\,dx\right)$.
* ❌ **NO existe regla del cociente:** $\int \frac{f(x)}{g(x)}\,dx \neq \frac{\int f(x)\,dx}{\int g(x)\,dx}$.
* ❌ **NUNCA saques la variable $x$ fuera de la integral:** solo pueden entrar y salir números constantes.

### 1.3. Tabla Maestra de Integrales Inmediatas y Casi Inmediatas

| Tipo | Forma Simple (con $x$) | Forma Compuesta (con $u = u(x)$) |
| :--- | :--- | :--- |
| **Constante** | $\int k\,dx = kx + C$ | $\int k\,u'\,dx = k\,u + C$ |
| **Potencia ($n \neq -1$)** | $\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$ | $\int u^n \cdot u'\,dx = \frac{u^{n+1}}{n+1} + C$ |
| **Logarítmica ($n = -1$)** | $\int \frac{1}{x}\,dx = \ln\lvert x\rvert + C$ | $\int \frac{u'}{u}\,dx = \ln\lvert u\rvert + C$ |
| **Exponencial base $e$** | $\int e^x\,dx = e^x + C$ | $\int e^u \cdot u'\,dx = e^u + C$ |
| **Exponencial base $a$** | $\int a^x\,dx = \frac{a^x}{\ln a} + C \;\;(a>0, a\neq 1)$ | $\int a^u \cdot u'\,dx = \frac{a^u}{\ln a} + C$ |
| **Seno** | $\int \sin x\,dx = -\cos x + C$ | $\int \sin(u)\cdot u'\,dx = -\cos(u) + C$ |
| **Coseno** | $\int \cos x\,dx = \sin x + C$ | $\int \cos(u)\cdot u'\,dx = \sin(u) + C$ |
| **Tangente** | $\int \tan x\,dx = -\ln\lvert\cos x\rvert + C$ | $\int \tan(u)\cdot u'\,dx = -\ln\lvert\cos u\rvert + C$ |
| **Cotangente** | $\int \cot x\,dx = \ln\lvert\sin x\rvert + C$ | $\int \cot(u)\cdot u'\,dx = \ln\lvert\sin u\rvert + C$ |
| **Secante cuadrado** | $\int \frac{dx}{\cos^2 x} = \int (1+\tan^2 x)\,dx = \tan x + C$ | $\int \frac{u'}{\cos^2 u}\,dx = \tan u + C$ |
| **Cosecante cuadrado** | $\int \frac{dx}{\sin^2 x} = \int (1+\cot^2 x)\,dx = -\cot x + C$ | $\int \frac{u'}{\sin^2 u}\,dx = -\cot u + C$ |
| **Arcoseno** | $\int \frac{dx}{\sqrt{1-x^2}} = \arcsin x + C$ | $\int \frac{u'}{\sqrt{a^2 - u^2}}\,dx = \arcsin\left(\frac{u}{a}\right) + C$ |
| **Arcotangente** | $\int \frac{dx}{1+x^2} = \arctan x + C$ | $\int \frac{u'}{a^2 + u^2}\,dx = \frac{1}{a}\arctan\left(\frac{u}{a}\right) + C$ |
| **Hiperbólicas (extra)** | $\int \sinh x\,dx = \cosh x + C$ | $\int \cosh x\,dx = \sinh x + C$ |

> **Trucos clave:**
> * El valor absoluto en $\ln|x|$ es obligatorio porque el dominio de $\frac{1}{x}$ incluye negativos y $(\ln|x|)' = \frac{1}{x}$ para todo $x \neq 0$.
> * Antes de integrar raíces o potencias en el denominador, pásalo todo a potencia: $\sqrt[n]{x^m} = x^{m/n}$ y $\frac{1}{x^k} = x^{-k}$.

### 1.4. Ejemplos Resueltos — Bloque 1: Inmediatas y Manipulación Algebraica Previa

1. **Polinomio directo:** $\int (5x^4 - 3x^2 + 6x - 7)\,dx = 5\frac{x^5}{5} - 3\frac{x^3}{3} + 6\frac{x^2}{2} - 7x + C = \mathbf{x^5 - x^3 + 3x^2 - 7x + C}$.
2. **Producto de polinomios (desarrollar antes):**
   $$\int (x - 1)(2x + 3)\,dx = \int (2x^2 + x - 3)\,dx = \mathbf{\frac{2}{3}x^3 + \frac{1}{2}x^2 - 3x + C}$$
3. **Potencias negativas y fraccionarias:**
   $$\int \left(\frac{3}{x^4} - 4\sqrt{x} + \frac{5}{\sqrt[3]{x}}\right)\,dx = \int \left(3x^{-4} - 4x^{1/2} + 5x^{-1/3}\right)\,dx = \mathbf{-\frac{1}{x^3} - \frac{8}{3}\sqrt{x^3} + \frac{15}{2}\sqrt[3]{x^2} + C}$$
4. **Cociente entre raíz y potencia:**
   $$\int \frac{\sqrt[3]{x}}{x^2}\,dx = \int x^{\frac{1}{3} - 2}\,dx = \int x^{-5/3}\,dx = \frac{x^{-2/3}}{-2/3} + C = \mathbf{-\frac{3}{2\sqrt[3]{x^2}} + C}$$
5. **División término a término por un monomio:**
   $$\int \frac{2x^3 - 5x + \sqrt{x}}{x^2}\,dx = \int \left(2x - \frac{5}{x} + x^{-3/2}\right)\,dx = \mathbf{x^2 - 5\ln|x| - \frac{2}{\sqrt{x}} + C}$$
6. **Binomio al cuadrado partido de raíz:**
   $$\int \frac{(\sqrt{x} - 3)^2}{\sqrt{x}}\,dx = \int \frac{x - 6\sqrt{x} + 9}{\sqrt{x}}\,dx = \int \left(x^{1/2} - 6 + 9x^{-1/2}\right)\,dx = \mathbf{\frac{2}{3}x^{3/2} - 6x + 18\sqrt{x} + C}$$
7. **Truco de sumar y restar en el numerador:**
   * **a)** $\int \frac{x}{x + 1}\,dx = \int \frac{x + 1 - 1}{x + 1}\,dx = \int \left(1 - \frac{1}{x+1}\right)\,dx = \mathbf{x - \ln|x + 1| + C}$.
   * **b)** $\int \frac{x^2}{x^2 + 1}\,dx = \int \frac{x^2 + 1 - 1}{x^2 + 1}\,dx = \int \left(1 - \frac{1}{x^2+1}\right)\,dx = \mathbf{x - \arctan x + C}$.
8. **Producto de exponenciales con igual exponente:**
   $$\int 2^x \cdot 3^x\,dx = \int 6^x\,dx = \mathbf{\frac{6^x}{\ln 6} + C}$$
9. **Cociente de exponenciales reducible:**
   $$\int \frac{e^{2x} - 3e^x + 1}{e^x}\,dx = \int \left(e^x - 3 + e^{-x}\right)\,dx = \mathbf{e^x - 3x - e^{-x} + C}$$
10. **Combinación lineal de trigonométricas inmediatas:**
    $$\int \left(3\sin x - 4\cos x + \frac{2}{\cos^2 x}\right)\,dx = \mathbf{-3\cos x - 4\sin x + 2\tan x + C}$$
11. **Integral de $\tan^2 x$ mediante identidad pitagórica:**
    $$\int \tan^2 x\,dx = \int \left(\frac{1}{\cos^2 x} - 1\right)\,dx = \mathbf{\tan x - x + C}$$
12. **Cálculo de la constante $C$ (Problema de valor inicial):**  
    Halla la primitiva $F(x)$ de $f(x) = 3x^2 - \frac{2}{x} + e^x$ que pasa por $P(1, e)$:
    * $F(x) = x^3 - 2\ln|x| + e^x + C$.
    * $F(1) = 1 - 0 + e + C = e \implies C = -1 \implies \mathbf{F(x) = x^3 - 2\ln|x| + e^x - 1}$.

---

## 2. Integrales Casi Inmediatas (Regla de la Cadena Inversa)

### 2.1. ¿Cómo se reconocen y cómo se resuelven?

Una integral es **casi inmediata** cuando aparece una función compuesta $f(u(x))$ multiplicada por una expresión que coincide con $u'(x)$, **salvo por una constante multiplicativa $k \neq 0$**:

1. Identifica la función interna $u(x)$.
2. Calcula su derivada $u'(x)$.
3. Multiplica dentro de la integral por la constante $k$ que falta y divide fuera por $\frac{1}{k}$ (nunca variables con $x$).
4. Aplica la tabla compuesta.

### 2.2. Ejemplos Resueltos — Bloque 2: Ajuste de Constantes

#### Subtipo 2.1: Potencias y Raíces Compuestas $\int u^n \cdot u'\,dx$
* **Ejemplo 2.1:** $\int x^2(x^3+5)^7\,dx = \frac{1}{3}\int 3x^2(x^3+5)^7\,dx = \mathbf{\frac{(x^3+5)^8}{24} + C}$
* **Ejemplo 2.2:** $\int \frac{x}{(3x^2+5)^4}\,dx = \frac{1}{6}\int 6x(3x^2+5)^{-4}\,dx = \mathbf{-\frac{1}{18(3x^2+5)^3} + C}$
* **Ejemplo 2.3:** $\int x\sqrt{1-x^2}\,dx = -\frac{1}{2}\int (-2x)(1-x^2)^{1/2}\,dx = \mathbf{-\frac{1}{3}\sqrt{(1-x^2)^3} + C}$
* **Ejemplo 2.4:** $\int \frac{\ln x}{x}\,dx = \int (\ln x)^1 \cdot \frac{1}{x}\,dx = \mathbf{\frac{(\ln x)^2}{2} + C}$
* **Ejemplo 2.5:** $\int \sin^3 x \cos x\,dx = \int (\sin x)^3 \cos x\,dx = \mathbf{\frac{\sin^4 x}{4} + C}$

#### Subtipo 2.2: Tipo Logaritmo Neperiano $\int \frac{u'}{u}\,dx$
* **Ejemplo 2.6:** $\int \frac{1}{3-2x}\,dx = -\frac{1}{2}\int \frac{-2}{3-2x}\,dx = \mathbf{-\frac{1}{2}\ln|3-2x| + C}$
* **Ejemplo 2.7:** $\int \frac{1}{x\ln x}\,dx = \int \frac{1/x}{\ln x}\,dx = \mathbf{\ln|\ln x| + C}$
* **Ejemplo 2.8:** $\int \frac{\sin x - \cos x}{\sin x + \cos x}\,dx = -\int \frac{\cos x - \sin x}{\sin x + \cos x}\,dx = \mathbf{-\ln|\sin x + \cos x| + C}$
* **Ejemplo 2.9:** $\int \frac{\sin(2x-1)}{\cos(2x-1)+3}\,dx = -\frac{1}{2}\int \frac{-2\sin(2x-1)}{\cos(2x-1)+3}\,dx = \mathbf{-\frac{1}{2}\ln|\cos(2x-1)+3| + C}$
* **Ejemplo 2.10:** $\int \frac{e^{3x}-e^{-3x}}{e^{3x}+e^{-3x}}\,dx = \frac{1}{3}\int \frac{3(e^{3x}-e^{-3x})}{e^{3x}+e^{-3x}}\,dx = \mathbf{\frac{1}{3}\ln(e^{3x}+e^{-3x}) + C}$

#### Subtipo 2.3: Exponenciales y Trigonométricas Compuestas
* **Ejemplo 2.11:** $\int x^3\cos(x^4-3)\,dx = \frac{1}{4}\int 4x^3\cos(x^4-3)\,dx = \mathbf{\frac{1}{4}\sin(x^4-3) + C}$
* **Ejemplo 2.12:** $\int \frac{\sin(\sqrt{x})}{\sqrt{x}}\,dx = 2\int \sin(\sqrt{x})\frac{1}{2\sqrt{x}}\,dx = \mathbf{-2\cos(\sqrt{x}) + C}$
* **Ejemplo 2.13:** $\int \frac{e^{\arctan x}}{1+x^2}\,dx = \mathbf{e^{\arctan x} + C}$

#### Subtipo 2.4: Arcotangente y Arcoseno Camuflados
* **Ejemplo 2.14:** $\int \frac{e^x}{1+e^{2x}}\,dx = \int \frac{e^x}{1+(e^x)^2}\,dx = \mathbf{\arctan(e^x) + C}$
* **Ejemplo 2.15:** $\int \frac{x}{1+x^4}\,dx = \frac{1}{2}\int \frac{2x}{1+(x^2)^2}\,dx = \mathbf{\frac{1}{2}\arctan(x^2) + C}$
* **Ejemplo 2.16:** $\int \frac{1}{\sqrt{9-4x^2}}\,dx = \frac{1}{2}\int \frac{2}{\sqrt{3^2-(2x)^2}}\,dx = \mathbf{\frac{1}{2}\arcsin\left(\frac{2x}{3}\right) + C}$

---

## 3. Integración por Cambio de Variable (Sustitución)

### 3.1. ¿Cuándo se usa y cómo elegir el cambio?

Se usa cuando sobran o faltan potencias de $x$, aparecen raíces molestas o de distinto índice, exponenciales en un denominador o radicales cuadráticos $\sqrt{a^2 \pm x^2}$.

1. **Elige el cambio** $t = g(x)$ (o $x = \varphi(t)$).
2. **Calcula el diferencial** $\mathrm{d}t = g'(x)\,\mathrm{d}x$ y despeja $\mathrm{d}x$ (y $x$ si queda alguna suelta).
3. **Sustituye todo** en $t$ (prohibido mezclar $x$ y $t$).
4. **Integra respecto a $t$ y deshaz el cambio** volviendo a $x$.

| Patrón en el integrando | Cambio recomendado | Motivo / Ventaja |
| :--- | :--- | :--- |
| Potencia o raíz lineal: $(ax+b)^n$, $\sqrt[n]{ax+b}$ | $t = ax+b$ ó $t^n = ax+b$ | Libera la $x$ suelta o elimina la raíz. |
| Varias raíces de $x$: $\sqrt[p]{x}$, $\sqrt[q]{x}$ | $x = t^m$, con $m = \mathrm{m.c.m.}(p,q)$ | Convierte en fracción polinómica. |
| Exponenciales sin $u'$ arriba: $R(e^x)$ | $t = e^x \implies \mathrm{d}x = \frac{\mathrm{d}t}{t}$ | Convierte en integral racional. |
| Radical $\sqrt{a^2 - x^2}$ | $x = a\sin t$ | $\sqrt{a^2 - a^2\sin^2 t} = a\cos t$. |
| Radical / suma $\sqrt{a^2 + x^2}$ o $(x^2+a^2)^k$ | $x = a\tan t$ | $a^2 + a^2\tan^2 t = a^2\sec^2 t$. |
| Radical $\sqrt{x^2 - a^2}$ | $x = a\sec t$ | $\sqrt{a^2\sec^2 t - a^2} = a\tan t$. |

### 3.2. Ejemplos Resueltos — Bloque 3

* **Ejemplo 3.1:** $\int x(x+2)^8\,dx$ ($t = x+2 \implies x = t-2$) $= \int (t^9-2t^8)\,dt = \mathbf{\frac{(x+2)^{10}}{10} - \frac{2(x+2)^9}{9} + C}$.
* **Ejemplo 3.2:** $\int x\sqrt{x+1}\,dx$ ($t = \sqrt{x+1} \implies x = t^2-1,\; dx = 2t\,dt$) $= 2\int (t^4-t^2)\,dt = \mathbf{\frac{2}{5}(x+1)^{5/2} - \frac{2}{3}(x+1)^{3/2} + C}$.
* **Ejemplo 3.3:** $\int \frac{1}{1+\sqrt{x}}\,dx$ ($t = \sqrt{x} \implies x = t^2,\; dx = 2t\,dt$) $= 2\int \frac{t}{t+1}\,dt = \mathbf{2\sqrt{x} - 2\ln(1+\sqrt{x}) + C}$.
* **Ejemplo 3.4:** $\int \frac{dx}{\sqrt{x}+\sqrt[3]{x}}$ ($x = t^6 \implies dx = 6t^5\,dt$) $= 6\int \frac{t^3}{t+1}\,dt = \mathbf{2\sqrt{x} - 3\sqrt[3]{x} + 6\sqrt[6]{x} - 6\ln(1+\sqrt[6]{x}) + C}$.
* **Ejemplo 3.5:** $\int \frac{1}{e^x+1}\,dx$ ($t = e^x \implies dx = dt/t$) $= \int \frac{dt}{t(t+1)} = \mathbf{x - \ln(e^x+1) + C}$.
* **Ejemplo 3.6:** $\int \frac{e^{2x}}{\sqrt{e^x+1}}\,dx$ ($t = \sqrt{e^x+1} \implies e^x = t^2-1,\; 2t\,dt = e^x\,dx$) $= 2\int (t^2-1)\,dt = \mathbf{\frac{2}{3}(e^x+1)^{3/2} - 2\sqrt{e^x+1} + C}$.
* **Ejemplo 3.7:** $\int \frac{dx}{x\sqrt{1+\ln x}}$ ($t = \sqrt{1+\ln x} \implies 2t\,dt = dx/x$) $= \int 2\,dt = \mathbf{2\sqrt{1+\ln x} + C}$.
* **Ejemplo 3.8:** $\int \frac{\cos x}{1+\sin^2 x}\,dx$ ($t = \sin x$) $= \int \frac{dt}{1+t^2} = \mathbf{\arctan(\sin x) + C}$.
* **Ejemplo 3.9:** $\int \sqrt{4-x^2}\,dx$ ($x = 2\sin t$) $= 4\int \cos^2 t\,dt = 2t + \sin(2t) + C = \mathbf{2\arcsin(x/2) + \frac{x\sqrt{4-x^2}}{2} + C}$.
* **Ejemplo 3.10:** $\int \frac{dx}{(x^2+1)^{3/2}}$ ($x = \tan t$) $= \int \cos t\,dt = \sin t + C = \mathbf{\frac{x}{\sqrt{x^2+1}} + C}$.
* **Ejemplo 3.11:** $\int \frac{\sqrt{x^2-9}}{x}\,dx$ ($x = 3\sec t$, $x>3$) $= 3\int \tan^2 t\,dt = \mathbf{\sqrt{x^2-9} - 3\arccos(3/x) + C}$.

---

## 4. Integración por Partes

### 4.1. Fórmula y Regla ALPES

$$\int u\,\mathrm{d}v = u\cdot v - \int v\,\mathrm{d}u$$

Prioridad para elegir $u$ (**ALPES**): **A**rcos $>$ **L**ogaritmos $>$ **P**olinomios $>$ **E**xponenciales $>$ **S**eno/Coseno.

### 4.2. Ejemplos Resueltos — Bloque 4

* **Ejemplo 4.1 (Básica):** $\int x e^x\,dx$ ($u=x,\, dv=e^x\,dx$) $= \mathbf{(x-1)e^x + C}$.
* **Ejemplo 4.2 (Polinomio $\times$ Trig.):** $\int (x-2)\sin x\,dx = \mathbf{-(x-2)\cos x + \sin x + C}$.
* **Ejemplo 4.3 (Reiterada / Tabular):** $\int (x^2+1)\sin(2x)\,dx = \mathbf{-\frac{x^2+1}{2}\cos(2x) + \frac{x}{2}\sin(2x) + \frac{1}{4}\cos(2x) + C}$.
* **Ejemplo 4.4 (Polinomio $\times$ Log.):** $\int x^2\ln x\,dx$ ($u=\ln x,\, dv=x^2\,dx$) $= \mathbf{\frac{x^3}{3}\ln x - \frac{x^3}{9} + C}$.
* **Ejemplo 4.5 (Cociente con log.):** $\int \frac{\ln x}{x^2}\,dx = \mathbf{-\frac{\ln x}{x} - \frac{1}{x} + C}$.
* **Ejemplo 4.6 (Función sola):** $\int \ln x\,dx$ ($u=\ln x,\, dv=1\,dx$) $= \mathbf{x\ln x - x + C}$.
* **Ejemplo 4.7 (Función sola):** $\int \arctan x\,dx = \mathbf{x\arctan x - \frac{1}{2}\ln(1+x^2) + C}$.
* **Ejemplo 4.8 (Función sola):** $\int \arcsin x\,dx = \mathbf{x\arcsin x + \sqrt{1-x^2} + C}$.
* **Ejemplo 4.9 (Cíclica):** $\int e^x\cos(2x)\,dx = \mathbf{\frac{e^x}{5}(\cos(2x)+2\sin(2x)) + C}$.
* **Ejemplo 4.10 (Cíclica de examen):** $\int \cos(\ln x)\,dx = \mathbf{\frac{x}{2}(\cos(\ln x)+\sin(\ln x)) + C}$.

> **Regla en cíclicas:** mantén siempre el mismo orden de elección para $u$ y $dv$ en ambas vueltas; si lo inviertes en la segunda aplicación obtendrás $I = I$.

---

## 5. Integrales Racionales $\int \frac{P(x)}{Q(x)}\,dx$

### 5.1. Algoritmo maestro de resolución

1. **Paso 0 (División previa):** si $\deg(P) \ge \deg(Q)$, divide $P(x) = Q(x)C(x) + R(x)$ para escribir $\frac{P}{Q} = C(x) + \frac{R(x)}{Q(x)}$.
2. **Paso 1 (Cuadrática irreducible $\Delta < 0$):** método directo **Neperiano + Arcotangente** (separar $u'$ arriba y completar cuadrados abajo).
3. **Paso 2 (Fracciones simples):**
   * Raíz real simple $(x-r)$: $\frac{A}{x-r}$.
   * Raíz real múltiple $(x-r)^k$: $\frac{B_1}{x-r} + \frac{B_2}{(x-r)^2} + \dots + \frac{B_k}{(x-r)^k}$.
   * Cuadrático irreducible $(ax^2+bx+c)$: $\frac{Mx+N}{ax^2+bx+c}$.

### 5.2. Ejemplos Resueltos — Bloque 5

* **Ejemplo 5.1 (División previa):** $\int \frac{x^3-3x^2+2x-1}{x-2}\,dx = \int \left(x^2-x-\frac{1}{x-2}\right)dx = \mathbf{\frac{x^3}{3}-\frac{x^2}{2}-\ln|x-2| + C}$.
* **Ejemplo 5.2 (Igual grado + simples):** $\int \frac{x^2+1}{x^2-1}\,dx = \int \left(1 + \frac{1}{x-1} - \frac{1}{x+1}\right)dx = \mathbf{x + \ln\left|\frac{x-1}{x+1}\right| + C}$.
* **Ejemplo 5.3 (2 raíces simples):** $\int \frac{2x+18}{x^2+2x-3}\,dx = \int \left(\frac{5}{x-1} - \frac{3}{x+3}\right)dx = \mathbf{5\ln|x-1| - 3\ln|x+3| + C}$.
* **Ejemplo 5.4 (3 raíces simples):** $\int \frac{x+5}{x^3-x}\,dx = \int \left(-\frac{5}{x} + \frac{3}{x-1} + \frac{2}{x+1}\right)dx = \mathbf{-5\ln|x| + 3\ln|x-1| + 2\ln|x+1| + C}$.
* **Ejemplo 5.5 (Raíz doble + simple):** $\int \frac{5x+1}{(x-1)^2(x+2)}\,dx = \int \left(\frac{1}{x-1} + \frac{2}{(x-1)^2} - \frac{1}{x+2}\right)dx = \mathbf{\ln|x-1| - \frac{2}{x-1} - \ln|x+2| + C}$.
* **Ejemplo 5.6 (Raíz triple):** $\int \frac{x^2+1}{(x-1)^3}\,dx = \int \left(\frac{1}{x-1} + \frac{2}{(x-1)^2} + \frac{2}{(x-1)^3}\right)dx = \mathbf{\ln|x-1| - \frac{2}{x-1} - \frac{1}{(x-1)^2} + C}$.
* **Ejemplo 5.7 (Irreducible con constante arriba):**
  * **a)** $\int \frac{1}{x^2+2x+5}\,dx = \int \frac{1}{(x+1)^2+2^2}\,dx = \mathbf{\frac{1}{2}\arctan\left(\frac{x+1}{2}\right) + C}$.
  * **b)** $\int \frac{1}{4x^2+4x+5}\,dx = \frac{1}{2}\int \frac{2}{(2x+1)^2+2^2}\,dx = \mathbf{\frac{1}{4}\arctan\left(\frac{2x+1}{2}\right) + C}$.
* **Ejemplo 5.8 (Neperiano + Arcotangente):** $\int \frac{4x+7}{x^2+2x+5}\,dx = 2\int \frac{2x+2}{x^2+2x+5}\,dx + 3\int \frac{1}{(x+1)^2+4}\,dx = \mathbf{2\ln(x^2+2x+5) + \frac{3}{2}\arctan\left(\frac{x+1}{2}\right) + C}$.
* **Ejemplo 5.9 (Mixto real + irreducible):** $\int \frac{3x^2+2x}{(x-1)(x^2+4)}\,dx = \int \left(\frac{1}{x-1} + \frac{2x+4}{x^2+4}\right)dx = \mathbf{\ln|x-1| + \ln(x^2+4) + 2\arctan(x/2) + C}$.
* **Ejemplo 5.10 (Síntesis completa):** $\int \frac{x^3+2x-3}{x^2-x-2}\,dx = \int \left(x+1 + \frac{3}{x-2} + \frac{2}{x+1}\right)dx = \mathbf{\frac{x^2}{2} + x + 3\ln|x-2| + 2\ln|x+1| + C}$.

---

## 6. Integrales Trigonométricas

### 6.1. Identidades clave y árbol de decisión

* **Pitagórica:** $\sin^2 x + \cos^2 x = 1$ ; \quad $1 + \tan^2 x = \sec^2 x = \frac{1}{\cos^2 x}$.
* **Reducción de grado (exponentes pares):** $\sin^2 x = \frac{1 - \cos(2x)}{2}$, \quad $\cos^2 x = \frac{1 + \cos(2x)}{2}$.
* **Ángulo doble:** $\sin(2x) = 2\sin x \cos x$.
* **Producto a suma:** $\sin A\cos B = \frac{1}{2}[\sin(A+B)+\sin(A-B)]$, \quad $\cos A\cos B = \frac{1}{2}[\cos(A+B)+\cos(A-B)]$, \quad $\sin A\sin B = \frac{1}{2}[\cos(A-B)-\cos(A+B)]$.
* **Cambio universal ($t = \tan(x/2)$):** $\sin x = \frac{2t}{1+t^2}$, \quad $\cos x = \frac{1-t^2}{1+t^2}$, \quad $\mathrm{d}x = \frac{2\,\mathrm{d}t}{1+t^2}$.

### 6.2. Ejemplos Resueltos — Bloque 6

* **Ejemplo 6.1:** $\int \sin^3 x\,dx = \int (1-\cos^2 x)\sin x\,dx = \mathbf{-\cos x + \frac{\cos^3 x}{3} + C}$.
* **Ejemplo 6.2:** $\int \sin^2 x\cos^3 x\,dx = \int \sin^2 x(1-\sin^2 x)\cos x\,dx = \mathbf{\frac{\sin^3 x}{3} - \frac{\sin^5 x}{5} + C}$.
* **Ejemplo 6.3:** $\int \sin^2 x\,dx = \int \frac{1-\cos(2x)}{2}\,dx = \mathbf{\frac{x}{2} - \frac{\sin(2x)}{4} + C}$.
* **Ejemplo 6.4:** $\int \cos^4 x\,dx = \int \left(\frac{1+\cos(2x)}{2}\right)^2 dx = \mathbf{\frac{3x}{8} + \frac{\sin(2x)}{4} + \frac{\sin(4x)}{32} + C}$.
* **Ejemplo 6.5:** $\int \tan^3 x\,dx = \int \tan x(\sec^2 x - 1)\,dx = \mathbf{\frac{\tan^2 x}{2} + \ln|\cos x| + C}$.
* **Ejemplo 6.6:** $\int \frac{dx}{\cos^3 x} = \int \sec^3 x\,dx = \mathbf{\frac{1}{2}\sec x\tan x + \frac{1}{2}\ln|\sec x + \tan x| + C}$.
* **Ejemplo 6.7:** $\int \sin(3x)\cos x\,dx = \frac{1}{2}\int (\sin 4x + \sin 2x)\,dx = \mathbf{-\frac{\cos(4x)}{8} - \frac{\cos(2x)}{4} + C}$.
* **Ejemplo 6.8:**
  * **a)** $\int \frac{1}{1+\cos x}\,dx = \int \frac{1-\cos x}{\sin^2 x}\,dx = -\cot x + \frac{1}{\sin x} + C = \mathbf{\tan(x/2) + C}$.
  * **b)** $\int \frac{1}{2+\cos x}\,dx$ ($t=\tan(x/2)$) $= \int \frac{2\,dt}{t^2+3} = \mathbf{\frac{2}{\sqrt{3}}\arctan\left(\frac{\tan(x/2)}{\sqrt{3}}\right) + C}$.
  * **c)** $\int \frac{1}{\sin x}\,dx$ ($t=\tan(x/2)$) $= \int \frac{dt}{t} = \mathbf{\ln|\tan(x/2)| + C}$.

---

## 7. Integral Definida, Regla de Barrow y Teorema Fundamental

### 7.1. Propiedades y Teoremas Clave

* **Regla de Barrow:** $\displaystyle \int_a^b f(x)\,dx = [F(x)]_a^b = F(b) - F(a)$.
* **Simetría en $[-a, a]$:** si $f$ es par, $\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$; si $f$ es impar, $\int_{-a}^a f(x)\,dx = 0$.
* **Valor Medio Integral:** $\mu = \frac{1}{b-a}\int_a^b f(x)\,dx = f(c)$ para algún $c \in (a, b)$.
* **Teorema Fundamental (TFCI) + Regla de la Cadena:** $\displaystyle \frac{\mathrm{d}}{\mathrm{d}x}\left[\int_{h(x)}^{g(x)} f(t)\,\mathrm{d}t\right] = f(g(x))\cdot g'(x) - f(h(x))\cdot h'(x)$.

### 7.2. Ejemplos Resueltos — Bloque 7

* **Ejemplo 7.1:** $\int_2^3 \frac{x}{x^2-1}\,dx = \left[\frac{1}{2}\ln|x^2-1|\right]_2^3 = \mathbf{\frac{1}{2}\ln\left(\frac{8}{3}\right)}$.
* **Ejemplo 7.2:**
  * **a)** $\int_0^{\pi/2} \cos x \cdot e^{\sin x}\,dx$ ($t = \sin x$, de $0$ a $1$) $= \int_0^1 e^t\,dt = \mathbf{e - 1}$.
  * **b)** $\int_0^3 x\sqrt{x+1}\,dx$ ($t = \sqrt{x+1}$, de $1$ a $2$) $= 2\int_1^2 (t^4-t^2)\,dt = \mathbf{\frac{116}{15}}$.
* **Ejemplo 7.3:** $\int_1^e x\ln x\,dx = \left[\frac{x^2}{2}\ln x - \frac{x^2}{4}\right]_1^e = \mathbf{\frac{e^2 + 1}{4}}$.
* **Ejemplo 7.4 (Simetría):** $\int_{-2}^2 (x^5\cos x + 3x^2 - 1)\,dx = 0 + 2\int_0^2 (3x^2 - 1)\,dx = \mathbf{12}$.
* **Ejemplo 7.5 (Valor absoluto):** $\int_{-1}^3 |x^2 - 1|\,dx = \int_{-1}^1 (1-x^2)\,dx + \int_1^3 (x^2-1)\,dx = \frac{4}{3} + \frac{20}{3} = \mathbf{8}$.
* **Ejemplo 7.6 (TFCI y L'Hôpital):**
  * **a)** $F(x) = \int_x^{x^2} e^{-t^2}\,dt \implies \mathbf{F'(x) = 2x\,e^{-x^4} - e^{-x^2}}$.
  * **b)** $\lim_{x\to 0} \frac{\int_0^x \sin(t^2)\,dt}{x^3} \stackrel{\text{L'Hôp}}{=} \lim_{x\to 0} \frac{\sin(x^2)}{3x^2} = \mathbf{\frac{1}{3}}$.
* **Ejemplo 7.7 (Valor Medio):** para $f(x)=x^2$ en $[0,3]$, $\mu = \frac{1}{3}\int_0^3 x^2\,dx = \mathbf{3}$, alcanzado en $\mathbf{c = \sqrt{3}}$.

---

## 8. Aplicaciones Geométricas: Cálculo de Áreas y Volúmenes

### 8.1. Fórmulas fundamentales

* **Área con eje $X$ en $[a,b]$:** hallar cortes $f(x)=0$ dentro de $(a,b)$ y sumar $\left|\int_{x_i}^{x_{i+1}} f(x)\,dx\right|$.
* **Área entre dos curvas:** hallar cortes $f(x)=g(x)$ ordenados y sumar $\left|\int_{x_i}^{x_{i+1}} (f(x)-g(x))\,dx\right|$.
* **Volumen de revolución (giro alrededor de $X$):** $V = \pi \int_a^b [f(x)]^2\,dx$ (una curva); $V = \pi \int_a^b ([f_{\text{ext}}(x)]^2 - [f_{\text{int}}(x)]^2)\,dx$ (arandela).

### 8.2. Ejemplos Resueltos — Bloque 8

* **Ejemplo 8.1:** Área entre $f(x)=x^3+x^2$ y $g(x)=2x$ (cortes $x=-2,0,1$): $\left|\int_{-2}^0 (x^3+x^2-2x)\,dx\right| + \left|\int_0^1 (x^3+x^2-2x)\,dx\right| = \frac{8}{3} + \frac{5}{12} = \mathbf{\frac{37}{12}\;\text{u}^2}$.
* **Ejemplo 8.2:** Área entre $f(x)=x^3+x^2-6$ y $g(x)=x^2+7x$ (cortes $x=-2,-1,3$): $\frac{3}{4} + 32 = \mathbf{\frac{131}{4}\;\text{u}^2}$.
* **Ejemplo 8.3:** Área entre $y=x^2$, su tangente en $x=2$ ($y=4x-4$) y el eje $X$: $\int_0^1 x^2\,dx + \int_1^2 (x^2-4x+4)\,dx = \frac{1}{3} + \frac{1}{3} = \mathbf{\frac{2}{3}\;\text{u}^2}$.
* **Ejemplo 8.4:** Área entre $y=e^x$, $y=e^{-x}$ y $x=1$ (corte $x=0$): $\int_0^1 (e^x - e^{-x})\,dx = \mathbf{e + \frac{1}{e} - 2\;\text{u}^2}$.
* **Ejemplo 8.5 (Parámetro):** $a > 0$ tal que el área entre $x^2$ y $ax$ sea $\frac{9}{2}$: $\frac{a^3}{6} = \frac{9}{2} \implies a^3 = 27 \implies \mathbf{a = 3}$.
* **Ejemplo 8.6 (Volúmenes):**
  * **a)** $f(x)=\sqrt{3x}$ en $[0,3]$: $V = \pi\int_0^3 3x\,dx = \mathbf{\frac{27\pi}{2}\;\text{u}^3}$.
  * **b)** $f(x)=\sin x$ en $[0,\pi]$: $V = \pi\int_0^\pi \sin^2 x\,dx = \mathbf{\frac{\pi^2}{2}\;\text{u}^3}$.
  * **c)** $f(x)=x e^x$ en $[0,1]$: $V = \pi\int_0^1 x^2 e^{2x}\,dx = \mathbf{\frac{\pi(e^2-1)}{4}\;\text{u}^3}$.
* **Ejemplo 8.7 (Arandela):** Región entre $y=\sqrt{x}$ e $y=x^2$ en $[0,1]$: $V = \pi\int_0^1 (x - x^4)\,dx = \mathbf{\frac{3\pi}{10}\;\text{u}^3}$.

---

## 9. Ampliación: Integrales Impropias Básicas

* **1ª especie:** $\int_a^{+\infty} f(x)\,dx = \lim_{b\to+\infty}\int_a^b f(x)\,dx$. ($\int_1^{+\infty} x^{-p}\,dx$ converge si $p>1$ y diverge si $p\le 1$).
* **2ª especie:** $\int_a^b f(x)\,dx = \lim_{\varepsilon\to 0^+}\int_{a+\varepsilon}^b f(x)\,dx$ si hay asíntota vertical en $x=a$.

**Ejemplos Resueltos:**
* **Ejemplo 9.1:** $\int_1^{+\infty} \frac{1}{x^2}\,dx = \lim_{b\to+\infty} (1 - \frac{1}{b}) = \mathbf{1}$ (converge).
* **Ejemplo 9.2:** $\int_1^{+\infty} \frac{1}{x}\,dx = \lim_{b\to+\infty} \ln b = \mathbf{+\infty}$ (diverge).
* **Ejemplo 9.3:** $\int_0^{+\infty} x e^{-x}\,dx = \lim_{b\to+\infty} [-(x+1)e^{-x}]_0^b = \mathbf{1}$ (converge, usando L'Hôpital).
* **Ejemplo 9.4:** $\int_0^1 \frac{1}{\sqrt{x}}\,dx = \lim_{\varepsilon\to 0^+} [2\sqrt{x}]_\varepsilon^1 = \mathbf{2}$ (converge).

---

## 10. Mapa Maestro de Decisión y los 10 Errores Letales

### 10.1. Árbol de decisión rápido

1. **¿Puedo simplificar algebraicamente?** (productos, raíces a potencias, dividir entre monomio) $\to$ Hazlo siempre primero.
2. **¿Está en la tabla o solo falta una constante $k$?** $\to$ Inmediata o casi inmediata (ajusta $k$ dentro y $1/k$ fuera).
3. **¿Cociente de polinomios $\frac{P(x)}{Q(x)}$?** $\to$ Si $\deg P \ge \deg Q$ divide primero; luego fracciones simples o método Neperiano + Arcotangente.
4. **¿Producto de familias distintas (ALPES) o $\ln/\arctan/\arcsin$ sola?** $\to$ Integración por partes (si es cíclica, 2 veces sin invertir el orden).
5. **¿Solo trigonométricas?** $\to$ Exponente impar: aparta 1 factor; pares: ángulo mitad; cocientes racionales: cambio universal $t=\tan(x/2)$.
6. **¿Raíces de distinto índice, $e^x$ mezclado o $\sqrt{a^2 \pm x^2}$?** $\to$ Cambio de variable.

### 10.2. Los 10 Errores Letales en Examen

1. Integrar un producto o cociente por separado.
2. Sacar variables $x$ fuera de la integral al ajustar $u'$.
3. Olvidar $+C$ o el diferencial $\mathrm{d}x$.
4. Confundir $\int x^{-2}\,dx$ con un logaritmo (solo da $\ln$ cuando el exponente en el denominador es $1$).
5. Olvidar dividir por el coeficiente interno ($a$ en $\sin(ax)$, $e^{ax}$, etc.).
6. No deshacer el cambio de variable en indefinidas.
7. Cambiar el orden $u \leftrightarrow \mathrm{d}v$ en el segundo paso de una integral cíclica.
8. Aplicar fracciones simples sin dividir previamente cuando $\deg P \ge \deg Q$.
9. Integrar áreas sin buscar primero los puntos de corte intermedios.
10. Olvidar $\pi$ o no elevar al cuadrado cada función por separado en volúmenes ($[f_{\text{ext}}]^2 - [f_{\text{int}}]^2$, nunca $[f-g]^2$).
