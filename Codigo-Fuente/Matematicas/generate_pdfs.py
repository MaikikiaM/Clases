import os
import subprocess

EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUTPUT_DIR = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Matematicas\Derivadas"

# SVG for Exercise 5 (Modelo)
SVG_INCLINED_PLANE_5 = r"""
<div style="text-align: center; margin: 20px 0;">
<svg width="340" height="190" viewBox="0 0 340 190">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d9534f"/>
    </marker>
  </defs>
  <polygon points="30,160 300,160 300,4.2" fill="#f4f4f4" stroke="#333" stroke-width="2"/>
  <path d="M 90 160 A 60 60 0 0 0 81.96 130" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="96" y="150" font-size="13" font-family="Calibri, sans-serif">&alpha; = 30&deg;</text>
  
  <g transform="translate(165, 82.1) rotate(-30)">
    <rect x="-35" y="-30" width="70" height="30" fill="#d0e1fd" stroke="#3366cc" stroke-width="2" rx="2"/>
    <text x="0" y="-11" text-anchor="middle" font-size="12" font-family="Calibri, sans-serif" font-weight="bold">m = 10 kg</text>
    <line x1="35" y1="-15" x2="105" y2="-15" stroke="#d9534f" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="115" y="-10" font-size="12" font-family="Calibri, sans-serif" font-weight="bold" fill="#333">F = 100 N</text>
  </g>
</svg>
</div>
"""

# SVG for Exercise 6 (Práctica)
SVG_INCLINED_PLANE_6 = r"""
<div style="text-align: center; margin: 20px 0;">
<svg width="340" height="190" viewBox="0 0 340 190">
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d9534f"/>
    </marker>
  </defs>
  <polygon points="30,160 300,160 300,4.2" fill="#f4f4f4" stroke="#333" stroke-width="2"/>
  <path d="M 90 160 A 60 60 0 0 0 81.96 130" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="96" y="150" font-size="13" font-family="Calibri, sans-serif">&alpha; = 30&deg;</text>
  
  <g transform="translate(165, 82.1) rotate(-30)">
    <rect x="-35" y="-30" width="70" height="30" fill="#d0e1fd" stroke="#3366cc" stroke-width="2" rx="2"/>
    <text x="0" y="-11" text-anchor="middle" font-size="12" font-family="Calibri, sans-serif" font-weight="bold">m = 8 kg</text>
    <line x1="35" y1="-15" x2="105" y2="-15" stroke="#d9534f" stroke-width="3" marker-end="url(#arrow2)"/>
    <text x="115" y="-10" font-size="12" font-family="Calibri, sans-serif" font-weight="bold" fill="#333">F = 80 N</text>
  </g>
</svg>
</div>
"""

# Solved SVG with forces
SVG_SOLVED = r"""
<div style="text-align: center; margin: 10px 0;">
<svg width="380" height="210" viewBox="0 0 380 210">
  <defs>
    <marker id="ar_red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d9534f"/></marker>
    <marker id="ar_blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0275d8"/></marker>
    <marker id="ar_orange" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#e67e22"/></marker>
    <marker id="ar_gray" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#666"/></marker>
    <marker id="ar_black" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000"/></marker>
  </defs>
  <polygon points="30,180 330,180 330,6.9" fill="#f4f4f4" stroke="#333" stroke-width="2"/>
  <path d="M 90 180 A 60 60 0 0 0 81.96 150" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="98" y="172" font-size="13" font-family="Calibri, sans-serif">30&deg;</text>
  
  <g transform="translate(185, 90) rotate(-30)">
    <rect x="-35" y="-30" width="70" height="30" fill="#d0e1fd" stroke="#3366cc" stroke-width="2" rx="2"/>
    <text x="0" y="-10" text-anchor="middle" font-size="13" font-family="Calibri, sans-serif" font-weight="bold">m</text>
    <!-- F -->
    <line x1="35" y1="-15" x2="105" y2="-15" stroke="#d9534f" stroke-width="2.5" marker-end="url(#ar_red)"/>
    <text x="110" y="-14" font-size="12" font-family="Calibri, sans-serif" font-weight="bold" fill="#d9534f">F</text>
    <!-- Fr -->
    <line x1="-35" y1="-15" x2="-85" y2="-15" stroke="#e67e22" stroke-width="2.5" marker-end="url(#ar_orange)"/>
    <text x="-110" y="-14" font-size="12" font-family="Calibri, sans-serif" font-weight="bold" fill="#e67e22">F_r</text>
    <!-- N -->
    <line x1="0" y1="-30" x2="0" y2="-85" stroke="#0275d8" stroke-width="2.5" marker-end="url(#ar_blue)"/>
    <text x="8" y="-75" font-size="12" font-family="Calibri, sans-serif" font-weight="bold" fill="#0275d8">N</text>
    <!-- Px -->
    <line x1="0" y1="-15" x2="-65" y2="-15" stroke="#777" stroke-width="2" stroke-dasharray="4" marker-end="url(#ar_gray)"/>
    <text x="-65" y="3" font-size="11" font-family="Calibri, sans-serif" fill="#555">P_x</text>
    <!-- Py -->
    <line x1="0" y1="-15" x2="0" y2="55" stroke="#777" stroke-width="2" stroke-dasharray="4" marker-end="url(#ar_gray)"/>
    <text x="-25" y="45" font-size="11" font-family="Calibri, sans-serif" fill="#555">P_y</text>
  </g>
  <!-- P (vertical down) -->
  <line x1="185" y1="100" x2="185" y2="185" stroke="#000" stroke-width="2.5" marker-end="url(#ar_black)"/>
  <text x="192" y="165" font-size="12" font-family="Calibri, sans-serif" font-weight="bold">P = m g</text>
</svg>
</div>
"""

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/mhchem.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 22mm 22mm 22mm 22mm;
  }
  * {
    box-sizing: border-box;
  }
  body {
    font-family: 'Calibri', 'Carlito', 'Segoe UI', sans-serif;
    font-size: 11pt;
    line-height: 1.4;
    color: #111;
    margin: 0;
    padding: 0;
  }
  .page {
    page-break-after: always;
    min-height: 245mm;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  .page:last-child {
    page-break-after: avoid;
  }
  .doc-header {
    text-align: center;
    margin-bottom: 25px;
    padding-bottom: 8px;
  }
  .doc-title {
    font-size: 16pt;
    font-weight: bold;
    margin-bottom: 4px;
  }
  .doc-subtitle {
    font-size: 12pt;
    font-weight: bold;
    color: #222;
  }
  .box {
    border: 0.8pt solid #000;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 18px;
    background: #fff;
    font-size: 10.5pt;
  }
  .box-title {
    font-weight: bold;
    margin-bottom: 6px;
  }
  ol, ul {
    margin-top: 6px;
    margin-bottom: 6px;
    padding-left: 24px;
  }
  li {
    margin-bottom: 8px;
  }
  .alpha-list {
    list-style-type: lower-alpha;
    font-weight: normal;
  }
  .alpha-list > li {
    margin-bottom: 14px;
  }
  .alpha-list > li::marker {
    font-weight: bold;
  }
  .num-list {
    list-style-type: decimal;
  }
  .num-list > li {
    margin-bottom: 6px;
  }
  .bold {
    font-weight: bold;
  }
  p {
    margin: 8px 0;
  }
  .katex-display {
    margin: 12px 0 !important;
  }
</style>
</head>
<body>
__BODY__
<script>
document.addEventListener("DOMContentLoaded", function() {
  renderMathInElement(document.body, {
    delimiters: [
      {left: '$$', right: '$$', display: true},
      {left: '\\[', right: '\\]', display: true},
      {left: '$', right: '$', display: false},
      {left: '\\(', right: '\\)', display: false}
    ],
    throwOnError: false
  });
});
</script>
</body>
</html>
"""

body_unresolved = r"""
<!-- PÁGINA 1: MATEMÁTICAS - RECTA TANGENTE (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Cuaderno de Ejercicios — Ficha de Trabajo</div>
    <div class="doc-subtitle">Matemáticas 1.º de Bachillerato | Ejercicio 1: Recta Tangente y Normal (Modelo)</div>
  </div>
  
  <p class="bold" style="font-size: 11.5pt;">1. Dada la función polinómica:</p>
  <p>$$f(x) = x^3 - 4x^2 + x + 6$$</p>
  
  <ol class="alpha-list" style="margin-top: 25px;">
    <li>Halla la ecuación de la recta tangente a la gráfica de $f(x)$ en el punto de abscisa $x_0 = 3$.</li>
    <li>Halla la ecuación de la recta normal a la gráfica de la función en dicho punto.</li>
  </ol>
</div>

<!-- PÁGINA 2: MATEMÁTICAS - RECTA TANGENTE (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Cuaderno de Ejercicios — Ficha de Trabajo</div>
    <div class="doc-subtitle">Matemáticas 1.º de Bachillerato | Ejercicio 2: Recta Tangente y Normal (Práctica)</div>
  </div>
  
  <p class="bold" style="font-size: 11.5pt;">2. Dada la función polinómica:</p>
  <p>$$g(x) = x^3 - 2x^2 - x + 2$$</p>
  
  <ol class="alpha-list" style="margin-top: 25px;">
    <li>Halla la ecuación de la recta tangente a la gráfica de $g(x)$ en el punto de abscisa $x_0 = 2$.</li>
    <li>Halla la ecuación de la recta normal a la gráfica de la función en dicho punto.</li>
  </ol>
</div>

<!-- PÁGINA 3: MATEMÁTICAS - OPTIMIZACIÓN (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Cuaderno de Ejercicios — Ficha de Trabajo</div>
    <div class="doc-subtitle">Matemáticas 1.º de Bachillerato | Ejercicio 3: Optimización de Superficie (Modelo)</div>
  </div>
  
  <p class="bold" style="font-size: 11.5pt;">3. Un agricultor dispone de $120\text{ metros}$ de valla metálica para delimitar un huerto rectangular. Uno de los lados del terreno limita con la orilla recta de un río, por lo que ese lado no necesita valla.</p>
  
  <ol class="alpha-list" style="margin-top: 25px;">
    <li>Expresa el área del huerto como una función de la longitud $x$ de los lados perpendiculares al río.</li>
    <li>Determina las dimensiones ($x$ e $y$) que debe tener el rectángulo para que la superficie cercada sea máxima.</li>
    <li>Calcula el valor de dicha área máxima y justifica, mediante el criterio de la segunda derivada, que se trata efectivamente de un máximo.</li>
  </ol>
</div>

<!-- PÁGINA 4: MATEMÁTICAS - OPTIMIZACIÓN (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Cuaderno de Ejercicios — Ficha de Trabajo</div>
    <div class="doc-subtitle">Matemáticas 1.º de Bachillerato | Ejercicio 4: Optimización de Superficie (Práctica)</div>
  </div>
  
  <p class="bold" style="font-size: 11.5pt;">4. Un ganadero dispone de $180\text{ metros}$ de valla metálica para construir un corral rectangular adosado a la pared recta de un establo, de manera que la pared sirve de cierre y no requiere valla en ese lado.</p>
  
  <ol class="alpha-list" style="margin-top: 25px;">
    <li>Expresa el área del corral como una función de la longitud $x$ de los dos lados perpendiculares a la pared.</li>
    <li>Determina las dimensiones ($x$ e $y$) que debe tener el corral para que la superficie cercada sea máxima.</li>
    <li>Calcula el valor de dicha área máxima y justifica, mediante el criterio de la segunda derivada, que se trata efectivamente de un máximo.</li>
  </ol>
</div>

<!-- PÁGINA 5: FÍSICA - PLANO INCLINADO (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Cuaderno de Ejercicios — Ficha de Trabajo</div>
    <div class="doc-subtitle">Física 1.º de Bachillerato | Ejercicio 5: Dinámica en Plano Inclinado (Modelo)</div>
  </div>
  
  <p class="bold" style="font-size: 11.5pt;">5. Sobre un plano inclinado de ángulo $\alpha = 30^\circ$ se encuentra un bloque de masa $m = 10\text{ kg}$. El coeficiente de rozamiento entre el bloque y el plano es $\mu = 0{,}25$. Se tira del bloque hacia arriba mediante una fuerza constante $F = 100\text{ N}$ paralela a la superficie del plano inclinado ($g = 9{,}8\text{ m/s}^2$).</p>
  
  __SVG_5__
  
  <ol class="alpha-list">
    <li>Dibuja el diagrama de cuerpo libre indicando todas las fuerzas que actúan sobre el bloque ($\vec{P}$, $\vec{N}$, $\vec{F}_r$ y $\vec{F}$) y descompón el peso en los ejes paralela y perpendicularmente al plano.</li>
    <li>Calcula el valor de la fuerza normal ($N$) y de la fuerza de rozamiento ($F_r$).</li>
    <li>Determina la aceleración con la que sube el bloque por el plano inclinado.</li>
    <li>Si el bloque parte del reposo y recorre una longitud de $10\text{ metros}$ sobre el plano, calcula el tiempo que tarda en recorrerlos y la velocidad final alcanzada.</li>
  </ol>
</div>

<!-- PÁGINA 6: FÍSICA - PLANO INCLINADO (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Cuaderno de Ejercicios — Ficha de Trabajo</div>
    <div class="doc-subtitle">Física 1.º de Bachillerato | Ejercicio 6: Dinámica en Plano Inclinado (Práctica)</div>
  </div>
  
  <p class="bold" style="font-size: 11.5pt;">6. Sobre un plano inclinado de ángulo $\alpha = 30^\circ$ se encuentra un bloque de masa $m = 8\text{ kg}$. El coeficiente de rozamiento entre el bloque y el plano es $\mu = 0{,}20$. Se tira del bloque hacia arriba mediante una fuerza constante $F = 80\text{ N}$ paralela a la superficie del plano inclinado ($g = 9{,}8\text{ m/s}^2$).</p>
  
  __SVG_6__
  
  <ol class="alpha-list">
    <li>Dibuja el diagrama de cuerpo libre indicando todas las fuerzas que actúan sobre el bloque ($\vec{P}$, $\vec{N}$, $\vec{F}_r$ y $\vec{F}$) y descompón el peso en los ejes paralela y perpendicularmente al plano.</li>
    <li>Calcula el valor de la fuerza normal ($N$) y de la fuerza de rozamiento ($F_r$).</li>
    <li>Determina la aceleración con la que sube el bloque por el plano inclinado.</li>
    <li>Si el bloque parte del reposo y recorre una longitud de $10\text{ metros}$ sobre el plano, calcula el tiempo que tarda en recorrerlos y la velocidad final alcanzada.</li>
  </ol>
</div>

<!-- PÁGINA 7: QUÍMICA - RENDIMIENTO (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Cuaderno de Ejercicios — Ficha de Trabajo</div>
    <div class="doc-subtitle">Química 1.º de Bachillerato | Ejercicio 7: Rendimiento de Reacciones (Modelo)</div>
  </div>
  
  <p class="bold" style="font-size: 11.5pt;">7. En una caldera de calefacción se queman $88\text{ g}$ de gas propano ($\ce{C3H8}$) con una cantidad suficiente de gas oxígeno ($\ce{O2}$) del aire, produciéndose dióxido de carbono ($\ce{CO2}$) y agua líquida ($\ce{H2O}$) según la siguiente reacción sin ajustar:</p>
  
  <p>$$\ce{C3H8 (g) + O2 (g) -> CO2 (g) + H2O (l)}$$</p>
  
  <ol class="alpha-list" style="margin-top: 20px;">
    <li>Escribe y ajusta la ecuación química de la combustión.</li>
    <li>Calcula los moles y la masa teórica máxima de dióxido de carbono ($\ce{CO2}$) que se producirían con un rendimiento del $100\%$.</li>
    <li>Sabiendo que las condiciones del quemador hacen que la reacción tenga un rendimiento real del $85\%$, calcula la masa real de $\ce{CO2}$ que se expulsa a la atmósfera.</li>
    <li>Determina el volumen real de gas $\ce{CO2}$ desprendido, medido en Condiciones Normales ($\text{C.N.}$: $1\text{ atm}$, $0^\circ\text{C}$, donde $1\text{ mol} = 22{,}4\text{ L}$).</li>
  </ol>
  
  <p style="margin-top: 25px;"><span class="bold">Datos:</span> Masas atómicas ($\text{u}$): $\mathrm{H} = 1$; $\mathrm{C} = 12$; $\mathrm{O} = 16$.</p>
</div>

<!-- PÁGINA 8: QUÍMICA - RENDIMIENTO (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Cuaderno de Ejercicios — Ficha de Trabajo</div>
    <div class="doc-subtitle">Química 1.º de Bachillerato | Ejercicio 8: Rendimiento de Reacciones (Práctica)</div>
  </div>
  
  <p class="bold" style="font-size: 11.5pt;">8. En un quemador industrial se queman $144\text{ g}$ de gas pentano ($\ce{C5H12}$) con una cantidad suficiente de gas oxígeno ($\ce{O2}$) del aire, produciéndose dióxido de carbono ($\ce{CO2}$) y agua líquida ($\ce{H2O}$) según la siguiente reacción sin ajustar:</p>
  
  <p>$$\ce{C5H12 (g) + O2 (g) -> CO2 (g) + H2O (l)}$$</p>
  
  <ol class="alpha-list" style="margin-top: 20px;">
    <li>Escribe y ajusta la ecuación química de la combustión.</li>
    <li>Calcula los moles y la masa teórica máxima de dióxido de carbono ($\ce{CO2}$) que se producirían con un rendimiento del $100\%$.</li>
    <li>Sabiendo que las condiciones del quemador hacen que la reacción tenga un rendimiento real del $75\%$, calcula la masa real de $\ce{CO2}$ que se expulsa a la atmósfera.</li>
    <li>Determina el volumen real de gas $\ce{CO2}$ desprendido, medido en Condiciones Normales ($\text{C.N.}$: $1\text{ atm}$, $0^\circ\text{C}$, donde $1\text{ mol} = 22{,}4\text{ L}$).</li>
  </ol>
  
  <p style="margin-top: 25px;"><span class="bold">Datos:</span> Masas atómicas ($\text{u}$): $\mathrm{H} = 1$; $\mathrm{C} = 12$; $\mathrm{O} = 16$.</p>
</div>
""".replace("__SVG_5__", SVG_INCLINED_PLANE_5).replace("__SVG_6__", SVG_INCLINED_PLANE_6)

body_solved = r"""
<!-- PÁGINA 1: MATEMÁTICAS - RESOLUCIÓN 1 (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución: Ejercicio 1 (Recta Tangente y Normal — Modelo)</div>
    <div class="doc-subtitle">Función: $f(x) = x^3 - 4x^2 + x + 6$ en $x_0 = 3$</div>
  </div>
  
  <div class="box">
    <div class="box-title">Fórmulas aplicadas:</div>
    <ul>
      <li>Punto de tangencia: $P(x_0, y_0) = (x_0, f(x_0))$.</li>
      <li>Pendiente tangente: $m = f'(x_0) \implies \text{Recta tangente: } y - y_0 = f'(x_0)(x - x_0)$.</li>
      <li>Pendiente normal: $m_{\text{norm}} = -\frac{1}{f'(x_0)} \implies \text{Recta normal: } y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)$.</li>
    </ul>
  </div>
  
  <ol class="alpha-list">
    <li><span class="bold">Ecuación de la recta tangente en $x_0 = 3$:</span>
      <ol class="num-list">
        <li><span class="bold">Ordenada del punto:</span>
          $$y_0 = f(3) = 3^3 - 4(3^2) + 3 + 6 = 27 - 36 + 3 + 6 = \mathbf{0} \implies P(3, 0)$$
        </li>
        <li><span class="bold">Derivada general:</span>
          $$f'(x) = 3x^2 - 8x + 1$$
        </li>
        <li><span class="bold">Pendiente en el punto ($x = 3$):</span>
          $$m = f'(3) = 3(3^2) - 8(3) + 1 = 27 - 24 + 1 = \mathbf{4}$$
        </li>
        <li><span class="bold">Ecuación de la recta tangente:</span>
          $$y - 0 = 4(x - 3) \implies \mathbf{y = 4x - 12}$$
        </li>
      </ol>
    </li>
    <li><span class="bold">Ecuación de la recta normal en $x_0 = 3$:</span>
      <ol class="num-list">
        <li><span class="bold">Pendiente de la recta normal:</span>
          $$m_{\text{normal}} = -\frac{1}{m} = -\frac{1}{4}$$
        </li>
        <li><span class="bold">Ecuación de la recta normal:</span>
          $$y - 0 = -\frac{1}{4}(x - 3) \implies \mathbf{y = -\frac{1}{4}x + \frac{3}{4}} \quad (\text{o en forma general: } x + 4y - 3 = 0)$$
        </li>
      </ol>
    </li>
  </ol>
</div>

<!-- PÁGINA 2: MATEMÁTICAS - RESOLUCIÓN 2 (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución: Ejercicio 2 (Recta Tangente y Normal — Práctica)</div>
    <div class="doc-subtitle">Función: $g(x) = x^3 - 2x^2 - x + 2$ en $x_0 = 2$</div>
  </div>
  
  <div class="box">
    <div class="box-title">Fórmulas aplicadas:</div>
    <ul>
      <li>Punto de tangencia: $P(x_0, y_0) = (x_0, g(x_0))$.</li>
      <li>Pendiente tangente: $m = g'(x_0) \implies \text{Recta tangente: } y - y_0 = g'(x_0)(x - x_0)$.</li>
      <li>Pendiente normal: $m_{\text{norm}} = -\frac{1}{g'(x_0)} \implies \text{Recta normal: } y - y_0 = -\frac{1}{g'(x_0)}(x - x_0)$.</li>
    </ul>
  </div>
  
  <ol class="alpha-list">
    <li><span class="bold">Ecuación de la recta tangente en $x_0 = 2$:</span>
      <ol class="num-list">
        <li><span class="bold">Ordenada del punto:</span>
          $$y_0 = g(2) = 2^3 - 2(2^2) - 2 + 2 = 8 - 8 - 2 + 2 = \mathbf{0} \implies P(2, 0)$$
        </li>
        <li><span class="bold">Derivada general:</span>
          $$g'(x) = 3x^2 - 4x - 1$$
        </li>
        <li><span class="bold">Pendiente en el punto ($x = 2$):</span>
          $$m = g'(2) = 3(2^2) - 4(2) - 1 = 12 - 8 - 1 = \mathbf{3}$$
        </li>
        <li><span class="bold">Ecuación de la recta tangente:</span>
          $$y - 0 = 3(x - 2) \implies \mathbf{y = 3x - 6}$$
        </li>
      </ol>
    </li>
    <li><span class="bold">Ecuación de la recta normal en $x_0 = 2$:</span>
      <ol class="num-list">
        <li><span class="bold">Pendiente de la recta normal:</span>
          $$m_{\text{normal}} = -\frac{1}{m} = -\frac{1}{3}$$
        </li>
        <li><span class="bold">Ecuación de la recta normal:</span>
          $$y - 0 = -\frac{1}{3}(x - 2) \implies \mathbf{y = -\frac{1}{3}x + \frac{2}{3}} \quad (\text{o en forma general: } x + 3y - 2 = 0)$$
        </li>
      </ol>
    </li>
  </ol>
</div>

<!-- PÁGINA 3: MATEMÁTICAS - RESOLUCIÓN 3 (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución: Ejercicio 3 (Optimización: Huerto y Río — Modelo)</div>
    <div class="doc-subtitle">Maximización de área con $120\text{ m}$ de valla disponible</div>
  </div>
  
  <p class="bold">Planteamiento geométrico y ligadura:</p>
  <ul>
    <li>Sean $x$ los dos lados perpendiculares a la orilla del río e $y$ el lado paralelo al río.</li>
    <li><span class="bold">Ecuación de ligadura (longitud de valla):</span>
      $$2x + y = 120 \implies \mathbf{y = 120 - 2x}$$
    </li>
  </ul>
  
  <ol class="alpha-list" style="margin-top: 15px;">
    <li><span class="bold">Función área $A(x)$ y dominio:</span>
      $$A(x) = \text{base} \times \text{altura} = y \cdot x = (120 - 2x)x = \mathbf{120x - 2x^2} \quad (\text{con } 0 < x < 60)$$
    </li>
    <li><span class="bold">Cálculo de las dimensiones óptimas:</span>
      <ol class="num-list">
        <li>Derivamos la función área e igualamos a cero:
          $$A'(x) = 120 - 4x = 0 \implies 4x = 120 \implies \mathbf{x = 30\text{ m}}$$
        </li>
        <li>Calculamos la otra dimensión $y$:
          $$y = 120 - 2(30) = 120 - 60 = \mathbf{60\text{ m}}$$
        </li>
        <li><span class="bold">Dimensiones óptimas:</span> <span class="bold">$30\text{ m}$ de fondo</span> y <span class="bold">$60\text{ m}$ de frente al río</span>.</li>
      </ol>
    </li>
    <li><span class="bold">Área máxima y justificación con la 2.ª derivada:</span>
      <ul>
        <li><span class="bold">Área máxima cercada:</span>
          $$A_{\text{máx}} = A(30) = 30\text{ m} \times 60\text{ m} = \mathbf{1800\text{ m}^2}$$
        </li>
        <li><span class="bold">Comprobación de máximo:</span>
          $$A''(x) = -4 \implies A''(30) = -4 < 0 \implies \text{\textbf{Máximo absoluto}}.$$
        </li>
      </ul>
    </li>
  </ol>
</div>

<!-- PÁGINA 4: MATEMÁTICAS - RESOLUCIÓN 4 (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución: Ejercicio 4 (Optimización: Corral y Muro — Práctica)</div>
    <div class="doc-subtitle">Maximización de área con $180\text{ m}$ de valla disponible</div>
  </div>
  
  <p class="bold">Planteamiento geométrico y ligadura:</p>
  <ul>
    <li>Sean $x$ los dos lados perpendiculares a la pared del establo e $y$ el lado paralelo a la pared.</li>
    <li><span class="bold">Ecuación de ligadura (longitud de valla):</span>
      $$2x + y = 180 \implies \mathbf{y = 180 - 2x}$$
    </li>
  </ul>
  
  <ol class="alpha-list" style="margin-top: 15px;">
    <li><span class="bold">Función área $A(x)$ y dominio:</span>
      $$A(x) = \text{base} \times \text{altura} = y \cdot x = (180 - 2x)x = \mathbf{180x - 2x^2} \quad (\text{con } 0 < x < 90)$$
    </li>
    <li><span class="bold">Cálculo de las dimensiones óptimas:</span>
      <ol class="num-list">
        <li>Derivamos la función área e igualamos a cero:
          $$A'(x) = 180 - 4x = 0 \implies 4x = 180 \implies \mathbf{x = 45\text{ m}}$$
        </li>
        <li>Calculamos la otra dimensión $y$:
          $$y = 180 - 2(45) = 180 - 90 = \mathbf{90\text{ m}}$$
        </li>
        <li><span class="bold">Dimensiones óptimas:</span> <span class="bold">$45\text{ m}$ de fondo</span> y <span class="bold">$90\text{ m}$ de frente a la pared</span>.</li>
      </ol>
    </li>
    <li><span class="bold">Área máxima y justificación con la 2.ª derivada:</span>
      <ul>
        <li><span class="bold">Área máxima cercada:</span>
          $$A_{\text{máx}} = A(45) = 45\text{ m} \times 90\text{ m} = \mathbf{4050\text{ m}^2}$$
        </li>
        <li><span class="bold">Comprobación de máximo:</span>
          $$A''(x) = -4 \implies A''(45) = -4 < 0 \implies \text{\textbf{Máximo absoluto}}.$$
        </li>
      </ul>
    </li>
  </ol>
</div>

<!-- PÁGINA 5: FÍSICA - RESOLUCIÓN 5 (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución: Ejercicio 5 (Plano Inclinado con Rozamiento — Modelo)</div>
    <div class="doc-subtitle">Física 1.º de Bachillerato | $m = 10\text{ kg}$, $\alpha = 30^\circ$, $\mu = 0{,}25$, $F = 100\text{ N}$</div>
  </div>
  
  __SVG_SOLVED__
  
  <ol class="alpha-list">
    <li><span class="bold">Descomposición del peso ($P = mg = 10 \cdot 9{,}8 = 98\text{ N}$):</span>
      $$P_x = P \cdot \sin 30^\circ = 98 \cdot 0{,}5 = \mathbf{49\text{ N}} \qquad P_y = P \cdot \cos 30^\circ = 98 \cdot \frac{\sqrt{3}}{2} = \mathbf{84{,}87\text{ N}}$$
    </li>
    <li><span class="bold">Fuerza normal ($N$) y fuerza de rozamiento ($F_r$):</span>
      <ul>
        <li>Eje Y ($\sum F_y = 0$): $N - P_y = 0 \implies \mathbf{N = P_y = 84{,}87\text{ N}}$.</li>
        <li>Fuerza de rozamiento: $\mathbf{F_r = \mu \cdot N} = 0{,}25 \cdot 84{,}87 = \mathbf{21{,}22\text{ N}}$.</li>
      </ul>
    </li>
    <li><span class="bold">Aceleración del bloque al subir por el plano:</span>
      <ul>
        <li>Eje X ($\sum F_x = m \cdot a$):
          $$F - P_x - F_r = m \cdot a \implies 100 - 49 - 21{,}22 = 10 \cdot a \implies \mathbf{a = 2{,}98\text{ m/s}^2}$$
        </li>
      </ul>
    </li>
    <li><span class="bold">Cinemática del movimiento sobre el plano ($L = 10\text{ m}$, $v_0 = 0$):</span>
      <ul>
        <li>Tiempo: $L = \frac{1}{2}at^2 \implies t = \sqrt{\frac{2L}{a}} = \sqrt{\frac{2 \cdot 10}{2{,}978}} = \mathbf{2{,}59\text{ s}}$.</li>
        <li>Velocidad final: $v = a \cdot t = 2{,}978 \cdot 2{,}592 = \mathbf{7{,}72\text{ m/s}}$.</li>
      </ul>
    </li>
  </ol>
</div>

<!-- PÁGINA 6: FÍSICA - RESOLUCIÓN 6 (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución: Ejercicio 6 (Plano Inclinado con Rozamiento — Práctica)</div>
    <div class="doc-subtitle">Física 1.º de Bachillerato | $m = 8\text{ kg}$, $\alpha = 30^\circ$, $\mu = 0{,}20$, $F = 80\text{ N}$</div>
  </div>
  
  __SVG_SOLVED__
  
  <ol class="alpha-list">
    <li><span class="bold">Descomposición del peso ($P = mg = 8 \cdot 9{,}8 = 78{,}4\text{ N}$):</span>
      $$P_x = P \cdot \sin 30^\circ = 78{,}4 \cdot 0{,}5 = \mathbf{39{,}2\text{ N}} \qquad P_y = P \cdot \cos 30^\circ = 78{,}4 \cdot \frac{\sqrt{3}}{2} = \mathbf{67{,}90\text{ N}}$$
    </li>
    <li><span class="bold">Fuerza normal ($N$) y fuerza de rozamiento ($F_r$):</span>
      <ul>
        <li>Eje Y ($\sum F_y = 0$): $N - P_y = 0 \implies \mathbf{N = P_y = 67{,}90\text{ N}}$.</li>
        <li>Fuerza de rozamiento: $\mathbf{F_r = \mu \cdot N} = 0{,}20 \cdot 67{,}90 = \mathbf{13{,}58\text{ N}}$.</li>
      </ul>
    </li>
    <li><span class="bold">Aceleración del bloque al subir por el plano:</span>
      <ul>
        <li>Eje X ($\sum F_x = m \cdot a$):
          $$F - P_x - F_r = m \cdot a \implies 80 - 39{,}2 - 13{,}58 = 8 \cdot a \implies 27{,}22 = 8a \implies \mathbf{a = 3{,}40\text{ m/s}^2}$$
        </li>
      </ul>
    </li>
    <li><span class="bold">Cinemática del movimiento sobre el plano ($L = 10\text{ m}$, $v_0 = 0$):</span>
      <ul>
        <li>Tiempo: $L = \frac{1}{2}at^2 \implies t = \sqrt{\frac{2L}{a}} = \sqrt{\frac{2 \cdot 10}{3{,}4025}} = \mathbf{2{,}42\text{ s}}$.</li>
        <li>Velocidad final: $v = a \cdot t = 3{,}4025 \cdot 2{,}424 = \mathbf{8{,}25\text{ m/s}}$.</li>
      </ul>
    </li>
  </ol>
</div>

<!-- PÁGINA 7: QUÍMICA - RESOLUCIÓN 7 (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución: Ejercicio 7 (Combustión de Propano — Modelo)</div>
    <div class="doc-subtitle">Química 1.º de Bachillerato</div>
  </div>
  
  <p class="bold">Cálculo de masas molares ($M$):</p>
  <ul>
    <li>$M(\ce{C3H8}) = 3(12) + 8(1) = 44\text{ g/mol} \qquad M(\ce{CO2}) = 12 + 2(16) = 44\text{ g/mol}$</li>
  </ul>
  
  <ol class="alpha-list" style="margin-top: 15px;">
    <li><span class="bold">Ajuste de la reacción química:</span>
      $$\ce{C3H8 (g) + 5 O2 (g) -> 3 CO2 (g) + 4 H2O (l)}$$
    </li>
    <li><span class="bold">Moles y masa teórica máxima de $\ce{CO2}$ ($100\%$ de rendimiento):</span>
      <ul>
        <li>Moles de reactivo inicial ($\ce{C3H8}$):
          $$n(\ce{C3H8}) = \frac{88\text{ g}}{44\text{ g/mol}} = 2{,}00\text{ mol de } \ce{C3H8}$$
        </li>
        <li>Relación estequiométrica ($1\text{ mol } \ce{C3H8} : 3\text{ mol } \ce{CO2}$):
          $$n_{\text{teórico}}(\ce{CO2}) = 2{,}00\text{ mol } \ce{C3H8} \times \frac{3\text{ mol } \ce{CO2}}{1\text{ mol } \ce{C3H8}} = \mathbf{6{,}00\text{ mol de } \ce{CO2}}$$
        </li>
        <li>Masa teórica de $\ce{CO2}$:
          $$m_{\text{teórica}}(\ce{CO2}) = 6{,}00\text{ mol} \times 44\text{ g/mol} = \mathbf{264\text{ g de } \ce{CO2}}$$
        </li>
      </ul>
    </li>
    <li><span class="bold">Masa real de $\ce{CO2}$ emitida con un rendimiento del $85\%$:</span>
      $$m_{\text{real}}(\ce{CO2}) = m_{\text{teórica}} \times 0{,}85 = 264\text{ g} \times 0{,}85 = \mathbf{224{,}4\text{ g de } \ce{CO2}}$$
    </li>
    <li><span class="bold">Volumen real de $\ce{CO2}$ en Condiciones Normales ($\text{C.N.}$):</span>
      <ul>
        <li>Moles reales de $\ce{CO2}$ producidos al $85\%$:
          $$n_{\text{real}}(\ce{CO2}) = 6{,}00\text{ mol} \times 0{,}85 = 5{,}10\text{ mol de } \ce{CO2}$$
        </li>
        <li>Volumen en C.N. ($V_{\text{molar}} = 22{,}4\text{ L/mol}$):
          $$V_{\text{real}}(\ce{CO2}) = 5{,}10\text{ mol} \times 22{,}4\text{ L/mol} = \mathbf{114{,}24\text{ L de } \ce{CO2}}$$
        </li>
      </ul>
    </li>
  </ol>
</div>

<!-- PÁGINA 8: QUÍMICA - RESOLUCIÓN 8 (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución: Ejercicio 8 (Combustión de Pentano — Práctica)</div>
    <div class="doc-subtitle">Química 1.º de Bachillerato</div>
  </div>
  
  <p class="bold">Cálculo de masas molares ($M$):</p>
  <ul>
    <li>$M(\ce{C5H12}) = 5(12) + 12(1) = 72\text{ g/mol} \qquad M(\ce{CO2}) = 12 + 2(16) = 44\text{ g/mol}$</li>
  </ul>
  
  <ol class="alpha-list" style="margin-top: 15px;">
    <li><span class="bold">Ajuste de la ecuación química:</span>
      $$\ce{C5H12 (g) + 8 O2 (g) -> 5 CO2 (g) + 6 H2O (l)}$$
    </li>
    <li><span class="bold">Moles y masa teórica máxima de dióxido de carbono ($\ce{CO2}$) al $100\%$:</span>
      <ul>
        <li>Moles iniciales de pentano:
          $$n(\ce{C5H12}) = \frac{144\text{ g}}{72\text{ g/mol}} = 2{,}00\text{ mol de } \ce{C5H12}$$
        </li>
        <li>Moles teóricos de $\ce{CO2}$ ($1\text{ mol } \ce{C5H12} : 5\text{ mol } \ce{CO2}$):
          $$n_{\text{teórico}}(\ce{CO2}) = 2{,}00\text{ mol } \ce{C5H12} \times \frac{5\text{ mol } \ce{CO2}}{1\text{ mol } \ce{C5H12}} = \mathbf{10{,}00\text{ mol de } \ce{CO2}}$$
        </li>
        <li>Masa teórica de $\ce{CO2}$:
          $$m_{\text{teórica}}(\ce{CO2}) = 10{,}00\text{ mol} \times 44\text{ g/mol} = \mathbf{440\text{ g de } \ce{CO2}}$$
        </li>
      </ul>
    </li>
    <li><span class="bold">Masa real de dióxido de carbono ($\ce{CO2}$) con rendimiento del $75\%$:</span>
      $$m_{\text{real}}(\ce{CO2}) = m_{\text{teórica}} \times 0{,}75 = 440\text{ g} \times 0{,}75 = \mathbf{330\text{ g de } \ce{CO2}}$$
    </li>
    <li><span class="bold">Volumen real de $\ce{CO2}$ en Condiciones Normales ($\text{C.N.}$):</span>
      <ul>
        <li>Moles reales de $\ce{CO2}$ producidos al $75\%$:
          $$n_{\text{real}}(\ce{CO2}) = 10{,}00\text{ mol} \times 0{,}75 = 7{,}50\text{ mol de } \ce{CO2}$$
        </li>
        <li>Volumen en C.N. ($V_{\text{molar}} = 22{,}4\text{ L/mol}$):
          $$V_{\text{real}}(\ce{CO2}) = 7{,}50\text{ mol} \times 22{,}4\text{ L/mol} = \mathbf{168{,}00\text{ L de } \ce{CO2}}$$
        </li>
      </ul>
    </li>
  </ol>
</div>
""".replace("__SVG_SOLVED__", SVG_SOLVED)

def compile_pdf(title, body_content, target_pdf_name):
    html_str = HTML_TEMPLATE.replace("__TITLE__", title).replace("__BODY__", body_content)
    temp_html = os.path.join(OUTPUT_DIR, f"temp_{target_pdf_name}.html")
    target_pdf = os.path.join(OUTPUT_DIR, target_pdf_name)
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_str)
        
    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=4000",
        f"--print-to-pdf={target_pdf}",
        temp_html
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)
        
    if os.path.exists(target_pdf):
        print(f"Exito: {target_pdf_name} ({os.path.getsize(target_pdf)} bytes)")
    else:
        print(f"Error: {res.stderr}")

if __name__ == "__main__":
    compile_pdf("Cuaderno de Ejercicios — Derivadas, Física y Química", body_unresolved, "ejercicios_derivadas_tangente_y_optimizacion.pdf")
    compile_pdf("Solucionario — Derivadas, Física y Química", body_solved, "ejercicios_derivadas_tangente_y_optimizacion_resueltos.pdf")
