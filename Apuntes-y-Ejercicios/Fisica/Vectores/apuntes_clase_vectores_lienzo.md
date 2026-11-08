# Hoja 1: Elementos de un Vector, Componentes y Descomposición Física

### 1.1 El Vector en la Física: Descomposición en un Plano Inclinado
En física, las magnitudes vectoriales no solo requieren una cantidad numérica, sino una orientación espacial.
Un ejemplo clásico es la descomposición del peso $\vec{P}$ sobre un plano inclinado:
* El vector peso se proyecta sobre los ejes coordenados en dos componentes perpendiculares:
  $$\vec{P} = (P_x, \, P_y)$$
* En el ejemplo desarrollado en clase:
  $$\vec{P} = (4, \, 5) \implies P_x = 4, \quad P_y = 5$$

### 1.2 Módulo de un Vector (Teorema de Pitágoras)
El módulo representa la longitud o magnitud física del vector. Al formar las componentes cartesianas un triángulo rectángulo:
$$|\vec{P}| = \sqrt{P_x^2 + P_y^2} = \sqrt{4^2 + 5^2} = \sqrt{16 + 25} = \sqrt{41}$$

### 1.3 Los Tres Elementos Fundamentales de un Vector
Todo vector $\vec{P}$ queda unívocamente determinado por:
1. **Módulo:** Magnitud o longitud del segmento orientado. Es siempre un valor **escalar** no negativo ($|\vec{P}| \ge 0$).
2. **Dirección:** Línea recta sobre la que descansa el vector (recta soporte o cualquier paralela a ella).
3. **Sentido:** Orientación sobre la recta de acción, indicada por la punta de la flecha.

### 1.4 Vector Determinado por Dos Puntos
Dados dos puntos en el plano, el origen $A(x_1, y_1)$ y el extremo $B(x_2, y_2)$, el vector $\vec{AB}$ que va de $A$ hacia $B$ se obtiene restando las coordenadas del extremo menos las del origen:
$$\vec{AB} = (B_x - A_x, \, B_y - A_y)$$

* **Ejemplo de clase:** Dados los puntos $A(2, 4)$ y $B(5, 4)$:
  $$\vec{AB} = (5 - 2, \, 4 - 4) = (3, 0)$$

* **Notación habitual de vectores:** $\vec{u}, \vec{v}, \vec{w}$.

<div class="page-break"></div>

# Hoja 2: Propiedades Algebraicas y Vectores Unitarios Canónicos

### 2.1 Propiedades del Álgebra Vectorial
Las operaciones básicas con vectores satisfacen las siguientes propiedades fundamentales:

* **Propiedad Conmutativa de la suma:**
  $$\vec{v} + \vec{u} = \vec{u} + \vec{v}$$

* **Propiedad Asociativa de la suma:**
  $$\vec{v} + (\vec{u} + \vec{w}) = (\vec{v} + \vec{u}) + \vec{w}$$

* **Propiedad Distributiva del producto por un escalar ($n \in \mathbb{R}$):**
  $$n(\vec{v} + \vec{u}) = n\vec{v} + n\vec{u}$$

### 2.2 Concepto y Obtención de un Vector Unitario
Un vector es **unitario** cuando su módulo es exactamente igual a la unidad ($|\vec{u}| = 1$).

Para normalizar cualquier vector no nulo (manteniendo su misma dirección y sentido pero con módulo 1), se divide cada una de sus componentes entre su módulo:
$$\vec{u}_{\vec{AB}} = \frac{\vec{AB}}{|\vec{AB}|} = \left(\frac{B_x - A_x}{|\vec{AB}|}, \, \frac{B_y - A_y}{|\vec{AB}|}\right)$$

* **Aplicación al vector $\vec{AB} = (3, 0)$ de la Hoja 1:**
  $$|\vec{AB}| = \sqrt{3^2 + 0^2} = 3 \implies \vec{u}_{\vec{AB}} = \left(\frac{3}{3}, \, \frac{0}{3}\right) = (1, 0) \equiv \vec{i}$$

### 2.3 Versores Canónicos en el Espacio Tridimensional
Los vectores unitarios asociados a las direcciones positivas de los ejes cartesianos se denominan versores canónicos:
* **Eje $X$:** $\vec{i} = (1, 0, 0)$ &nbsp;|&nbsp; *(en el plano 2D: $(1, 0)$)*
* **Eje $Y$:** $\vec{j} = (0, 1, 0)$ &nbsp;|&nbsp; *(en el plano 2D: $(0, 1)$)*
* **Eje $Z$:** $\vec{k} = (0, 0, 1)$

### 2.4 Representación Vectorial de Componentes Físicas
Cuando se indica una componente escalar junto con su orientación vectorial, se expresa multiplicando la magnitud por el versor unitario correspondiente:
$$\vec{P}_x = 7\vec{i}\text{ N} \quad (\text{o metros})$$

<div class="page-break"></div>

# Hoja 3: Bases Ortonormales y Expresión Analítica

### 3.1 Definición de Base Ortonormal
Una base ortonormal está constituida por un conjunto de vectores que cumplen dos requisitos simultáneos:

1. **Ortogonalidad:** Todos los vectores de la base son perpendiculares entre sí formando ángulos de $90^\circ$:
   $$\vec{u} \perp \vec{v}$$
2. **Normalidad:** Cada vector de la base tiene módulo unitario:
   $$|\vec{u}| = 1, \quad |\vec{v}| = 1 \implies \frac{\vec{u}}{|\vec{u}|} \perp \frac{\vec{v}}{|\vec{v}|}$$

En el plano cartesiano $XY$, los versores canónicos $\{\vec{i}, \vec{j}\}$ forman la base ortonormal estándar.

### 3.2 Expresión Analítica de un Vector
Cualquier vector del plano puede escribirse de forma única como combinación lineal de los vectores de la base ortonormal:
$$\vec{v}(v_x, v_y) = v_x \vec{i} + v_y \vec{j}$$

* **$v_x$:** Proyección o componente escalar a lo largo del eje horizontal $X$.
* **$v_y$:** Proyección o componente escalar a lo largo del eje vertical $Y$.

### 3.3 Ángulo entre dos Vectores ($\alpha$)
Dos vectores $\vec{u}$ y $\vec{v}$ con origen común definen un ángulo $\alpha$ ($0^\circ \le \alpha \le 180^\circ$).  
La determinación de este ángulo y de la interacción entre ambas direcciones conduce directamente a las operaciones de producto escalar y proyección.

<div class="page-break"></div>

# Hoja 4: Producto Escalar y Proyección de Vectores

### 4.1 Definición del Producto Escalar ($\vec{u} \cdot \vec{v}$)
El producto escalar combina dos vectores para dar como resultado un número real (**escalar**):

* **Expresión analítica (en base ortonormal):**
  $$\vec{u} \cdot \vec{v} = u_x v_x + u_y v_y$$

* **Expresión geométrica:**
  $$\vec{u} \cdot \vec{v} = |\vec{u}| \cdot |\vec{v}| \cdot \cos \alpha$$

### 4.2 Cálculo del Ángulo entre dos Vectores
Igualando ambas expresiones se obtiene la fórmula para determinar el coseno del ángulo formado por dos vectores:
$$\cos \alpha = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}| \cdot |\vec{v}|} = \frac{u_x v_x + u_y v_y}{\sqrt{u_x^2 + u_y^2} \cdot \sqrt{v_x^2 + v_y^2}}$$

### 4.3 Interpretación Geométrica: Proyección de un Vector sobre Otro
Al proyectar ortogonalmente el vector $\vec{v}$ sobre la dirección del vector $\vec{u}$, se forma un triángulo rectángulo:

<div style="text-align: center; margin: 10px 0;">
<svg width="440" height="135" viewBox="0 0 440 135" xmlns="http://www.w3.org/2000/svg" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <marker id="arr-u" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#475569" />
    </marker>
    <marker id="arr-v" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284c7" />
    </marker>
    <marker id="arr-proj" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#dc2626" />
    </marker>
  </defs>

  <rect x="5" y="5" width="430" height="125" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>

  <!-- Recta soporte / vector u -->
  <line x1="50" y1="80" x2="380" y2="80" stroke="#94a3b8" stroke-width="1.8" marker-end="url(#arr-u)"/>
  <!-- Label u con flecha -->
  <g transform="translate(388, 84)">
    <text x="0" y="0" fill="#334155" font-weight="700" font-size="13" font-style="italic">u</text>
    <path d="M 0 -13 L 9 -13 M 7 -15 L 9 -13 L 7 -11" fill="none" stroke="#334155" stroke-width="1.2"/>
  </g>

  <!-- Vector v -->
  <line x1="50" y1="80" x2="215" y2="20" stroke="#0284c7" stroke-width="2.4" marker-end="url(#arr-v)"/>
  <!-- Label v con flecha -->
  <g transform="translate(118, 44)">
    <text x="0" y="0" fill="#0284c7" font-weight="700" font-size="14" font-style="italic">v</text>
    <path d="M 0 -14 L 9 -14 M 7 -16 L 9 -14 L 7 -12" fill="none" stroke="#0284c7" stroke-width="1.3"/>
  </g>

  <!-- Línea perpendicular de proyección -->
  <line x1="215" y1="20" x2="215" y2="80" stroke="#64748b" stroke-width="1.4" stroke-dasharray="4 3"/>

  <!-- Símbolo de ángulo recto -->
  <path d="M 203 80 L 203 68 L 215 68" fill="none" stroke="#64748b" stroke-width="1.2"/>
  <circle cx="209" cy="74" r="1.2" fill="#64748b"/>

  <!-- Arco de ángulo alfa -->
  <path d="M 85 80 A 35 35 0 0 0 78 61" fill="none" stroke="#334155" stroke-width="1.4"/>
  <text x="92" y="73" fill="#334155" font-weight="600" font-size="12">α</text>

  <!-- Vector Proyección (resaltado en rojo) -->
  <line x1="50" y1="80" x2="207" y2="80" stroke="#dc2626" stroke-width="3.5" marker-end="url(#arr-proj)"/>

  <!-- Acotación de la proyección escalar -->
  <line x1="50" y1="96" x2="215" y2="96" stroke="#dc2626" stroke-width="1.2"/>
  <line x1="50" y1="92" x2="50" y2="100" stroke="#dc2626" stroke-width="1.2"/>
  <line x1="215" y1="92" x2="215" y2="100" stroke="#dc2626" stroke-width="1.2"/>

  <!-- Texto identificativo limpio -->
  <g transform="translate(60, 114)">
    <text x="0" y="0" fill="#dc2626" font-weight="700" font-size="11">Vector Proyección:</text>
    <text x="105" y="0" fill="#dc2626" font-weight="700" font-size="11" font-style="italic">Proy</text>
    <text x="130" y="3" fill="#dc2626" font-weight="700" font-size="9" font-style="italic">u</text>
    <text x="138" y="0" fill="#dc2626" font-weight="700" font-size="11" font-style="italic"> v</text>
  </g>
  <text x="245" y="114" fill="#475569" font-size="10.5">Módulo: |v|·cos α = (u·v) / |u|</text>
</svg>
</div>

$$\cos \alpha = \frac{\text{cateto contiguo}}{\text{hipotenusa}} = \frac{|\text{Proy}_{\vec{u}} \vec{v}|}{|\vec{v}|}$$

* **Proyección Escalar (módulo de la sombra):**
  Despejando el cateto contiguo:
  $$|\text{Proy}_{\vec{u}} \vec{v}| = |\vec{v}| \cos \alpha = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}|} \quad (\text{magnitud escalar})$$

* **Vector Proyección ($\vec{\text{Proy}}_{\vec{u}} \vec{v}$):**
  Para convertir la longitud escalar en un vector con la dirección y sentido de $\vec{u}$, se multiplica por el vector unitario $\frac{\vec{u}}{|\vec{u}|}$:
  $$\vec{\text{Proy}}_{\vec{u}} \vec{v} = |\text{Proy}_{\vec{u}} \vec{v}| \cdot \frac{\vec{u}}{|\vec{u}|} = \left(\frac{\vec{u} \cdot \vec{v}}{|\vec{u}|}\right) \frac{\vec{u}}{|\vec{u}|} = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}|^2} \vec{u}$$

<div class="page-break"></div>

# Hoja 5: Producto Vectorial, Base Canónica y Resumen de Operaciones

### 5.1 Ejemplo Práctico de Vector entre dos Puntos
Dados los puntos $A(3, 2)$ y $B(4, 0)$:
$$\vec{AB} = (B_x - A_x, \, B_y - A_y) = (4 - 3, \, 0 - 2) = (1, \, -2)$$

### 5.2 El Producto Vectorial ($\vec{u} \times \vec{v}$)
A diferencia del producto escalar (que produce un número real), el producto vectorial genera un **nuevo vector** $\vec{w} = \vec{u} \times \vec{v}$:

1. **Módulo:** $|\vec{u} \times \vec{v}| = |\vec{u}| \cdot |\vec{v}| \cdot \sin \alpha$ *(área geométrica del paralelogramo sustentado por $\vec{u}$ y $\vec{v}$)*.
2. **Dirección:** Perpendicular simultáneamente a ambos vectores: $\vec{w} \perp \vec{u}$ y $\vec{w} \perp \vec{v}$.
3. **Sentido:** Determinado por la regla de la mano derecha (o del sacacorchos).

### 5.3 La Base Canónica Tridimensional y sus Relaciones
Versores fundamentales en el espacio tridimensional: $\vec{i} = (1, 0, 0)$, $\vec{j} = (0, 1, 0)$, $\vec{k} = (0, 0, 1)$.
* **Productos vectoriales directos y anticonmutatividad:**
  $$\vec{i} \times \vec{j} = \vec{k} = -\vec{j} \times \vec{i} \qquad\Big|\qquad \vec{j} \times \vec{k} = \vec{i} = -\vec{k} \times \vec{j} \qquad\Big|\qquad \vec{k} \times \vec{i} = \vec{j} = -\vec{i} \times \vec{k}$$
* **Paralelos y producto escalar:**
  $$\vec{i} \times \vec{i} = \vec{j} \times \vec{j} = \vec{k} \times \vec{k} = \vec{0} \qquad\Big|\qquad \vec{i} \cdot \vec{i} = 1, \quad \vec{i} \cdot \vec{j} = 0$$

### 5.4 Cuadro Resumen de Operaciones (Síntesis de la Clase)
* **Vector Unitario (normalización):** $\vec{u}_{\vec{w}} = \dfrac{\vec{w}}{|\vec{w}|}$
* **Descomposición Cartesiana y Módulo:** $\vec{P} = P_x\vec{i} + P_y\vec{j} \implies |\vec{P}| = \sqrt{P_x^2 + P_y^2}$
* **Producto Escalar:** $\vec{u} \cdot \vec{v} = u_x v_x + u_y v_y = |\vec{u}||\vec{v}|\cos\alpha \quad (\text{magnitud escalar})$
* **Producto Vectorial:** $\vec{u} \times \vec{v} = |\vec{u}||\vec{v}|\sin\alpha \cdot \vec{n} \quad (\text{vector } \perp \vec{u}, \vec{v})$
* **Vector Proyección:** $\vec{\text{Proy}}_{\vec{u}}\vec{v} = \dfrac{\vec{u}\cdot\vec{v}}{|\vec{u}|^2}\vec{u}$

