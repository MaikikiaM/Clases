import os
import subprocess

OUTPUT_DIR = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Matematicas\Derivadas"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# SVG Diagram of the Cylinder Breakdown
SVG_CYLINDER = r"""
<div style="text-align: center; margin: 15px 0;">
<svg width="420" height="170" viewBox="0 0 420 170">
  <defs>
    <!-- Gradients -->
    <linearGradient id="grad_wall" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fdba74"/>
      <stop offset="50%" stop-color="#fed7aa"/>
      <stop offset="100%" stop-color="#fb923c"/>
    </linearGradient>
  </defs>

  <!-- 3D Cylinder -->
  <!-- Lateral Body -->
  <rect x="40" y="45" width="100" height="85" fill="url(#grad_wall)" stroke="#ea580c" stroke-width="1.5"/>
  <!-- Bottom Base (Suelo) -->
  <ellipse cx="90" cy="130" rx="50" ry="16" fill="#86efac" stroke="#16a34a" stroke-width="2"/>
  <!-- Top Base (Tapa) -->
  <ellipse cx="90" cy="45" rx="50" ry="16" fill="#93c5fd" stroke="#2563eb" stroke-width="2"/>
  
  <!-- Radius r -->
  <line x1="90" y1="45" x2="140" y2="45" stroke="#1e40af" stroke-width="2" stroke-dasharray="3"/>
  <circle cx="90" cy="45" r="2.5" fill="#1e40af"/>
  <text x="110" y="38" font-size="12" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#1e40af">r</text>
  
  <!-- Height h -->
  <line x1="25" y1="45" x2="25" y2="130" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="20" y1="45" x2="30" y2="45" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="20" y1="130" x2="30" y2="130" stroke="#c2410c" stroke-width="1.5"/>
  <text x="10" y="92" font-size="12" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#c2410c">h</text>

  <!-- Breakdown arrows & components -->
  <!-- Tapa -->
  <rect x="180" y="20" width="220" height="32" rx="5" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
  <circle cx="195" cy="36" r="6" fill="#3b82f6"/>
  <text x="210" y="40" font-size="11" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#1e40af">TAPA: Área = &pi; r&sup2; (Precio p_tapa)</text>

  <!-- Pared -->
  <rect x="180" y="65" width="220" height="36" rx="5" fill="#fff7ed" stroke="#f97316" stroke-width="1.5"/>
  <circle cx="195" cy="83" r="6" fill="#f97316"/>
  <text x="210" y="81" font-size="11" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#c2410c">PARED: Área = 2&pi; r h</text>
  <text x="210" y="94" font-size="9.5" font-family="Segoe UI, sans-serif" fill="#7c2d12">(Desarrollo rectangular 2&pi;r &times; h)</text>

  <!-- Suelo -->
  <rect x="180" y="114" width="220" height="32" rx="5" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
  <circle cx="195" cy="130" r="6" fill="#22c55e"/>
  <text x="210" y="134" font-size="11" font-family="Segoe UI, sans-serif" font-weight="bold" fill="#166534">SUELO: Área = &pi; r&sup2; (Precio p_suelo)</text>
</svg>
</div>
"""

# HTML TEMPLATE
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 18mm 20mm 18mm 20mm;
  }
  * {
    box-sizing: border-box;
  }
  body {
    font-family: 'Segoe UI', 'Calibri', sans-serif;
    font-size: 10.5pt;
    line-height: 1.38;
    color: #1f2937;
    margin: 0;
    padding: 0;
  }
  .page {
    page-break-after: always;
    min-height: 260mm;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  .page:last-child {
    page-break-after: avoid;
  }
  .doc-header {
    background: linear-gradient(135deg, #0f766e, #0d9488);
    color: white;
    padding: 12px 16px;
    border-radius: 8px;
    margin-bottom: 15px;
    text-align: center;
  }
  .doc-title {
    font-size: 15pt;
    font-weight: 800;
    margin-bottom: 2px;
  }
  .doc-subtitle {
    font-size: 10.5pt;
    font-weight: 500;
    opacity: 0.95;
  }
  .card-box {
    background: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-left: 5px solid #0f766e;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 14px;
  }
  .card-title {
    font-size: 11pt;
    font-weight: bold;
    color: #0f766e;
    margin-bottom: 5px;
  }
  .step-badge {
    background: #0f766e;
    color: white;
    font-weight: bold;
    display: inline-block;
    width: 20px;
    height: 20px;
    line-height: 20px;
    border-radius: 50%;
    text-align: center;
    font-size: 9pt;
    margin-right: 5px;
  }
  .result-box {
    background: #f0fdf4;
    border: 1.5px solid #86efac;
    padding: 8px 12px;
    border-radius: 6px;
    margin: 8px 0;
    color: #166534;
  }
  ol, ul {
    margin: 5px 0;
    padding-left: 22px;
  }
  li {
    margin-bottom: 6px;
  }
  .alpha-list {
    list-style-type: lower-alpha;
  }
  .alpha-list > li {
    margin-bottom: 8px;
  }
  .alpha-list > li::marker {
    font-weight: bold;
  }
  p {
    margin: 5px 0;
  }
  .bold {
    font-weight: bold;
  }
  .katex-display {
    margin: 8px 0 !important;
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

# UNRESOLVED HTML (PÁGINA 1: MODELO, PÁGINA 2: PRÁCTICA)
body_unresolved = r"""
<!-- PÁGINA 1: EJERCICIO 1 (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Optimización: Coste de Fabricación de un Cilindro</div>
    <div class="doc-subtitle">Matemáticas 1.º de Bachillerato | Ejercicio 1 (Modelo para Pizarra)</div>
  </div>

  __SVG__

  <div class="card-box">
    <div class="card-title">Enunciado 1 (Modelo):</div>
    <p>Una empresa industrial desea fabricar un depósito cilíndrico cerrado con una capacidad fija de <b>$V = 16\pi\text{ m}^3$</b> (aproximadamente $50{,}27\text{ m}^3$).</p>
    <p>Debido a las condiciones estructurales y mecánicas del depósito, los materiales empleados para cada una de las partes tienen distintos costes por metro cuadrado:</p>
    <ul>
      <li><b>Tapa superior:</b> $3\text{ €/m}^2$.</li>
      <li><b>Suelo / base inferior:</b> $5\text{ €/m}^2$ (material reforzado).</li>
      <li><b>Pared lateral:</b> $4\text{ €/m}^2$.</li>
    </ul>
  </div>

  <ol class="alpha-list" style="margin-top: 15px; font-size: 11pt;">
    <li>Expresa la altura $h$ del cilindro en función del radio $r$ de la base utilizando la condición de volumen fijo.</li>
    <li>Escribe la función del coste total de fabricación $C(r)$ en función únicamente del radio $r$.</li>
    <li>Determina las dimensiones del depósito (radio $r$ y altura $h$) que consiguen que el coste de producción sea <b>mínimo</b>.</li>
    <li>Justifica, mediante el criterio de la segunda derivada, que las dimensiones halladas corresponden efectivamente a un mínimo absoluto de coste.</li>
    <li>Calcula el valor numérico del coste mínimo total de fabricación.</li>
  </ol>
</div>

<!-- PÁGINA 2: EJERCICIO 2 (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Optimización: Coste de Fabricación de un Cilindro</div>
    <div class="doc-subtitle">Matemáticas 1.º de Bachillerato | Ejercicio 2 (Práctica para el Alumno - Clon)</div>
  </div>

  __SVG__

  <div class="card-box">
    <div class="card-title">Enunciado 2 (Práctica del Alumno):</div>
    <p>Una empresa química necesita diseñar un tanque cilíndrico cerrado con un volumen total constante de <b>$V = 54\pi\text{ m}^3$</b> (aproximadamente $169{,}65\text{ m}^3$).</p>
    <p>Los costes de los materiales anticorrosión necesarios para cada sección del tanque son:</p>
    <ul>
      <li><b>Tapa superior:</b> $4\text{ €/m}^2$.</li>
      <li><b>Suelo / base inferior:</b> $8\text{ €/m}^2$ (aislante de alta densidad).</li>
      <li><b>Pared lateral:</b> $6\text{ €/m}^2$.</li>
    </ul>
  </div>

  <ol class="alpha-list" style="margin-top: 15px; font-size: 11pt;">
    <li>Expresa la altura $h$ del cilindro en función del radio $r$ de la base utilizando la condición de volumen fijo.</li>
    <li>Escribe la función del coste total de fabricación $C(r)$ en función únicamente del radio $r$.</li>
    <li>Determina las dimensiones del tanque (radio $r$ y altura $h$) que hacen que el coste total sea <b>mínimo</b>.</li>
    <li>Justifica, aplicando el criterio de la segunda derivada, que se trata de un mínimo absoluto.</li>
    <li>Calcula el coste mínimo total que costará fabricar dicho tanque cilíndrico.</li>
  </ol>
</div>
""".replace("__SVG__", SVG_CYLINDER)

# SOLVED HTML
body_solved = r"""
<!-- PÁGINA 1: RESOLUCIÓN 1 (MODELO) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución Detallada: Ejercicio 1 (Cilindro $16\pi\text{ m}^3$ — Modelo)</div>
    <div class="doc-subtitle">Costes: Tapa $3\text{ €/m}^2$, Suelo $5\text{ €/m}^2$, Pared $4\text{ €/m}^2$</div>
  </div>

  <div class="card-box">
    <p><span class="step-num">1</span> <b>Ecuación de ligadura (Volumen constante):</b></p>
    $$V = \text{Área base} \times \text{altura} = \pi r^2 h = 16\pi \implies \mathbf{h = \frac{16}{r^2}} \quad (r > 0)$$

    <p><span class="step-num">2</span> <b>Construcción de la función de coste total $C(r)$:</b></p>
    <ul>
      <li>Coste tapa: $\text{Área} \times \text{Precio} = (\pi r^2) \times 3 = 3\pi r^2$.</li>
      <li>Coste suelo: $\text{Área} \times \text{Precio} = (\pi r^2) \times 5 = 5\pi r^2$.</li>
      <li>Coste pared lateral: $\text{Área} \times \text{Precio} = (2\pi r h) \times 4 = 8\pi r h$.</li>
    </ul>
    $$C(r) = 3\pi r^2 + 5\pi r^2 + 8\pi r \left(\frac{16}{r^2}\right) = 8\pi r^2 + \frac{128\pi}{r}$$

    <p><span class="step-num">3</span> <b>Cálculo del punto crítico (Primera derivada $C'(r) = 0$):</b></p>
    $$C'(r) = 16\pi r - \frac{128\pi}{r^2} = 0 \implies 16\pi r = \frac{128\pi}{r^2} \implies 16\pi r^3 = 128\pi \implies r^3 = \frac{128}{16} = 8 \implies \mathbf{r = 2\text{ m}}$$
    $$\text{Altura correspondiente: } h = \frac{16}{2^2} = \frac{16}{4} = \mathbf{4\text{ m}}$$

    <p><span class="step-num">4</span> <b>Justificación de Mínimo con la Segunda Derivada:</b></p>
    $$C''(r) = 16\pi + \frac{256\pi}{r^3} \implies C''(2) = 16\pi + \frac{256\pi}{8} = 16\pi + 32\pi = \mathbf{48\pi > 0} \implies \textbf{Mínimo Absoluto}$$

    <div class="result-box">
      <p class="bold" style="margin: 0; font-size: 11pt;">Dimensiones óptimas y Coste mínimo:</p>
      <p style="margin: 3px 0;">Radio: $\mathbf{r = 2\text{ m}}$, &nbsp;&nbsp;&nbsp; Altura: $\mathbf{h = 4\text{ m}}$</p>
      <p style="margin: 3px 0;">Coste mínimo: $C(2) = 8\pi(2^2) + \frac{128\pi}{2} = 32\pi + 64\pi = \mathbf{96\pi\text{ €} \approx 301{,}59\text{ €}}$</p>
    </div>
  </div>
</div>

<!-- PÁGINA 2: RESOLUCIÓN 2 (PRÁCTICA) -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Resolución Detallada: Ejercicio 2 (Cilindro $54\pi\text{ m}^3$ — Práctica)</div>
    <div class="doc-subtitle">Costes: Tapa $4\text{ €/m}^2$, Suelo $8\text{ €/m}^2$, Pared $6\text{ €/m}^2$</div>
  </div>

  <div class="card-box">
    <p><span class="step-num">1</span> <b>Ecuación de ligadura (Volumen constante):</b></p>
    $$V = \text{Área base} \times \text{altura} = \pi r^2 h = 54\pi \implies \mathbf{h = \frac{54}{r^2}} \quad (r > 0)$$

    <p><span class="step-num">2</span> <b>Construcción de la función de coste total $C(r)$:</b></p>
    <ul>
      <li>Coste tapa: $(\pi r^2) \times 4 = 4\pi r^2$.</li>
      <li>Coste suelo: $(\pi r^2) \times 8 = 8\pi r^2$.</li>
      <li>Coste pared lateral: $(2\pi r h) \times 6 = 12\pi r h$.</li>
    </ul>
    $$C(r) = 4\pi r^2 + 8\pi r^2 + 12\pi r \left(\frac{54}{r^2}\right) = 12\pi r^2 + \frac{648\pi}{r}$$

    <p><span class="step-num">3</span> <b>Cálculo del punto crítico (Primera derivada $C'(r) = 0$):</b></p>
    $$C'(r) = 24\pi r - \frac{648\pi}{r^2} = 0 \implies 24\pi r = \frac{648\pi}{r^2} \implies 24\pi r^3 = 648\pi \implies r^3 = \frac{648}{24} = 27 \implies \mathbf{r = 3\text{ m}}$$
    $$\text{Altura correspondiente: } h = \frac{54}{3^2} = \frac{54}{9} = \mathbf{6\text{ m}}$$

    <p><span class="step-num">4</span> <b>Justificación de Mínimo con la Segunda Derivada:</b></p>
    $$C''(r) = 24\pi + \frac{1296\pi}{r^3} \implies C''(3) = 24\pi + \frac{1296\pi}{27} = 24\pi + 48\pi = \mathbf{72\pi > 0} \implies \textbf{Mínimo Absoluto}$$

    <div class="result-box">
      <p class="bold" style="margin: 0; font-size: 11pt;">Dimensiones óptimas y Coste mínimo:</p>
      <p style="margin: 3px 0;">Radio: $\mathbf{r = 3\text{ m}}$, &nbsp;&nbsp;&nbsp; Altura: $\mathbf{h = 6\text{ m}}$</p>
      <p style="margin: 3px 0;">Coste mínimo: $C(3) = 12\pi(3^2) + \frac{648\pi}{3} = 108\pi + 216\pi = \mathbf{324\pi\text{ €} \approx 1017{,}88\text{ €}}$</p>
    </div>
  </div>
</div>
"""

# LaTeX sources
tex_unresolved = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[top=2cm, bottom=2cm, left=2.2cm, right=2.2cm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{enumitem}
\usepackage{tcolorbox}
\usepackage{microtype}

\setmainfont{Calibri}
\linespread{1.15}

\tcbset{
    colback=white,
    colframe=black,
    boxrule=0.8pt,
    arc=2mm,
    left=6pt, right=6pt, top=4pt, bottom=4pt
}

\begin{document}
\pagestyle{empty}

\begin{center}
    {\LARGE \textbf{Optimización: Coste de Fabricación de un Cilindro}}\\[4pt]
    {\large \textbf{Matemáticas 1.º de Bachillerato | Ejercicio 1: Modelo para Pizarra}}
\end{center}

\vspace{0.3cm}
\noindent\textbf{1.} Una empresa industrial desea fabricar un depósito cilíndrico cerrado con una capacidad fija de $V = 16\pi\text{ m}^3$ (aproximadamente $50{,}27\text{ m}^3$).

Debido a las condiciones estructurales y mecánicas del depósito, los materiales empleados para cada una de las partes tienen distintos costes por metro cuadrado:
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Tapa superior:} $3\text{ €/m}^2$.
    \item \textbf{Suelo / base inferior:} $5\text{ €/m}^2$ (material reforzado).
    \item \textbf{Pared lateral:} $4\text{ €/m}^2$.
\end{itemize}

\vspace{0.2cm}
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Expresa la altura $h$ del cilindro en función del radio $r$ de la base utilizando la condición de volumen fijo.
    \item Escribe la función del coste total de fabricación $C(r)$ en función únicamente del radio $r$.
    \item Determina las dimensiones del depósito (radio $r$ y altura $h$) que consiguen que el coste de producción sea \textbf{mínimo}.
    \item Justifica, mediante el criterio de la segunda derivada, que las dimensiones halladas corresponden efectivamente a un mínimo absoluto de coste.
    \item Calcula el valor numérico del coste mínimo total de fabricación.
\end{enumerate}

\newpage

\begin{center}
    {\LARGE \textbf{Optimización: Coste de Fabricación de un Cilindro}}\\[4pt]
    {\large \textbf{Matemáticas 1.º de Bachillerato | Ejercicio 2: Práctica para el Alumno (Clon)}}
\end{center}

\vspace{0.3cm}
\noindent\textbf{2.} Una empresa química necesita diseñar un tanque cilíndrico cerrado con un volumen total constante de $V = 54\pi\text{ m}^3$ (aproximadamente $169{,}65\text{ m}^3$).

Los costes de los materiales anticorrosión necesarios para cada sección del tanque son:
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item \textbf{Tapa superior:} $4\text{ €/m}^2$.
    \item \textbf{Suelo / base inferior:} $8\text{ €/m}^2$ (aislante de alta densidad).
    \item \textbf{Pared lateral:} $6\text{ €/m}^2$.
\end{itemize}

\vspace{0.2cm}
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Expresa la altura $h$ del cilindro en función del radio $r$ de la base utilizando la condición de volumen fijo.
    \item Escribe la función del coste total de fabricación $C(r)$ en función únicamente del radio $r$.
    \item Determina las dimensiones del tanque (radio $r$ y altura $h$) que hacen que el coste total sea \textbf{mínimo}.
    \item Justifica, aplicando el criterio de la segunda derivada, que se trata de un mínimo absoluto.
    \item Calcula el coste mínimo total que costará fabricar dicho tanque cilíndrico.
\end{enumerate}

\end{document}
"""

tex_solved = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[top=2cm, bottom=2cm, left=2.2cm, right=2.2cm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{enumitem}
\usepackage{tcolorbox}
\usepackage{microtype}

\setmainfont{Calibri}
\linespread{1.15}

\tcbset{
    colback=white,
    colframe=black,
    boxrule=0.8pt,
    arc=2mm,
    left=6pt, right=6pt, top=4pt, bottom=4pt
}

\begin{document}
\pagestyle{empty}

\begin{center}
    {\LARGE \textbf{Resolución Detallada: Ejercicio 1 (Cilindro $16\pi\text{ m}^3$ — Modelo)}}\\[4pt]
    {\large \textbf{Costes: Tapa $3\text{ €/m}^2$, Suelo $5\text{ €/m}^2$, Pared $4\text{ €/m}^2$}}
\end{center}

\vspace{0.3cm}
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=8pt]
    \item \textbf{Ecuación de ligadura (Volumen constante):}
    \[
    V = \text{Área base} \times \text{altura} = \pi r^2 h = 16\pi \implies \mathbf{h = \frac{16}{r^2}} \quad (r > 0)
    \]

    \item \textbf{Función de coste total $C(r)$:}
    \begin{itemize}[leftmargin=1.5em, itemsep=3pt]
        \item Coste tapa: $(\pi r^2) \times 3 = 3\pi r^2$.
        \item Coste suelo: $(\pi r^2) \times 5 = 5\pi r^2$.
        \item Coste pared lateral: $(2\pi r h) \times 4 = 8\pi r h$.
    \end{itemize}
    \[
    C(r) = 3\pi r^2 + 5\pi r^2 + 8\pi r \left(\frac{16}{r^2}\right) = \mathbf{8\pi r^2 + \frac{128\pi}{r}}
    \]

    \item \textbf{Cálculo de las dimensiones óptimas ($C'(r) = 0$):}
    \[
    C'(r) = 16\pi r - \frac{128\pi}{r^2} = 0 \implies 16\pi r^3 = 128\pi \implies r^3 = 8 \implies \mathbf{r = 2\text{ m}}
    \]
    \[
    h = \frac{16}{2^2} = \mathbf{4\text{ m}}
    \]

    \item \textbf{Justificación de mínimo con la segunda derivada:}
    \[
    C''(r) = 16\pi + \frac{256\pi}{r^3} \implies C''(2) = 16\pi + \frac{256\pi}{8} = 48\pi > 0 \implies \textbf{Mínimo absoluto}
    \]

    \item \textbf{Coste mínimo total:}
    \[
    C(2) = 8\pi(2^2) + \frac{128\pi}{2} = 32\pi + 64\pi = \mathbf{96\pi\text{ €} \approx 301{,}59\text{ €}}
    \]
\end{enumerate}

\newpage

\begin{center}
    {\LARGE \textbf{Resolución Detallada: Ejercicio 2 (Cilindro $54\pi\text{ m}^3$ — Práctica)}}\\[4pt]
    {\large \textbf{Costes: Tapa $4\text{ €/m}^2$, Suelo $8\text{ €/m}^2$, Pared $6\text{ €/m}^2$}}
\end{center}

\vspace{0.3cm}
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=8pt]
    \item \textbf{Ecuación de ligadura (Volumen constante):}
    \[
    V = \text{Área base} \times \text{altura} = \pi r^2 h = 54\pi \implies \mathbf{h = \frac{54}{r^2}} \quad (r > 0)
    \]

    \item \textbf{Función de coste total $C(r)$:}
    \begin{itemize}[leftmargin=1.5em, itemsep=3pt]
        \item Coste tapa: $(\pi r^2) \times 4 = 4\pi r^2$.
        \item Coste suelo: $(\pi r^2) \times 8 = 8\pi r^2$.
        \item Coste pared lateral: $(2\pi r h) \times 6 = 12\pi r h$.
    \end{itemize}
    \[
    C(r) = 4\pi r^2 + 8\pi r^2 + 12\pi r \left(\frac{54}{r^2}\right) = \mathbf{12\pi r^2 + \frac{648\pi}{r}}
    \]

    \item \textbf{Cálculo de las dimensiones óptimas ($C'(r) = 0$):}
    \[
    C'(r) = 24\pi r - \frac{648\pi}{r^2} = 0 \implies 24\pi r^3 = 648\pi \implies r^3 = 27 \implies \mathbf{r = 3\text{ m}}
    \]
    \[
    h = \frac{54}{3^2} = \mathbf{6\text{ m}}
    \]

    \item \textbf{Justificación de mínimo con la segunda derivada:}
    \[
    C''(r) = 24\pi + \frac{1296\pi}{r^3} \implies C''(3) = 24\pi + \frac{1296\pi}{27} = 72\pi > 0 \implies \textbf{Mínimo absoluto}
    \]

    \item \textbf{Coste mínimo total:}
    \[
    C(3) = 12\pi(3^2) + \frac{648\pi}{3} = 108\pi + 216\pi = \mathbf{324\pi\text{ €} \approx 1017{,}88\text{ €}}
    \]
\end{enumerate}

\end{document}
"""

with open(os.path.join(OUTPUT_DIR, "ejercicios_optimizacion_cilindro_precios.tex"), "w", encoding="utf-8") as f:
    f.write(tex_unresolved)

with open(os.path.join(OUTPUT_DIR, "ejercicios_optimizacion_cilindro_precios_resueltos.tex"), "w", encoding="utf-8") as f:
    f.write(tex_solved)

def compile_pdf(title, body, filename):
    html = HTML_TEMPLATE.replace("__TITLE__", title).replace("__BODY__", body)
    temp_html = os.path.join(OUTPUT_DIR, f"temp_{filename}.html")
    target_pdf = os.path.join(OUTPUT_DIR, filename)
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html)
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
        print(f"Exito: {filename} ({os.path.getsize(target_pdf)} bytes)")

compile_pdf("Ejercicios Optimización: Cilindro con Precios", body_unresolved, "ejercicios_optimizacion_cilindro_precios.pdf")
compile_pdf("Solucionario Optimización: Cilindro con Precios", body_solved, "ejercicios_optimizacion_cilindro_precios_resueltos.pdf")
