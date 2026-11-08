# Resumen Completo: Teoría y Operaciones con Vectores

> **Documento de Referencia:** Apuntes manuscritos de vectores (Fundamentos, Álgebra, Producto Escalar, Producto Vectorial y Aplicaciones Físicas).

---

## 1. Fundamentos: Visión Estática vs. Visión Dinámica

| Enfoque | Descripción | Representación Matemática |
| :--- | :--- | :--- |
| **Visión Estática** | Puntos aislados en el espacio sin noción de cambio o dirección. | Coordenadas $(2\text{D}/3\text{D})$ en plano cartesiano: $P(x,y,z)$. |
| **Visión Dinámica / Cambio** | Se añade información: magnitud, línea de acción y sentido de desplazamiento. | **Vector** $\vec{v} = \vec{AB}$ desde origen $A$ hasta extremo $B$. |

### Definición Geométrica de un Vector ($\vec{v}$)
Un vector queda unívocamente determinado por tres elementos:
1. **Módulo ($|\vec{v}|$):** Longitud o magnitud del segmento orientado $|\vec{v}| = \overline{AB} \ge 0$.
2. **Dirección ($\text{Dir } \vec{v}$):** Línea recta soporte $r$ que une los puntos $A$ y $B$ (o cualquier recta paralela a ella).
3. **Sentido ($\text{Sentido } \vec{v}$):** Orientación indicada por la punta de flecha ($\exists$ un orden unívoco: $A \to B$).

* **Vector de Posición:** Parte del origen de coordenadas $O$ hacia un punto $P$ ($\vec{r} = \vec{OP}$). *Indica desde dónde se está observando y aporta dinamismo a la descripción física.*
* **Espacio Vectorial ($V$):** Estructura algebraica con operaciones definidas (interna y externa). Todo vector $\vec{v} \in V$ se representa como una combinación lineal (C.L.) de los vectores de una base elegida.

---

## 2. Álgebra Vectorial Básica y Clasificación de Bases

### A. Suma y Resta de Vectores ($\vec{a} \pm \vec{b}$)
* **Construcción geométrica:** Regla del triángulo o paralelogramo ($\vec{c} = \vec{a} + \vec{b}$; resta sumando el opuesto: $\vec{c}' = \vec{a} - \vec{b} = \vec{a} + (-\vec{b})$).
* **Operación interna ($V \times V \to V$):** La suma de dos vectores es otro vector.
* **Propiedades:**
  * **Conmutativa:** $(\vec{v} + \vec{w} = \vec{w} + \vec{v})$
  * **Asociativa:** $((\vec{v} + \vec{w}) + \vec{u} = \vec{v} + (\vec{w} + \vec{u}))$
  * **Elemento Neutro ($\vec{0}$):** $(\vec{v} + \vec{0} = \vec{0} + \vec{v} = \vec{v})$
  * **Elemento Simétrico / Opuesto ($-\vec{v}$):** $(\vec{v} + (-\vec{v}) = \vec{0})$

### B. Producto por un Escalar ($m \cdot \vec{v}$, con $m \in \mathbb{R}$)
* **Geometría:** Escala la longitud del vector ($m$ veces $\vec{v}$); si $m < 0$, invierte su sentido.
* **Operación externa ($\mathbb{R} \times V \to V$):** Resultado es otro vector.
* **Propiedades:**
  * **Conmutativa:** $(m\vec{v} = \vec{v}m)$
  * **Asociativa mixta:** $((n \cdot m)\vec{v} = n(m\vec{v}))$
  * **Distributiva respecto a la suma en $\mathbb{R}$:** $((n + m)\vec{v} = n\vec{v} + m\vec{v})$
  * **Distributiva respecto a la suma en $V$:** $(n(\vec{v} + \vec{u}) = n\vec{v} + n\vec{u})$
  * **Elemento Unidad:** $(1 \cdot \vec{v} = \vec{v})$

### C. Combinación Lineal y Tipos de Bases
* **Combinación Lineal:** Generación de vectores a partir de un conjunto finito de vectores dados: $\vec{w} = a\vec{u} + b\vec{v}$.
* **Base:** Conjunto de vectores linealmente independientes ($\vec{u} \neq k\vec{v}$, no colineales/proporcionales) capaces de generar todo el espacio.
* **Clasificación de Bases:**
  1. **Base no ortogonal:** Los vectores de la base forman un ángulo $\alpha \neq 90^\circ$.
  2. **Base ortogonal:** Los vectores son mutuamente perpendiculares ($\vec{u} \perp \vec{v}$), pero con módulos arbitrarios ($|\vec{u}| \neq |\vec{v}|$).
  3. **Base ortonormal:** Vectores mutuamente perpendiculares y de longitud unitaria ($|\vec{u}_1| = |\vec{u}_2| = 1$, $\vec{u}_1 \perp \vec{u}_2$). En el plano y espacio se usan los versores canónicos $\{\vec{i}, \vec{j}, \vec{k}\}$.

---

## 3. Expresión Analítica en Base Ortonormal

En una base ortonormal $\{\vec{i}, \vec{j}\}$:
* **Componentes:** $\vec{v} = v_x \vec{i} + v_y \vec{j} \equiv (v_x, v_y)$
* **Módulo (Teorema de Pitágoras):** $|\vec{v}| = +\sqrt{v_x^2 + v_y^2}$
* **Suma y Resta:** $\vec{u} \pm \vec{v} = (u_x \pm v_x, \, u_y \pm v_y)$
* **Producto por Escalar:** $m\vec{u} = (m u_x, \, m u_y)$
* **Vector Unitario y Normalización:** $|\vec{u}| = 1 \implies \vec{u}_{\vec{v}} = \dfrac{\vec{v}}{|\vec{v}|} = \left(\dfrac{v_x}{|\vec{v}|}, \dfrac{v_y}{|\vec{v}|}\right)$
* **Combinación Lineal por Componentes:** $\vec{w} = a\vec{u} + b\vec{v} \iff \begin{cases} w_x = a u_x + b v_x \\ w_y = a u_y + b v_y \end{cases}$

---

## 4. Producto Escalar ($\vec{u} \cdot \vec{v}$)

### Definición y Significado Físico
* **Definición geométrica:** $\vec{u} \cdot \vec{v} = |\vec{u}| \cdot |\vec{v}| \cdot \cos \alpha$
* **Interpretación:** Multiplica la magnitud de un vector por la proyección del otro en su misma dirección:
  $$\vec{u} \cdot \vec{v} = \overline{PM} \cdot |\vec{v}| \quad \text{donde } \overline{PM} = |\vec{u}|\cos \alpha$$
* **Resultado:** Es un **número real** ($\in \mathbb{R}$), **NO** un vector.
* **Expresión analítica (base ortonormal):** $\vec{u} \cdot \vec{v} = u_x v_x + u_y v_y$
* **Módulo mediante producto escalar:** $(\vec{u} \cdot \vec{u} = |\vec{u}|^2 \cos 0^\circ = |\vec{u}|^2 \implies |\vec{u}| = \sqrt{\vec{u} \cdot \vec{u}})$

### Propiedades Algebraicas
1. **Conmutativa:** $(\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u})$
2. **Asociativa mixta con escalares:** $(m(\vec{u} \cdot \vec{v}) = (m\vec{u}) \cdot \vec{v} = \vec{u} \cdot (m\vec{v}))$
3. **Distributiva respecto a la suma vectorial:** $(\vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w})$
4. **Ortogonalidad:** $(\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0)$

### Proyección Escalar vs. Vector Proyección (Geometría y Teorema de Pitágoras)

En el triángulo rectángulo formado al proyectar el vector $\vec{u}$ sobre la recta que contiene a $\vec{v}$:

```
           Q (extremo de u)
          /|
         / |
      u /  |  u_perp (cateto opuesto, perpendicular a v)
       /   |
      / α  |
  P -------+------> v
      PM = u_paralelo (cateto adyacente, proyeccion sobre v)
```

1. **Proyección Escalar (longitud con signo del segmento $\overline{PM}$):**
   $$\text{proy}_{\vec{v}}(\vec{u}) = \overline{PM} = |\vec{u}| \cos \alpha = \frac{\vec{u} \cdot \vec{v}}{|\vec{v}|}$$
   * Si $\alpha < 90^\circ \implies \overline{PM} > 0$ (mismo sentido que $\vec{v}$).
   * Si $\alpha > 90^\circ \implies \overline{PM} < 0$ (sentido opuesto a $\vec{v}$).

2. **Vector Proyección ($\vec{\text{proy}}_{\vec{v}}(\vec{u})$ o $\vec{u}_\parallel$):**
   Es un vector en la recta soporte de $\vec{v}$. Se construye multiplicando la proyección escalar por el versor unitario $\vec{u}_{\vec{v}} = \frac{\vec{v}}{|\vec{v}|}$:
   $$\vec{u}_\parallel = \vec{\text{proy}}_{\vec{v}}(\vec{u}) = (\overline{PM}) \cdot \frac{\vec{v}}{|\vec{v}|} = \left(\frac{\vec{u} \cdot \vec{v}}{|\vec{v}|}\right) \frac{\vec{v}}{|\vec{v}|} = \frac{\vec{u} \cdot \vec{v}}{|\vec{v}|^2} \vec{v}$$

3. **Descomposición Ortogonal y Teorema de Pitágoras:**
   Todo vector $\vec{u}$ se descompone de forma única en dos componentes perpendiculares:
   $$\vec{u} = \vec{u}_\parallel + \vec{u}_\perp \implies \vec{u}_\perp = \vec{u} - \vec{u}_\parallel = \vec{u} - \frac{\vec{u} \cdot \vec{v}}{|\vec{v}|^2} \vec{v}$$
   Al ser $\vec{u}_\parallel \perp \vec{u}_\perp$, el triángulo $\triangle PMQ$ es rectángulo en $M$, donde $\vec{u}$ es la **hipotenusa**:
   $$|\text{Hipotenusa}|^2 = |\text{Cateto adyacente}|^2 + |\text{Cateto opuesto}|^2$$
   $$|\vec{u}|^2 = |\vec{u}_\parallel|^2 + |\vec{u}_\perp|^2$$
   * **Relación trigonométrica:**
     $$|\vec{u}_\parallel| = |\vec{u}| \cos \alpha, \qquad |\vec{u}_\perp| = |\vec{u}| \sin \alpha$$
     $$|\vec{u}_\parallel|^2 + |\vec{u}_\perp|^2 = |\vec{u}|^2 \cos^2 \alpha + |\vec{u}|^2 \sin^2 \alpha = |\vec{u}|^2(\cos^2 \alpha + \sin^2 \alpha) = |\vec{u}|^2$$
   * **Módulo de la componente perpendicular (distancia a la recta):**
     $$|\vec{u}_\perp| = \sqrt{|\vec{u}|^2 - |\vec{u}_\parallel|^2} = \sqrt{|\vec{u}|^2 - \left(\frac{\vec{u} \cdot \vec{v}}{|\vec{v}|}\right)^2}$$
     *(Conexión física/geométrica con el producto vectorial: $|\vec{u}_\perp| = |\vec{u}|\sin\alpha = \frac{|\vec{u}\times\vec{v}|}{|\vec{v}|}$)*.

---

## 5. Producto Vectorial ($\vec{a} \times \vec{b}$)

### Definición Geométrica
Genera un **nuevo vector** $\vec{c} = \vec{a} \times \vec{b}$ con las siguientes características:
1. **Módulo:** $|\vec{a} \times \vec{b}| = |\vec{a}| \cdot |\vec{b}| \cdot \sin \alpha$ (numéricamente igual al área del paralelogramo que sustentan).
2. **Dirección:** Perpendicular al plano formado por $\vec{a}$ y $\vec{b}$ ($\vec{c} \perp \vec{a}$ y $\vec{c} \perp \vec{b}$).
3. **Sentido:** Viene dado por la **regla del tornillo** (o regla de la mano derecha / sacacorchos).

### Propiedades y Base Canónica 3D
* **Anticonmutativa:** $(\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a}))$ *(al permutar factores se invierte el sentido)*.
* **Distributiva respecto a la suma vectorial:** $(\vec{a} \times (\vec{b} + \vec{c}) = \vec{a} \times \vec{b} + \vec{a} \times \vec{c})$
* **Asociativa mixta con escalares:** $(m(\vec{a} \times \vec{b}) = (m\vec{a}) \times \vec{b} = \vec{a} \times (m\vec{b}))$
* **Condición de Paralelismo:** $(\vec{a} \parallel \vec{b} \iff \vec{a} \times \vec{b} = \vec{0})$ (en particular $(\vec{a} \times \vec{a} = \vec{0})$ pues $\sin 0^\circ = 0$).
* **NO asociativa:** $(\vec{a} \times (\vec{b} \times \vec{c}) \neq (\vec{a} \times \vec{b}) \times \vec{c})$
* **Productos entre versores canónicos:**
  * $\vec{i} \times \vec{i} = \vec{j} \times \vec{j} = \vec{k} \times \vec{k} = \vec{0}$
  * Sentido directo / horario: $\vec{i} \times \vec{j} = \vec{k}, \quad \vec{j} \times \vec{k} = \vec{i}, \quad \vec{k} \times \vec{i} = \vec{j}$
  * Sentido inverso / antihorario: $\vec{j} \times \vec{i} = -\vec{k}, \quad \vec{k} \times \vec{j} = -\vec{i}, \quad \vec{i} \times \vec{k} = -\vec{j}$

### Expresión por Determinantes
$$\vec{a} \times \vec{b} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix} = \vec{i} \begin{vmatrix} a_y & a_z \\ b_y & b_z \end{vmatrix} - \vec{j} \begin{vmatrix} a_x & a_z \\ b_x & b_z \end{vmatrix} + \vec{k} \begin{vmatrix} a_x & a_y \\ b_x & b_y \end{vmatrix}$$
$$\vec{a} \times \vec{b} = (a_y b_z - a_z b_y)\vec{i} + (a_z b_x - a_x b_z)\vec{j} + (a_x b_y - a_y b_x)\vec{k}$$

---

## 6. Aplicaciones Físicas y Geométricas del Producto Vectorial

### 1. Momento de un Vector respecto a un Punto ($\vec{M}_O^{\vec{v}}$)
*(Concepto fundamental en mecánica clásica: momento de fuerzas, momento cinético / angular).*
$$\vec{M}_O^{\vec{v}} = \vec{r} \times \vec{v} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ r_x & r_y & r_z \\ v_x & v_y & v_z \end{vmatrix}$$
* $\vec{r}$: Vector posición o distancia que va desde el centro de momentos $O$ hasta el punto de aplicación del vector $\vec{v}$.

### 2. Representación Vectorial de una Superficie
*(Válido para toda superficie **abierta y finita**).*
Toda superficie plana de área $S$ se puede caracterizar mediante un vector superficie $\vec{S}$:
* **Módulo:** $|\vec{S}| = S$ (magnitud del área geométrica).
* **Dirección:** Perpendicular (normal) al plano de la superficie.
* **Sentido:** Fijado según la orientación de recorrido del contorno de la superficie (regla de la mano derecha).
* **Punto de aplicación:** En un punto $O$ interior de la superficie.
