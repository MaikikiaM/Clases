import os
import subprocess

OUTPUT_DIR = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Matematicas\Derivadas"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

derivatives_list = [
    r"y = 5x^3 - 4x^2 + 7x - 9",
    r"y = -3x^5 + 2x^4 - x^2 + 8",
    r"y = \frac{1}{2}x^4 - \frac{2}{3}x^3 + 5x - 1",
    r"y = x^6 - 4x^3 + \sqrt{2}x - \pi",
    r"y = (2x - 3)(x^2 + 4)",
    r"y = (x^2 - 1)(3x^3 + 2x)",
    r"y = \frac{3}{x^2}",
    r"y = \frac{5}{x^4} - \frac{2}{x}",
    r"y = 4\sqrt{x}",
    r"y = \sqrt[3]{x^2}",
    r"y = \frac{2}{\sqrt{x}}",
    r"y = 3\sqrt[4]{x^3} - 2\sqrt{x}",
    r"y = (3x^2 - 5x + 1)^4",
    r"y = (2 - 5x)^6",
    r"y = \left(\frac{x}{3} - 1\right)^5",
    r"y = \sqrt{4x^2 - 7x + 2}",
    r"y = \sqrt{1 - x^2}",
    r"y = \sqrt[3]{2x^3 - 5x}",
    r"y = \frac{1}{3x^2 - 4}",
    r"y = \frac{1}{(2x+1)^3}",
    r"y = e^x + 5^x",
    r"y = e^{3x - 2}",
    r"y = e^{-x^2}",
    r"y = 3^{x^2 + 1}",
    r"y = 2^{4x - 3}",
    r"y = e^{\sqrt{x}}",
    r"y = \ln(x)",
    r"y = \ln(3x^2 + 4x - 1)",
    r"y = \ln(5 - 2x)",
    r"y = \log_2(x^3 - 2x)",
    r"y = \log(4x^2 + 1)",
    r"y = \ln\left(\frac{1}{x}\right)",
    r"y = \sin(x) - 3\cos(x)",
    r"y = \sin(4x - 1)",
    r"y = \cos(x^2 + 3)",
    r"y = \tan(5x)",
    r"y = \sin^3(x)",
    r"y = \cos^4(2x)",
    r"y = \tan(x^2 - 1)",
    r"y = x^2 \cdot e^x",
    r"y = (2x - 1)e^{3x}",
    r"y = x^3 \ln(x)",
    r"y = \sqrt{x}\ln(x)",
    r"y = x \sin(x)",
    r"y = x^2 \cos(2x)",
    r"y = e^x \sin(x)",
    r"y = e^{-x}\cos(x)",
    r"y = \sin(x)\cos(x)",
    r"y = \frac{2x + 1}{x - 3}",
    r"y = \frac{x^2 - 4}{x^2 + 1}",
    r"y = \frac{3x - 5}{2x^2 + 1}",
    r"y = \frac{x^3 + 2}{x^2 - 1}",
    r"y = \frac{e^x}{x}",
    r"y = \frac{e^{2x}}{x^2 + 1}",
    r"y = \frac{\ln(x)}{x}",
    r"y = \frac{\ln(x)}{x^2}",
    r"y = \frac{\sin(x)}{x}",
    r"y = \frac{1 + \sin(x)}{1 - \sin(x)}",
    r"y = \ln(\sin(x))",
    r"y = \sqrt{e^{2x} + 1}"
]

# Generate LaTeX file
tex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[top=1.8cm, bottom=1.8cm, left=1.8cm, right=1.8cm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{microtype}

\setmainfont{Calibri}
\linespread{1.2}

\begin{document}
\pagestyle{empty}

\begin{multicols}{2}
\begin{enumerate}[label=\textbf{\arabic*.}, leftmargin=2em, itemsep=10pt]
"""

for i in range(30):
    tex_content += f"    \\item ${derivatives_list[i]}$\n"

tex_content += r"""\end{enumerate}
\end{multicols}

\newpage

\begin{multicols}{2}
\begin{enumerate}[label=\textbf{\arabic*.}, leftmargin=2em, itemsep=10pt, start=31]
"""

for i in range(30, 60):
    tex_content += f"    \\item ${derivatives_list[i]}$\n"

tex_content += r"""\end{enumerate}
\end{multicols}

\end{document}
"""

tex_path = os.path.join(OUTPUT_DIR, "ejercicios_60_derivadas.tex")
with open(tex_path, "w", encoding="utf-8") as f:
    f.write(tex_content)

print(f"Archivo LaTeX generado: {tex_path}")

# Generate HTML for PDF compilation
def build_html():
    col1_p1 = derivatives_list[0:15]
    col2_p1 = derivatives_list[15:30]
    col1_p2 = derivatives_list[30:45]
    col2_p2 = derivatives_list[45:60]
    
    def render_col(items, start_idx):
        res = "<ol class='deriv-list' start='" + str(start_idx) + "'>\n"
        for it in items:
            res += f"  <li>${it}$</li>\n"
        res += "</ol>\n"
        return res

    html = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>60 Derivadas</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 18mm 18mm 18mm 18mm;
  }
  * {
    box-sizing: border-box;
  }
  body {
    font-family: 'Calibri', 'Carlito', 'Segoe UI', sans-serif;
    font-size: 11pt;
    line-height: 1.35;
    color: #000;
    margin: 0;
    padding: 0;
  }
  .page {
    page-break-after: always;
    min-height: 260mm;
    display: flex;
    justify-content: space-between;
  }
  .page:last-child {
    page-break-after: avoid;
  }
  .col {
    width: 48%;
  }
  .deriv-list {
    margin: 0;
    padding-left: 28px;
    list-style-type: decimal;
  }
  .deriv-list > li {
    font-weight: normal;
    padding: 3.5px 0;
    min-height: 15.5mm;
    display: list-item;
  }
  .deriv-list > li::marker {
    font-weight: bold;
  }
  .katex {
    font-size: 1.05em;
  }
</style>
</head>
<body>

<!-- PÁGINA 1 (1 - 30) -->
<div class="page">
  <div class="col">
""" + render_col(col1_p1, 1) + r"""
  </div>
  <div class="col">
""" + render_col(col2_p1, 16) + r"""
  </div>
</div>

<!-- PÁGINA 2 (31 - 60) -->
<div class="page">
  <div class="col">
""" + render_col(col1_p2, 31) + r"""
  </div>
  <div class="col">
""" + render_col(col2_p2, 46) + r"""
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
"""
    return html

html_content = build_html()
temp_html = os.path.join(OUTPUT_DIR, "temp_60_derivadas.html")
target_pdf = os.path.join(OUTPUT_DIR, "ejercicios_60_derivadas.pdf")

with open(temp_html, "w", encoding="utf-8") as f:
    f.write(html_content)

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
    print(f"Exito generando PDF: {target_pdf} ({os.path.getsize(target_pdf)} bytes)")
else:
    print(f"Error: {res.stderr}")
