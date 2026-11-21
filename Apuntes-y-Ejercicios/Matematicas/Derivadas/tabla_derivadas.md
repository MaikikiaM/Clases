# Tabla Maestra de Derivadas y Reglas de Derivación

> Referencia rápida de derivadas simples y compuestas ($u = u(x)$), reglas operativas, derivación logarítmica y ejemplos resueltos.

---

## 1. Reglas Operativas (Álgebra de Derivadas)

* **Constante por función:** $(k\cdot f)' = k\cdot f'$
* **Suma y resta:** $(f \pm g)' = f' \pm g'$
* **Producto:** $(f \cdot g)' = f'\cdot g + f\cdot g'$
* **Producto triple:** $(fgh)' = f'gh + fg'h + fgh'$
* **Cociente:** $\displaystyle \left(\frac{f}{g}\right)' = \frac{f'\cdot g - f\cdot g'}{g^2}$
* **Regla de la Cadena:** $\big[f(u(x))\big]' = f'(u(x))\cdot u'(x)$

---

## 2. Tabla Completa de Derivadas

| Familia / Función | Forma Simple ($x$) | Forma Compuesta ($u = u(x)$) | Condición / Nota |
| :--- | :--- | :--- | :--- |
| **Constante** | $(k)' = 0$ | $(k)' = 0$ | $k \in \mathbb{R}$ |
| **Identidad / Lineal** | $(x)' = 1$ | $(ax + b)' = a$ | Pendiente constante |
| **Potencia** | $(x^n)' = n\,x^{n-1}$ | $(u^n)' = n\,u^{n-1}\cdot u'$ | Válida para todo $n \in \mathbb{R}$ |
| **Inversa ($n=-1$)** | $\left(\frac{1}{x}\right)' = -\frac{1}{x^2}$ | $\left(\frac{1}{u}\right)' = -\frac{u'}{u^2}$ | Más rápida que el cociente |
| **Raíz cuadrada** | $(\sqrt{x})' = \frac{1}{2\sqrt{x}}$ | $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$ | $u > 0$ |
| **Raíz $n$-ésima** | $(\sqrt[n]{x})' = \frac{1}{n\sqrt[n]{x^{n-1}}}$ | $(\sqrt[n]{u})' = \frac{u'}{n\sqrt[n]{u^{n-1}}}$ | Equivalente a derivar $u^{1/n}$ |
| **Exponencial base $e$** | $(e^x)' = e^x$ | $(e^u)' = e^u \cdot u'$ | $\ln e = 1$ |
| **Exponencial base $a$** | $(a^x)' = a^x \cdot \ln a$ | $(a^u)' = a^u \cdot \ln a \cdot u'$ | $a > 0,\; a \neq 1$ |
| **Logaritmo neperiano** | $(\ln x)' = \frac{1}{x}$ | $(\ln u)' = \frac{u'}{u}$ | $u > 0$ (también $\ln\lvert u\rvert$) |
| **Logaritmo base $a$** | $(\log_a x)' = \frac{1}{x\,\ln a}$ | $(\log_a u)' = \frac{u'}{u\,\ln a}$ | $a > 0,\; a \neq 1,\; u > 0$ |
| **Seno** | $(\sin x)' = \cos x$ | $(\sin u)' = \cos(u)\cdot u'$ | Radianes |
| **Coseno** | $(\cos x)' = -\sin x$ | $(\cos u)' = -\sin(u)\cdot u'$ | Cuidado con el signo $-$ |
| **Tangente** | $(\tan x)' = \frac{1}{\cos^2 x} = 1+\tan^2 x$ | $(\tan u)' = \frac{u'}{\cos^2 u} = (1+\tan^2 u)u'$ | $\cos u \neq 0$ |
| **Cotangente** | $(\cot x)' = -\frac{1}{\sin^2 x} = -(1+\cot^2 x)$ | $(\cot u)' = -\frac{u'}{\sin^2 u}$ | $\sin u \neq 0$ |
| **Secante** | $(\sec x)' = \sec x\tan x$ | $(\sec u)' = \sec u\tan u \cdot u'$ | $\sec u = \frac{1}{\cos u}$ |
| **Cosecante** | $(\csc x)' = -\csc x\cot x$ | $(\csc u)' = -\csc u\cot u \cdot u'$ | $\csc u = \frac{1}{\sin u}$ |
| **Arcoseno** | $(\arcsin x)' = \frac{1}{\sqrt{1-x^2}}$ | $(\arcsin u)' = \frac{u'}{\sqrt{1-u^2}}$ | $\lvert u\rvert < 1$ |
| **Arcocoseno** | $(\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$ | $(\arccos u)' = -\frac{u'}{\sqrt{1-u^2}}$ | $\lvert u\rvert < 1$ |
| **Arcotangente** | $(\arctan x)' = \frac{1}{1+x^2}$ | $(\arctan u)' = \frac{u'}{1+u^2}$ | Todo $u \in \mathbb{R}$ |
| **Arcocotangente** | $(\operatorname{arccot} x)' = -\frac{1}{1+x^2}$ | $(\operatorname{arccot} u)' = -\frac{u'}{1+u^2}$ | Todo $u \in \mathbb{R}$ |
| **Hiperbólicas (extra)** | $(\sinh x)' = \cosh x$, $(\cosh x)' = \sinh x$ | $(\sinh u)' = \cosh(u)u'$, $(\cosh u)' = \sinh(u)u'$ | $(\tanh u)' = \frac{u'}{\cosh^2 u}$ |

> **Por qué sale $\ln a$ en $a^x$ y $\log_a x$:**  
> Como $a^x = e^{x\ln a}$, al derivar por regla de la cadena queda $e^{x\ln a}\cdot \ln a = a^x \ln a$.  
> Como $\log_a x = \frac{\ln x}{\ln a}$, al derivar queda $\frac{1}{\ln a}\cdot\frac{1}{x} = \frac{1}{x\ln a}$.

---

## 3. Los 3 Casos Potenciales/Exponenciales y Derivación Logarítmica

1. **Base variable, exponente constante ($x^5$):** regla de la potencia $\to 5x^4$.
2. **Base constante, exponente variable ($5^x$):** regla exponencial $\to 5^x \ln 5$.
3. **Base variable y exponente variable ($y = f(x)^{g(x)}$):** **derivación logarítmica** (tomar $\ln y = g(x)\ln f(x)$, derivar $\frac{y'}{y} = g'\ln f + g\frac{f'}{f}$ y multiplicar por $y$):
   $$y' = f(x)^{g(x)} \cdot \left(g'(x)\ln f(x) + g(x)\frac{f'(x)}{f(x)}\right)$$

---

## 4. 10 Ejemplos Resueltos de Referencia Rápida

1. $y = 3^x + e^{4x-1} \implies \mathbf{y' = 3^x\ln 3 + 4e^{4x-1}}$
2. $y = 2^{x^2+3x} \implies \mathbf{y' = (2x+3)\cdot 2^{x^2+3x}\ln 2}$
3. $y = \log_5(3x^2-1) \implies \mathbf{y' = \frac{6x}{(3x^2-1)\ln 5}}$
4. $y = \frac{4}{x^3} - 2\sqrt{x} + \sqrt[3]{x^2} \implies \mathbf{y' = -\frac{12}{x^4} - \frac{1}{\sqrt{x}} + \frac{2}{3\sqrt[3]{x}}}$
5. $y = x^2 e^{-3x} \implies \mathbf{y' = (2x - 3x^2)e^{-3x}}$
6. $y = \frac{\ln x}{x^2} \implies \mathbf{y' = \frac{1 - 2\ln x}{x^3}}$
7. $y = \sin^3(2x) \implies \mathbf{y' = 6\sin^2(2x)\cos(2x)}$
8. $y = \arctan(e^x) \implies \mathbf{y' = \frac{e^x}{1 + e^{2x}}}$
9. $y = \ln\left(\frac{x^3}{\sqrt{x+1}}\right) = 3\ln x - \frac{1}{2}\ln(x+1) \implies \mathbf{y' = \frac{3}{x} - \frac{1}{2(x+1)}}$
10. $y = x^x \;(x>0) \implies \ln y = x\ln x \implies \mathbf{y' = x^x(\ln x + 1)}$
