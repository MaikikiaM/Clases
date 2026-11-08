import os
import subprocess

DIR_PATH = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Fisica\Movimiento-Circular"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# =========================================================================
# CONTENIDO LATEX (.TEX) CON SOLUCIONES ENTRE PARÉNTESIS
# =========================================================================
TEX_CONTENT = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[top=2cm, bottom=2cm, left=2.2cm, right=2.2cm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{enumitem}
\usepackage{microtype}

\setmainfont{Calibri}
\linespread{1.18}

\begin{document}
\pagestyle{empty}

\noindent\textbf{1.} Un cuerpo describe un movimiento circular uniforme (MCU) en una circunferencia de radio $R = 30\text{ cm}$, girando con una velocidad constante de $120\text{ rpm}$. Determina:
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=4pt]
    \item La velocidad angular ($\omega$) expresada en radianes por segundo ($\text{rad/s}$). \hfill \textbf{(Sol: $\omega \approx 12{,}57\text{ rad/s}$)}
    \item El período ($T$) y la frecuencia ($f$) del movimiento. \hfill \textbf{(Sol: $T = 0{,}50\text{ s}$; $f = 2{,}00\text{ Hz}$)}
    \item El módulo de la velocidad lineal ($v$) de un punto situado en el borde exterior. \hfill \textbf{(Sol: $v \approx 3{,}77\text{ m/s}$)}
    \item La aceleración normal o centrípeta ($a_n$) que experimenta dicho punto. \hfill \textbf{(Sol: $a_n \approx 47{,}37\text{ m/s}^2$)}
\end{enumerate}

\vspace{0.6cm}
\noindent\textbf{2.} Un cuerpo describe un movimiento circular uniforme (MCU) en una circunferencia de radio $R = 40\text{ cm}$, girando con una velocidad constante de $150\text{ rpm}$. Determina:
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=4pt]
    \item La velocidad angular ($\omega$) expresada en radianes por segundo ($\text{rad/s}$). \hfill \textbf{(Sol: $\omega \approx 15{,}71\text{ rad/s}$)}
    \item El período ($T$) y la frecuencia ($f$) del movimiento. \hfill \textbf{(Sol: $T = 0{,}40\text{ s}$; $f = 2{,}50\text{ Hz}$)}
    \item El módulo de la velocidad lineal ($v$) de un punto situado en el borde exterior. \hfill \textbf{(Sol: $v \approx 6{,}28\text{ m/s}$)}
    \item La aceleración normal o centrípeta ($a_n$) que experimenta dicho punto. \hfill \textbf{(Sol: $a_n \approx 98{,}70\text{ m/s}^2$)}
\end{enumerate}

\vspace{0.6cm}
\noindent\textbf{3.} Un disco macizo de $0{,}50\text{ m}$ de diámetro, inicialmente en reposo, comienza a girar con una aceleración angular constante $\alpha = 1{,}2\text{ rad/s}^2$. En el instante en que completa $10\text{ vueltas}$, calcula:
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=4pt]
    \item La velocidad angular ($\omega$) alcanzada en ese instante. \hfill \textbf{(Sol: $\omega \approx 12{,}28\text{ rad/s}$)}
    \item El tiempo transcurrido desde el reposo hasta completar dichas vueltas. \hfill \textbf{(Sol: $t \approx 10{,}23\text{ s}$)}
    \item La velocidad lineal ($v$) de un punto situado en la periferia del disco. \hfill \textbf{(Sol: $v \approx 3{,}07\text{ m/s}$)}
    \item El módulo de la aceleración tangencial ($a_t$) y de la aceleración normal ($a_n$) en ese instante. \hfill \textbf{(Sol: $a_t = 0{,}30\text{ m/s}^2$; $a_n \approx 37{,}70\text{ m/s}^2$)}
\end{enumerate}

\vspace{0.6cm}
\noindent\textbf{4.} Un volante circular de $0{,}80\text{ m}$ de diámetro, inicialmente en reposo, comienza a girar con una aceleración angular constante $\alpha = 1{,}5\text{ rad/s}^2$. En el instante en que completa $12\text{ vueltas}$, calcula:
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=4pt]
    \item La velocidad angular ($\omega$) alcanzada en ese instante. \hfill \textbf{(Sol: $\omega \approx 15{,}04\text{ rad/s}$)}
    \item El tiempo transcurrido desde el reposo hasta completar dichas vueltas. \hfill \textbf{(Sol: $t \approx 10{,}03\text{ s}$)}
    \item La velocidad lineal ($v$) de un punto situado en la periferia del volante. \hfill \textbf{(Sol: $v \approx 6{,}02\text{ m/s}$)}
    \item El módulo de la aceleración tangencial ($a_t$) y de la aceleración normal ($a_n$) en ese instante. \hfill \textbf{(Sol: $a_t = 0{,}60\text{ m/s}^2$; $a_n \approx 90{,}48\text{ m/s}^2$)}
\end{enumerate}

\end{document}
"""

# =========================================================================
# PLANTILLA HTML MAESTRA
# =========================================================================
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Ejercicios Movimiento Circular</title>
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
    font-family: 'Calibri', 'Carlito', 'Segoe UI', sans-serif;
    font-size: 10.5pt;
    line-height: 1.38;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
  }
  .exercise {
    margin-bottom: 22px;
  }
  .exercise:last-child {
    margin-bottom: 0;
  }
  .exercise-statement {
    text-align: justify;
    margin-bottom: 5px;
  }
  .bold {
    font-weight: bold;
  }
  .sub-list {
    margin: 0;
    padding-left: 20px;
    list-style: none;
    counter-reset: subitem;
  }
  .sub-list li {
    counter-increment: subitem;
    margin-bottom: 4px;
    line-height: 1.35;
    position: relative;
    padding-left: 22px;
  }
  .sub-list li:last-child {
    margin-bottom: 0;
  }
  .sub-list li::before {
    content: counter(subitem, lower-alpha) ")";
    font-weight: bold;
    position: absolute;
    left: 0;
    top: 0;
  }
  .sol {
    font-weight: normal;
    color: #2b2b2b;
    margin-left: 5px;
    white-space: nowrap;
  }
</style>
</head>
<body>

<div class="exercise">
  <div class="exercise-statement">
    <span class="bold">1.</span> Un cuerpo describe un movimiento circular uniforme (MCU) en una circunferencia de radio $R = 30\text{ cm}$, girando con una velocidad constante de $120\text{ rpm}$. Determina:
  </div>
  <ul class="sub-list">
    <li>La velocidad angular ($\omega$) expresada en radianes por segundo ($\text{rad/s}$). <span class="sol"><strong>(Sol: $\omega \approx 12{,}57\text{ rad/s}$)</strong></span></li>
    <li>El período ($T$) y la frecuencia ($f$) del movimiento. <span class="sol"><strong>(Sol: $T = 0{,}50\text{ s}$; $f = 2{,}00\text{ Hz}$)</strong></span></li>
    <li>El módulo de la velocidad lineal ($v$) de un punto situado en el borde exterior. <span class="sol"><strong>(Sol: $v \approx 3{,}77\text{ m/s}$)</strong></span></li>
    <li>La aceleración normal o centrípeta ($a_n$) que experimenta dicho punto. <span class="sol"><strong>(Sol: $a_n \approx 47{,}37\text{ m/s}^2$)</strong></span></li>
  </ul>
</div>

<div class="exercise">
  <div class="exercise-statement">
    <span class="bold">2.</span> Un cuerpo describe un movimiento circular uniforme (MCU) en una circunferencia de radio $R = 40\text{ cm}$, girando con una velocidad constante de $150\text{ rpm}$. Determina:
  </div>
  <ul class="sub-list">
    <li>La velocidad angular ($\omega$) expresada en radianes por segundo ($\text{rad/s}$). <span class="sol"><strong>(Sol: $\omega \approx 15{,}71\text{ rad/s}$)</strong></span></li>
    <li>El período ($T$) y la frecuencia ($f$) del movimiento. <span class="sol"><strong>(Sol: $T = 0{,}40\text{ s}$; $f = 2{,}50\text{ Hz}$)</strong></span></li>
    <li>El módulo de la velocidad lineal ($v$) de un punto situado en el borde exterior. <span class="sol"><strong>(Sol: $v \approx 6{,}28\text{ m/s}$)</strong></span></li>
    <li>La aceleración normal o centrípeta ($a_n$) que experimenta dicho punto. <span class="sol"><strong>(Sol: $a_n \approx 98{,}70\text{ m/s}^2$)</strong></span></li>
  </ul>
</div>

<div class="exercise">
  <div class="exercise-statement">
    <span class="bold">3.</span> Un disco macizo de $0{,}50\text{ m}$ de diámetro, inicialmente en reposo, comienza a girar con una aceleración angular constante $\alpha = 1{,}2\text{ rad/s}^2$. En el instante en que completa $10\text{ vueltas}$, calcula:
  </div>
  <ul class="sub-list">
    <li>La velocidad angular ($\omega$) alcanzada en ese instante. <span class="sol"><strong>(Sol: $\omega \approx 12{,}28\text{ rad/s}$)</strong></span></li>
    <li>El tiempo transcurrido desde el reposo hasta completar dichas vueltas. <span class="sol"><strong>(Sol: $t \approx 10{,}23\text{ s}$)</strong></span></li>
    <li>La velocidad lineal ($v$) de un punto situado en la periferia del disco. <span class="sol"><strong>(Sol: $v \approx 3{,}07\text{ m/s}$)</strong></span></li>
    <li>El módulo de la aceleración tangencial ($a_t$) y de la aceleración normal ($a_n$) en ese instante. <span class="sol"><strong>(Sol: $a_t = 0{,}30\text{ m/s}^2$; $a_n \approx 37{,}70\text{ m/s}^2$)</strong></span></li>
  </ul>
</div>

<div class="exercise">
  <div class="exercise-statement">
    <span class="bold">4.</span> Un volante circular de $0{,}80\text{ m}$ de diámetro, inicialmente en reposo, comienza a girar con una aceleración angular constante $\alpha = 1{,}5\text{ rad/s}^2$. En el instante en que completa $12\text{ vueltas}$, calcula:
  </div>
  <ul class="sub-list">
    <li>La velocidad angular ($\omega$) alcanzada en ese instante. <span class="sol"><strong>(Sol: $\omega \approx 15{,}04\text{ rad/s}$)</strong></span></li>
    <li>El tiempo transcurrido desde el reposo hasta completar dichas vueltas. <span class="sol"><strong>(Sol: $t \approx 10{,}03\text{ s}$)</strong></span></li>
    <li>La velocidad lineal ($v$) de un punto situado en la periferia del volante. <span class="sol"><strong>(Sol: $v \approx 6{,}02\text{ m/s}$)</strong></span></li>
    <li>El módulo de la aceleración tangencial ($a_t$) y de la aceleración normal ($a_n$) en ese instante. <span class="sol"><strong>(Sol: $a_t = 0{,}60\text{ m/s}^2$; $a_n \approx 90{,}48\text{ m/s}^2$)</strong></span></li>
  </ul>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  renderMathInElement(document.body, {
    delimiters: [
      {left: '$$', right: '$$', display: true},
      {left: '$', right: '$', display: false}
    ],
    throwOnError: false
  });
});
</script>
</body>
</html>
"""

def main():
    tex_path = os.path.join(DIR_PATH, "ejercicios_mcu.tex")
    html_path = os.path.join(DIR_PATH, "temp_ejercicios_mcu.html")
    pdf_path = os.path.join(DIR_PATH, "ejercicios_mcu.pdf")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(TEX_CONTENT)
    print(f"Guardado {tex_path}")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)

    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=3000",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(html_path):
        os.remove(html_path)

    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
        print(f"Éxito: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    else:
        print(f"Error compilando PDF: {res.stderr}")

if __name__ == "__main__":
    main()
