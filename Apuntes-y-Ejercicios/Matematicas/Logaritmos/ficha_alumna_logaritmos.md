# FICHA DE REPASO RÁPIDO: LOGARITMOS SIN DRAMAS
> **Para tener a mano antes del examen:** Conceptos clave, propiedades, errores prohibidos y ejercicios modelo.

---

## 1. ¿QUÉ ES UN LOGARITMO EN ESPAÑOL CLARO?

Un logaritmo es simplemente una **pregunta sobre una potencia**:

$$\log_{\text{base}}(\text{resultado}) = \text{exponente} \iff \text{base}^{\text{exponente}} = \text{resultado}$$

> 💡 **La pregunta mágica que debes hacerte siempre:**  
> **"¿A qué número tengo que elevar la base para que me dé el número de dentro?"**
>
> - $\log_2(8) = 3$ $\longrightarrow$ porque $2^3 = 8$.
> - $\log_3(9) = 2$ $\longrightarrow$ porque $3^2 = 9$.
> - $\log_{10}(1000) = 3$ $\longrightarrow$ porque $10^3 = 1000$.

* **Si no ves ninguna base:** es en base 10 $\to \log(x) \equiv \log_{10}(x)$.
* **Si ves "$\ln$":** es el logaritmo neperiano (base $e \approx 2.718$). Las propiedades son exactamente las mismas.

---

## 2. REGLAS BÁSICAS Y CONDICIONES VITALES

1. $\log_b(1) = 0$ (cualquier número elevado a 0 vale 1).
2. $\log_b(b) = 1$ (cualquier número elevado a 1 es él mismo).
3. ⚠️ **¡PROHIBIDO!** No existen los logaritmos de números negativos ni de cero:
   $$\log(-5) \to \text{NO EXISTE} \qquad \log(0) \to \text{NO EXISTE}$$

---

## 3. LAS 4 PROPIEDADES DE ORO

| Operación dentro del logaritmo | ¿En qué se transforma fuera? | Ejemplo |
|:---|:---|:---|
| **Multiplicación:** $\log(A \cdot B)$ | **Suma:** $\log A + \log B$ | $\log(2x) = \log 2 + \log x$ |
| **División:** $\log\left(\frac{A}{B}\right)$ | **Resta:** $\log A - \log B$ | $\log\left(\frac{x}{3}\right) = \log x - \log 3$ |
| **Potencia:** $\log(A^n)$ | **Baja multiplicando:** $n \cdot \log A$ | $\log(x^4) = 4\log x$ |
| **Raíz:** $\log(\sqrt[n]{A})$ | **Fracción:** $\frac{1}{n}\log A$ | $\log(\sqrt{x}) = \frac{1}{2}\log x$ |
| **Potencia en la BASE:** $\log_{b^k}(A)$ | **Divide fuera:** $\frac{1}{k}\log_b(A)$ | $\log_{36}(6) = \log_{6^2}(6) = \frac{1}{2}\log_6(6) = \mathbf{\frac{1}{2}}$ |

---

## 3b. EL CASO DE NÚMEROS COMPUESTOS (EL CASO DEL 36)

En el examen te pedirán calcular logaritmos de números grandes sabiendo solo $\log 2 = a$ y $\log 3 = b$.
¿Cómo se hace con el **36**? ¡Descomponiendo en factores primos!

1. **Factoriza el número:** $36 = 2^2 \cdot 3^2$.
2. **Separa en sumas y baja los exponentes:**  
   $$\log(36) = \log(2^2 \cdot 3^2) = \log(2^2) + \log(3^2) = 2\log(2) + 2\log(3) = \mathbf{2a + 2b}$$
3. **El truco maestro del 5 que cae siempre:**  
   Como $5 = \frac{10}{2}$, su logaritmo es:  
   $$\log(5) = \log(10) - \log(2) = \mathbf{1 - a}$$
4. **Si hay decimales:** $0.36 = \frac{36}{100} \implies \log(0.36) = \log(36) - \log(100) = \mathbf{2a + 2b - 2}$.

---

## 4. ❌ LOS 3 ERRORES QUE SUSPENDEN (NO LO HAGAS NUNCA)

* ❌ **$\log(A + B) \neq \log A + \log B$**  
  *La suma dentro de un logaritmo NO se separa jamás. Se queda como está.*
* ❌ **$\frac{\log A}{\log B} \neq \log A - \log B$**  
  *Dividir dos logaritmos distintos no es restar sus argumentos.*
* ❌ **Olvidar comprobar las soluciones en una ecuación logarítmica.**  
  *Si una solución hace que algún argumento sea negativo o cero, ¡debes tacharla y descartarla!*

---

## 5. CÓMO RESOLVER UNA ECUACIÓN LOGARÍTMICA EN 3 PASOS

### Modelo clásico: $\log(x + 3) + \log(x - 1) = \log(5)$

* **Paso 1: Agrupar todo en un solo logaritmo por lado (usando las propiedades)**  
  La suma de la izquierda se convierte en producto:
  $$\log\big((x + 3)(x - 1)\big) = \log(5)$$

* **Paso 2: Quitar los logaritmos (igualar los argumentos)**  
  $$(x + 3)(x - 1) = 5$$
  $$x^2 + 2x - 3 = 5 \implies x^2 + 2x - 8 = 0$$

* **Paso 3: Resolver la ecuación y COMPROBAR soluciones**  
  Resolviendo la ecuación de segundo grado obtenemos:
  $$x = 2 \quad \text{y} \quad x = -4$$
  - **Comprobación $x = 2$:** $\log(2+3) = \log(5)$ y $\log(2-1) = \log(1)$. ¡Todo positivo! $\implies \mathbf{x = 2 \text{ es válida}}$.
  - **Comprobación $x = -4$:** $\log(-4+3) = \log(-1)$ ¡Error! No existe logaritmo de negativo $\implies \mathbf{x = -4 \text{ se descarta}}$.

---

## 5b. ECUACIONES CON VARIAS BASES Y DIFERENTES EXPONENTES

¿Qué pasa si te ponen bases distintas (2 y 3) con exponentes distintos ($x+2$ y $x-1$)?
> 💡 **La regla de oro:** Desglosa los exponentes usando $a^{x+n} = a^x \cdot a^n$ y $a^{x-n} = \frac{a^x}{a^n}$ para aislar las $x$ y multiplicar las bases.

**Ejemplo de examen:**  
$$2^{x+2} \cdot 3^{x-1} = 48$$
1. **Desglosa potencias:** $2^x \cdot 2^2 \cdot \frac{3^x}{3} = 48 \implies 4 \cdot 2^x \cdot \frac{3^x}{3} = 48$
2. **Junta los números y las bases:** $\frac{4}{3} \cdot (2 \cdot 3)^x = 48 \implies \frac{4}{3} \cdot 6^x = 48$
3. **Despeja el $6^x$:** $6^x = \frac{48 \cdot 3}{4} = 36$
4. **Relaciona con potencias:** $6^x = 6^2 \implies \mathbf{x = 2}$

---

## 5c. EXPONENTES POTENCIADOS (GRADO 2 Y TORRES DE POTENCIAS)

1. **No confundir nunca:**
   - Con paréntesis $(2^3)^2 = 2^6 = 64$ *(se multiplican)*.
   - Sin paréntesis $2^{3^2} = 2^9 = 512$ *(se eleva el de arriba: $3^2=9$)*.
2. **Con $x^2$ en el exponente:**  
   $$\mathbf{2^{x^2 + 1} \cdot 3^{x^2 - 1} = 24 \implies \frac{2}{3} \cdot 6^{x^2} = 24 \implies 6^{x^2} = 36 = 6^2 \implies x^2 = 2 \implies x = \pm\sqrt{2}}$$

---

## 6. BATERÍA DE ENTRENAMIENTO PARA EL EXAMEN

### Bloque A: Cálculo directo a mano (sin calculadora)
1. $\log_2(32) =$
2. $\log_5\left(\frac{1}{25}\right) =$
3. $\log_3(\sqrt{27}) =$
4. $\log(0.001) =$

### Bloque B: Comprimir en un único logaritmo
5. $3\log(x) + 2\log(y) =$
6. $2\log(a) - \frac{1}{2}\log(b) =$

### Bloque C: Ecuaciones de examen
7. $\log(x) + \log(x + 9) = 1$
8. $2\log(x) - \log(x + 24) = 0$
9. $2^x = 10$ *(despeja la $x$ con logaritmos)*
10. $2^{x+2} \cdot 3^{x-1} = 48$ *(desglosa potencias y junta bases)*
11. $2^{x^2 + 1} \cdot 3^{x^2 - 1} = 24$ *(exponentes con grado 2)*

---

## 7. SOLUCIONES PARA AUTOCORRECCIÓN
1. $\mathbf{5}$ (porque $2^5 = 32$)
2. $\mathbf{-2}$ (porque $5^{-2} = \frac{1}{25}$)
3. $\mathbf{\frac{3}{2}}$ (porque $\sqrt{27} = 3^{3/2}$)
4. $\mathbf{-3}$ (porque $10^{-3} = 0.001$)
5. $\mathbf{\log(x^3 \cdot y^2)}$
6. $\mathbf{\log\left(\frac{a^2}{\sqrt{b}}\right)}$
7. $\log(x(x+9)) = \log(10) \implies x^2+9x-10=0 \implies \mathbf{x=1}$ (se descarta $x=-10$).
8. $\log(x^2) = \log(x+24) \implies x^2-x-24 \implies$ la positiva válida es $\mathbf{x = \frac{1+\sqrt{97}}{2}} \approx 5.42$.
9. $\mathbf{x = \frac{\ln(10)}{\ln(2)}} \approx 3.32$
10. $\frac{4}{3} \cdot 6^x = 48 \implies 6^x = 36 \implies \mathbf{x = 2}$
11. $\frac{2}{3} \cdot 6^{x^2} = 24 \implies 6^{x^2} = 36 = 6^2 \implies x^2 = 2 \implies \mathbf{x = \pm\sqrt{2}}$
