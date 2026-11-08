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
<title>Apuntes de Clase: Estructura Electrónica y Formulación Química</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/mhchem.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.1/marked.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 18mm 16mm 18mm 16mm;
  }

  * {
    box-sizing: border-box;
  }

  html, body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 9.2pt;
    line-height: 1.45;
    color: #1e293b;
    margin: 0 !important;
    padding: 0 !important;
  }

  h1 {
    font-size: 14pt;
    color: #0f172a;
    border-bottom: 1.5pt solid #0f172a;
    padding-bottom: 4px;
    margin-top: 0;
    margin-bottom: 10px;
    font-weight: 700;
    letter-spacing: -0.2px;
    page-break-after: avoid;
  }

  h2 {
    font-size: 11pt;
    color: #1e293b;
    border-bottom: 0.6pt solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 10px;
    margin-bottom: 6px;
    font-weight: 600;
    page-break-after: avoid;
  }

  h3 {
    font-size: 10pt;
    color: #0f172a;
    margin-top: 9px;
    margin-bottom: 4px;
    font-weight: 600;
    page-break-after: avoid;
  }

  h4 {
    font-size: 9.3pt;
    color: #334155;
    margin-top: 8px;
    margin-bottom: 3px;
    font-weight: 600;
    page-break-after: avoid;
  }

  p {
    margin: 4px 0;
  }

  ul, ol {
    margin: 3px 0 6px 18px;
    padding: 0;
  }

  li {
    margin-bottom: 2.5px;
  }

  /* ---- TABLAS TIPO BOOKTABS ACADÉMICAS ---- */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
  }
  th {
    border-top: 1.4pt solid #0f172a;
    border-bottom: 0.8pt solid #0f172a;
    padding: 4px 6px;
    text-align: left;
    background-color: #f8fafc;
    color: #0f172a;
    font-weight: 600;
  }
  td {
    border-bottom: 0.4pt solid #e2e8f0;
    padding: 3.5px 6px;
    vertical-align: middle;
  }
  tr:last-child td {
    border-bottom: 1.4pt solid #0f172a;
  }

  /* ---- CITAS / APUNTES DE CÁTEDRA SOBRIOS ---- */
  blockquote {
    border-left: 3px solid #0284c7;
    background-color: #f8fafc;
    margin: 8px 0;
    padding: 6px 12px;
    font-size: 8.8pt;
    color: #334155;
    border-radius: 2px;
    page-break-inside: avoid;
  }
  blockquote p {
    margin: 2px 0;
  }

  /* ---- PREVENCIÓN DEL BUG DE SELECCIÓN DE TEXTO EN PDF (CHROMIUM / KATEX) ---- */
  /* 1. Elimina la capa MathML invisible de 1px que sitúa glifos fantasma en (0,0) */
  .katex-mathml {
    display: none !important;
  }

  /* 2. Unifica el contexto de apilamiento para que el flujo de texto de Chromium */
  /*    respete estrictamente el orden del DOM (evita que las fórmulas se emitan al final de la página) */
  p, li, h1, h2, h3, h4, table, blockquote, .katex-display, div {
    position: relative;
  }

  .katex-display {
    max-width: 100%;
    margin: 5px 0 !important;
  }
  .katex {
    font-size: 1.02em !important;
  }

  .page-break {
    page-break-before: always !important;
    break-before: page !important;
    height: 0;
    margin: 0;
    padding: 0;
  }

  code {
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    background: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
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
        clases_root_pdf = r"C:\Users\migue\Antigravity\Clases\apuntes_clase_formulacion_lienzo.pdf"
        import shutil
        shutil.copyfile(abs_pdf, clases_root_pdf)
        print(f"[OK] Copia sincronizada en: {clases_root_pdf}")
        return True
    else:
        print(f"[ERROR] No se pudo generar {pdf_path}. Detalle: {res.stderr}")
        return False

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    md_file = os.path.join(current_dir, "apuntes_clase_formulacion_lienzo.md")
    pdf_file = os.path.join(current_dir, "apuntes_clase_formulacion_lienzo.pdf")

    if len(sys.argv) >= 3:
        generate_pdf(sys.argv[1], sys.argv[2])
    else:
        generate_pdf(md_file, pdf_file)
