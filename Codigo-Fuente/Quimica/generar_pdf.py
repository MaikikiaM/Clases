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
<title>Guión Docente y Chuleta de Cátedra: Formulación Química Inorgánica</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/mhchem.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.1/marked.min.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 15mm 13mm 14mm 13mm;
    @top-left {
      content: "Guión Docente: Formulación Química Inorgánica (IUPAC 2005)";
      font-family: 'Segoe UI', 'Calibri', Arial, sans-serif;
      font-size: 7.8pt;
      color: #0369a1;
      font-weight: 600;
      border-bottom: 0.6pt solid #cbd5e1;
      padding-bottom: 2px;
    }
    @top-right {
      content: "1º y 2º Bachillerato • Preparación EvAU / PAU";
      font-family: 'Segoe UI', 'Calibri', Arial, sans-serif;
      font-size: 7.8pt;
      color: #64748b;
      border-bottom: 0.6pt solid #cbd5e1;
      padding-bottom: 2px;
    }
    @bottom-center {
      content: "Página " counter(page);
      font-family: 'Segoe UI', 'Calibri', Arial, sans-serif;
      font-size: 8pt;
      color: #64748b;
    }
  }

  @page cover-page {
    size: A4 portrait;
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
  }

  * {
    box-sizing: border-box;
  }

  html, body {
    font-family: 'Segoe UI', 'Calibri', Arial, sans-serif;
    font-size: 9.3pt;
    line-height: 1.38;
    color: #1e293b;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* ---- PORTADA OFICIAL DOCENTE ---- */
  .cover-page {
    page: cover-page;
    page-break-after: always;
    background: linear-gradient(145deg, #0a192f 0%, #172a45 45%, #0f393b 100%);
    color: #ffffff;
    width: 210mm;
    height: 297mm;
    margin: 0;
    padding: 42mm 24mm 25mm 24mm;
    box-sizing: border-box;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
  }
  .cover-badge {
    background-color: rgba(56, 189, 248, 0.15);
    border: 1px solid #38bdf8;
    color: #38bdf8;
    font-size: 9pt;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    padding: 5px 16px;
    border-radius: 20px;
    margin-bottom: 22px;
  }
  .cover-supertitle {
    font-size: 13pt;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 8px;
    font-weight: 500;
  }
  .cover-title {
    font-size: 30pt;
    font-weight: 800;
    font-family: 'Segoe UI', 'Calibri', sans-serif;
    line-height: 1.15;
    margin: 0 0 14px 0;
    color: #ffffff;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
  }
  .cover-rule {
    width: 80px;
    height: 3px;
    background-color: #38bdf8;
    margin: 16px auto 20px auto;
    border: none;
    border-radius: 2px;
  }
  .cover-subtitle {
    font-size: 14pt;
    font-weight: 500;
    color: #cbd5e1;
    margin: 0 0 28px 0;
    line-height: 1.35;
    max-width: 90%;
  }
  .cover-features {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    width: 100%;
    max-width: 165mm;
    margin: 20px 0;
    text-align: left;
  }
  .cover-feature-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    padding: 12px 14px;
  }
  .cover-feature-title {
    font-size: 9.5pt;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .cover-feature-desc {
    font-size: 8pt;
    color: #94a3b8;
    line-height: 1.3;
  }
  .cover-footer {
    margin-top: auto;
    margin-bottom: 15mm;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 14px;
    width: 100%;
  }
  .cover-inst {
    font-size: 11pt;
    font-weight: 600;
    color: #f8fafc;
  }
  .cover-course {
    font-size: 9pt;
    color: #94a3b8;
    margin-top: 4px;
  }

  /* ---- ENCABEZADOS Y SECCIONES ---- */
  h1 {
    font-size: 13.5pt;
    color: #0f172a;
    border-bottom: 1.8pt solid #0284c7;
    padding-bottom: 3px;
    margin-top: 4px;
    margin-bottom: 6px;
    font-weight: 800;
    page-break-after: avoid;
  }
  h2 {
    font-size: 11pt;
    color: #0369a1;
    border-bottom: 0.8pt solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 8px;
    margin-bottom: 5px;
    font-weight: 700;
    page-break-after: avoid;
  }
  h3 {
    font-size: 9.8pt;
    color: #0f172a;
    margin-top: 7px;
    margin-bottom: 3px;
    font-weight: 700;
    page-break-after: avoid;
  }
  h4 {
    font-size: 9pt;
    color: #0369a1;
    margin-top: 5px;
    margin-bottom: 2px;
    font-weight: 700;
    page-break-after: avoid;
  }

  p { margin: 2.5px 0; }
  ul, ol { margin: 2px 0 5px 16px; padding: 0; }
  li { margin-bottom: 1.5px; }

  /* ---- TABLAS ESTILO ELEGANTE DE ALTA DENSIDAD ---- */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 8.2pt;
    page-break-inside: avoid;
  }
  th {
    border-top: 1.8pt solid #0369a1;
    border-bottom: 1pt solid #0369a1;
    padding: 3.5px 5px;
    text-align: left;
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
  }
  td {
    border-bottom: 0.5pt solid #e2e8f0;
    padding: 2.8px 5px;
    vertical-align: middle;
  }
  tr:nth-child(even) td {
    background-color: #f8fafc;
  }
  tr:last-child td {
    border-bottom: 1.8pt solid #0369a1;
  }

  /* ---- CAJAS DE ALERTA Y LLAMADA (ESTILO TCOLORBOX) ---- */
  .tcolorbox {
    position: relative;
    margin: 9px 0 6px 0;
    padding: 8px 10px 5px 10px;
    border-radius: 3px;
    page-break-inside: avoid;
    font-size: 8.6pt;
    line-height: 1.35;
  }
  .tcolorbox-title {
    position: absolute;
    top: -8.5px;
    left: 10px;
    color: #ffffff;
    font-family: 'Segoe UI', 'Calibri', sans-serif;
    font-size: 7.5pt;
    font-weight: bold;
    padding: 1px 7px;
    border-radius: 2px;
    display: inline-block;
    line-height: 1.2;
    text-transform: uppercase;
    letter-spacing: 0.4px;
  }

  /* Variantes de Color */
  .box-def {
    border: 1.1pt solid #059669;
    background-color: #ecfdf5;
  }
  .box-def .tcolorbox-title { background-color: #059669; }

  .box-alert {
    border: 1.1pt solid #dc2626;
    background-color: #fef2f2;
  }
  .box-alert .tcolorbox-title { background-color: #dc2626; }

  .box-formula {
    border: 1.1pt solid #d97706;
    background-color: #fffbeb;
  }
  .box-formula .tcolorbox-title { background-color: #d97706; }

  .box-tutor {
    border: 1.1pt solid #4f46e5;
    background-color: #eef2ff;
  }
  .box-tutor .tcolorbox-title { background-color: #4f46e5; }

  .box-resultado {
    border: 1.1pt solid #0284c7;
    background-color: #f0f9ff;
  }
  .box-resultado .tcolorbox-title { background-color: #0284c7; }

  #content {
    max-width: 100%;
  }
  .katex-display {
    max-width: 100%;
    margin: 4px 0 !important;
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
</style>
</head>
<body>

<!-- PORTADA DE CÁTEDRA -->
<div class="cover-page">
  <div class="cover-badge">Guión Docente & Tarima de Pizarra</div>
  <div class="cover-supertitle">Departamento de Física y Química • Bachillerato</div>
  <div class="cover-title">Formulación Química<br>Inorgánica</div>
  <hr class="cover-rule">
  <div class="cover-subtitle">Guión Pedagógico, Chuleta Rápida de Apoyo y Criterios Oficiales IUPAC 2005 para Selectividad (EvAU / PAU)</div>
  
  <div class="cover-features">
    <div class="cover-feature-card">
      <div class="cover-feature-title">⏱️ Gestión de Tiempos</div>
      <div class="cover-feature-desc">Cronograma sugerido por bloques temáticos con dinámicas activas de aula.</div>
    </div>
    <div class="cover-feature-card">
      <div class="cover-feature-title">⚠️ Radar de Errores</div>
      <div class="cover-feature-desc">Detección y vacunación preventiva de los 10 errores más comunes de examen.</div>
    </div>
    <div class="cover-feature-card">
      <div class="cover-feature-title">⚡ Deducción Matemática</div>
      <div class="cover-feature-desc">Algoritmo infalible par/impar para oxoácidos sin memorizar de memoria.</div>
    </div>
    <div class="cover-feature-card">
      <div class="cover-feature-title">🎯 Batería de Pizarra</div>
      <div class="cover-feature-desc">20 retos relámpago con trampas conceptuales y solución directa.</div>
    </div>
  </div>

  <div class="cover-footer">
    <div class="cover-inst">Guía de Cátedra para Clases Teórico-Prácticas</div>
    <div class="cover-course">1º y 2º de Bachillerato &nbsp;•&nbsp; Preparación para la Universidad &nbsp;•&nbsp; Curso 2025–2026</div>
  </div>
</div>

<!-- CUERPO PRINCIPAL -->
<div style="padding-top: 2px;">
  <div id="content"></div>
</div>

<script>
const rawMd = __MARKDOWN_JSON__;

function transformAlerts(html) {
  return html.replace(/<blockquote>\s*<p>\[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\]([\s\S]*?)<\/blockquote>/gi, function(match, type, content) {
    type = type.toUpperCase();
    let boxClass = 'box-def';
    let defaultTitle = 'Definición';

    let customTitle = '';
    const titleMatch = content.match(/^\s*<strong>\s*(.*?)\s*<\/strong>\s*:?\s*(?:<br\s*\/?>)?/i);
    if (titleMatch) {
      customTitle = titleMatch[1].trim();
      content = content.replace(titleMatch[0], '');
    }

    const textToCheck = (type + ' ' + customTitle + ' ' + content).toLowerCase();

    if (type === 'WARNING' || textToCheck.includes('atención') || textToCheck.includes('trampa') || textToCheck.includes('error')) {
      boxClass = 'box-alert';
      defaultTitle = '¡Atención / Error Típico!';
    } else if (textToCheck.includes('mnemotecnia') || textToCheck.includes('truco') || type === 'TIP') {
      boxClass = 'box-formula';
      defaultTitle = 'Mnemotecnia / Regla de Oro';
    } else if (type === 'IMPORTANT' || textToCheck.includes('iupac')) {
      boxClass = 'box-resultado';
      defaultTitle = 'Criterio Oficial IUPAC';
    } else if (textToCheck.includes('guión') || textToCheck.includes('planificación') || textToCheck.includes('pizarra')) {
      boxClass = 'box-tutor';
      defaultTitle = 'Guión Docente';
    } else {
      boxClass = 'box-def';
      defaultTitle = 'Fundamento Clave';
    }

    let finalTitle = customTitle || defaultTitle;
    content = content.replace(/^\s*:\s*/, '');
    content = content.replace(/<p>\s*<\/p>/g, '');

    return `<div class="tcolorbox ${boxClass}"><div class="tcolorbox-title">${finalTitle}</div>${content}</div>`;
  });
}

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
parsed = transformAlerts(parsed);
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
    default_dir = os.path.join(clases_root, "Apuntes-y-Ejercicios", "Quimica", "Formulacion-Inorganica")
    md_file = os.path.join(default_dir, "guion_chuleta_formulacion_inorganica.md")
    pdf_file = os.path.join(default_dir, "guion_chuleta_formulacion_inorganica.pdf")

    if len(sys.argv) >= 3:
        generate_pdf(sys.argv[1], sys.argv[2])
    else:
        generate_pdf(md_file, pdf_file)
