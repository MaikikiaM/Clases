import os
import subprocess

OUTPUT_DIR = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Fisica\Cinematica"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# SVG Diagram: Vector and Unit Vector
SVG_VECTOR_UNIT = r"""
<div style="text-align: center; margin: 12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150">
  <defs>
    <marker id="ar_blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0275d8"/></marker>
    <marker id="ar_green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0ca678"/></marker>
  </defs>
  <!-- Axes -->
  <line x1="30" y1="130" x2="310" y2="130" stroke="#aaa" stroke-width="1.5"/>
  <line x1="40" y1="140" x2="40" y2="20" stroke="#aaa" stroke-width="1.5"/>
  <text x="315" y="134" font-size="11" font-family="Segoe UI, sans-serif" fill="#666">x</text>
  <text x="36" y="15" font-size="11" font-family="Segoe UI, sans-serif" fill="#666">y</text>
  
  <!-- Vector v = (3, 4) scaled -->
  <!-- Origin at (40, 130). Target (40 + 3*60 = 220, 130 - 4*25 = 30) -->
  <line x1="40" y1="130" x2="220" y2="30" stroke="#0275d8" stroke-width="3" marker-end="url(#ar_blue)"/>
  <text x="225" y="32" font-size="13" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#0275d8">v = (3, 4) &rarr; |v| = 5</text>
  
  <!-- Unit Vector u = (3/5, 4/5) -->
  <line x1="40" y1="130" x2="76" y2="110" stroke="#0ca678" stroke-width="4" marker-end="url(#ar_green)"/>
  <text x="82" y="112" font-size="12" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#0ca678">u = v / |v| (|u| = 1)</text>
</svg>
</div>
"""

# SVG Diagram: Trajectory with Tangential and Normal Acceleration
SVG_KINEMATICS_DECOMP = r"""
<div style="text-align: center; margin: 12px 0;">
<svg width="360" height="150" viewBox="0 0 360 150">
  <defs>
    <marker id="ar_red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#e03131"/></marker>
    <marker id="ar_green2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0ca678"/></marker>
    <marker id="ar_purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#7c3aed"/></marker>
    <marker id="ar_orange" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#f76707"/></marker>
  </defs>
  <!-- Parabolic curve -->
  <path d="M 30 130 Q 150 10 330 130" fill="none" stroke="#adb5bd" stroke-width="2" stroke-dasharray="5"/>
  
  <!-- Point P at t=1 -->
  <circle cx="110" cy="52" r="4" fill="#333"/>
  <text x="92" y="44" font-size="11" font-family="Segoe UI, sans-serif" font-weight="bold">P(x, y)</text>
  
  <!-- Velocity vector (tangent) -->
  <line x1="110" y1="52" x2="190" y2="28" stroke="#0ca678" stroke-width="2.5" marker-end="url(#ar_green2)"/>
  <text x="195" y="26" font-size="12" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#0ca678">v(t) (Tangente)</text>
  
  <!-- Total Acceleration a = (0, -10) -->
  <line x1="110" y1="52" x2="110" y2="125" stroke="#e03131" stroke-width="2.5" marker-end="url(#ar_red)"/>
  <text x="115" y="125" font-size="12" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#e03131">a = g (Vertical)</text>
  
  <!-- Tangential component at -->
  <line x1="110" y1="52" x2="80" y2="61" stroke="#f76707" stroke-width="2.5" marker-end="url(#ar_orange)"/>
  <text x="50" y="78" font-size="11" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#f76707">a_t (frena)</text>
  
  <!-- Normal component an -->
  <line x1="110" y1="52" x2="135" y2="115" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#ar_purple)"/>
  <text x="140" y="112" font-size="11" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#7c3aed">a_n (curva)</text>
</svg>
</div>
"""

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Guía Visual: Vectores y Derivadas en Física</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 16mm 18mm 16mm 18mm;
  }
  * {
    box-sizing: border-box;
  }
  body {
    font-family: 'Segoe UI', 'Calibri', sans-serif;
    font-size: 10.5pt;
    line-height: 1.35;
    color: #1f2937;
    margin: 0;
    padding: 0;
  }
  .page {
    page-break-after: always;
    min-height: 265mm;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  .page:last-child {
    page-break-after: avoid;
  }
  
  /* Modern Header */
  .doc-header {
    background: linear-gradient(135deg, #1e3a8a, #3b82f6);
    color: white;
    padding: 12px 18px;
    border-radius: 8px;
    margin-bottom: 12px;
    text-align: center;
  }
  .doc-title {
    font-size: 15pt;
    font-weight: 800;
    margin-bottom: 2px;
    letter-spacing: 0.3px;
  }
  .doc-subtitle {
    font-size: 10.5pt;
    font-weight: 500;
    opacity: 0.95;
  }

  /* Colored Content Cards */
  .card-blue {
    background: #f0f7ff;
    border: 1.5px solid #3b82f6;
    border-left: 6px solid #1d4ed8;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 12px;
  }
  .card-purple {
    background: #faf5ff;
    border: 1.5px solid #a855f7;
    border-left: 6px solid #7e22ce;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 12px;
  }
  .card-green {
    background: #f0fdf4;
    border: 1.5px solid #22c55e;
    border-left: 6px solid #15803d;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 12px;
  }
  .card-amber {
    background: #fffbeb;
    border: 1.5px solid #f59e0b;
    border-left: 6px solid #b45309;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 12px;
  }

  .card-title {
    font-size: 11pt;
    font-weight: bold;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
  }
  .card-title.blue { color: #1e40af; }
  .card-title.purple { color: #6b21a8; }
  .card-title.green { color: #166534; }
  .card-title.amber { color: #92400e; }

  .badge {
    display: inline-block;
    padding: 2px 7px;
    font-size: 8.5pt;
    font-weight: 700;
    border-radius: 4px;
    color: white;
    margin-right: 6px;
    text-transform: uppercase;
  }
  .bg-blue { background-color: #2563eb; }
  .bg-purple { background-color: #7c3aed; }
  .bg-green { background-color: #16a34a; }
  .bg-amber { background-color: #d97706; }

  .step-num {
    background: #1e3a8a;
    color: white;
    font-weight: bold;
    display: inline-block;
    width: 19px;
    height: 19px;
    line-height: 19px;
    border-radius: 50%;
    text-align: center;
    font-size: 9pt;
    margin-right: 4px;
  }

  .highlight-result {
    background: #fef08a;
    border: 1px solid #eab308;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: bold;
    color: #713f12;
  }

  ul, ol {
    margin: 4px 0;
    padding-left: 20px;
  }
  li {
    margin-bottom: 4px;
  }
  p {
    margin: 4px 0;
  }
  .bold { font-weight: bold; }
  .katex-display { margin: 6px 0 !important; }
</style>
</head>
<body>

<!-- ========================================================================= -->
<!-- PÁGINA 1: PARTE 1 - VECTORES Y FUERZAS VECTORIALES                       -->
<!-- ========================================================================= -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">GUÍA VISUAL: VECTORES Y DERIVADAS EN FÍSICA 1.º BACH</div>
    <div class="doc-subtitle">Conceptos Clave, Fórmulas en Color y Modelos Resueltos de Examen Oficial</div>
  </div>

  <!-- BLOQUE 1: VECTORES UNITARIOS -->
  <div class="card-blue">
    <div class="card-title blue"><span class="badge bg-blue">Bloque 1</span> Vectores Unitarios: Qué son y cómo calcularlos</div>
    <p>Un <b>vector unitario</b> $\vec{u}$ es un vector que apunta en la misma dirección y sentido que un vector dado $\vec{v}$, pero cuyo <b>módulo es exactamente $1$</b> ($|\vec{u}| = 1$).</p>
    <div style="background: white; padding: 6px 12px; border-radius: 6px; border: 1px solid #bfdbfe; margin: 4px 0;">
      <p style="text-align: center; font-size: 11pt; margin: 2px 0;">
        $$\mathbf{\vec{u} = \frac{\vec{v}}{|\vec{v}|}} = \left(\frac{v_x}{\sqrt{v_x^2 + v_y^2}}, \frac{v_y}{\sqrt{v_x^2 + v_y^2}}\right)$$
      </p>
    </div>
    __SVG_VECTOR_UNIT__
  </div>

  <!-- EJERCICIO OFICIAL RESUELTO: VECTORES Y FUERZAS -->
  <div class="card-green">
    <div class="card-title green"><span class="badge bg-green">Ejercicio Examen 1</span> Vectores Unitarios y Fuerzas Vectoriales</div>
    <p class="bold">Enunciado (del examen oficial del colegio):</p>
    <p><i>a) Dados los puntos $G(1, 2)$ y $H(4, 6)$, encuentra el vector unitario $\vec{u}_{GH}$.<br>
    b) Una fuerza de magnitud $|\vec{F}| = 50\text{ N}$ actúa en la dirección del vector $\vec{k} = (3, 4)$. Expresa la fuerza en forma vectorial.</i></p>
    
    <div style="margin-top: 8px;">
      <p><span class="step-num">1</span> <b>Vector entre dos puntos y su módulo:</b></p>
      $$\vec{GH} = H - G = (4 - 1)\,\vec{i} + (6 - 2)\,\vec{j} = \mathbf{3\,\vec{i} + 4\,\vec{j}} \implies |\vec{GH}| = \sqrt{3^2 + 4^2} = \sqrt{25} = \mathbf{5}$$
      
      <p><span class="step-num">2</span> <b>Cálculo del vector unitario $\vec{u}_{GH}$:</b></p>
      $$\vec{u}_{GH} = \frac{\vec{GH}}{|\vec{GH}|} = \frac{3\,\vec{i} + 4\,\vec{j}}{5} = \mathbf{\frac{3}{5}\,\vec{i} + \frac{4}{5}\,\vec{j}} \quad \left(\text{o bien } (0{,}6\,\vec{i} + 0{,}8\,\vec{j})\right)$$
      <p style="font-size: 9.5pt; color: #166534;"><i>Comprobación: $|\vec{u}_{GH}| = \sqrt{0{,}6^2 + 0{,}8^2} = \sqrt{0{,}36 + 0{,}64} = \sqrt{1} = 1$ ✔</i></p>

      <p><span class="step-num">3</span> <b>Expresar la fuerza $\vec{F}$ en forma vectorial:</b></p>
      <p>Multiplicamos el módulo de la fuerza ($50\text{ N}$) por el vector unitario director ($\vec{u}_k$):</p>
      $$\vec{F} = |\vec{F}| \cdot \vec{u}_k = 50 \cdot \left(\frac{3}{5}\,\vec{i} + \frac{4}{5}\,\vec{j}\right) = \mathbf{30\,\vec{i} + 40\,\vec{j}\text{ (N)}}$$
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- PÁGINA 2: PARTE 2 - DERIVADAS EN CINEMÁTICA Y CURVATURA                 -->
<!-- ========================================================================= -->
<div class="page">
  <div class="card-purple">
    <div class="card-title purple"><span class="badge bg-purple">Bloque 2</span> El "Camino de las Derivadas" en Cinemática</div>
    <div style="background: white; padding: 6px 10px; border-radius: 6px; border: 1px solid #e9d5ff; margin-bottom: 6px;">
      <p style="text-align: center; margin: 2px 0;">
        $$\text{Posición: } \mathbf{\vec{r}(t)} \quad \xrightarrow{\text{Derivar }\frac{d}{dt}} \quad \text{Velocidad: } \mathbf{\vec{v}(t) = \frac{d\vec{r}}{dt}} \quad \xrightarrow{\text{Derivar }\frac{d}{dt}} \quad \text{Aceleración: } \mathbf{\vec{a}(t) = \frac{d\vec{v}}{dt}}$$
      </p>
    </div>
    <ul style="font-size: 10pt;">
      <li><b>Velocidad instantánea:</b> Se deriva componente a componente respecto al tiempo $t$.</li>
      <li><b>Aceleración tangencial ($a_t$):</b> Proyección de $\vec{a}$ sobre $\vec{v} \implies \mathbf{a_t = \frac{\vec{v}\cdot\vec{a}}{|\vec{v}|}}$ (cambia el <i>módulo</i> de la rapidez).</li>
      <li><b>Aceleración normal ($a_n$):</b> Componente perpendicular $\implies \mathbf{a_n = \sqrt{a^2 - a_t^2}}$ (cambia la <i>dirección</i> de la curva).</li>
      <li><b>Radio de curvatura ($\rho$):</b> Radio de la circunferencia que mejor se ajusta a la curva en ese punto $\implies \mathbf{\rho = \frac{v^2}{a_n}}$.</li>
    </ul>
    __SVG_KINEMATICS_DECOMP__
  </div>

  <!-- EJERCICIO MASTER DE EXAMEN RESUELTO -->
  <div class="card-amber">
    <div class="card-title amber"><span class="badge bg-amber">Ejercicio Examen 2</span> Cinemática Vectorial con Derivadas (Paso a Paso)</div>
    <p class="bold">Enunciado Oficial:</p>
    <p><i>Un móvil se desplaza según la ecuación: $\vec{r}(t) = (3t + 6)\,\vec{i} + (9t^2 - 15)\,\vec{j}\text{ (m)}$. Halla en $t = 1\text{ s}$ la velocidad $\vec{v}$, la aceleración $\vec{a}$, $a_t$, $a_n$ y el radio de curvatura $\rho$.</i></p>

    <div style="margin-top: 6px;">
      <p><span class="step-num">1</span> <b>Derivada de la posición $\to$ Vector Velocidad $\vec{v}(t)$:</b></p>
      $$\vec{v}(t) = \frac{d(3t+6)}{dt}\,\vec{i} + \frac{d(9t^2-15)}{dt}\,\vec{j} = \mathbf{3\,\vec{i} + 18t\,\vec{j}\text{ (m/s)}}$$
      $$\text{En } t = 1\text{ s}: \quad \vec{v}(1) = \mathbf{3\,\vec{i} + 18\,\vec{j}\text{ m/s}} \implies |\vec{v}(1)| = \sqrt{3^2 + 18^2} = \sqrt{333} = \mathbf{3\sqrt{37} \approx 18{,}25\text{ m/s}}$$

      <p><span class="step-num">2</span> <b>Derivada de la velocidad $\to$ Vector Aceleración $\vec{a}(t)$:</b></p>
      $$\vec{a}(t) = \frac{d(3)}{dt}\,\vec{i} + \frac{d(18t)}{dt}\,\vec{j} = \mathbf{0\,\vec{i} + 18\,\vec{j}\text{ (m/s}^2\text{)}} \implies |\vec{a}| = \mathbf{18\text{ m/s}^2}$$

      <p><span class="step-num">3</span> <b>Aceleración Tangencial ($a_t$) por producto escalar:</b></p>
      $$a_t = \frac{\vec{v} \cdot \vec{a}}{|\vec{v}|} = \frac{(3)(0) + (18)(18)}{\sqrt{333}} = \frac{324}{3\sqrt{37}} = \mathbf{\frac{108}{\sqrt{37}} \approx 17{,}75\text{ m/s}^2}$$

      <p><span class="step-num">4</span> <b>Aceleración Normal ($a_n$) y Radio de Curvatura ($\rho$):</b></p>
      $$a_n = \sqrt{a^2 - a_t^2} = \sqrt{18^2 - \left(\frac{108}{\sqrt{37}}\right)^2} = \sqrt{324 - \frac{11664}{37}} = \sqrt{\frac{324}{37}} = \mathbf{\frac{18}{\sqrt{37}} \approx 2{,}96\text{ m/s}^2}$$
      $$\rho = \frac{v^2}{a_n} = \frac{333}{\frac{18}{\sqrt{37}}} = \frac{333\sqrt{37}}{18} = \mathbf{\frac{37\sqrt{37}}{2} \approx 112{,}53\text{ m}}$$
    </div>
  </div>
</div>

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
""".replace("__SVG_VECTOR_UNIT__", SVG_VECTOR_UNIT).replace("__SVG_KINEMATICS_DECOMP__", SVG_KINEMATICS_DECOMP)

temp_html = os.path.join(OUTPUT_DIR, "temp_guia_visual.html")
target_pdf = os.path.join(OUTPUT_DIR, "guia_visual_vectores_y_derivadas_fisica.pdf")

with open(temp_html, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

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
    print(f"Exito generando PDF visual en colorines: {target_pdf} ({os.path.getsize(target_pdf)} bytes)")
else:
    print(f"Error: {res.stderr}")
