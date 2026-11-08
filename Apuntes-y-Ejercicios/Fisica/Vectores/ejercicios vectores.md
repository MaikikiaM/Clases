# Ejercicios de Refuerzo: Vectores (Física y Matemáticas)

---

## Boletín de Ejercicios (Enunciados)

### 1. Descomposición en una rampa y fuerza total (Hoja 1)
Tenemos un bloque apoyado en un plano inclinado. Su peso se descompone en dos fuerzas perpendiculares entre sí: una que tira hacia abajo por la rampa de $P_x = 12\text{ N}$ y otra que lo empuja contra la superficie de $P_y = 5\text{ N}$.
* **a)** Calcula la fuerza total del peso (su módulo $|\vec{P}|$) aplicando el teorema de Pitágoras.
* **b)** ¿Qué ángulo de inclinación $\theta$ forma el vector peso con la superficie de la rampa?

### 2. Moverse entre dos puntos y fuerza con dirección (Hojas 1 y 2)
Tiramos de un objeto con una fuerza constante de $50\text{ N}$ a lo largo de una guía que va desde el punto $A(1, 2)$ hasta el punto $B(5, 5)$ (coordenadas en metros).
* **a)** Saca el vector desplazamiento $\vec{AB}$ (extremo menos origen) y la distancia en línea recta recorrida ($|\vec{AB}|$).
* **b)** Encuentra el **vector unitario** $\vec{u}_{\vec{AB}}$ en esa dirección (es decir, el vector $\vec{AB}$ reducido a módulo 1: $\frac{\vec{AB}}{|\vec{AB}|}$).
* **c)** Escribe el vector fuerza $\vec{F}$ multiplicando esos $50\text{ N}$ por el vector unitario, tanto por componentes como con los versores $\vec{i}$ y $\vec{j}$.

### 3. ¿Qué hace que una base sea ortonormal? (Hoja 3)
En clase vimos que una base es **ortonormal** si cumple dos requisitos muy concretos: que los vectores sean **perpendiculares** entre sí (formen $90^\circ$) y que sean **unitarios** (midan 1).
Comprueba si los vectores $\vec{u} = \left(\frac{3}{5}, \, \frac{4}{5}\right)$ y $\vec{v} = \left(-\frac{4}{5}, \, \frac{3}{5}\right)$ forman una base ortonormal:
* **a)** Comprueba que ambos miden 1 calculando sus módulos $|\vec{u}|$ y $|\vec{v}|$.
* **b)** Comprueba que son perpendiculares haciendo su producto escalar ($\vec{u} \cdot \vec{v} = 0$).

### 4. Ángulo entre vectores y condición de perpendicularidad (Hoja 4)
Tenemos dos vectores en el plano: $\vec{u} = (4, 2)$ y $\vec{v} = (1, 3)$.
* **a)** Calcula su producto escalar multiplicando componente a componente ($u_x v_x + u_y v_y$).
* **b)** Saca los módulos de ambos vectores y averigua el ángulo $\alpha$ exacto que forman mediante $\cos\alpha = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}$.
* **c)** ¿Qué número debe valer $k$ para que el vector $\vec{w} = (k, -6)$ sea perpendicular a $\vec{u}$?

### 5. La sombra de una fuerza: Proyección sobre el movimiento (Hoja 4)
Arrastramos un trineo en horizontal sobre el suelo una distancia de $8\text{ metros}$ ($\vec{d} = (8, 0)$), tirando de él con una fuerza inclinada $\vec{F} = (6, 4)\text{ N}$.
* **a)** A partir del triángulo rectángulo y el coseno ($\cos\alpha = \frac{\text{sombra}}{|\vec{F}|}$), deduce por qué la longitud de la sombra (proyección escalar) se calcula como $\frac{\vec{F}\cdot\vec{d}}{|\vec{d}|}$.
* **b)** Calcula cuánto mide esa proyección escalar y escribe el **vector proyección** $\vec{\text{Proy}}_{\vec{d}}\vec{F}$.
* **c)** Explica por qué ese vector proyección da exactamente $(6, 0)\text{ N}$: ¿la parte vertical de $4\text{ N}$ ayuda a avanzar en horizontal?

### 6. Producto vectorial, área del paralelogramo y base canónica 3D (Hoja 5)
En el suelo (plano $XY$) tenemos dos vectores: $\vec{a} = 6\vec{i}$ y $\vec{b} = 2\vec{i} + 5\vec{j}$.
* **a)** Multiplica vectorialmente $\vec{w} = \vec{a} \times \vec{b}$ aplicando la propiedad distributiva término a término y usando las reglas de la base canónica ($\vec{i}\times\vec{i}=\vec{0}$ e $\vec{i}\times\vec{j}=\vec{k}$).
* **b)** Comprueba que el módulo del resultado coincide con el área del paralelogramo que forman ($\text{base} \times \text{altura}$). ¿Cuánto valdría el área del triángulo?
* **c)** Usando la regla de la mano derecha y la base 3D, simplifica: $\vec{k} \times \vec{j}$ y el producto mixto $(\vec{i} \times \vec{j}) \cdot \vec{k}$.

<div class="page-break"></div>

---

## Solucionario Detallado Paso a Paso (Página 1 de 2)

### Solución al Ejercicio 1 (Rampa y Pitágoras)
* **a) Módulo del peso:**
  Como las dos componentes forman los catetos de un triángulo rectángulo de $12\text{ N}$ y $5\text{ N}$:
  $$|\vec{P}| = \sqrt{P_x^2 + P_y^2} = \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13\text{ N}$$
* **b) Ángulo con la superficie:**
  La tangente del ángulo es cateto opuesto entre cateto contiguo:
  $$\tan\theta = \frac{P_y}{P_x} = \frac{5}{12} \implies \theta = \arctan\left(\frac{5}{12}\right) \approx 22.62^\circ$$

### Solución al Ejercicio 2 (Trayectoria y Fuerza Direccional)
* **a) Vector desplazamiento y distancia recorrida:**
  Restamos punto final menos punto inicial:
  $$\vec{AB} = (B_x - A_x, \, B_y - A_y) = (5 - 1, \, 5 - 2) = (4, \, 3)\text{ m}$$
  La distancia en línea recta es el módulo del vector:
  $$|\vec{AB}| = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\text{ m}$$
* **b) Vector unitario director:**
  Dividimos el vector entre su propia longitud para que mida exactamente $1$:
  $$\vec{u}_{\vec{AB}} = \frac{\vec{AB}}{|\vec{AB}|} = \left(\frac{4}{5}, \, \frac{3}{5}\right) = (0.8, \, 0.6)$$
* **c) Vector fuerza física:**
  Multiplicamos la magnitud ($50\text{ N}$) por el vector unitario que le da la orientación:
  $$\vec{F} = 50 \cdot (0.8, \, 0.6) = (40, \, 30)\text{ N} = 40\vec{i} + 30\vec{j}\text{ N}$$

### Solución al Ejercicio 3 (Base Ortonormal)
* **a) Comprobación de que son unitarios (miden 1):**
  $$|\vec{u}| = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2} = \sqrt{\frac{9+16}{25}} = \sqrt{\frac{25}{25}} = 1$$
  $$|\vec{v}| = \sqrt{\left(-\frac{4}{5}\right)^2 + \left(\frac{3}{5}\right)^2} = \sqrt{\frac{16+9}{25}} = \sqrt{\frac{25}{25}} = 1$$
  Ambos vectores tienen longitud $1$ (son unitarios).
* **b) Comprobación de que son perpendiculares (forman $90^\circ$):**
  Calculamos su producto escalar:
  $$\vec{u} \cdot \vec{v} = \left(\frac{3}{5}\right)\left(-\frac{4}{5}\right) + \left(\frac{4}{5}\right)\left(\frac{3}{5}\right) = -\frac{12}{25} + \frac{12}{25} = 0$$
  Al dar exactamente cero, los vectores son perpendiculares ($\vec{u} \perp \vec{v}$). Cumplen las dos condiciones, por lo que forman una base ortonormal.

### Solución al Ejercicio 4 (Ángulo y Perpendicularidad)
* **a) Producto escalar analítico:**
  $$\vec{u} \cdot \vec{v} = 4\cdot 1 + 2\cdot 3 = 4 + 6 = 10$$
* **b) Ángulo que forman:**
  Módulos: $|\vec{u}| = \sqrt{4^2 + 2^2} = \sqrt{20} = 2\sqrt{5}$; $|\vec{v}| = \sqrt{1^2 + 3^2} = \sqrt{10}$.
  $$\cos\alpha = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|} = \frac{10}{\sqrt{200}} = \frac{10}{10\sqrt{2}} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2} \implies \alpha = 45^\circ$$
* **c) Valor de $k$ para que $\vec{w}$ sea perpendicular a $\vec{u}$:**
  Dos vectores son perpendiculares si su producto escalar es cero:
  $$\vec{w} \cdot \vec{u} = 0 \implies k\cdot 4 + (-6)\cdot 2 = 0 \implies 4k - 12 = 0 \implies 4k = 12 \implies k = 3$$

<div class="page-break"></div>

---

## Solucionario Detallado Paso a Paso (Página 2 de 2)

### Solución al Ejercicio 5 (Sombra y Proyección)
* **a) Deducción de la longitud de la sombra (proyección escalar):**  
  En el triángulo rectángulo que forma la fuerza $\vec{F}$ con el suelo, el cateto contiguo es la sombra:
  $$\cos\alpha = \frac{\text{cateto contiguo}}{\text{hipotenusa}} = \frac{|\text{Proy}_{\vec{d}}\vec{F}|}{|\vec{F}|} \implies |\text{Proy}_{\vec{d}}\vec{F}| = |\vec{F}|\cos\alpha = \frac{|\vec{F}||\vec{d}|\cos\alpha}{|\vec{d}|} = \frac{\vec{F}\cdot\vec{d}}{|\vec{d}|}$$
* **b) Cálculo numérico:**
  * Producto escalar: $\vec{F}\cdot\vec{d} = 6\cdot 8 + 4\cdot 0 = 48$; módulo: $|\vec{d}| = \sqrt{8^2 + 0^2} = 8\text{ m}$.
  * **Proyección escalar (longitud de la sombra):** $|\text{Proy}_{\vec{d}}\vec{F}| = \dfrac{48}{8} = 6\text{ N}$.
  * **Vector proyección:** Le damos la dirección horizontal multiplicando por el unitario $\frac{\vec{d}}{|\vec{d}|}$:
    $$\vec{\text{Proy}}_{\vec{d}}\vec{F} = \left(\frac{\vec{F}\cdot\vec{d}}{|\vec{d}|^2}\right)\vec{d} = \frac{48}{64}(8, 0) = \frac{3}{4}(8, 0) = (6, 0) = 6\vec{i}\text{ N}$$
* **c) Significado físico:**  
  Como el desplazamiento es puramente horizontal sobre el eje $X$, la sombra de la fuerza es simplemente su componente horizontal ($F_x = 6\text{ N}$). La fuerza vertical ($F_y = 4\text{ N}$) tira hacia arriba formando $90^\circ$ con el suelo, por lo que no aporta nada al avance ni proyecta sombra en esa dirección.

### Solución al Ejercicio 6 (Producto Vectorial y Geometría)
* **a) Desarrollo distributivo:**
  Multiplicamos el término de fuera por cada término del paréntesis:
  $$\vec{w} = (6\vec{i}) \times (2\vec{i} + 5\vec{j}) = 12(\vec{i} \times \vec{i}) + 30(\vec{i} \times \vec{j})$$
  Aplicamos las reglas de la base canónica vistas en la pizarra:
  * $\vec{i} \times \vec{i} = \vec{0}$ (un vector por sí mismo siempre da cero).
  * $\vec{i} \times \vec{j} = \vec{k}$ (al girar de $X$ a $Y$, la mano derecha apunta a $+Z$).
  $$\vec{w} = 12(\vec{0}) + 30\vec{k} = 30\vec{k} = (0, 0, 30)$$
* **b) Área del paralelogramo y del triángulo:**
  * El módulo del vector resultante es $|\vec{w}| = 30$.
  * Geométricamente, la base en el eje $X$ mide $b = 6$ y la altura en el eje $Y$ mide $h = 5$:
    $$\text{Área del paralelogramo} = \text{base} \times \text{altura} = 6 \times 5 = 30\text{ u}^2$$
    ¡El módulo del producto vectorial coincide exactamente con el área del paralelogramo!
  * El triángulo ocupa justo la mitad del paralelogramo:
    $$\text{Área del triángulo} = \frac{30}{2} = 15\text{ u}^2$$
* **c) Operaciones de la base 3D:**
  * $\vec{k} \times \vec{j} = -\vec{i}$ *(porque al ir al revés del ciclo horario se invierte el signo por anticonmutatividad: si $\vec{j}\times\vec{k}=\vec{i}$, entonces $\vec{k}\times\vec{j}=-\vec{i}$)*.
  * $(\vec{i} \times \vec{j}) \cdot \vec{k} = \vec{k} \cdot \vec{k} = 1$ *(es el volumen del cubo unidad generado por los tres ejes coordenados)*.
