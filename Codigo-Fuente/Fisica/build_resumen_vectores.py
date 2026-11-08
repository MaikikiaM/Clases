import os
import subprocess

OUTPUT_DIR = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Fisica\Vectores"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Resumen: Teoría y Operaciones con Vectores</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {delimiters: [
    {left: '$$', right: '$$', display: true},
    {left: '$', right: '$', display: false}
  ]});"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 8mm 9mm 6mm 9mm;
  }
  * { box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif;
    font-size: 7.6pt;
    line-height: 1.25;
    color: #1e293b;
    margin: 0;
    padding: 0;
  }
  .header {
    text-align: center;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 2px;
    margin-bottom: 6px;
  }
  h1 {
    font-size: 11.5pt;
    font-weight: 800;
    color: #1e3a8a;
    margin: 0 0 1px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .subtitle {
    font-size: 7.2pt;
    color: #64748b;
    font-weight: 600;
  }
  .columns {
    display: flex;
    gap: 10px;
  }
  .col {
    flex: 1;
    min-width: 0;
  }
  .card {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    margin-bottom: 5px;
    padding: 4px 6px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03);
  }
  .card-title {
    font-size: 8pt;
    font-weight: 700;
    color: #1e3a8a;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 2px;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
  }
  .badge {
    background: #2563eb;
    color: #ffffff;
    font-size: 6.5pt;
    padding: 1px 3px;
    border-radius: 3px;
    margin-right: 4px;
  }
  ul {
    margin: 0;
    padding-left: 12px;
  }
  li {
    margin-bottom: 1px;
  }
  .formula-box {
    background: #f8fafc;
    border-left: 3px solid #2563eb;
    padding: 2px 5px;
    margin: 2px 0;
    border-radius: 0 4px 4px 0;
    font-size: 7.8pt;
  }
  .highlight {
    font-weight: 600;
    color: #0f172a;
  }
</style>
</head>
<body>

<div class="header">
  <h1>Resumen General: Teoría y Operaciones con Vectores</h1>
  <div class="subtitle">Síntesis completa de apuntes manuscritos (Fundamentos, Representación Analítica, Producto Escalar, Producto Vectorial y Aplicaciones Físicas)</div>
</div>

<div class="columns">
  <!-- COLUMNA IZQUIERDA -->
  <div class="col">
    
    <div class="card">
      <div class="card-title"><span class="badge">1</span> Fundamentos: Estática vs. Dinámica</div>
      <ul>
        <li><span class="highlight">Visión Estática:</span> Puntos fijos en el espacio mediante coordenadas cartesianas: $P(x,y,z)$ en $\mathbb{R}^2/\mathbb{R}^3$.</li>
        <li><span class="highlight">Visión Dinámica:</span> Incorpora desplazamiento y cambio mediante el <span class="highlight">Vector</span> $\vec{v} = \vec{AB}$ (origen $A$, extremo $B$).</li>
        <li><span class="highlight">3 Elementos Definitorios:</span>
          <ul>
            <li><b>Módulo ($|\vec{v}|$):</b> Longitud o magnitud $|\vec{v}| = \overline{AB} \ge 0$.</li>
            <li><b>Dirección:</b> Recta soporte $r$ que une $A$ y $B$ (o rectas paralelas).</li>
            <li><b>Sentido:</b> Indicado por la flecha ($\exists$ orden unívoco $A \to B$).</li>
          </ul>
        </li>
        <li><span class="highlight">Vector de Posición ($\vec{r} = \vec{OP}$):</span> Une el origen $O$ con el punto $P$. Indica <i>desde dónde se observa</i> y aporta dinamismo al movimiento.</li>
        <li><span class="highlight">Espacio Vectorial ($V$):</span> Todo $\vec{v} \in V$ se expresa como combinación lineal (C.L.) respecto a una base elegida.</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-title"><span class="badge">2</span> Álgebra de Operaciones y Bases</div>
      <ul>
        <li><span class="highlight">Suma y Resta ($\vec{a} \pm \vec{b}$):</span> Op. interna ($V \times V \to V$). Resta: $\vec{a} - \vec{b} = \vec{a} + (-\vec{b})$.
          <br><b>Propiedades:</b> Conmutativa ($\vec{v}+\vec{w}=\vec{w}+\vec{v}$), Asociativa ($(\vec{v}+\vec{w})+\vec{u}=\vec{v}+(\vec{w}+\vec{u})$), Neutro ($\vec{v}+\vec{0}=\vec{v}$) y Opuesto ($\vec{v}+(-\vec{v})=\vec{0}$).</li>
        <li><span class="highlight">Producto por Escalar ($m \in \mathbb{R}$):</span> Op. externa ($\mathbb{R} \times V \to V$). Dilata, contrae o invierte ($m\vec{v}$).
          <br><b>Propiedades:</b> Conmutativa ($m\vec{v}=\vec{v}m$), Asociativa mixta ($(nm)\vec{v}=n(m\vec{v})$), Distributiva $\mathbb{R}$ ($(n+m)\vec{v}=n\vec{v}+m\vec{v}$), Distributiva $V$ ($n(\vec{v}+\vec{u})=n\vec{v}+n\vec{u}$), Unidad ($1\vec{v}=\vec{v}$).</li>
        <li><span class="highlight">Combinación Lineal:</span> $\vec{w} = a\vec{u} + b\vec{v}$.</li>
        <li><span class="highlight">Bases:</span> Vectores linealmente independientes ($\vec{u} \neq k\vec{v}$).
          <ul>
            <li><i>No ortogonal:</i> Ángulo entre vectores $\alpha \neq 90^\circ$.</li>
            <li><i>Ortogonal:</i> $\vec{u} \perp \vec{v}$, pero con módulos $|\vec{u}| \neq |\vec{v}|$.</li>
            <li><i>Ortonormal:</i> Mutuamente perpendiculares y unitarios ($|\vec{u}_1|=|\vec{u}_2|=1$, $\vec{u}_1 \perp \vec{u}_2$). Versores canónicos: $\{\vec{i}, \vec{j}, \vec{k}\}$.</li>
          </ul>
        </li>
      </ul>
    </div>

    <div class="card">
      <div class="card-title"><span class="badge">3</span> Expresión Analítica (Base Ortonormal)</div>
      <ul>
        <li><b>Componentes:</b> $\vec{v}(v_x, v_y) = v_x \vec{i} + v_y \vec{j} \equiv (v_x, v_y)$.</li>
        <li><b>Módulo (Pitágoras):</b> $|\vec{v}| = +\sqrt{v_x^2 + v_y^2}$ (hipotenusa).</li>
        <li><b>Suma / Resta:</b> $\vec{u} \pm \vec{v} = (u_x \pm v_x, \, u_y \pm v_y)$.</li>
        <li><b>Multiplicación por escalar:</b> $m\vec{u} = (m u_x, \, m u_y)$.</li>
        <li><b>Normalización:</b> Vector unitario $\vec{u}_{\vec{v}} = \dfrac{\vec{v}}{|\vec{v}|}$ tal que $|\vec{u}_{\vec{v}}| = 1$.</li>
        <li><b>C.L. Analítica:</b> $\vec{w} = a\vec{u} + b\vec{v} \iff \begin{cases} w_x = a u_x + b v_x \\ w_y = a u_y + b v_y \end{cases}$</li>
      </ul>
    </div>

  </div>

  <!-- COLUMNA DERECHA -->
  <div class="col">
    
    <div class="card">
      <div class="card-title"><span class="badge">4</span> Producto Escalar y Vector Proyección</div>
      <div class="formula-box">
        $$\vec{u} \cdot \vec{v} = |\vec{u}| \cdot |\vec{v}| \cdot \cos \alpha = u_x v_x + u_y v_y \quad (\in \mathbb{R})$$
      </div>
      <ul>
        <li><b>Propiedades:</b> Conmutativa ($\vec{u}\cdot\vec{v}=\vec{v}\cdot\vec{u}$), Asoc. mixta ($m(\vec{u}\cdot\vec{v})=(m\vec{u})\cdot\vec{v}$), Distributiva ($\vec{u}\cdot(\vec{v}+\vec{w})=\vec{u}\cdot\vec{v}+\vec{u}\cdot\vec{w}$).</li>
        <li><b>Proyección Escalar:</b> $\overline{PM} = |\vec{u}|\cos\alpha = \dfrac{\vec{u}\cdot\vec{v}}{|\vec{v}|}$.</li>
        <li><span class="highlight">Vector Proyección:</span> $\vec{u}_\parallel = \vec{\text{proy}}_{\vec{v}}(\vec{u}) = \overline{PM}\cdot \dfrac{\vec{v}}{|\vec{v}|} = \left(\dfrac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2}\right)\vec{v}$.</li>
        <li><span class="highlight">Con Pitágoras ($\vec{u} = \vec{u}_\parallel + \vec{u}_\perp$):</span>
          <br>$\vec{u}_\parallel \perp \vec{u}_\perp \implies |\vec{u}|^2 = |\vec{u}_\parallel|^2 + |\vec{u}_\perp|^2 \implies |\vec{u}_\perp| = \sqrt{|\vec{u}|^2 - |\vec{u}_\parallel|^2}$.
          <br>Trigonométricamente: $(|\vec{u}|\cos\alpha)^2 + (|\vec{u}|\sin\alpha)^2 = |\vec{u}|^2$.</li>
        <li><b>Ortogonalidad:</b> $(\vec{u} \perp \vec{v} \iff \vec{u}\cdot\vec{v}=0)$. En 2D: $(u_x, u_y) \perp (-u_y, u_x)$.</li>
        <li><b>Ángulo:</b> $\cos\alpha = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}$. ($>0 \implies$ agudo; $<0 \implies$ obtuso).</li>
      </ul>
    </div>

    <div class="card">
      <div class="card-title"><span class="badge">5</span> Producto Vectorial ($\vec{a} \times \vec{b}$)</div>
      <ul>
        <li><b>Definición:</b> Genera un <span class="highlight">nuevo vector</span> $\vec{c} = \vec{a} \times \vec{b}$:
          <ul>
            <li><b>Módulo:</b> $|\vec{a} \times \vec{b}| = |\vec{a}| \cdot |\vec{b}| \cdot \sin \alpha$ (área del paralelogramo).</li>
            <li><b>Dirección:</b> $\perp$ a $\vec{a}$ y $\perp$ a $\vec{b}$ (perpendicular al plano).</li>
            <li><b>Sentido:</b> Regla del tornillo / mano derecha.</li>
          </ul>
        </li>
        <li><b>Propiedades:</b> Anticonmutativa ($\vec{a}\times\vec{b}=-(\vec{b}\times\vec{a})$), Distributiva ($\vec{a}\times(\vec{b}+\vec{c})=\vec{a}\times\vec{b}+\vec{a}\times\vec{c}$), Paralelismo ($\vec{a}\parallel\vec{b}\iff\vec{a}\times\vec{b}=\vec{0}$).</li>
        <li><b>Base 3D:</b> $\vec{i}\times\vec{i}=\vec{j}\times\vec{j}=\vec{k}\times\vec{k}=\vec{0}$.
          <br>Cíclicos: $\vec{i}\times\vec{j}=\vec{k}, \; \vec{j}\times\vec{k}=\vec{i}, \; \vec{k}\times\vec{i}=\vec{j}$.</li>
      </ul>
      <div class="formula-box">
        $$\vec{a}\times\vec{b} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix} = \begin{pmatrix} a_y b_z - a_z b_y \\ a_z b_x - a_x b_z \\ a_x b_y - a_y b_x \end{pmatrix}$$
      </div>
    </div>

    <div class="card">
      <div class="card-title"><span class="badge">6</span> Aplicaciones Físicas y Geométricas</div>
      <ul>
        <li><span class="highlight">Momento de un vector respecto a un punto $O$:</span>
          <br>Fundamental en física (momento de fuerzas $\vec{M} = \vec{r} \times \vec{F}$, momento angular $\vec{L} = \vec{r} \times \vec{p}$):
          $$\vec{M}_O^{\vec{v}} = \vec{r} \times \vec{v} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ r_x & r_y & r_z \\ v_x & v_y & v_z \end{vmatrix}$$
          donde $\vec{r}$ es el vector distancia / posición desde el centro de momentos $O$ hasta el punto de aplicación de $\vec{v}$.
        </li>
        <li><span class="highlight">Representación vectorial de una superficie:</span>
          <br>Para una superficie plana <span class="highlight">abierta y finita</span> de área $S$, se define el vector superficie $\vec{S}$:
          <ul>
            <li><b>Módulo:</b> $|\vec{S}| = S$ (área de la superficie).</li>
            <li><b>Dirección:</b> Normal (perpendicular) a la superficie.</li>
            <li><b>Sentido:</b> Fijado según orientación del contorno.</li>
            <li><b>Punto de aplicación:</b> En un punto interior $O$.</li>
          </ul>
        </li>
      </ul>
    </div>

  </div>
</div>

</body>
</html>
"""

temp_html = os.path.join(OUTPUT_DIR, "temp_resumen_vectores.html")
target_pdf = os.path.join(OUTPUT_DIR, "resumen_vectores.pdf")

with open(temp_html, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

cmd = [
    EDGE_EXE,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--virtual-time-budget=3000",
    f"--print-to-pdf={target_pdf}",
    temp_html
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(temp_html):
    os.remove(temp_html)

if os.path.exists(target_pdf):
    print(f"[OK] Generado PDF resumen de 1 pagina: {target_pdf} ({os.path.getsize(target_pdf)} bytes)")
else:
    print(f"[ERROR] Error al generar PDF: {res.stderr}")
