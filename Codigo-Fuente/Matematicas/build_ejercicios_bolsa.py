import os
import subprocess

OUTPUT_DIR = r"c:\Users\migue\Antigravity\Clases"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# =========================================================================
# SVGs DE ALTA CALIDAD PARA CADA EJERCICIO
# =========================================================================

SVG_EJ1 = r"""
<div style="text-align: center; margin: 15px 0;">
<svg width="420" height="150" viewBox="0 0 420 150">
  <defs>
    <marker id="arr1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d9534f"/>
    </marker>
  </defs>
  <!-- Suelo -->
  <line x1="20" y1="120" x2="400" y2="120" stroke="#333" stroke-width="2"/>
  <line x1="30" y1="120" x2="20" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="60" y1="120" x2="50" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="90" y1="120" x2="80" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="120" y1="120" x2="110" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="150" y1="120" x2="140" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="180" y1="120" x2="170" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="210" y1="120" x2="200" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="240" y1="120" x2="230" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="270" y1="120" x2="260" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="300" y1="120" x2="290" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="120" x2="320" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="360" y1="120" x2="350" y2="130" stroke="#888" stroke-width="1.5"/>
  <line x1="390" y1="120" x2="380" y2="130" stroke="#888" stroke-width="1.5"/>

  <!-- Trayectoria -->
  <path d="M 50 120 Q 215 0 380 120" fill="none" stroke="#2b5797" stroke-width="2.2" stroke-dasharray="5,4"/>

  <!-- Balón en origen -->
  <circle cx="50" cy="120" r="5" fill="#333"/>
  <!-- Vector v0 -->
  <line x1="50" y1="120" x2="105" y2="88" stroke="#d9534f" stroke-width="2.5" marker-end="url(#arr1)"/>
  <text x="110" y="85" font-family="Calibri, sans-serif" font-size="12" font-weight="bold" fill="#d9534f">v₀ = 20 m/s</text>

  <!-- Ángulo alfa -->
  <path d="M 85 120 A 35 35 0 0 0 80 103" fill="none" stroke="#333" stroke-width="1.2"/>
  <text x="90" y="115" font-family="Calibri, sans-serif" font-size="11">α = 30°</text>

  <!-- Vértice (altura máxima) -->
  <line x1="215" y1="60" x2="215" y2="120" stroke="#666" stroke-dasharray="3,3" stroke-width="1.2"/>
  <circle cx="215" cy="60" r="4" fill="#2b5797"/>
  <text x="222" y="75" font-family="Calibri, sans-serif" font-size="11" fill="#2b5797" font-weight="bold">y_máx</text>

  <!-- Punto de impacto -->
  <circle cx="380" cy="120" r="5" fill="#d9534f"/>
  <line x1="50" y1="138" x2="380" y2="138" stroke="#333" stroke-width="1"/>
  <line x1="50" y1="133" x2="50" y2="143" stroke="#333" stroke-width="1"/>
  <line x1="380" y1="133" x2="380" y2="143" stroke="#333" stroke-width="1"/>
  <text x="215" y="148" text-anchor="middle" font-family="Calibri, sans-serif" font-size="11" fill="#333">Distancia horizontal de impacto (x)</text>
</svg>
</div>
"""

SVG_EJ2 = r"""
<div style="text-align: center; margin: 15px 0;">
<svg width="440" height="170" viewBox="0 0 440 170">
  <defs>
    <marker id="arr2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d9534f"/>
    </marker>
  </defs>
  <!-- Acantilado -->
  <polygon points="20,150 100,150 100,60 20,60" fill="#e2e3e5" stroke="#495057" stroke-width="1.8"/>
  <text x="50" y="110" font-family="Calibri, sans-serif" font-size="12" font-weight="bold" fill="#495057" text-anchor="middle">h = 45 m</text>

  <!-- Agua marina -->
  <line x1="100" y1="150" x2="420" y2="150" stroke="#0077b6" stroke-width="3"/>
  <path d="M 100 155 Q 115 152 130 155 T 160 155 T 190 155 T 220 155 T 250 155 T 280 155 T 310 155 T 340 155 T 370 155 T 400 155 T 420 155" fill="none" stroke="#0096c7" stroke-width="1.5"/>

  <!-- Punto de disparo -->
  <circle cx="100" cy="60" r="4.5" fill="#333"/>
  <!-- Vector v0 -->
  <line x1="100" y1="60" x2="160" y2="25" stroke="#d9534f" stroke-width="2.5" marker-end="url(#arr2)"/>
  <text x="165" y="24" font-family="Calibri, sans-serif" font-size="12" font-weight="bold" fill="#d9534f">v₀ = 30 m/s (α = 30°)</text>

  <!-- Trayectoria con vértice y caída al agua -->
  <path d="M 100 60 Q 150 30 200 48 T 375 150" fill="none" stroke="#2b5797" stroke-width="2.2" stroke-dasharray="5,4"/>

  <!-- Impacto en agua -->
  <circle cx="375" cy="150" r="5" fill="#d9534f"/>
  <line x1="375" y1="150" x2="400" y2="170" stroke="#d9534f" stroke-width="2" marker-end="url(#arr2)"/>
  <text x="365" y="140" font-family="Calibri, sans-serif" font-size="11" fill="#0077b6" font-weight="bold">Impacto (y = 0)</text>

  <!-- Cota horizontal -->
  <line x1="100" y1="165" x2="375" y2="165" stroke="#333" stroke-width="1"/>
  <text x="237" y="163" text-anchor="middle" font-family="Calibri, sans-serif" font-size="10.5" fill="#333">Distancia desde la base del acantilado</text>
</svg>
</div>
"""

SVG_EJ3 = r"""
<div style="text-align: center; margin: 15px 0;">
<svg width="380" height="190" viewBox="0 0 380 190">
  <defs>
    <marker id="arrF" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d9534f"/>
    </marker>
  </defs>
  <!-- Rampa triangular -->
  <polygon points="30,160 330,160 330,20" fill="#f8f9fa" stroke="#333" stroke-width="2"/>
  <path d="M 90 160 A 60 60 0 0 0 82 135" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="96" y="152" font-size="13" font-family="Calibri, sans-serif">α = 30°</text>

  <!-- Bloque sobre la rampa (únicamente con la fuerza aplicada F = 85 N dada en el enunciado) -->
  <g transform="translate(180, 90) rotate(-25)">
    <!-- Bloque -->
    <rect x="-35" y="-30" width="70" height="30" fill="#d0e1fd" stroke="#2b5797" stroke-width="2" rx="3"/>
    <text x="0" y="-11" text-anchor="middle" font-size="11.5" font-family="Calibri, sans-serif" font-weight="bold">m = 8 kg</text>

    <!-- Fuerza F = 85 N (única fuerza visible) -->
    <line x1="35" y1="-15" x2="105" y2="-15" stroke="#d9534f" stroke-width="2.8" marker-end="url(#arrF)"/>
    <text x="110" y="-10" font-size="11.5" font-family="Calibri, sans-serif" font-weight="bold" fill="#d9534f">F = 85 N</text>
  </g>
</svg>
</div>
"""

SVG_EJ3_SOLVED = r"""
<div style="text-align: center; margin: 15px 0;">
<svg width="400" height="210" viewBox="0 0 400 210">
  <defs>
    <marker id="arrFS" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d9534f"/>
    </marker>
    <marker id="arrVS" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2b5797"/>
    </marker>
    <marker id="arrFrS" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#e67e22"/>
    </marker>
    <marker id="arrP" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#6c757d"/>
    </marker>
  </defs>
  <!-- Rampa triangular -->
  <polygon points="30,175 350,175 350,30" fill="#f8f9fa" stroke="#333" stroke-width="2"/>
  <path d="M 90 175 A 60 60 0 0 0 82 150" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="96" y="167" font-size="13" font-family="Calibri, sans-serif">α = 30°</text>

  <!-- Bloque y diagrama de cuerpo libre resuelto -->
  <g transform="translate(190, 105) rotate(-25)">
    <!-- Bloque -->
    <rect x="-35" y="-30" width="70" height="30" fill="#d0e1fd" stroke="#2b5797" stroke-width="2" rx="3"/>
    <text x="0" y="-11" text-anchor="middle" font-size="11.5" font-family="Calibri, sans-serif" font-weight="bold">m = 8 kg</text>

    <!-- Fuerza F hacia arriba -->
    <line x1="35" y1="-15" x2="105" y2="-15" stroke="#d9534f" stroke-width="2.8" marker-end="url(#arrFS)"/>
    <text x="110" y="-10" font-size="11" font-family="Calibri, sans-serif" font-weight="bold" fill="#d9534f">F = 85 N</text>

    <!-- Fuerza de rozamiento Fr hacia abajo del plano -->
    <line x1="-35" y1="-15" x2="-80" y2="-15" stroke="#e67e22" stroke-width="2.3" marker-end="url(#arrFrS)"/>
    <text x="-120" y="-10" font-size="10.5" font-family="Calibri, sans-serif" font-weight="bold" fill="#e67e22">F_r</text>

    <!-- Normal N perpendicular -->
    <line x1="0" y1="-30" x2="0" y2="-80" stroke="#2b5797" stroke-width="2.3" marker-end="url(#arrVS)"/>
    <text x="8" y="-70" font-size="11" font-family="Calibri, sans-serif" font-weight="bold" fill="#2b5797">N</text>

    <!-- Componente P_y hacia abajo -->
    <line x1="0" y1="0" x2="0" y2="50" stroke="#6c757d" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arrP)"/>
    <text x="6" y="45" font-size="10" font-family="Calibri, sans-serif" fill="#495057">P_y</text>

    <!-- Componente P_x hacia abajo -->
    <line x1="-35" y1="0" x2="-75" y2="0" stroke="#6c757d" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arrP)"/>
    <text x="-105" y="10" font-size="10" font-family="Calibri, sans-serif" fill="#495057">P_x</text>
  </g>
</svg>
</div>
"""

SVG_EJ6 = r"""
<div style="text-align: center; margin: 15px 0;">
<svg width="460" height="150" viewBox="0 0 460 150">
  <!-- Barra original -->
  <rect x="30" y="20" width="400" height="14" fill="#6c757d" stroke="#343a40" stroke-width="1.5" rx="3"/>
  <!-- Línea de corte -->
  <line x1="250" y1="12" x2="250" y2="42" stroke="#dc3545" stroke-width="2.5" stroke-dasharray="4,2"/>
  <text x="250" y="10" text-anchor="middle" font-family="Calibri, sans-serif" font-size="11" font-weight="bold" fill="#dc3545">Corte</text>

  <!-- Cotas de la barra -->
  <text x="140" y="52" text-anchor="middle" font-family="Calibri, sans-serif" font-size="11" font-weight="bold" fill="#2b5797">Trozo 1: x (m) ➔ Triángulo</text>
  <text x="335" y="52" text-anchor="middle" font-family="Calibri, sans-serif" font-size="11" font-weight="bold" fill="#28a745">Trozo 2: (12 - x) (m) ➔ Cuadrado</text>

  <!-- Triángulo equilátero -->
  <polygon points="100,140 140,140 120,105" fill="#cfe2ff" stroke="#2b5797" stroke-width="2"/>
  <text x="120" y="128" text-anchor="middle" font-family="Calibri, sans-serif" font-size="9.5" fill="#2b5797">l = x/3</text>

  <!-- Cuadrado -->
  <rect x="300" y="105" width="35" height="35" fill="#d1e7dd" stroke="#28a745" stroke-width="2"/>
  <text x="317" y="127" text-anchor="middle" font-family="Calibri, sans-serif" font-size="9.5" fill="#28a745">l = (12-x)/4</text>
</svg>
</div>
"""

SVG_EJ7 = r"""
<div style="text-align: center; margin: 15px 0;">
<svg width="440" height="230" viewBox="0 0 440 230">
  <!-- Ejes coordenados -->
  <line x1="20" y1="115" x2="420" y2="115" stroke="#444" stroke-width="1.8"/>
  <line x1="200" y1="15" x2="200" y2="215" stroke="#444" stroke-width="1.8"/>
  <text x="415" y="110" font-family="Calibri, sans-serif" font-size="12" font-weight="bold">X</text>
  <text x="205" y="25" font-family="Calibri, sans-serif" font-size="12" font-weight="bold">Y</text>

  <!-- Asíntota vertical x = -1 -->
  <line x1="175" y1="15" x2="175" y2="215" stroke="#dc3545" stroke-width="1.8" stroke-dasharray="5,4"/>
  <text x="140" y="30" font-family="Calibri, sans-serif" font-size="10.5" font-weight="bold" fill="#dc3545">x = -1</text>

  <!-- Asíntota horizontal y = 2 para x > 2 -->
  <line x1="250" y1="65" x2="420" y2="65" stroke="#28a745" stroke-width="1.8" stroke-dasharray="5,4"/>
  <text x="365" y="58" font-family="Calibri, sans-serif" font-size="10.5" font-weight="bold" fill="#28a745">y = 2 (x → +∞)</text>

  <!-- Asíntota horizontal y = -2 para x < -1 -->
  <line x1="20" y1="165" x2="175" y2="165" stroke="#28a745" stroke-width="1.8" stroke-dasharray="5,4"/>
  <text x="30" y="180" font-family="Calibri, sans-serif" font-size="10.5" font-weight="bold" fill="#28a745">y = -2 (x → -∞)</text>

  <!-- Curva tramo x < -1 -->
  <path d="M 30,172 Q 120,185 160,215" fill="none" stroke="#2b5797" stroke-width="2.5"/>

  <!-- Curva tramo -1 < x < 2 -->
  <path d="M 182,20 Q 188,40 200,65 Q 225,100 250,115" fill="none" stroke="#2b5797" stroke-width="2.5"/>

  <!-- Curva tramo x > 2 -->
  <path d="M 250,115 Q 290,75 410,68" fill="none" stroke="#2b5797" stroke-width="2.5"/>

  <!-- Puntos clave -->
  <circle cx="200" cy="65" r="4.5" fill="#6f42c1"/>
  <text x="206" y="65" font-family="Calibri, sans-serif" font-size="10.5" font-weight="bold" fill="#6f42c1">(0, 4)</text>

  <circle cx="250" cy="115" r="5" fill="#d9534f"/>
  <text x="245" y="132" font-family="Calibri, sans-serif" font-size="10.5" font-weight="bold" fill="#d9534f">(2, 0) Vértice anguloso</text>
</svg>
</div>
"""

# =========================================================================
# PLANTILLA HTML MAESTRA
# =========================================================================
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/mhchem.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 16mm 18mm 16mm 18mm;
  }
  * {
    box-sizing: border-box;
  }
  body {
    font-family: 'Calibri', 'Carlito', 'Segoe UI', sans-serif;
    font-size: 10.5pt;
    line-height: 1.36;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
  }
  .page {
    page-break-after: always;
    min-height: 255mm;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  .page:last-child {
    page-break-after: avoid;
  }
  .header-box {
    border-bottom: 2pt solid #2b5797;
    padding-bottom: 7px;
    margin-bottom: 12px;
    text-align: center;
  }
  .inst-title {
    font-size: 9.5pt;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #555;
    font-weight: bold;
    margin-bottom: 2px;
  }
  .doc-title {
    font-size: 14.5pt;
    font-weight: bold;
    color: #1b365d;
    margin-bottom: 2px;
  }
  .doc-subtitle {
    font-size: 10.5pt;
    font-weight: 600;
    color: #444;
  }
  .section-tag {
    display: inline-block;
    background: #e8eef7;
    color: #1b365d;
    font-weight: bold;
    font-size: 9.5pt;
    padding: 3px 8px;
    border-radius: 4px;
    margin-top: 4px;
    margin-bottom: 8px;
    border-left: 3.5px solid #2b5797;
  }
  .exercise-title {
    font-size: 11.5pt;
    font-weight: bold;
    color: #111;
    margin-top: 4px;
    margin-bottom: 6px;
  }
  .exercise-statement {
    text-align: justify;
    margin-bottom: 8px;
    font-size: 10.5pt;
  }
  .sub-list {
    margin: 4px 0 8px 0;
    padding-left: 22px;
  }
  .sub-list li {
    margin-bottom: 5px;
  }
  .box-sol {
    margin: 6px 0 10px 0;
    font-size: 10pt;
  }
  .sol-step {
    margin-bottom: 7px;
  }
  .sol-title {
    font-weight: bold;
    color: #1e3a8a;
  }
  .data-footer {
    font-size: 9.5pt;
    margin-top: 8px;
    color: #334155;
  }
  .bold { font-weight: bold; }
  .katex-display { margin: 5px 0 !important; }
</style>
</head>
<body>
__BODY__
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "$", right: "$", display: false},
        {left: "\\[", right: "\\]", display: true},
        {left: "\\(", right: "\\)", display: false}
      ],
      throwOnError: false
    });
  });
</script>
</body>
</html>
"""

# =========================================================================
# CONTENIDO 1: FICHA DE TRABAJO (SIN RESOLVER - PARA EL ALUMNO / IMPRIMIR)
# =========================================================================

body_unresolved = r"""
<!-- PÁGINA 1: EJERCICIO 1 -->
<div class="page">
  <div class="exercise-statement">
    <span class="bold">1.</span> Un futbolista golpea un balón situado en reposo sobre el césped horizontal comunicándole una velocidad inicial $v_0 = 20\text{ m/s}$ con un ángulo de elevación de $\alpha = 30^\circ$ sobre el suelo horizontal. Despreciando el rozamiento con el aire y tomando $g = 9{,}8\text{ m/s}^2$:
  </div>
  __SVG_EJ1__
  <ol class="sub-list" type="a">
    <li>Escribe las ecuaciones del movimiento en cada eje ($X$ e $Y$).</li>
    <li>Calcula el tiempo que tarda en alcanzar el punto más alto de su trayectoria y determina la altura máxima alcanzada sobre el suelo.</li>
    <li>Determina el tiempo total de permanencia en el aire hasta el instante en que contacta de nuevo contra el terreno de juego.</li>
    <li>Calcula la distancia horizontal medida sobre el suelo entre el punto inicial de lanzamiento y el punto de impacto.</li>
    <li>Halla las componentes cartesianas del vector velocidad y el módulo de la velocidad en el instante inmediatamente anterior a la colisión con el suelo.</li>
  </ol>
</div>

<!-- PÁGINA 2: EJERCICIO 2 -->
<div class="page">
  <div class="exercise-statement">
    <span class="bold">2.</span> Desde el borde superior de un acantilado vertical situado a una altura $h = 45\text{ m}$ sobre el nivel del mar, una dotación de emergencia lanza una cápsula de salvamento marítimo con una velocidad inicial $v_0 = 30\text{ m/s}$ orientada a un ángulo de $\alpha = 30^\circ$ por encima de la línea horizontal. Se considera despreciable la resistencia aerodinámica y se toma $g = 9{,}8\text{ m/s}^2$.
  </div>
  __SVG_EJ2__
  <ol class="sub-list" type="a">
    <li>Escribe las ecuaciones del movimiento en cada eje ($X$ e $Y$).</li>
    <li>Halla el tiempo que transcurre hasta alcanzar la cota más elevada del vuelo y determina dicha altura máxima absoluta respecto a la superficie marina.</li>
    <li>Determina el tiempo total que tarda la cápsula desde el instante de su lanzamiento hasta que impacta contra el agua del mar ($y = 0$).</li>
    <li>Calcula la distancia horizontal comprendida entre la base vertical del acantilado y el punto exacto de entrada en el agua marina.</li>
    <li>Calcula las componentes del vector velocidad de entrada en el agua y halla el módulo de la velocidad final de impacto.</li>
  </ol>
</div>

<!-- PÁGINA 3: EJERCICIO 3 -->
<div class="page">
  <div class="exercise-statement">
    <span class="bold">3.</span> Sobre una rampa rectilínea que forma un ángulo $\alpha = 30^\circ$ con el suelo horizontal descansa un cajón metálico de masa $m = 8\text{ kg}$. El coeficiente de rozamiento dinámico entre el cajón y la superficie de la rampa es $\mu = 0{,}20$. Para desplazarlo pendiente arriba, se aplica una fuerza constante $F = 85\text{ N}$ paralela en todo momento a la superficie de la rampa y orientada en sentido ascendente ($g = 9{,}8\text{ m/s}^2$).
  </div>
  __SVG_EJ3__
  <ol class="sub-list" type="a">
    <li>Dibuja el diagrama de cuerpo libre detallado, identificando y rotulando todas las fuerzas actuantes ($\vec{P}$, $\vec{N}$, $\vec{F}_r$ y $\vec{F}$) y descomponiendo vectorialmente el peso en las direcciones paralela y perpendicular al plano inclinado.</li>
    <li>Calcula el valor numérico exacto de la fuerza normal ejercida por el plano ($N$) y de la fuerza de rozamiento por deslizamiento ($F_r$).</li>
    <li>Aplica el principio fundamental de la dinámica (segunda ley de Newton) para deducir la aceleración $a$ con la que asciende el cajón.</li>
    <li>Sabiendo que el cajón arranca desde el reposo ($v_0 = 0$), halla el tiempo requerido para avanzar una distancia de $10\text{ m}$ a lo largo de la rampa y calcula la velocidad final que alcanza en ese instante.</li>
  </ol>
</div>

<!-- PÁGINA 4: EJERCICIOS 4 Y 5 -->
<div class="page">
  <div class="exercise-statement">
    <span class="bold">4.</span> En un ensayo de laboratorio se dispone de una probeta con $250\text{ mL}$ de una disolución acuosa de ácido sulfúrico ($\ce{H2SO4}$) de concentración $0{,}40\text{ M}$. Se desea neutralizar completamente dicho volumen mediante la adición controlada de hidróxido de sodio ($\ce{NaOH}$).
  </div>
  <ol class="sub-list" type="a">
    <li>Escribe y ajusta la ecuación química de la reacción de neutralización.</li>
    <li>Calcula la cantidad de sustancia (en moles) de ácido sulfúrico presentes en la muestra inicial y los moles de hidróxido de sodio estequiométricamente precisos para neutralizarlo.</li>
    <li>Determina la masa en gramos de reactivo puro $\ce{NaOH}$ correspondiente a dicha cantidad.</li>
    <li>Si en el laboratorio se dispone de una disolución comercial de sosa acuosa $1{,}25\text{ M}$, ¿qué volumen en mililitros de esta disolución se debe pipetear para completar la neutralización?</li>
    <li>Calcula la masa en gramos de sulfato de sodio ($\ce{Na2SO4}$) que se obtendrá en la disolución al concluir la reacción.</li>
  </ol>
  <div class="data-footer">
    <span class="bold">Datos atómicos:</span> Masas atómicas relativas ($\text{u}$): $\mathrm{H} = 1{,}0;\; \mathrm{O} = 16{,}0;\; \mathrm{Na} = 23{,}0;\; \mathrm{S} = 32{,}0$.
  </div>

  <div style="margin-top: 25px;"></div>
  <div class="exercise-statement">
    <span class="bold">5.</span> En un reactor industrial se introducen $56{,}0\text{ g}$ de gas nitrógeno puro ($\ce{N2}$) y $18{,}0\text{ g}$ de gas hidrógeno puro ($\ce{H2}$) a presión elevada para sintetizar amoniaco gaseoso según la reacción sin ajustar:
    $$\ce{N2 + 3 H2 -> 2 NH3}$$
  </div>
  <ol class="sub-list" type="a">
    <li>Ajusta la ecuación química y explica el significado molecular y molar de los coeficientes estequiométricos.</li>
    <li>Determina de forma cuantitativa y razonada cuál de los dos reactivos actúa como reactivo limitante y cuál está en exceso.</li>
    <li>Calcula la masa en gramos del reactivo en exceso que quedará sin consumir al agotarse el reactivo limitante.</li>
    <li>Calcula la masa teórica máxima de gas amoniaco ($\ce{NH3}$) susceptible de formarse suponiendo un rendimiento del $100\%$.</li>
    <li>Si las condiciones reales de operación fijan un rendimiento de la reacción del $85{,}0\%$, calcula la masa real de amoniaco producida y el volumen real que ocupará medido a temperatura ambiente de $25^\circ\text{C}$ ($298\text{ K}$) y $1\text{ atm}$ de presión ($R = 0{,}082\text{ atm}\cdot\text{L}/(\text{mol}\cdot\text{K})$).</li>
  </ol>
  <div class="data-footer">
    <span class="bold">Constantes y datos:</span> Masas atómicas relativas ($\text{u}$): $\mathrm{H} = 1{,}0;\; \mathrm{N} = 14{,}0$. Constante de los gases ideales: $R = 0{,}082\text{ atm}\cdot\text{L}/(\text{mol}\cdot\text{K})$ ($V_m \approx 24{,}4\text{ L/mol}$ a $25^\circ\text{C}$ y $1\text{ atm}$).
  </div>
</div>

<!-- PÁGINA 5: EJERCICIOS 6 Y 7 -->
<div class="page">
  <div class="exercise-statement">
    <span class="bold">6.</span> Se quiere enlosar un jardín con forma de triángulo rectángulo de catetos $42\text{ m}$ y $56\text{ m}$. Dentro del jardín se va a diferenciar un espacio rectangular techado de forma que dos de sus lados sean paralelos a los catetos del triángulo, un vértice coincida con el vértice del ángulo recto del triángulo y el vértice opuesto esté sobre su hipotenusa. Alicatar la parte cubierta cuesta $30\text{ €/m}^2$ y la parte no techada, $50\text{ €/m}^2$ pues las baldosas llevan un tratamiento especial resistente al agua. Calcule las dimensiones de la parte techada que hacen que el coste de instalar el suelo en el jardín sea mínimo.
  </div>

  <hr style="border: 0; border-top: 1px solid #cbd5e1; margin: 35px 0 25px 0;">

  <div class="exercise-statement">
    <span class="bold">7.</span> Se considera la función real de variable real definida por la expresión analítica:
    $$f(x) = \frac{|2x - 4|}{x + 1}$$
  </div>
  <ol class="sub-list" type="a">
    <li>Pinta la función.</li>
  </ol>
</div>
"""

# =========================================================================
# CONTENIDO 2: SOLUCIONARIO COMPLETO PASO A PASO (PARA EL PROFESOR / AUTOAPRENDIZAJE)
# =========================================================================

body_solved = r"""
<!-- PÁGINA 1 RESUELTA: EJERCICIO 1 -->
<div class="page">
  <div style="font-size: 12pt; font-weight: bold; color: #0f172a; margin-bottom: 8px;">Ejercicio 1</div>

  __SVG_EJ1__

  <div class="box-sol">
    <span class="sol-title">Condiciones iniciales y descomposición vectorial:</span><br>
    Posición inicial: $(x_0, y_0) = (0, 0)$. Componentes de la velocidad de salida ($v_0 = 20\text{ m/s}$, $\alpha = 30^\circ$):
    $$v_{0x} = v_0 \cos 30^\circ = 20 \cdot \frac{\sqrt{3}}{2} = 10\sqrt{3} \approx 17{,}32\text{ m/s}$$
    $$v_{0y} = v_0 \sin 30^\circ = 20 \cdot \frac{1}{2} = 10{,}00\text{ m/s}$$
  </div>

  <div class="sol-step">
    <span class="bold">a) Ecuaciones del movimiento en cada eje:</span>
    <ul>
      <li><b>Eje $X$ (MRU):</b> $\quad x(t) = v_{0x} \cdot t = \mathbf{10\sqrt{3}\,t\text{ (m)}} \approx 17{,}32\,t, \qquad v_x(t) = \mathbf{10\sqrt{3}\text{ m/s}} \approx 17{,}32\text{ m/s}$</li>
      <li><b>Eje $Y$ (MRUA):</b> $\quad y(t) = v_{0y} \cdot t - \frac{1}{2}gt^2 = \mathbf{10t - 4{,}9t^2\text{ (m)}}, \qquad v_y(t) = v_{0y} - gt = \mathbf{10 - 9{,}8t\text{ (m/s)}}$</li>
    </ul>
  </div>

  <div class="sol-step">
    <span class="bold">b) Altura máxima y tiempo de subida:</span><br>
    En el punto más alto, la velocidad vertical se anula instantáneamente ($v_y = 0$):
    $$10 - 9{,}8t_s = 0 \implies t_s = \frac{10}{9{,}8} = \frac{50}{49} \approx \mathbf{1{,}02\text{ s}}$$
    Sustituyendo en la coordenada vertical $y(t)$:
    $$y_{\text{máx}} = y(1{,}0204) = 10\left(\frac{50}{49}\right) - 4{,}9\left(\frac{50}{49}\right)^2 = \frac{500}{49} - \frac{250}{49} = \frac{250}{49} \approx \mathbf{5{,}10\text{ m}}$$
  </div>

  <div class="sol-step">
    <span class="bold">c) Tiempo total en el aire:</span><br>
    El balón toca el suelo cuando $y(t) = 0$:
    $$10t - 4{,}9t^2 = 0 \iff t(10 - 4{,}9t) = 0$$
    Descartando $t = 0$ (instante del despegue):
    $$t_{\text{vuelo}} = \frac{10}{4{,}9} = 2 \cdot t_s = \frac{100}{49} \approx \mathbf{2{,}04\text{ s}}$$
  </div>

  <div class="sol-step">
    <span class="bold">d) Distancia horizontal hasta el impacto:</span><br>
    Al ser un movimiento rectilíneo uniforme (MRU) en el eje horizontal:
    $$x_{\text{impacto}} = v_{0x} \cdot t_{\text{vuelo}} = 10\sqrt{3} \cdot \left(\frac{100}{49}\right) \approx 17{,}3205 \times 2{,}0408 = \mathbf{35{,}35\text{ m}}$$
  </div>

  <div class="sol-step">
    <span class="bold">e) Vector velocidad y módulo al chocar contra el suelo:</span>
    $$v_x(2{,}04) = 10\sqrt{3} \approx 17{,}32\text{ m/s}$$
    $$v_y(2{,}04) = 10 - 9{,}8\left(\frac{100}{49}\right) = 10 - 20 = -10{,}00\text{ m/s}$$
    $$\vec{v}_{\text{impacto}} = \mathbf{10\sqrt{3}\,\vec{i} - 10\,\vec{j}\text{ m/s}} \approx \mathbf{17{,}32\,\vec{i} - 10{,}00\,\vec{j}\text{ m/s}}$$
    $$|\vec{v}_{\text{impacto}}| = \sqrt{(10\sqrt{3})^2 + (-10)^2} = \sqrt{300 + 100} = \sqrt{400} = \mathbf{20{,}00\text{ m/s}}$$
    <i>(Por simetría parabólica sin rozamiento, impacta con la misma rapidez con la que fue lanzado).</i>
  </div>
</div>

<!-- PÁGINA 2 RESUELTA: EJERCICIO 2 -->
<div class="page">
  <div style="font-size: 12pt; font-weight: bold; color: #0f172a; margin-bottom: 8px;">Ejercicio 2</div>

  __SVG_EJ2__

  <div class="box-sol">
    <span class="sol-title">Condiciones iniciales:</span> Origen en la base del acantilado. $(x_0, y_0) = (0, 45\text{ m})$.<br>
    Descomposición de $v_0 = 30\text{ m/s}$ a $\alpha = 30^\circ$:
    $$v_{0x} = 30 \cos 30^\circ = 15\sqrt{3} \approx 25{,}98\text{ m/s}, \qquad v_{0y} = 30 \sin 30^\circ = 15{,}00\text{ m/s}$$
  </div>

  <div class="sol-step">
    <span class="bold">a) Ecuaciones del movimiento en cada eje:</span><br>
    Tomando el origen en la base del acantilado ($x_0 = 0$, $y_0 = 45\text{ m}$):
    <ul>
      <li><b>Eje $X$ (MRU):</b> $\quad x(t) = v_{0x} \cdot t = \mathbf{15\sqrt{3}\,t\text{ (m)}} \approx 25{,}98\,t, \qquad v_x(t) = \mathbf{15\sqrt{3}\text{ m/s}} \approx 25{,}98\text{ m/s}$</li>
      <li><b>Eje $Y$ (MRUA):</b> $\quad y(t) = y_0 + v_{0y} \cdot t - \frac{1}{2}gt^2 = \mathbf{45 + 15t - 4{,}9t^2\text{ (m)}}, \qquad v_y(t) = v_{0y} - gt = \mathbf{15 - 9{,}8t\text{ (m/s)}}$</li>
    </ul>
  </div>

  <div class="sol-step">
    <span class="bold">b) Altura máxima y tiempo hasta el vértice:</span><br>
    En la cúspide $v_y = 0 \implies 15 - 9{,}8t = 0 \implies t_{\text{cima}} = \frac{15}{9{,}8} \approx \mathbf{1{,}53\text{ s}}$.
    $$y_{\text{máx}} = 45 + 15(1{,}5306) - 4{,}9(1{,}5306)^2 = 45 + 22{,}96 - 11{,}48 = \mathbf{56{,}48\text{ m}}$$
  </div>

  <div class="sol-step">
    <span class="bold">c) Tiempo de vuelo hasta el impacto en el agua ($y = 0$):</span>
    $$45 + 15t - 4{,}9t^2 = 0 \iff 4{,}9t^2 - 15t - 45 = 0$$
    Aplicando la fórmula cuadrática:
    $$t = \frac{-(-15) \pm \sqrt{(-15)^2 - 4(4{,}9)(-45)}}{2(4{,}9)} = \frac{15 \pm \sqrt{225 + 882}}{9{,}8} = \frac{15 \pm \sqrt{1107}}{9{,}8}$$
    Como $\sqrt{1107} \approx 33{,}2716$:
    $$t = \frac{15 + 33{,}2716}{9{,}8} = \frac{48{,}2716}{9{,}8} \approx \mathbf{4{,}93\text{ s}}$$
    <i>(La raíz negativa $t = -1{,}86\text{ s}$ carece de significado temporal físico para el suceso).</i>
  </div>

  <div class="sol-step">
    <span class="bold">d) Distancia horizontal desde la base del acantilado:</span>
    $$x(4{,}9257) = 15\sqrt{3} \times 4{,}9257 = 25{,}9808 \times 4{,}9257 \approx \mathbf{127{,}97\text{ m}} \approx \mathbf{128{,}0\text{ m}}$$
  </div>

  <div class="sol-step">
    <span class="bold">e) Vector velocidad y módulo de impacto:</span>
    $$v_x(4{,}93) = 15\sqrt{3} \approx 25{,}98\text{ m/s}$$
    $$v_y(4{,}9257) = 15 - 9{,}8(4{,}9257) = 15 - 48{,}272 = -33{,}27\text{ m/s}$$
    $$\vec{v}_{\text{impacto}} = \mathbf{25{,}98\,\vec{i} - 33{,}27\,\vec{j}\text{ m/s}}$$
    $$|\vec{v}_{\text{impacto}}| = \sqrt{25{,}98^2 + (-33{,}27)^2} = \sqrt{675 + 1107} = \sqrt{1782} \approx \mathbf{42{,}21\text{ m/s}}$$
    <i>(Comprobación energética: $v = \sqrt{v_0^2 + 2gh} = \sqrt{900 + 2(9{,}8)(45)} = \sqrt{1782} \approx 42{,}21\text{ m/s}$).</i>
  </div>
</div>

<!-- PÁGINA 3 RESUELTA: EJERCICIO 3 -->
<div class="page">
  <div style="font-size: 12pt; font-weight: bold; color: #0f172a; margin-bottom: 8px;">Ejercicio 3</div>

  __SVG_EJ3__

  <div class="sol-step">
    <span class="bold">a) Diagrama de cuerpo libre y descomposición del peso:</span><br>
    Elegimos el eje $X'$ paralelo al plano (positivo pendiente arriba) y el eje $Y'$ perpendicular al plano (positivo hacia afuera).
    $$P = m \cdot g = 8\text{ kg} \times 9{,}8\text{ m/s}^2 = 78{,}40\text{ N}$$
    $$P_x = P \sin 30^\circ = 78{,}40 \cdot 0{,}5 = \mathbf{39{,}20\text{ N}} \quad (\text{hacia abajo del plano})$$
    $$P_y = P \cos 30^\circ = 78{,}40 \cdot \frac{\sqrt{3}}{2} = 39{,}20\sqrt{3} \approx \mathbf{67{,}90\text{ N}} \quad (\text{hacia el interior del plano})$$
  </div>

  <div class="sol-step">
    <span class="bold">b) Cálculo de la fuerza normal y de la fuerza de rozamiento:</span><br>
    En el eje perpendicular no hay desplazamiento ($\sum F_y = 0$):
    $$N - P_y = 0 \implies N = P_y = 67{,}896\text{ N} \approx \mathbf{67{,}90\text{ N}}$$
    La fuerza de rozamiento dinámico se opone al deslizamiento ascendente:
    $$F_r = \mu \cdot N = 0{,}20 \times 67{,}896\text{ N} \approx \mathbf{13{,}58\text{ N}}$$
  </div>

  <div class="sol-step">
    <span class="bold">c) Aplicación de la 2.ª Ley de Newton y aceleración de ascenso:</span><br>
    En el eje longitudinal de la rampa: $\sum F_x = m \cdot a$
    $$F - P_x - F_r = m \cdot a$$
    $$85 - 39{,}20 - 13{,}58 = 8 \cdot a \implies 32{,}22 = 8 \cdot a$$
    $$a = \frac{32{,}22\text{ N}}{8\text{ kg}} \approx \mathbf{4{,}03\text{ m/s}^2}$$
  </div>

  <div class="sol-step">
    <span class="bold">d) Cinemática del ascenso ($d = 10\text{ m}$, $v_0 = 0$):</span><br>
    Tratándose de un Movimiento Rectilíneo Uniformemente Acelerado (MRUA):
    $$d = \frac{1}{2} a t^2 \implies t = \sqrt{\frac{2d}{a}} = \sqrt{\frac{2 \times 10}{4{,}0275}} = \sqrt{4{,}9659} \approx \mathbf{2{,}23\text{ s}}$$
    Velocidad al completar los $10\text{ m}$:
    $$v = v_0 + a \cdot t = 4{,}0275 \times 2{,}2284 \approx \mathbf{8{,}98\text{ m/s}}$$
    <i>(Comprobación directa de Torricelli: $v = \sqrt{2 a d} = \sqrt{2 \times 4{,}0275 \times 10} = \sqrt{80{,}55} \approx 8{,}98\text{ m/s}$).</i>
  </div>
</div>

<!-- PÁGINA 4 RESUELTA: EJERCICIOS 4 Y 5 -->
<div class="page">
  <div style="font-size: 12pt; font-weight: bold; color: #0f172a; margin-bottom: 8px;">Ejercicio 4</div>
  <div class="sol-step">
    <span class="bold">a) Ecuación química ajustada:</span>
    $$\ce{H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O}$$
  </div>
  <div class="sol-step">
    <span class="bold">b) Cantidad de sustancia (moles) de ácido y base:</span>
    $$n(\ce{H2SO4}) = M \cdot V = 0{,}40\text{ mol/L} \times 0{,}250\text{ L} = \mathbf{0{,}100\text{ mol de } \ce{H2SO4}}$$
    Estequiometría: $1\text{ mol } \ce{H2SO4} \iff 2\text{ mol } \ce{NaOH} \implies n(\ce{NaOH}) = 0{,}100 \times 2 = \mathbf{0{,}200\text{ mol de } \ce{NaOH}}$.
  </div>
  <div class="sol-step">
    <span class="bold">c) Masa en gramos de $\ce{NaOH}$ puro:</span>
    $$M(\ce{NaOH}) = 23 + 16 + 1 = 40{,}0\text{ g/mol} \implies m(\ce{NaOH}) = 0{,}200\text{ mol} \times 40{,}0\text{ g/mol} = \mathbf{8{,}00\text{ g de } \ce{NaOH}}$$
  </div>
  <div class="sol-step">
    <span class="bold">d) Volumen de disolución acuosa $1{,}25\text{ M}$:</span>
    $$V = \frac{n}{M} = \frac{0{,}200\text{ mol}}{1{,}25\text{ mol/L}} = 0{,}160\text{ L} = \mathbf{160\text{ mL de disolución}}$$
  </div>
  <div class="sol-step">
    <span class="bold">e) Masa de sulfato de sodio ($\ce{Na2SO4}$) formada:</span>
    $$M(\ce{Na2SO4}) = 2(23) + 32 + 4(16) = 142{,}0\text{ g/mol}$$
    $$n(\ce{Na2SO4}) = 0{,}100\text{ mol} \implies m(\ce{Na2SO4}) = 0{,}100\text{ mol} \times 142{,}0\text{ g/mol} = \mathbf{14{,}20\text{ g de } \ce{Na2SO4}}$$
  </div>

  <hr style="border: 0; border-top: 1px solid #cbd5e1; margin: 15px 0;">

  <div style="font-size: 12pt; font-weight: bold; color: #0f172a; margin-bottom: 8px;">Ejercicio 5</div>
  <div class="sol-step">
    <span class="bold">a) Ecuación ajustada y significado molar:</span>
    $$\ce{N2 (g) + 3 H2 (g) -> 2 NH3 (g)}$$
    $1\text{ mol}$ de moléculas de nitrógeno gas reacciona con $3\text{ moles}$ de moléculas de hidrógeno para originar $2\text{ moles}$ de amoniaco gaseoso.
  </div>
  <div class="sol-step">
    <span class="bold">b) Determinación del reactivo limitante:</span>
    $$M(\ce{N2}) = 28{,}0\text{ g/mol} \implies n(\ce{N2}) = \frac{56{,}0\text{ g}}{28{,}0\text{ g/mol}} = 2{,}00\text{ mol}$$
    $$M(\ce{H2}) = 2{,}0\text{ g/mol} \implies n(\ce{H2}) = \frac{18{,}0\text{ g}}{2{,}0\text{ g/mol}} = 9{,}00\text{ mol}$$
    Proporción estequiométrica: Para consumir $2{,}00\text{ mol de } \ce{N2}$ se requieren $2{,}00 \times 3 = 6{,}00\text{ mol de } \ce{H2}$. Al disponer de $9{,}00\text{ mol}$, el <b>reactivo limitante es el $\ce{N2}$</b> y el <b>$\ce{H2}$ está en exceso</b>.
  </div>
  <div class="sol-step">
    <span class="bold">c) Reactivo en exceso sin reaccionar:</span>
    $$n_{\text{sobrante}}(\ce{H2}) = 9{,}00 - 6{,}00 = 3{,}00\text{ mol} \implies m_{\text{sobrante}}(\ce{H2}) = 3{,}00\text{ mol} \times 2{,}0\text{ g/mol} = \mathbf{6{,}00\text{ g de } \ce{H2}}$$
  </div>
  <div class="sol-step">
    <span class="bold">d) Masa teórica máxima de $\ce{NH3}$ (rendimiento $100\%$):</span>
    $$n_{\text{teórico}}(\ce{NH3}) = 2{,}00\text{ mol } \ce{N2} \times 2 = 4{,}00\text{ mol de } \ce{NH3}$$
    $$M(\ce{NH3}) = 14 + 3(1) = 17{,}0\text{ g/mol} \implies m_{\text{teórica}} = 4{,}00\text{ mol} \times 17{,}0\text{ g/mol} = \mathbf{68{,}00\text{ g de } \ce{NH3}}$$
  </div>
  <div class="sol-step">
    <span class="bold">e) Producción real al $85{,}0\%$ de rendimiento y volumen a $25^\circ\text{C}$ ($298\text{ K}$) y $1\text{ atm}$:</span>
    $$m_{\text{real}}(\ce{NH3}) = 68{,}00\text{ g} \times 0{,}850 = \mathbf{57{,}80\text{ g de } \ce{NH3}}$$
    $$n_{\text{real}}(\ce{NH3}) = 4{,}00\text{ mol} \times 0{,}850 = 3{,}40\text{ mol de } \ce{NH3}$$
    $$V_{\text{real}} = \frac{n_{\text{real}} \cdot R \cdot T}{P} = \frac{3{,}40\text{ mol} \times 0{,}082\text{ atm}\cdot\text{L}/(\text{mol}\cdot\text{K}) \times 298\text{ K}}{1\text{ atm}} = \mathbf{83{,}08\text{ L de } \ce{NH3}}$$
    <i>(O empleando el volumen molar a $25^\circ\text{C}$: $V_{\text{real}} = 3{,}40\text{ mol} \times 24{,}4\text{ L/mol} = \mathbf{82{,}96\text{ L}}$).</i>
  </div>
</div>

<!-- PÁGINA 5 RESUELTA: EJERCICIO 6 -->
<div class="page">
  <div style="font-size: 12pt; font-weight: bold; color: #0f172a; margin-bottom: 8px;">Ejercicio 6</div>

  <div class="sol-step">
    <span class="bold">1. Planteamiento geométrico y relación entre variables:</span><br>
    Consideramos el jardín triangular rectángulo con catetos de longitud $56\text{ m}$ (base horizontal) y $42\text{ m}$ (altura vertical). El área total del jardín es:
    $$A_{\text{total}} = \frac{56 \times 42}{2} = 1176\text{ m}^2$$
    Dentro del jardín se inscribe un espacio rectangular techado de dimensiones $x$ e $y$ paralelas a los catetos, con un vértice en el ángulo recto y el vértice opuesto $(x, y)$ apoyado sobre la hipotenusa.<br>
    Por semejanza de triángulos entre el triángulo superior y el triángulo total (o por la recta de la hipotenusa $\frac{x}{56} + \frac{y}{42} = 1$):
    $$\frac{42 - y}{x} = \frac{42}{56} = \frac{3}{4} \implies 4(42 - y) = 3x \implies y = 42 - \frac{3}{4}x \quad (0 \le x \le 56)$$
    Las superficies de cada zona se expresan en función de $x$:
    <ul>
      <li><b>Parte techada:</b> $\quad A_{\text{techada}}(x) = x \cdot y = x\left(42 - \frac{3}{4}x\right) = 42x - \frac{3}{4}x^2$</li>
      <li><b>Parte no techada:</b> $\quad A_{\text{no techada}}(x) = A_{\text{total}} - A_{\text{techada}} = 1176 - \left(42x - \frac{3}{4}x^2\right)$</li>
    </ul>
  </div>

  <div class="sol-step">
    <span class="bold">2. Función objetivo de coste total:</span><br>
    El coste unitario es de $30\text{ €/m}^2$ para la parte cubierta y de $50\text{ €/m}^2$ para la descubierta:
    $$C(x) = 30 \cdot A_{\text{techada}} + 50 \cdot A_{\text{no techada}} = 30 \cdot A_{\text{techada}} + 50(1176 - A_{\text{techada}}) = 58800 - 20 \cdot A_{\text{techada}}$$
    Sustituyendo $A_{\text{techada}}(x)$:
    $$C(x) = 58800 - 20\left(42x - \frac{3}{4}x^2\right) = \mathbf{15x^2 - 840x + 58800}, \quad x \in [0, 56]$$
    <i>(Nótese que minimizar el coste equivale a maximizar el área techada, puesto que cada metro cuadrado cubierto ahorra $20\text{ €}$ frente a dejarlo a la intemperie).</i>
  </div>

  <div class="sol-step">
    <span class="bold">3. Búsqueda del mínimo (cálculo de derivadas):</span><br>
    Derivamos la función de coste respecto a la variable $x$:
    $$C'(x) = 30x - 840$$
    Igualamos a cero para obtener el punto crítico:
    $$30x - 840 = 0 \implies 30x = 840 \implies \mathbf{x = \frac{840}{30} = 28\text{ m}}$$
    <b>Justificación del extremo (segunda derivada):</b>
    $$C''(x) = 30 > 0 \quad \forall x \in \mathbb{R}$$
    Al ser la segunda derivada estrictamente positiva en todo el dominio, la función es convexa y el punto crítico $\mathbf{x = 28\text{ m}}$ corresponde a un <b>mínimo absoluto</b>.
  </div>

  <div class="sol-step">
    <span class="bold">4. Dimensiones óptimas y coste mínimo resultante:</span><br>
    Calculamos la otra dimensión $y$ sustituyendo $x = 28\text{ m}$:
    $$y = 42 - \frac{3}{4}(28) = 42 - 21 = \mathbf{21\text{ m}}$$
    <b>Conclusión:</b> Las dimensiones del espacio rectangular techado que hacen mínimo el coste de instalación son de $\mathbf{28\text{ metros}}$ y $\mathbf{21\text{ metros}}$ (coincidentes con la mitad exacta de cada uno de los catetos del jardín).
    <br><br>
    <i>Comprobación de valores asociados:</i>
    <ul>
      <li>Área techada: $A_{\text{techada}} = 28 \times 21 = \mathbf{588\text{ m}^2}$ (la mitad del área total).</li>
      <li>Área no techada: $A_{\text{no techada}} = 1176 - 588 = \mathbf{588\text{ m}^2}$.</li>
      <li>Coste mínimo total: $C(28) = 30 \times 588 + 50 \times 588 = 80 \times 588 = \mathbf{47\,040\text{ €}}$.</li>
    </ul>
  </div>
</div>

<!-- PÁGINA 6 RESUELTA: EJERCICIO 7 -->
<div class="page">
  <div style="font-size: 12pt; font-weight: bold; color: #0f172a; margin-bottom: 8px;">Ejercicio 7</div>

  __SVG_EJ7__

  <div class="sol-step">
    <span class="bold">1. Desdoblamiento por tramos:</span><br>
    El argumento del valor absoluto cambia de signo en $2x - 4 = 0 \iff x = 2$:
    $$|2x - 4| = \begin{cases} -(2x - 4) = 4 - 2x, & \text{si } x < 2 \\ 2x - 4, & \text{si } x \ge 2 \end{cases}$$
    Por consiguiente, para todo $x \ne -1$:
    $$f(x) = \begin{cases} \mathbf{\dfrac{4 - 2x}{x + 1}}, & \text{si } x < 2 \text{ con } x \ne -1 \\[9pt] \mathbf{\dfrac{2x - 4}{x + 1}}, & \text{si } x \ge 2 \end{cases}$$
  </div>

  <div class="sol-step">
    <span class="bold">2. Dominio, cortes con los ejes y signo:</span>
    <ul>
      <li><b>Dominio:</b> $\mathbf{\text{Dom}(f) = \mathbb{R} \setminus \{-1\} = (-\infty, -1) \cup (-1, +\infty)}$.</li>
      <li><b>Corte con el eje $OX$ ($y = 0$):</b> $|2x - 4| = 0 \implies 2x - 4 = 0 \implies x = 2 \implies \mathbf{(2, 0)}$.</li>
      <li><b>Corte con el eje $OY$ ($x = 0$):</b> $f(0) = \frac{|-4|}{0+1} = 4 \implies \mathbf{(0, 4)}$.</li>
      <li><b>Signo:</b> Dado que $|2x - 4| \ge 0$, el signo viene determinado exclusivamente por el denominador $(x + 1)$:
        <br>— Para $x \in (-\infty, -1)$: $f(x) < 0$ (negativa).
        <br>— Para $x \in (-1, 2) \cup (2, +\infty)$: $f(x) > 0$ (positiva). En $x = 2$: $f(2) = 0$.
      </li>
    </ul>
  </div>

  <div class="sol-step">
    <span class="bold">3. Estudio de asíntotas y ramas infinitas:</span>
    <ul>
      <li><b>Asíntota Vertical en $x = -1$:</b>
        $$\lim_{x \to -1^-} f(x) = \lim_{x \to -1^-} \frac{4 - 2x}{x + 1} = \frac{6}{0^-} = \mathbf{-\infty}$$
        $$\lim_{x \to -1^+} f(x) = \lim_{x \to -1^+} \frac{4 - 2x}{x + 1} = \frac{6}{0^+} = \mathbf{+\infty}$$
        Por tanto, la recta $\mathbf{x = -1}$ es asíntota vertical bilateral.
      </li>
      <li><b>Asíntotas Horizontales:</b>
        <br>— Rama hacia $+\infty$: $\lim_{x \to +\infty} \frac{2x - 4}{x + 1} = \mathbf{2} \implies \mathbf{y = 2}$ es asíntota horizontal hacia $+\infty$.
        <br>Posición relativa: $f(x) - 2 = \frac{2x - 4 - 2x - 2}{x + 1} = \frac{-6}{x + 1} < 0 \implies$ la curva discurre <i>por debajo</i> de $y = 2$.
        <br>— Rama hacia $-\infty$: $\lim_{x \to -\infty} \frac{4 - 2x}{x + 1} = \mathbf{-2} \implies \mathbf{y = -2}$ es asíntota horizontal hacia $-\infty$.
        <br>Posición relativa: $f(x) - (-2) = \frac{4 - 2x + 2x + 2}{x + 1} = \frac{6}{x + 1} < 0 \implies$ la curva discurre <i>por debajo</i> de $y = -2$.
      </li>
    </ul>
  </div>

  <div class="sol-step">
    <span class="bold">4. Monotonía y punto anguloso en $x = 2$:</span>
    <ul>
      <li>Para $x < 2$ ($x \ne -1$): $f'(x) = \frac{-2(x+1) - (4-2x)}{(x+1)^2} = \mathbf{\frac{-6}{(x+1)^2} < 0} \implies$ <b>Estrictamente decreciente</b> en $(-\infty, -1)$ y en $(-1, 2)$.</li>
      <li>Para $x > 2$: $f'(x) = \frac{2(x+1) - (2x-4)}{(x+1)^2} = \mathbf{\frac{6}{(x+1)^2} > 0} \implies$ <b>Estrictamente creciente</b> en $(2, +\infty)$.</li>
      <li><b>Derivadas laterales en $x = 2$:</b>
        $$f'_-(2) = \lim_{x \to 2^-} \frac{-6}{(x+1)^2} = \frac{-6}{3^2} = -\frac{2}{3}$$
        $$f'_+(2) = \lim_{x \to 2^+} \frac{6}{(x+1)^2} = \frac{6}{3^2} = \frac{2}{3}$$
        Al ser $f'_-(2) \ne f'_+(2)$, la función <b>no es derivable en $x = 2$</b>. La gráfica presenta un <b>punto anguloso</b> en $(2, 0)$, que constituye un mínimo relativo estricto.
      </li>
    </ul>
  </div>
</div>
"""

# =========================================================================
# CÓDIGO FUENTE LATEX (TEX) PARA ARCHIVO EDITABLE
# =========================================================================

tex_unresolved = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage[version=4]{mhchem}
\usepackage{enumitem}
\usepackage{microtype}

\setmainfont{Calibri}
\linespread{1.15}

\begin{document}
\pagestyle{empty}

\begin{center}
    {\LARGE \textbf{Bolsa de Ejercicios — 4.º ESO / 1.º de Bachillerato}}\\[6pt]
    {\normalsize Nombre: \underline{\hspace{8cm}} \quad Fecha: \underline{\hspace{3cm}}}
\end{center}

\vspace{0.5cm}
\noindent\textbf{1.} Un futbolista golpea un balón situado en reposo sobre el césped horizontal comunicándole una velocidad inicial $v_0 = 20\text{ m/s}$ con un ángulo de elevación de $\alpha = 30^\circ$ sobre el suelo horizontal. Despreciando el rozamiento con el aire y tomando $g = 9{,}8\text{ m/s}^2$:
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Escribe las ecuaciones del movimiento en cada eje ($X$ e $Y$).
    \item Calcula el tiempo que tarda en alcanzar el punto más alto de su trayectoria y determina la altura máxima alcanzada sobre el suelo.
    \item Determina el tiempo total de permanencia en el aire hasta el instante en que contacta de nuevo contra el terreno de juego.
    \item Calcula la distancia horizontal medida sobre el suelo entre el punto inicial de lanzamiento y el punto de impacto.
    \item Halla las componentes cartesianas del vector velocidad y el módulo de la velocidad en el instante inmediatamente anterior a la colisión con el suelo.
\end{enumerate}

\vspace{0.4cm}
\noindent\textbf{2.} Desde el borde superior de un acantilado vertical situado a una altura $h = 45\text{ m}$ sobre el nivel del mar, una dotación de emergencia lanza una cápsula de salvamento marítimo con una velocidad inicial $v_0 = 30\text{ m/s}$ orientada a un ángulo de $\alpha = 30^\circ$ por encima de la línea horizontal. Se considera despreciable la resistencia aerodinámica y se toma $g = 9{,}8\text{ m/s}^2$.
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Escribe las ecuaciones del movimiento en cada eje ($X$ e $Y$).
    \item Halla el tiempo que transcurre hasta alcanzar la cota más elevada del vuelo y determina dicha altura máxima absoluta respecto a la superficie marina.
    \item Determina el tiempo total que tarda la cápsula desde el instante de su lanzamiento hasta que impacta contra el agua del mar ($y = 0$).
    \item Calcula la distancia horizontal comprendida entre la base vertical del acantilado y el punto exacto de entrada en el agua marina.
    \item Calcula las componentes del vector velocidad de entrada en el agua y halla el módulo de la velocidad final de impacto.
\end{enumerate}

\newpage

\noindent\textbf{3.} Sobre una rampa rectilínea que forma un ángulo $\alpha = 30^\circ$ con el suelo horizontal descansa un cajón metálico de masa $m = 8\text{ kg}$. El coeficiente de rozamiento dinámico entre el cajón y la superficie de la rampa es $\mu = 0{,}20$. Para desplazarlo pendiente arriba, se aplica una fuerza constante $F = 85\text{ N}$ paralela en todo momento a la superficie de la rampa y orientada en sentido ascendente ($g = 9{,}8\text{ m/s}^2$).
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Dibuja el diagrama de cuerpo libre detallado, identificando y rotulando todas las fuerzas actuantes ($\vec{P}$, $\vec{N}$, $\vec{F}_r$ y $\vec{F}$) y descomponiendo vectorialmente el peso en las direcciones paralela y perpendicular al plano inclinado.
    \item Calcula el valor numérico exacto de la fuerza normal ejercida por el plano ($N$) y de la fuerza de rozamiento por deslizamiento ($F_r$).
    \item Aplica el principio fundamental de la dinámica (segunda ley de Newton) para deducir la aceleración $a$ con la que asciende el cajón.
    \item Sabiendo que el cajón arranca desde el reposo ($v_0 = 0$), halla el tiempo requerido para avanzar una distancia de $10\text{ m}$ a lo largo de la rampa y calcula la velocidad final que alcanza en ese instante.
\end{enumerate}

\vspace{0.4cm}
\noindent\textbf{4.} En un ensayo de laboratorio se dispone de una probeta con $250\text{ mL}$ de una disolución acuosa de ácido sulfúrico (\ce{H2SO4}) de concentración $0{,}40\text{ M}$. Se desea neutralizar completamente dicho volumen mediante la adición controlada de hidróxido de sodio (\ce{NaOH}).
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Escribe y ajusta la ecuación química de la reacción de neutralización.
    \item Calcula la cantidad de sustancia (en moles) de ácido sulfúrico presentes en la muestra inicial y los moles de hidróxido de sodio estequiométricamente precisos para neutralizarlo.
    \item Determina la masa en gramos de reactivo puro \ce{NaOH} correspondiente a dicha cantidad.
    \item Si en el laboratorio se dispone de una disolución comercial de sosa acuosa $1{,}25\text{ M}$, ¿qué volumen en mililitros de esta disolución se debe pipetear para completar la neutralización?
    \item Calcula la masa en gramos de sulfato de sodio (\ce{Na2SO4}) que se obtendrá en la disolución al concluir la reacción.
\end{enumerate}
\noindent\textbf{Datos atómicos:} Masas atómicas relativas ($\text{u}$): $\mathrm{H} = 1{,}0;\; \mathrm{O} = 16{,}0;\; \mathrm{Na} = 23{,}0;\; \mathrm{S} = 32{,}0$.

\vspace{0.4cm}
\noindent\textbf{5.} En un reactor industrial se introducen $56{,}0\text{ g}$ de gas nitrógeno puro (\ce{N2}) y $18{,}0\text{ g}$ de gas hidrógeno puro (\ce{H2}) a presión elevada para sintetizar amoniaco gaseoso según la reacción sin ajustar: $\ce{N2 (g) + H2 (g) -> NH3 (g)}$.
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Ajusta la ecuación química y explica el significado molecular y molar de los coeficientes estequiométricos.
    \item Determina de forma cuantitativa y razonada cuál de los dos reactivos actúa como reactivo limitante y cuál está en exceso.
    \item Calcula la masa en gramos del reactivo en exceso que quedará sin consumir al agotarse el reactivo limitante.
    \item Calcula la masa teórica máxima de gas amoniaco (\ce{NH3}) susceptible de formarse suponiendo un rendimiento del $100\%$.
    \item Si las condiciones reales de operación fijan un rendimiento de la reacción del $85{,}0\%$, calcula la masa real de amoniaco producida y el volumen real que ocupará medido a temperatura ambiente de $25^\circ\text{C}$ ($298\text{ K}$) y $1\text{ atm}$ de presión ($R = 0{,}082\text{ atm}\cdot\text{L}/(\text{mol}\cdot\text{K})$).
\end{enumerate}
\noindent\textbf{Constantes y datos:} Masas atómicas relativas ($\text{u}$): $\mathrm{H} = 1{,}0;\; \mathrm{N} = 14{,}0$. Constante de los gases ideales: $R = 0{,}082\text{ atm}\cdot\text{L}/(\text{mol}\cdot\text{K})$ ($V_m \approx 24{,}4\text{ L/mol}$ a $25^\circ\text{C}$ y $1\text{ atm}$).

\newpage

\noindent\textbf{6.} Se quiere enlosar un jardín con forma de triángulo rectángulo de catetos $42\text{ m}$ y $56\text{ m}$. Dentro del jardín se va a diferenciar un espacio rectangular techado de forma que dos de sus lados sean paralelos a los catetos del triángulo, un vértice coincida con el vértice del ángulo recto del triángulo y el vértice opuesto esté sobre su hipotenusa. Alicatar la parte cubierta cuesta $30\text{ €/m}^2$ y la parte no techada, $50\text{ €/m}^2$ pues las baldosas llevan un tratamiento especial resistente al agua. Calcule las dimensiones de la parte techada que hacen que el coste de instalar el suelo en el jardín sea mínimo.

\vspace{0.4cm}
\noindent\textbf{7.} Se considera la función real de variable real definida por la expresión analítica:
\[
f(x) = \frac{|2x - 4|}{x + 1}
\]
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em]
    \item Pinta la función.
\end{enumerate}

\end{document}
"""

def insert_svgs(content, is_solved=False):
    svg_ej3_to_use = SVG_EJ3_SOLVED if is_solved else SVG_EJ3
    return (content
        .replace("__SVG_EJ1__", SVG_EJ1)
        .replace("__SVG_EJ2__", SVG_EJ2)
        .replace("__SVG_EJ3__", svg_ej3_to_use)
        .replace("__SVG_EJ6__", SVG_EJ6)
        .replace("__SVG_EJ7__", SVG_EJ7)
    )

def compile_pdf(title, body_content, target_pdf_name, is_solved=False):
    resolved_body = insert_svgs(body_content, is_solved=is_solved)
    html_str = HTML_TEMPLATE.replace("__TITLE__", title).replace("__BODY__", resolved_body)
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
        print(f"Éxito: {target_pdf_name} ({os.path.getsize(target_pdf)} bytes)")
    else:
        print(f"Error generando {target_pdf_name}: {res.stderr}")

if __name__ == "__main__":
    import shutil
    # Guardar archivos TeX para referencia
    for tex_name in ["ejercicios varios.tex", "ejercicios_bolsa_4eso_1bach.tex"]:
        with open(os.path.join(OUTPUT_DIR, tex_name), "w", encoding="utf-8") as f:
            f.write(tex_unresolved)
        print(f"Guardado {tex_name}")

    if os.path.exists(os.path.join(OUTPUT_DIR, "ejercicios_bolsa_4eso_1bach_resueltos.tex")):
        shutil.copyfile(
            os.path.join(OUTPUT_DIR, "ejercicios_bolsa_4eso_1bach_resueltos.tex"),
            os.path.join(OUTPUT_DIR, "ejercicios varios resueltos.tex")
        )

    # Compilar PDFs usando Microsoft Edge Headless con KaTeX
    compile_pdf(
        "Ejercicios Varios",
        body_unresolved,
        "ejercicios varios.pdf",
        is_solved=False
    )
    
    compile_pdf(
        "Ejercicios Varios — Resueltos",
        body_solved,
        "ejercicios varios resueltos.pdf",
        is_solved=True
    )
    
    # Mantener sincronizados los nombres anteriores también
    shutil.copyfile(os.path.join(OUTPUT_DIR, "ejercicios varios.pdf"), os.path.join(OUTPUT_DIR, "ejercicios_bolsa_4eso_1bach.pdf"))
    shutil.copyfile(os.path.join(OUTPUT_DIR, "ejercicios varios resueltos.pdf"), os.path.join(OUTPUT_DIR, "ejercicios_bolsa_4eso_1bach_resueltos.pdf"))
