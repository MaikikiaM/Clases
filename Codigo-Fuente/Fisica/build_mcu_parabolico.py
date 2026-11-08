import os
import subprocess

OUTPUT_DIR = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Fisica\Cinematica"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# LATEX: UNRESOLVED (FICHA DE TRABAJO)
# -------------------------------------------------------------------------
tex_unresolved = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[top=2.2cm, bottom=2.2cm, left=2.2cm, right=2.2cm]{geometry}
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
    {\LARGE \textbf{Ficha de Trabajo: Cinemática Vectorial, MCU y Tiro Parabólico}}\\[4pt]
    {\large \textbf{Física 1.º de Bachillerato | Preparación para Cinemática Vectorial y Curvatura}}
\end{center}

\vspace{0.3cm}
\begin{tcolorbox}
\textbf{Formulario de apoyo intrínseco y vectorial:}
\begin{itemize}[leftmargin=1.5em, itemsep=2pt]
    \item Velocidad y aceleración vectoriales: $\vec{v}(t) = \frac{d\vec{r}}{dt}$, \quad $\vec{a}(t) = \frac{d\vec{v}}{dt}$.
    \item Aceleración tangencial: $a_t = \frac{\vec{v} \cdot \vec{a}}{|\vec{v}|} = \frac{dv}{dt}$. \quad Mide la variación del módulo de la velocidad.
    \item Aceleración normal / centrípeta: $a_n = \sqrt{a^2 - a_t^2} = \frac{|\vec{v} \times \vec{a}|}{|\vec{v}|} = \frac{v^2}{\rho}$. \quad Mide el cambio de dirección.
    \item Radio de curvatura: $\rho = \frac{v^2}{a_n}$. \quad En un MCU: $\rho = R \implies a_n = \frac{v^2}{R} = \omega^2 R$.
\end{itemize}
\end{tcolorbox}

\vspace{0.4cm}
\noindent\textbf{Bloque 1: Movimiento Circular Uniforme y Componentes de la Aceleración}

\vspace{0.2cm}
\noindent\textbf{1.} Un móvil describe un Movimiento Circular Uniforme (MCU) en una pista de radio $R = 50\text{ m}$ con una velocidad angular constante $\omega = 4\text{ rad/s}$.
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Calcula el período ($T$) y la frecuencia ($f$) del movimiento.
    \item Determina el módulo de la velocidad lineal ($v$) del móvil.
    \item Calcula la aceleración normal o centrípeta ($a_n$).
    \item Sabiendo que en MCU la aceleración tangencial es $a_t = 0$, justifica que el radio de curvatura en cualquier punto coincide con el radio de la circunferencia ($\rho = R$).
\end{enumerate}

\vspace{0.5cm}
\noindent\textbf{2.} Un vehículo circula por una curva de radio $R = 80\text{ m}$. En un instante determinado, su rapidez es $v = 20\text{ m/s}$ y el conductor pisa el acelerador, produciendo una aceleración tangencial constante $a_t = 3\text{ m/s}^2$.
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Calcula la aceleración normal ($a_n$) en ese instante.
    \item Determina el módulo de la aceleración total ($\vec{a} = \vec{a}_t + \vec{a}_n$).
    \item Calcula el radio de curvatura ($\rho$) a partir de $v$ y $a_n$ y explica por qué coincide con el radio de la curva.
\end{enumerate}

\newpage

\noindent\textbf{Bloque 2: Tiro Parabólico, Cinemática Vectorial y Radio de Curvatura}

\vspace{0.4cm}
\noindent\textbf{3.} Desde lo alto de un acantilado vertical de $y_0 = 45\text{ m}$ de altura sobre el nivel del mar, se lanza horizontalmente un proyectil con una velocidad inicial de $v_0 = 30\text{ m/s}$ ($g = 9{,}8\text{ m/s}^2$).
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Escribe las ecuaciones vectoriales de posición $\vec{r}(t) = x(t)\,\vec{i} + y(t)\,\vec{j}$ y de velocidad $\vec{v}(t)$.
    \item Obtén la ecuación de la trayectoria $y(x)$ eliminando el tiempo $t$. ¿Qué forma geométrica tiene?
    \item Calcula el tiempo que tarda el proyectil en impactar contra el agua ($y = 0$) y el alcance horizontal máximo ($x_{\text{máx}}$).
    \item Halla el vector velocidad $\vec{v}$ y su rapidez al tocar el agua.
\end{enumerate}

\vspace{0.6cm}
\noindent\textbf{4.} Una partícula describe un tiro parabólico cuya ecuación vectorial de posición en el Sistema Internacional viene dada por:
\[
\vec{r}(t) = (20t)\,\vec{i} + (15t - 5t^2)\,\vec{j}\text{ (m)}
\]
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Obtén las expresiones vectoriales de la velocidad $\vec{v}(t)$ y de la aceleración $\vec{a}(t)$ mediante derivación respecto al tiempo.
    \item Deduce la ecuación cartesiana de la trayectoria $y(x)$ y determina la altura máxima alcanzada (instante en que $v_y = 0$).
    \item En el punto más alto de la trayectoria ($t = 1{,}5\text{ s}$), calcula la velocidad $v$, la aceleración tangencial $a_t$, la aceleración normal $a_n$ y el radio de curvatura $\rho$.
    \item En el instante $t = 1\text{ s}$, calcula:
    \begin{itemize}[leftmargin=1.5em, itemsep=3pt]
        \item El vector velocidad $\vec{v}(1)$ y su módulo $|\vec{v}(1)|$.
        \item La aceleración tangencial $a_t = \frac{\vec{v} \cdot \vec{a}}{|\vec{v}|}$.
        \item La aceleración normal $a_n = \sqrt{a^2 - a_t^2}$.
        \item El radio de curvatura $\rho = \frac{v^2}{a_n}$.
    \end{itemize}
\end{enumerate}

\end{document}
"""

with open(os.path.join(OUTPUT_DIR, "ejercicios_preparacion_mcu_y_parabolico.tex"), "w", encoding="utf-8") as f:
    f.write(tex_unresolved)

# -------------------------------------------------------------------------
# LATEX: SOLVED (SOLUCIONARIO DETALLADO)
# -------------------------------------------------------------------------
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
    {\LARGE \textbf{Solucionario Detallado: MCU y Tiro Parabólico}}\\[4pt]
    {\large \textbf{Física 1.º de Bachillerato | Preparación para Cinemática Vectorial}}
\end{center}

\vspace{0.2cm}
\noindent\textbf{Resolución Ejercicio 1 (MCU y Aceleración Centrípeta):}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{a) Período y frecuencia:}
    \[
    T = \frac{2\pi}{\omega} = \frac{2\pi}{4} = \frac{\pi}{2} \approx \mathbf{1{,}57\text{ s}} \qquad f = \frac{1}{T} = \frac{2}{\pi} \approx \mathbf{0{,}64\text{ Hz}}
    \]
    \item \textbf{b) Velocidad lineal ($v$):}
    \[
    v = \omega \cdot R = 4\text{ rad/s} \times 50\text{ m} = \mathbf{200\text{ m/s}}
    \]
    \item \textbf{c) Aceleración centrípeta o normal ($a_n$):}
    \[
    a_n = \frac{v^2}{R} = \omega^2 R = 4^2 \times 50 = \mathbf{800\text{ m/s}^2}
    \]
    \item \textbf{d) Radio de curvatura ($\rho$):}
    \[
    \rho = \frac{v^2}{a_n} = \frac{200^2}{800} = \frac{40000}{800} = \mathbf{50\text{ m}} = R
    \]
    Como la trayectoria es una circunferencia de radio $R$, su radio de curvatura es exactamente $R$ en todos los puntos.
\end{itemize}

\vspace{0.4cm}
\noindent\textbf{Resolución Ejercicio 2 (Componentes de la Aceleración):}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{a) Aceleración normal ($a_n$):}
    \[
    a_n = \frac{v^2}{R} = \frac{20^2}{80} = \frac{400}{80} = \mathbf{5\text{ m/s}^2}
    \]
    \item \textbf{b) Aceleración total ($a$):}
    Como $\vec{a}_t \perp \vec{a}_n$:
    \[
    a = \sqrt{a_t^2 + a_n^2} = \sqrt{3^2 + 5^2} = \sqrt{9 + 25} = \sqrt{34} \approx \mathbf{5{,}83\text{ m/s}^2}
    \]
    \item \textbf{c) Radio de curvatura ($\rho$):}
    \[
    \rho = \frac{v^2}{a_n} = \frac{20^2}{5} = \frac{400}{5} = \mathbf{80\text{ m}} = R
    \]
    La aceleración tangencial solo incrementa la rapidez, mientras que la curvatura de la trayectoria está determinada únicamente por la aceleración normal que desvía la trayectoria.
\end{itemize}

\vspace{0.4cm}
\noindent\textbf{Resolución Ejercicio 3 (Tiro Parabólico y Trayectoria):}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{a) Ecuaciones vectoriales:}
    \[
    \vec{r}(t) = (30t)\,\vec{i} + (45 - 4{,}9t^2)\,\vec{j}\text{ (m)} \qquad \vec{v}(t) = 30\,\vec{i} - 9{,}8t\,\vec{j}\text{ (m/s)}
    \]
    \item \textbf{b) Ecuación de la trayectoria $y(x)$:}
    \[
    x = 30t \implies t = \frac{x}{30} \implies y(x) = 45 - 4{,}9\left(\frac{x}{30}\right)^2 = \mathbf{45 - \frac{49}{9000}x^2 \approx 45 - 0{,}00544\,x^2}
    \]
    \item \textbf{c) Tiempo de vuelo y alcance horizontal:}
    \[
    y = 0 \implies 45 - 4{,}9t^2 = 0 \implies t = \sqrt{\frac{45}{4{,}9}} \approx \mathbf{3{,}03\text{ s}}
    \]
    \[
    x_{\text{máx}} = 30 \times 3{,}0305 = \mathbf{90{,}91\text{ m}}
    \]
    \item \textbf{d) Velocidad de impacto:}
    \[
    \vec{v}(3{,}03) = 30\,\vec{i} - 9{,}8(3{,}0305)\,\vec{j} = \mathbf{30\,\vec{i} - 29{,}70\,\vec{j}\text{ m/s}}
    \]
    \[
    v = \sqrt{30^2 + (-29{,}70)^2} = \sqrt{900 + 882} = \sqrt{1782} \approx \mathbf{42{,}21\text{ m/s}}
    \]
\end{itemize}

\newpage

\noindent\textbf{Resolución Ejercicio 4 (Cinemática Vectorial, $a_t$, $a_n$ y Curvatura):}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{a) Vectores velocidad y aceleración:}
    \[
    \vec{v}(t) = \frac{d\vec{r}}{dt} = \mathbf{20\,\vec{i} + (15 - 10t)\,\vec{j}\text{ (m/s)}} \qquad \vec{a}(t) = \frac{d\vec{v}}{dt} = \mathbf{-10\,\vec{j}\text{ (m/s}^2\text{)}}
    \]
    \item \textbf{b) Trayectoria y altura máxima:}
    \[
    x = 20t \implies t = \frac{x}{20} \implies y(x) = 15\left(\frac{x}{20}\right) - 5\left(\frac{x}{20}\right)^2 = \mathbf{\frac{3}{4}x - \frac{1}{80}x^2}
    \]
    Altura máxima ($v_y = 0 \implies 15 - 10t = 0 \implies t = 1{,}5\text{ s}$):
    \[
    y_{\text{máx}} = y(1{,}5) = 15(1{,}5) - 5(1{,}5^2) = 22{,}5 - 11{,}25 = \mathbf{11{,}25\text{ m}}
    \]
    \item \textbf{c) En el vértice de la parábola ($t = 1{,}5\text{ s}$):}
    \begin{itemize}[leftmargin=1.5em, itemsep=2pt]
        \item $\vec{v}(1{,}5) = 20\,\vec{i} + 0\,\vec{j}\text{ m/s} \implies v = \mathbf{20\text{ m/s}}$ (horizontal).
        \item $\vec{a} = -10\,\vec{j}\text{ m/s}^2$ (vertical hacia abajo, perpendicular a $\vec{v}$).
        \item $a_t = \frac{\vec{v} \cdot \vec{a}}{v} = \frac{(20)(0) + (0)(-10)}{20} = \mathbf{0\text{ m/s}^2}$.
        \item $a_n = |\vec{a}| = \mathbf{10\text{ m/s}^2}$.
        \item Radio de curvatura: $\rho = \frac{v^2}{a_n} = \frac{20^2}{10} = \frac{400}{10} = \mathbf{40\text{ m}}$.
    \end{itemize}
    \item \textbf{d) En el instante $t = 1\text{ s}$:}
    \begin{itemize}[leftmargin=1.5em, itemsep=2pt]
        \item Vector velocidad: $\vec{v}(1) = 20\,\vec{i} + [15 - 10(1)]\,\vec{j} = \mathbf{20\,\vec{i} + 5\,\vec{j}\text{ m/s}}$.
        \item Módulo: $v(1) = \sqrt{20^2 + 5^2} = \sqrt{425} = 5\sqrt{17} \approx \mathbf{20{,}62\text{ m/s}}$.
        \item Aceleración tangencial ($a_t$):
        \[
        a_t = \frac{\vec{v} \cdot \vec{a}}{|\vec{v}|} = \frac{(20)(0) + (5)(-10)}{\sqrt{425}} = \frac{-50}{5\sqrt{17}} = -\frac{10}{\sqrt{17}} \approx \mathbf{-2{,}43\text{ m/s}^2}
        \]
        *(Signo negativo porque el cuerpo asciende frenándose)*.
        \item Aceleración normal ($a_n$):
        \[
        a_n = \sqrt{a^2 - a_t^2} = \sqrt{10^2 - \left(-\frac{10}{\sqrt{17}}\right)^2} = \sqrt{100 - \frac{100}{17}} = \sqrt{\frac{1600}{17}} = \frac{40}{\sqrt{17}} \approx \mathbf{9{,}70\text{ m/s}^2}
        \]
        \item Radio de curvatura ($\rho$):
        \[
        \rho = \frac{v^2}{a_n} = \frac{425}{\frac{40}{\sqrt{17}}} = \frac{425\sqrt{17}}{40} = \frac{85\sqrt{17}}{8} \approx \mathbf{43{,}81\text{ m}}
        \]
    \end{itemize}
\end{itemize}

\end{document}
"""

with open(os.path.join(OUTPUT_DIR, "ejercicios_preparacion_mcu_y_parabolico_resueltos.tex"), "w", encoding="utf-8") as f:
    f.write(tex_solved)

print("Archivos LaTeX guardados.")

# -------------------------------------------------------------------------
# HTML FOR PDF COMPILATION
# -------------------------------------------------------------------------
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
    margin: 20mm 22mm 20mm 22mm;
  }
  * {
    box-sizing: border-box;
  }
  body {
    font-family: 'Calibri', 'Carlito', 'Segoe UI', sans-serif;
    font-size: 11pt;
    line-height: 1.38;
    color: #111;
    margin: 0;
    padding: 0;
  }
  .page {
    page-break-after: always;
    min-height: 250mm;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  .page:last-child {
    page-break-after: avoid;
  }
  .doc-header {
    text-align: center;
    margin-bottom: 18px;
  }
  .doc-title {
    font-size: 15pt;
    font-weight: bold;
    margin-bottom: 3px;
  }
  .doc-subtitle {
    font-size: 11pt;
    font-weight: bold;
    color: #333;
  }
  .box {
    border: 0.8pt solid #000;
    border-radius: 6px;
    padding: 8px 12px;
    margin-bottom: 15px;
    background: #fafafa;
    font-size: 10pt;
  }
  .box-title {
    font-weight: bold;
    margin-bottom: 4px;
  }
  ol, ul {
    margin-top: 4px;
    margin-bottom: 4px;
    padding-left: 22px;
  }
  li {
    margin-bottom: 6px;
  }
  .alpha-list {
    list-style-type: lower-alpha;
    font-weight: normal;
  }
  .alpha-list > li {
    margin-bottom: 10px;
  }
  .alpha-list > li::marker {
    font-weight: bold;
  }
  .bold {
    font-weight: bold;
  }
  .section-heading {
    font-size: 11.5pt;
    font-weight: bold;
    margin: 12px 0 6px 0;
    padding-bottom: 2px;
    border-bottom: 0.8pt solid #ccc;
  }
  p {
    margin: 6px 0;
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

body_unresolved_html = r"""
<!-- PÁGINA 1 -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Ficha de Trabajo: Cinemática Vectorial, MCU y Tiro Parabólico</div>
    <div class="doc-subtitle">Física 1.º de Bachillerato | Preparación para Cinemática Vectorial y Curvatura</div>
  </div>

  <div class="box">
    <div class="box-title">Formulario de apoyo intrínseco y vectorial:</div>
    <ul>
      <li>Velocidad y aceleración vectoriales: $\vec{v}(t) = \frac{d\vec{r}}{dt}, \quad \vec{a}(t) = \frac{d\vec{v}}{dt}$.</li>
      <li>Aceleración tangencial: $a_t = \frac{\vec{v} \cdot \vec{a}}{|\vec{v}|} = \frac{dv}{dt}$. Mide la variación del módulo de la velocidad.</li>
      <li>Aceleración normal / centrípeta: $a_n = \sqrt{a^2 - a_t^2} = \frac{|\vec{v} \times \vec{a}|}{|\vec{v}|} = \frac{v^2}{\rho}$. Mide el cambio de dirección.</li>
      <li>Radio de curvatura: $\rho = \frac{v^2}{a_n}$. En un MCU: $\rho = R \implies a_n = \frac{v^2}{R} = \omega^2 R$.</li>
    </ul>
  </div>

  <div class="section-heading">Bloque 1: Movimiento Circular Uniforme y Componentes de la Aceleración</div>

  <p><span class="bold">1.</span> Un móvil describe un Movimiento Circular Uniforme (MCU) en una pista de radio $R = 50\text{ m}$ con una velocidad angular constante $\omega = 4\text{ rad/s}$.</p>
  <ol class="alpha-list">
    <li>Calcula el período ($T$) y la frecuencia ($f$) del movimiento.</li>
    <li>Determina el módulo de la velocidad lineal ($v$) del móvil.</li>
    <li>Calcula la aceleración normal o centrípeta ($a_n$).</li>
    <li>Sabiendo que en MCU la aceleración tangencial es $a_t = 0$, justifica que el radio de curvatura en cualquier punto coincide con el radio de la circunferencia ($\rho = R$).</li>
  </ol>

  <p style="margin-top: 15px;"><span class="bold">2.</span> Un vehículo circula por una curva de radio $R = 80\text{ m}$. En un instante determinado, su rapidez es $v = 20\text{ m/s}$ y el conductor pisa el acelerador, produciendo una aceleración tangencial constante $a_t = 3\text{ m/s}^2$.</p>
  <ol class="alpha-list">
    <li>Calcula la aceleración normal ($a_n$) en ese instante.</li>
    <li>Determina el módulo de la aceleración total ($\vec{a} = \vec{a}_t + \vec{a}_n$).</li>
    <li>Calcula el radio de curvatura ($\rho$) a partir de $v$ y $a_n$ y explica por qué coincide con el radio de la curva.</li>
  </ol>
</div>

<!-- PÁGINA 2 -->
<div class="page">
  <div class="section-heading" style="margin-top: 0;">Bloque 2: Tiro Parabólico, Cinemática Vectorial y Radio de Curvatura</div>

  <p><span class="bold">3.</span> Desde lo alto de un acantilado vertical de $y_0 = 45\text{ m}$ de altura sobre el nivel del mar, se lanza horizontalmente un proyectil con una velocidad inicial de $v_0 = 30\text{ m/s}$ ($g = 9{,}8\text{ m/s}^2$).</p>
  <ol class="alpha-list">
    <li>Escribe las ecuaciones vectoriales de posición $\vec{r}(t) = x(t)\,\vec{i} + y(t)\,\vec{j}$ y de velocidad $\vec{v}(t)$.</li>
    <li>Obtén la ecuación de la trayectoria $y(x)$ eliminando el tiempo $t$. ¿Qué forma geométrica tiene?</li>
    <li>Calcula el tiempo que tarda el proyectil en impactar contra el agua ($y = 0$) y el alcance horizontal máximo ($x_{\text{máx}}$).</li>
    <li>Halla el vector velocidad $\vec{v}$ y su rapidez al tocar el agua.</li>
  </ol>

  <p style="margin-top: 20px;"><span class="bold">4.</span> Una partícula describe un tiro parabólico cuya ecuación vectorial de posición en el Sistema Internacional viene dada por:
  $$\vec{r}(t) = (20t)\,\vec{i} + (15t - 5t^2)\,\vec{j}\text{ (m)}$$</p>
  <ol class="alpha-list">
    <li>Obtén las expresiones vectoriales de la velocidad $\vec{v}(t)$ y de la aceleración $\vec{a}(t)$ mediante derivación respecto al tiempo.</li>
    <li>Deduce la ecuación cartesiana de la trayectoria $y(x)$ y determina la altura máxima alcanzada (instante en que $v_y = 0$).</li>
    <li>En el punto más alto de la trayectoria ($t = 1{,}5\text{ s}$), calcula la velocidad $v$, la aceleración tangencial $a_t$, la aceleración normal $a_n$ y el radio de curvatura $\rho$.</li>
    <li>En el instante $t = 1\text{ s}$, calcula:
      <ul>
        <li>El vector velocidad $\vec{v}(1)$ y su módulo $|\vec{v}(1)|$.</li>
        <li>La aceleración tangencial $a_t = \frac{\vec{v} \cdot \vec{a}}{|\vec{v}|}$.</li>
        <li>La aceleración normal $a_n = \sqrt{a^2 - a_t^2}$.</li>
        <li>El radio de curvatura $\rho = \frac{v^2}{a_n}$.</li>
      </ul>
    </li>
  </ol>
</div>
"""

body_solved_html = r"""
<!-- PÁGINA 1 -->
<div class="page">
  <div class="doc-header">
    <div class="doc-title">Solucionario Detallado: MCU y Tiro Parabólico</div>
    <div class="doc-subtitle">Física 1.º de Bachillerato | Preparación para Cinemática Vectorial</div>
  </div>

  <p class="bold" style="font-size: 11.5pt;">Resolución Ejercicio 1 (MCU y Aceleración Centrípeta):</p>
  <ul>
    <li><span class="bold">a) Período y frecuencia:</span>
      $$T = \frac{2\pi}{\omega} = \frac{2\pi}{4} = \frac{\pi}{2} \approx \mathbf{1{,}57\text{ s}} \qquad f = \frac{1}{T} = \frac{2}{\pi} \approx \mathbf{0{,}64\text{ Hz}}$$
    </li>
    <li><span class="bold">b) Velocidad lineal ($v$):</span>
      $$v = \omega \cdot R = 4\text{ rad/s} \times 50\text{ m} = \mathbf{200\text{ m/s}}$$
    </li>
    <li><span class="bold">c) Aceleración centrípeta o normal ($a_n$):</span>
      $$a_n = \frac{v^2}{R} = \omega^2 R = 4^2 \times 50 = \mathbf{800\text{ m/s}^2}$$
    </li>
    <li><span class="bold">d) Radio de curvatura ($\rho$):</span>
      $$\rho = \frac{v^2}{a_n} = \frac{200^2}{800} = \frac{40000}{800} = \mathbf{50\text{ m}} = R$$
      Como la trayectoria es circular, el radio de curvatura coincide con el radio de la pista.
    </li>
  </ul>

  <p class="bold" style="font-size: 11.5pt; margin-top: 15px;">Resolución Ejercicio 2 (Componentes de la Aceleración):</p>
  <ul>
    <li><span class="bold">a) Aceleración normal ($a_n$):</span>
      $$a_n = \frac{v^2}{R} = \frac{20^2}{80} = \frac{400}{80} = \mathbf{5\text{ m/s}^2}$$
    </li>
    <li><span class="bold">b) Aceleración total ($a$):</span>
      $$a = \sqrt{a_t^2 + a_n^2} = \sqrt{3^2 + 5^2} = \sqrt{9 + 25} = \sqrt{34} \approx \mathbf{5{,}83\text{ m/s}^2}$$
    </li>
    <li><span class="bold">c) Radio de curvatura ($\rho$):</span>
      $$\rho = \frac{v^2}{a_n} = \frac{20^2}{5} = \frac{400}{5} = \mathbf{80\text{ m}} = R$$
    </li>
  </ul>

  <p class="bold" style="font-size: 11.5pt; margin-top: 15px;">Resolución Ejercicio 3 (Tiro Parabólico y Trayectoria):</p>
  <ul>
    <li><span class="bold">a) Ecuaciones vectoriales:</span>
      $$\vec{r}(t) = (30t)\,\vec{i} + (45 - 4{,}9t^2)\,\vec{j}\text{ (m)} \qquad \vec{v}(t) = 30\,\vec{i} - 9{,}8t\,\vec{j}\text{ (m/s)}$$
    </li>
    <li><span class="bold">b) Ecuación de la trayectoria $y(x)$:</span>
      $$x = 30t \implies t = \frac{x}{30} \implies y(x) = 45 - 4{,}9\left(\frac{x}{30}\right)^2 = \mathbf{45 - \frac{49}{9000}x^2 \approx 45 - 0{,}00544\,x^2}$$
    </li>
    <li><span class="bold">c) Tiempo de vuelo y alcance:</span>
      $$y = 0 \implies 45 - 4{,}9t^2 = 0 \implies t = \sqrt{\frac{45}{4{,}9}} \approx \mathbf{3{,}03\text{ s}} \qquad x_{\text{máx}} = 30(3{,}0305) = \mathbf{90{,}91\text{ m}}$$
    </li>
    <li><span class="bold">d) Velocidad al llegar al suelo:</span>
      $$\vec{v}(3{,}03) = 30\,\vec{i} - 29{,}70\,\vec{j}\text{ m/s} \implies v = \sqrt{30^2 + (-29{,}70)^2} = \sqrt{1782} \approx \mathbf{42{,}21\text{ m/s}}$$
    </li>
  </ul>
</div>

<!-- PÁGINA 2 -->
<div class="page">
  <p class="bold" style="font-size: 11.5pt; margin-top: 0;">Resolución Ejercicio 4 (Cinemática Vectorial, $a_t$, $a_n$ y Curvatura):</p>
  <ul>
    <li><span class="bold">a) Vectores velocidad y aceleración:</span>
      $$\vec{v}(t) = \frac{d\vec{r}}{dt} = \mathbf{20\,\vec{i} + (15 - 10t)\,\vec{j}\text{ (m/s)}} \qquad \vec{a}(t) = \frac{d\vec{v}}{dt} = \mathbf{-10\,\vec{j}\text{ (m/s}^2\text{)}}$$
    </li>
    <li><span class="bold">b) Trayectoria y altura máxima:</span>
      $$x = 20t \implies t = \frac{x}{20} \implies y(x) = 15\left(\frac{x}{20}\right) - 5\left(\frac{x}{20}\right)^2 = \mathbf{\frac{3}{4}x - \frac{1}{80}x^2}$$
      Altura máxima ($v_y = 0 \implies 15 - 10t = 0 \implies t = 1{,}5\text{ s}$):
      $$y_{\text{máx}} = y(1{,}5) = 15(1{,}5) - 5(1{,}5^2) = 22{,}5 - 11{,}25 = \mathbf{11{,}25\text{ m}}$$
    </li>
    <li><span class="bold">c) En el vértice de la parábola ($t = 1{,}5\text{ s}$):</span>
      <ul>
        <li>$\vec{v}(1{,}5) = 20\,\vec{i} + 0\,\vec{j}\text{ m/s} \implies v = \mathbf{20\text{ m/s}}$ (horizontal).</li>
        <li>$\vec{a} = -10\,\vec{j}\text{ m/s}^2$ (vertical hacia abajo, perpendicular a $\vec{v}$).</li>
        <li>$a_t = \frac{\vec{v} \cdot \vec{a}}{v} = \frac{(20)(0) + (0)(-10)}{20} = \mathbf{0\text{ m/s}^2}$.</li>
        <li>$a_n = |\vec{a}| = \mathbf{10\text{ m/s}^2}$.</li>
        <li>Radio de curvatura: $\rho = \frac{v^2}{a_n} = \frac{20^2}{10} = \frac{400}{10} = \mathbf{40\text{ m}}$.</li>
      </ul>
    </li>
    <li><span class="bold">d) En el instante $t = 1\text{ s}$:</span>
      <ul>
        <li>Vector velocidad: $\vec{v}(1) = 20\,\vec{i} + [15 - 10(1)]\,\vec{j} = \mathbf{20\,\vec{i} + 5\,\vec{j}\text{ m/s}}$.</li>
        <li>Módulo: $v(1) = \sqrt{20^2 + 5^2} = \sqrt{425} = 5\sqrt{17} \approx \mathbf{20{,}62\text{ m/s}}$.</li>
        <li>Aceleración tangencial ($a_t$):
          $$a_t = \frac{\vec{v} \cdot \vec{a}}{|\vec{v}|} = \frac{(20)(0) + (5)(-10)}{\sqrt{425}} = \frac{-50}{5\sqrt{17}} = -\frac{10}{\sqrt{17}} \approx \mathbf{-2{,}43\text{ m/s}^2}$$
        </li>
        <li>Aceleración normal ($a_n$):
          $$a_n = \sqrt{a^2 - a_t^2} = \sqrt{10^2 - \left(-\frac{10}{\sqrt{17}}\right)^2} = \sqrt{100 - \frac{100}{17}} = \frac{40}{\sqrt{17}} \approx \mathbf{9{,}70\text{ m/s}^2}$$
        </li>
        <li>Radio de curvatura ($\rho$):
          $$\rho = \frac{v^2}{a_n} = \frac{425}{\frac{40}{\sqrt{17}}} = \frac{425\sqrt{17}}{40} = \frac{85\sqrt{17}}{8} \approx \mathbf{43{,}81\text{ m}}$$
        </li>
      </ul>
    </li>
  </ul>
</div>
"""

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
    compile_pdf("Ficha de Trabajo: MCU y Tiro Parabólico", body_unresolved_html, "ejercicios_preparacion_mcu_y_parabolico.pdf")
    compile_pdf("Solucionario: MCU y Tiro Parabólico", body_solved_html, "ejercicios_preparacion_mcu_y_parabolico_resueltos.pdf")
