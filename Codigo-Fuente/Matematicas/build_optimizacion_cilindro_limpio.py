import os
import subprocess

OUTPUT_DIR = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Matematicas\Derivadas"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# -------------------------------------------------------------------------
# LATEX SOURCE: EJERCICIOS (LIMPIO)
# -------------------------------------------------------------------------
tex_unresolved = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[top=2.2cm, bottom=2.2cm, left=2.2cm, right=2.2cm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{enumitem}
\usepackage{microtype}

\setmainfont{Calibri}
\linespread{1.15}

\begin{document}
\pagestyle{empty}

\noindent\textbf{1.} Se desea fabricar un depósito cilíndrico cerrado con una capacidad de $16\pi\text{ m}^3$. El coste del material utilizado para la tapa superior es de $3\text{ €/m}^2$, el del suelo o base inferior es de $5\text{ €/m}^2$, y el de la pared lateral es de $4\text{ €/m}^2$.
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Expresa la función del coste total de fabricación, $C(r)$, en función únicamente del radio $r$ de la base.
    \item Determina las dimensiones que debe tener el depósito (radio $r$ y altura $h$) para que el coste total sea mínimo.
    \item Justifica, mediante el criterio de la segunda derivada, que se trata efectivamente de un mínimo de coste y calcula el valor de dicho coste mínimo.
\end{enumerate}

\vspace{1cm}

\noindent\textbf{2.} Se desea fabricar un depósito cilíndrico cerrado con una capacidad de $54\pi\text{ m}^3$. El coste del material utilizado para la tapa superior es de $4\text{ €/m}^2$, el del suelo o base inferior es de $8\text{ €/m}^2$, y el de la pared lateral es de $6\text{ €/m}^2$.
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item Expresa la función del coste total de fabricación, $C(r)$, en función únicamente del radio $r$ de la base.
    \item Determina las dimensiones que debe tener el depósito (radio $r$ y altura $h$) para que el coste total sea mínimo.
    \item Justifica, mediante el criterio de la segunda derivada, que se trata efectivamente de un mínimo de coste y calcula el valor de dicho coste mínimo.
\end{enumerate}

\end{document}
"""

# -------------------------------------------------------------------------
# LATEX SOURCE: RESUELTO (LIMPIO)
# -------------------------------------------------------------------------
tex_solved = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[top=2.2cm, bottom=2.2cm, left=2.2cm, right=2.2cm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{enumitem}
\usepackage{microtype}

\setmainfont{Calibri}
\linespread{1.15}

\begin{document}
\pagestyle{empty}

\noindent\textbf{1.} Se desea fabricar un depósito cilíndrico cerrado con una capacidad de $V = 16\pi\text{ m}^3$. Materiales: tapa superior a $3\text{ €/m}^2$, base inferior a $5\text{ €/m}^2$ y pared lateral a $4\text{ €/m}^2$.
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item \textbf{Función del coste total $C(r)$:}
    \begin{itemize}[leftmargin=1.5em, itemsep=2pt]
        \item Ligadura del volumen: $V = \pi r^2 h = 16\pi \implies h = \frac{16}{r^2}$.
        \item Coste total:
        \[
        C(r) = 3(\pi r^2) + 5(\pi r^2) + 4(2\pi r h) = 8\pi r^2 + 8\pi r \left(\frac{16}{r^2}\right) = \mathbf{8\pi r^2 + \frac{128\pi}{r}}
        \]
    \end{itemize}

    \item \textbf{Dimensiones óptimas:}
    \begin{itemize}[leftmargin=1.5em, itemsep=2pt]
        \item Primera derivada:
        \[
        C'(r) = 16\pi r - \frac{128\pi}{r^2} = 0 \implies 16\pi r^3 = 128\pi \implies r^3 = 8 \implies \mathbf{r = 2\text{ m}}
        \]
        \item Altura correspondiente:
        \[
        h = \frac{16}{2^2} = \mathbf{4\text{ m}}
        \]
    \end{itemize}

    \item \textbf{Justificación y coste mínimo:}
    \begin{itemize}[leftmargin=1.5em, itemsep=2pt]
        \item Segunda derivada: $C''(r) = 16\pi + \frac{256\pi}{r^3} \implies C''(2) = 16\pi + \frac{256\pi}{8} = 48\pi > 0 \implies \textbf{Mínimo}$.
        \item Coste mínimo: $C(2) = 8\pi(2^2) + \frac{128\pi}{2} = 32\pi + 64\pi = \mathbf{96\pi\text{ €} \approx 301{,}59\text{ €}}$.
    \end{itemize}
\end{enumerate}

\vspace{0.8cm}

\noindent\textbf{2.} Se desea fabricar un depósito cilíndrico cerrado con una capacidad de $V = 54\pi\text{ m}^3$. Materiales: tapa superior a $4\text{ €/m}^2$, base inferior a $8\text{ €/m}^2$ y pared lateral a $6\text{ €/m}^2$.
\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=2em, itemsep=6pt]
    \item \textbf{Función del coste total $C(r)$:}
    \begin{itemize}[leftmargin=1.5em, itemsep=2pt]
        \item Ligadura del volumen: $V = \pi r^2 h = 54\pi \implies h = \frac{54}{r^2}$.
        \item Coste total:
        \[
        C(r) = 4(\pi r^2) + 8(\pi r^2) + 6(2\pi r h) = 12\pi r^2 + 12\pi r \left(\frac{54}{r^2}\right) = \mathbf{12\pi r^2 + \frac{648\pi}{r}}
        \]
    \end{itemize}

    \item \textbf{Dimensiones óptimas:}
    \begin{itemize}[leftmargin=1.5em, itemsep=2pt]
        \item Primera derivada:
        \[
        C'(r) = 24\pi r - \frac{648\pi}{r^2} = 0 \implies 24\pi r^3 = 648\pi \implies r^3 = 27 \implies \mathbf{r = 3\text{ m}}
        \]
        \item Altura correspondiente:
        \[
        h = \frac{54}{3^2} = \mathbf{6\text{ m}}
        \]
    \end{itemize}

    \item \textbf{Justificación y coste mínimo:}
    \begin{itemize}[leftmargin=1.5em, itemsep=2pt]
        \item Segunda derivada: $C''(r) = 24\pi + \frac{1296\pi}{r^3} \implies C''(3) = 24\pi + \frac{1296\pi}{27} = 72\pi > 0 \implies \textbf{Mínimo}$.
        \item Coste mínimo: $C(3) = 12\pi(3^2) + \frac{648\pi}{3} = 108\pi + 216\pi = \mathbf{324\pi\text{ €} \approx 1017{,}88\text{ €}}$.
    \end{itemize}
\end{enumerate}

\end{document}
"""

with open(os.path.join(OUTPUT_DIR, "ejercicios_optimizacion_cilindro_precios.tex"), "w", encoding="utf-8") as f:
    f.write(tex_unresolved)

with open(os.path.join(OUTPUT_DIR, "ejercicios_optimizacion_cilindro_precios_resueltos.tex"), "w", encoding="utf-8") as f:
    f.write(tex_solved)

# -------------------------------------------------------------------------
# HTML TEMPLATE (BLACK & WHITE, CLEAN, NO HEADERS, NO TITLES)
# -------------------------------------------------------------------------
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
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
    line-height: 1.45;
    color: #000;
    margin: 0;
    padding: 0;
  }
  .page {
    page-break-after: always;
    min-height: 250mm;
  }
  .page:last-child {
    page-break-after: avoid;
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
  }
  .alpha-list > li::marker {
    font-weight: bold;
  }
  p {
    margin: 8px 0;
  }
  .bold {
    font-weight: bold;
  }
  .katex-display {
    margin: 10px 0 !important;
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
<div class="page">
  <p><span class="bold">1.</span> Se desea fabricar un depósito cilíndrico cerrado con una capacidad fija de $16\pi\text{ m}^3$. El coste del material utilizado para la tapa superior es de $3\text{ €/m}^2$, el del suelo o base inferior es de $5\text{ €/m}^2$, y el de la pared lateral es de $4\text{ €/m}^2$.</p>
  
  <ol class="alpha-list" style="margin-top: 14px;">
    <li>Expresa la función del coste total de fabricación, $C(r)$, en función únicamente del radio $r$ de la base.</li>
    <li>Determina las dimensiones que debe tener el depósito (radio $r$ y altura $h$) para que el coste total sea mínimo.</li>
    <li>Justifica, mediante el criterio de la segunda derivada, que se trata efectivamente de un mínimo de coste y calcula el valor de dicho coste mínimo.</li>
  </ol>

  <div style="margin-top: 40px;"></div>

  <p><span class="bold">2.</span> Se desea fabricar un depósito cilíndrico cerrado con una capacidad fija de $54\pi\text{ m}^3$. El coste del material utilizado para la tapa superior es de $4\text{ €/m}^2$, el del suelo o base inferior es de $8\text{ €/m}^2$, y el de la pared lateral es de $6\text{ €/m}^2$.</p>
  
  <ol class="alpha-list" style="margin-top: 14px;">
    <li>Expresa la función del coste total de fabricación, $C(r)$, en función únicamente del radio $r$ de la base.</li>
    <li>Determina las dimensiones que debe tener el depósito (radio $r$ y altura $h$) para que el coste total sea mínimo.</li>
    <li>Justifica, mediante el criterio de la segunda derivada, que se trata efectivamente de un mínimo de coste y calcula el valor de dicho coste mínimo.</li>
  </ol>
</div>
"""

body_solved_html = r"""
<!-- PÁGINA 1: EJERCICIO 1 -->
<div class="page">
  <p><span class="bold">1.</span> Se desea fabricar un depósito cilíndrico cerrado con una capacidad de $V = 16\pi\text{ m}^3$. Materiales: tapa superior a $3\text{ €/m}^2$, base inferior a $5\text{ €/m}^2$ y pared lateral a $4\text{ €/m}^2$.</p>
  
  <ol class="alpha-list" style="margin-top: 15px;">
    <li><span class="bold">Función del coste total $C(r)$ y ligadura:</span>
      <ul>
        <li>Ligadura del volumen:
          $$V = \pi r^2 h = 16\pi \implies \mathbf{h = \frac{16}{r^2}}$$
        </li>
        <li>Coste total de los materiales (Tapa + Suelo + Pared):
          $$C(r) = 3(\pi r^2) + 5(\pi r^2) + 4(2\pi r h) = 8\pi r^2 + 8\pi r \left(\frac{16}{r^2}\right) = \mathbf{8\pi r^2 + \frac{128\pi}{r}}$$
        </li>
      </ul>
    </li>
    <li><span class="bold">Dimensiones óptimas ($C'(r) = 0$):</span>
      <ul>
        <li>Derivamos e igualamos a cero:
          $$C'(r) = 16\pi r - \frac{128\pi}{r^2} = 0 \implies 16\pi r = \frac{128\pi}{r^2} \implies 16\pi r^3 = 128\pi \implies r^3 = 8 \implies \mathbf{r = 2\text{ m}}$$
        </li>
        <li>Altura correspondiente:
          $$h = \frac{16}{2^2} = \frac{16}{4} = \mathbf{4\text{ m}}$$
        </li>
      </ul>
    </li>
    <li><span class="bold">Justificación y coste mínimo:</span>
      <ul>
        <li>Segunda derivada:
          $$C''(r) = 16\pi + \frac{256\pi}{r^3} \implies C''(2) = 16\pi + \frac{256\pi}{8} = 16\pi + 32\pi = \mathbf{48\pi > 0} \implies \textbf{Mínimo absoluto}$$
        </li>
        <li>Coste mínimo total:
          $$C(2) = 8\pi(2^2) + \frac{128\pi}{2} = 32\pi + 64\pi = \mathbf{96\pi\text{ €} \approx 301{,}59\text{ €}}$$
        </li>
      </ul>
    </li>
  </ol>
</div>

<!-- PÁGINA 2: EJERCICIO 2 -->
<div class="page">
  <p><span class="bold">2.</span> Se desea fabricar un depósito cilíndrico cerrado con una capacidad de $V = 54\pi\text{ m}^3$. Materiales: tapa superior a $4\text{ €/m}^2$, base inferior a $8\text{ €/m}^2$ y pared lateral a $6\text{ €/m}^2$.</p>
  
  <ol class="alpha-list" style="margin-top: 15px;">
    <li><span class="bold">Función del coste total $C(r)$ y ligadura:</span>
      <ul>
        <li>Ligadura del volumen:
          $$V = \pi r^2 h = 54\pi \implies \mathbf{h = \frac{54}{r^2}}$$
        </li>
        <li>Coste total de los materiales (Tapa + Suelo + Pared):
          $$C(r) = 4(\pi r^2) + 8(\pi r^2) + 6(2\pi r h) = 12\pi r^2 + 12\pi r \left(\frac{54}{r^2}\right) = \mathbf{12\pi r^2 + \frac{648\pi}{r}}$$
        </li>
      </ul>
    </li>
    <li><span class="bold">Dimensiones óptimas ($C'(r) = 0$):</span>
      <ul>
        <li>Derivamos e igualamos a cero:
          $$C'(r) = 24\pi r - \frac{648\pi}{r^2} = 0 \implies 24\pi r = \frac{648\pi}{r^2} \implies 24\pi r^3 = 648\pi \implies r^3 = 27 \implies \mathbf{r = 3\text{ m}}$$
        </li>
        <li>Altura correspondiente:
          $$h = \frac{54}{3^2} = \frac{54}{9} = \mathbf{6\text{ m}}$$
        </li>
      </ul>
    </li>
    <li><span class="bold">Justificación y coste mínimo:</span>
      <ul>
        <li>Segunda derivada:
          $$C''(r) = 24\pi + \frac{1296\pi}{r^3} \implies C''(3) = 24\pi + \frac{1296\pi}{27} = 24\pi + 48\pi = \mathbf{72\pi > 0} \implies \textbf{Mínimo absoluto}$$
        </li>
        <li>Coste mínimo total:
          $$C(3) = 12\pi(3^2) + \frac{648\pi}{3} = 108\pi + 216\pi = \mathbf{324\pi\text{ €} \approx 1017{,}88\text{ €}}$$
        </li>
      </ul>
    </li>
  </ol>
</div>
"""

def compile_pdf(body_content, target_pdf_name):
    html_str = HTML_TEMPLATE.replace("__BODY__", body_content)
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
    compile_pdf(body_unresolved_html, "ejercicios_optimizacion_cilindro_precios.pdf")
    compile_pdf(body_solved_html, "ejercicios_optimizacion_cilindro_precios_resueltos.pdf")
