import os
import sys
import json
import subprocess
import re

EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Apuntes de Clase: Vectores</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/mhchem.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.1/marked.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 22mm 18mm 22mm 18mm;
  }

  * {
    box-sizing: border-box;
  }

  html, body {
    font-family: "Latin Modern Roman", "Computer Modern", "Cambria", "Times New Roman", Times, serif;
    font-size: 10pt;
    line-height: 1.42;
    color: #111111;
    background-color: #ffffff;
    text-align: justify;
    text-justify: inter-word;
    margin: 0 !important;
    padding: 0 !important;
  }

  .document-title {
    text-align: center;
    font-size: 16pt;
    font-weight: 700;
    color: #000000;
    letter-spacing: 0.3px;
    margin-top: 0;
    margin-bottom: 18pt;
    padding-bottom: 0;
    border-bottom: none !important;
  }

  h1 {
    font-family: "Latin Modern Roman", "Computer Modern", "Cambria", "Times New Roman", Times, serif;
    font-size: 13.5pt;
    color: #000000;
    border-bottom: 0.8pt solid #000000;
    padding-bottom: 3pt;
    margin-top: 18pt;
    margin-bottom: 8pt;
    font-weight: 700;
    letter-spacing: 0.2px;
    page-break-after: avoid;
  }

  h2 {
    font-family: "Latin Modern Roman", "Computer Modern", "Cambria", "Times New Roman", Times, serif;
    font-size: 11.5pt;
    color: #000000;
    border-bottom: none;
    padding-bottom: 0;
    margin-top: 14pt;
    margin-bottom: 5pt;
    font-weight: 700;
    page-break-after: avoid;
  }

  h3 {
    font-family: "Latin Modern Roman", "Computer Modern", "Cambria", "Times New Roman", Times, serif;
    font-size: 10.5pt;
    color: #000000;
    margin-top: 11pt;
    margin-bottom: 4pt;
    font-weight: 700;
    font-style: italic;
    page-break-after: avoid;
  }

  h4 {
    font-family: "Latin Modern Roman", "Computer Modern", "Cambria", "Times New Roman", Times, serif;
    font-size: 10pt;
    color: #111111;
    margin-top: 9pt;
    margin-bottom: 3pt;
    font-weight: 700;
    page-break-after: avoid;
  }

  p {
    margin: 5pt 0;
  }

  ul, ol {
    margin: 4pt 0 7pt 20pt;
    padding: 0;
  }

  li {
    margin-bottom: 2.5pt;
  }

  /* ---- TABLAS TIPO LATEX BOOKTABS ---- */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 10pt 0;
    font-size: 9pt;
    page-break-inside: avoid;
    background-color: transparent;
  }
  th {
    border-top: 1.2pt solid #000000;
    border-bottom: 0.8pt solid #000000;
    padding: 5pt 6pt;
    text-align: left;
    background-color: transparent;
    color: #000000;
    font-weight: 700;
  }
  td {
    border-bottom: 0.3pt solid #d4d4d4;
    padding: 4.5pt 6pt;
    vertical-align: middle;
    background-color: transparent;
    color: #111111;
  }
  tr:last-child td {
    border-bottom: 1.2pt solid #000000;
  }

  /* ---- CITAS Y BLOQUES MINIMALISTAS ---- */
  blockquote {
    border-left: 1.5pt solid #555555;
    background-color: transparent;
    margin: 8pt 0 8pt 14pt;
    padding: 2pt 8pt;
    font-size: 9.5pt;
    font-style: italic;
    color: #222222;
    page-break-inside: avoid;
  }
  blockquote p {
    margin: 2pt 0;
  }

  .katex-display {
    max-width: 100%;
    margin: 7pt 0 !important;
  }
  .katex {
    font-size: 1.05em !important;
  }

  .page-break {
    page-break-before: always !important;
    break-before: page !important;
    height: 0;
    margin: 0;
    padding: 0;
  }

  pre {
    background-color: #fafafa;
    border: 0.5pt solid #cccccc;
    padding: 6pt 8pt;
    font-size: 8.5pt;
    font-family: "Consolas", "Courier New", monospace;
    border-radius: 0;
    margin: 8pt 0;
    page-break-inside: avoid;
    white-space: pre-wrap;
    word-break: break-word;
  }

  code {
    font-family: "Consolas", "Courier New", monospace;
    font-size: 9pt;
    background: #f4f4f4;
    padding: 1px 3px;
    border-radius: 0;
  }
</style>
</head>
<body>

<div id="content"></div>

<script>
const rawMd = __MARKDOWN_JSON__;

marked.setOptions({
  gfm: true,
  breaks: false
});

function protectMath(text) {
  const mathBlocks = [];
  text = text.replace(/\$\$([\s\S]*?)\$\$/g, function(match) {
    mathBlocks.push(match);
    return `%%%MATH_BLOCK_${mathBlocks.length - 1}%%%`;
  });
  text = text.replace(/\$([^\$\n]+?)\$/g, function(match) {
    mathBlocks.push(match);
    return `%%%MATH_BLOCK_${mathBlocks.length - 1}%%%`;
  });
  return { text, mathBlocks };
}

function restoreMath(html, mathBlocks) {
  return html.replace(/%%%MATH_BLOCK_(\d+)%%%/g, function(match, index) {
    return mathBlocks[parseInt(index, 10)];
  });
}

const { text: protectedMd, mathBlocks } = protectMath(rawMd);
let parsed = marked.parse(protectedMd);
parsed = restoreMath(parsed, mathBlocks);
document.getElementById('content').innerHTML = parsed;

renderMathInElement(document.getElementById('content'), {
  delimiters: [
    {left: "$$", right: "$$", display: true},
    {left: "$", right: "$", display: false},
    {left: "\\\\[", right: "\\\\]", display: true},
    {left: "\\\\(", right: "\\\\)", display: false}
  ],
  throwOnError: false
});
</script>
</body>
</html>
"""

def generate_pdf(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    md_text = re.sub(r'^---\s*\n[\s\S]*?\n---\s*\n', '', md_text)
    json_md = json.dumps(md_text)

    html = HTML_TEMPLATE.replace("__MARKDOWN_JSON__", json_md)

    temp_html = md_path + ".temp.html"
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html)

    abs_html = os.path.abspath(temp_html)
    abs_pdf = os.path.abspath(pdf_path)

    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=6000",
        f"--print-to-pdf={abs_pdf}",
        f"file:///{abs_html.replace(os.sep, '/')}"
    ]

    print(f"[*] Ejecutando Edge headless para compilar PDF...")
    res = subprocess.run(cmd, capture_output=True, text=True)

    if os.path.exists(temp_html):
        os.remove(temp_html)

    if os.path.exists(abs_pdf) and os.path.getsize(abs_pdf) > 2000:
        print(f"[OK] PDF generado con exito: {abs_pdf}")
        print(f"     Tamano del archivo: {os.path.getsize(abs_pdf)} bytes")
        return True
    else:
        print(f"[ERROR] No se pudo generar {pdf_path}. Detalle: {res.stderr}")
        return False

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    clases_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    default_dir = os.path.join(clases_root, "Apuntes-y-Ejercicios", "Fisica", "Vectores")
    md_file = os.path.join(default_dir, "apuntes_clase_vectores_lienzo.md")
    pdf_file = os.path.join(default_dir, "apuntes_clase_vectores_lienzo.pdf")

    if len(sys.argv) >= 3:
        generate_pdf(sys.argv[1], sys.argv[2])
    else:
        generate_pdf(md_file, pdf_file)
