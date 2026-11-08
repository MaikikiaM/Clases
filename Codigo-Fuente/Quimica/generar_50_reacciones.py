import os
import subprocess
import shutil

OUTPUT_DIR = r"C:\Users\migue\Antigravity\Clases\Apuntes-y-Ejercicios\Quimica\Reacciones-Organicas"
ROOT_DIR = r"c:\Users\migue\Antigravity\Clases"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def arrow(cond="", is_rev=False, width_dashes=3):
    dashes = "─" * width_dashes
    symbol = "⇌" if is_rev else "⟶"
    arr_str = f"{dashes}{symbol}" if not is_rev else f"{dashes}⇌{dashes}"
    if cond:
        return f'<span class="rxn-arrow"><span class="cond">{cond}</span><span class="arr">{arr_str}</span></span>'
    else:
        return f'<span class="rxn-arrow"><span class="arr">{arr_str}</span></span>'

# Datos de los 9 ejercicios con sus 50 reacciones depuradas a nivel 100% Bachillerato estándar
exercises_data = [
    {
        "num": 1,
        "title": "Completa y ajusta las siguientes reacciones orgánicas, indicando el nombre de los productos orgánicos obtenidos y el tipo de reacción en cada caso:",
        "items": [
            {
                "lbl": "a)",
                "student": f'CH<sub>2</sub>=CH–CH<sub>3</sub> + H<sub>2</sub> {arrow("Pt")} ',
                "solved": f'CH<sub>2</sub>=CH–CH<sub>3</sub> + H<sub>2</sub> {arrow("Pt")} <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>3</sub></b> <span class="sol-tag">(<b>propano</b>) — <span class="sol-type">Adición (hidrogenación)</span></span>'
            },
            {
                "lbl": "b)",
                "student": f'CH<sub>3</sub>–CH=CH–CH<sub>3</sub> + Br<sub>2</sub> {arrow()} ',
                "solved": f'CH<sub>3</sub>–CH=CH–CH<sub>3</sub> + Br<sub>2</sub> {arrow()} <b>CH<sub>3</sub>–CHBr–CHBr–CH<sub>3</sub></b> <span class="sol-tag">(<b>2,3-dibromobutano</b>) — <span class="sol-type">Adición (halogenación)</span></span>'
            },
            {
                "lbl": "c)",
                "student": f'CH≡C–CH<sub>3</sub> + 2 Cl<sub>2</sub> {arrow()} ',
                "solved": f'CH≡C–CH<sub>3</sub> + 2 Cl<sub>2</sub> {arrow()} <b>CHCl<sub>2</sub>–CCl<sub>2</sub>–CH<sub>3</sub></b> <span class="sol-tag">(<b>1,1,2,2-tetracloropropano</b>) — <span class="sol-type">Adición a triple enlace</span></span>'
            },
            {
                "lbl": "d)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–OH {arrow("H<sub>2</sub>SO<sub>4</sub> conc., calor", width_dashes=4)} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–OH {arrow("H<sub>2</sub>SO<sub>4</sub> conc., calor", width_dashes=4)} <b>CH<sub>2</sub>=CH<sub>2</sub> + H<sub>2</sub>O</b> <span class="sol-tag">(<b>eteno</b>) — <span class="sol-type">Eliminación (deshidratación)</span></span>'
            },
            {
                "lbl": "e)",
                "student": f'CH<sub>2</sub>=CH<sub>2</sub> + HCl {arrow()} ',
                "solved": f'CH<sub>2</sub>=CH<sub>2</sub> + HCl {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–Cl</b> <span class="sol-tag">(<b>cloroetano</b>) — <span class="sol-type">Adición (hidrohalogenación)</span></span>'
            },
            {
                "lbl": "f)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–Br + NaOH (ac) {arrow()} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–Br + NaOH (ac) {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–OH + NaBr</b> <span class="sol-tag">(<b>propan-1-ol</b>) — <span class="sol-type">Sustitución nucleófila</span></span>'
            },
            {
                "lbl": "g)",
                "student": f'CH<sub>3</sub>–CH(OH)–CH<sub>3</sub> {arrow("K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> / H<sup>+</sup>", width_dashes=4)} ',
                "solved": f'CH<sub>3</sub>–CH(OH)–CH<sub>3</sub> {arrow("K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> / H<sup>+</sup>", width_dashes=4)} <b>CH<sub>3</sub>–CO–CH<sub>3</sub></b> <span class="sol-tag">(<b>propanona</b>) — <span class="sol-type">RedOx (oxidación de alcohol secundario)</span></span>'
            },
            {
                "lbl": "h)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–COOH + CH<sub>3</sub>–OH {arrow("H<sup>+</sup>", is_rev=True)} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–COOH + CH<sub>3</sub>–OH {arrow("H<sup>+</sup>", is_rev=True)} <b>CH<sub>3</sub>–CH<sub>2</sub>–COO–CH<sub>3</sub> + H<sub>2</sub>O</b> <span class="sol-tag">(<b>propanoato de metilo</b>) — <span class="sol-type">Condensación (esterificación)</span></span>'
            },
            {
                "lbl": "i)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–COOH + KOH {arrow()} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–COOH + KOH {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–COOK + H<sub>2</sub>O</b> <span class="sol-tag">(<b>propanoato de potasio</b>) — <span class="sol-type">Ácido-base (neutralización)</span></span>'
            },
            {
                "lbl": "j)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CH<sub>3</sub> + O<sub>2</sub> {arrow()} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CH<sub>3</sub> + 13/2 O<sub>2</sub> {arrow()} <b>4 CO<sub>2</sub> + 5 H<sub>2</sub>O</b> <span class="sol-tag">(o ajustado entero: 2 C<sub>4</sub>H<sub>10</sub> + 13 O<sub>2</sub> ⟶ 8 CO<sub>2</sub> + 10 H<sub>2</sub>O) — <span class="sol-type">Combustión</span></span>'
            }
        ]
    },
    {
        "num": 2,
        "title": "Formula todos los productos que se obtienen en las siguientes reacciones. Cuando puedan formarse dos isómeros constitucionales, escribe ambos e indica cuál es el mayoritario:",
        "items": [
            {
                "lbl": "a)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–CH=CH<sub>2</sub> + HBr {arrow()} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CH=CH<sub>2</sub> + HBr {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–CHBr–CH<sub>3</sub></b> (<b>2-bromobutano</b>, mayoritario, regla de Markovnikov) + <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CH<sub>2</sub>Br</b> (1-bromobutano, minoritario) <span class="sol-tag">— <span class="sol-type">Adición electrófila</span></span>'
            },
            {
                "lbl": "b)",
                "student": f'CH<sub>3</sub>–C(CH<sub>3</sub>)=CH<sub>2</sub> + H<sub>2</sub>O {arrow("H<sub>2</sub>SO<sub>4</sub> dil.", width_dashes=4)} ',
                "solved": f'CH<sub>3</sub>–C(CH<sub>3</sub>)=CH<sub>2</sub> + H<sub>2</sub>O {arrow("H<sub>2</sub>SO<sub>4</sub> dil.", width_dashes=4)} <b>CH<sub>3</sub>–C(CH<sub>3</sub>)(OH)–CH<sub>3</sub></b> (<b>2-metilpropan-2-ol</b>, mayoritario, Markovnikov) + <b>CH<sub>3</sub>–CH(CH<sub>3</sub>)–CH<sub>2</sub>OH</b> (2-metilpropan-1-ol, minoritario) <span class="sol-tag">— <span class="sol-type">Adición (hidratación)</span></span>'
            },
            {
                "lbl": "c)",
                "student": f'CH<sub>3</sub>–C≡C–CH<sub>3</sub> + H<sub>2</sub> (1 mol) {arrow("Pt")} ',
                "solved": f'CH<sub>3</sub>–C≡C–CH<sub>3</sub> + H<sub>2</sub> (1 mol) {arrow("Pt")} <b>CH<sub>3</sub>–CH=CH–CH<sub>3</sub></b> <span class="sol-tag">(<b>but-2-eno</b>) — <span class="sol-type">Adición parcial a triple enlace</span></span>'
            },
            {
                "lbl": "d)",
                "student": f'CH≡C–CH<sub>2</sub>–CH<sub>3</sub> + HCl (1 mol) {arrow()} ',
                "solved": f'CH≡C–CH<sub>2</sub>–CH<sub>3</sub> + HCl (1 mol) {arrow()} <b>CH<sub>2</sub>=CCl–CH<sub>2</sub>–CH<sub>3</sub></b> (<b>2-clorobut-1-eno</b>, mayoritario, Markovnikov) + <b>CHCl=CH–CH<sub>2</sub>–CH<sub>3</sub></b> (1-clorobut-1-eno, minoritario) <span class="sol-tag">— <span class="sol-type">Adición a triple enlace</span></span>'
            },
            {
                "lbl": "e)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CHCl–CH<sub>3</sub> + KOH (etanol) {arrow("calor")} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CHCl–CH<sub>3</sub> + KOH (etanol) {arrow("calor")} <b>CH<sub>3</sub>–CH<sub>2</sub>–CH=CH–CH<sub>3</sub></b> (<b>pent-2-eno</b>, mayoritario, regla de Zaitsev) + <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CH=CH<sub>2</sub></b> (pent-1-eno, minoritario) + <b>KCl + H<sub>2</sub>O</b> <span class="sol-tag">— <span class="sol-type">Eliminación</span></span>'
            },
            {
                "lbl": "f)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CHCl–CH<sub>3</sub> + KOH (ac) {arrow()} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CHCl–CH<sub>3</sub> + KOH (ac) {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CH(OH)–CH<sub>3</sub> + KCl</b> <span class="sol-tag">(<b>pentan-2-ol</b>) — <span class="sol-type">Sustitución nucleófila</span></span>'
            },
            {
                "lbl": "g)",
                "student": f'CH<sub>3</sub>–CH(CH<sub>3</sub>)–CH(OH)–CH<sub>3</sub> {arrow("H<sub>2</sub>SO<sub>4</sub> conc., calor", width_dashes=4)} ',
                "solved": f'CH<sub>3</sub>–CH(CH<sub>3</sub>)–CH(OH)–CH<sub>3</sub> {arrow("H<sub>2</sub>SO<sub>4</sub> conc., calor", width_dashes=4)} <b>CH<sub>3</sub>–C(CH<sub>3</sub>)=CH–CH<sub>3</sub></b> (<b>2-metilbut-2-eno</b>, mayoritario, regla de Zaitsev) + <b>CH<sub>3</sub>–CH(CH<sub>3</sub>)–CH=CH<sub>2</sub></b> (3-metilbut-1-eno, minoritario) + <b>H<sub>2</sub>O</b> <span class="sol-tag">— <span class="sol-type">Eliminación (deshidratación)</span></span>'
            },
            {
                "lbl": "h)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–OH {arrow("KMnO<sub>4</sub> / H<sup>+</sup>, calor", width_dashes=4)} ',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–OH {arrow("KMnO<sub>4</sub> / H<sup>+</sup>, calor", width_dashes=4)} <b>CH<sub>3</sub>–CH<sub>2</sub>–COOH</b> <span class="sol-tag">(<b>ácido propanoico</b>) — <span class="sol-type">RedOx (oxidación enérgica de alcohol primario)</span></span>'
            }
        ]
    },
    {
        "num": 3,
        "title": "Escribe y ajusta mediante fórmulas semidesarrolladas las ecuaciones químicas correspondientes a los siguientes procesos, nombrando los productos orgánicos formados:",
        "items": [
            {
                "lbl": "a)",
                "student": "Reacción en caliente entre el ácido etanoico y la metanamina.",
                "solved": f'CH<sub>3</sub>–COOH + CH<sub>3</sub>–NH<sub>2</sub> {arrow("calor")} <b>CH<sub>3</sub>–CONH–CH<sub>3</sub> + H<sub>2</sub>O</b> <span class="sol-tag">(<b><i>N</i>-metiletanamida</b>) — <span class="sol-type">Condensación</span></span>'
            },
            {
                "lbl": "b)",
                "student": "Esterificación entre el ácido propanoico y el etanol en presencia de ácido sulfúrico.",
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–COOH + CH<sub>3</sub>–CH<sub>2</sub>–OH {arrow("H<sup>+</sup>", is_rev=True)} <b>CH<sub>3</sub>–CH<sub>2</sub>–COO–CH<sub>2</sub>–CH<sub>3</sub> + H<sub>2</sub>O</b> <span class="sol-tag">(<b>propanoato de etilo</b>) — <span class="sol-type">Condensación (esterificación)</span></span>'
            },
            {
                "lbl": "c)",
                "student": "Reacción de la propan-1-amina con ácido clorhídrico.",
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–NH<sub>2</sub> + HCl {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–NH<sub>3</sub><sup>+</sup>Cl<sup>–</sup></b> <span class="sol-tag">(<b>cloruro de propilamonio</b>) — <span class="sol-type">Ácido-base</span></span>'
            },
            {
                "lbl": "d)",
                "student": "Neutralización del ácido metanoico con hidrogenocarbonato de sodio.",
                "solved": f'H–COOH + NaHCO<sub>3</sub> {arrow()} <b>H–COONa + CO<sub>2</sub> + H<sub>2</sub>O</b> <span class="sol-tag">(<b>metanoato de sodio</b>) — <span class="sol-type">Ácido-base</span></span>'
            },
            {
                "lbl": "e)",
                "student": "Nitración del benceno con ácido nítrico en presencia de ácido sulfúrico.",
                "solved": f'C<sub>6</sub>H<sub>6</sub> + HNO<sub>3</sub> {arrow("H<sub>2</sub>SO<sub>4</sub>")} <b>C<sub>6</sub>H<sub>5</sub>–NO<sub>2</sub> + H<sub>2</sub>O</b> <span class="sol-tag">(<b>nitrobenceno</b>) — <span class="sol-type">Sustitución electrófila aromática</span></span>'
            },
            {
                "lbl": "f)",
                "student": "Combustión completa del etanol con oxígeno.",
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–OH + 3 O<sub>2</sub> {arrow()} <b>2 CO<sub>2</sub> + 3 H<sub>2</sub>O</b> <span class="sol-tag">— <span class="sol-type">Combustión</span></span>'
            }
        ]
    },
    {
        "num": 4,
        "title": "En cada una de las siguientes reacciones falta un reactivo, condición o producto representado por la letra <b>A</b>. Identifica qué especie es <b>A</b> en cada caso (y nómbrala si se trata de un compuesto orgánico):",
        "items": [
            {
                "lbl": "a)",
                "student": f'<b>A</b> + HCl {arrow()} CH<sub>3</sub>–CHCl–CH<sub>3</sub> <i>(producto mayoritario)</i>',
                "solved": f'<b>A</b> = <b>CH<sub>2</sub>=CH–CH<sub>3</sub></b> (<b>propeno</b>) <span class="sol-tag">[Reacción: CH<sub>2</sub>=CH–CH<sub>3</sub> + HCl ⟶ CH<sub>3</sub>–CHCl–CH<sub>3</sub>, adición Markovnikov]</span>'
            },
            {
                "lbl": "b)",
                "student": f'H–COOH + <b>A</b> {arrow("H<sup>+</sup>", is_rev=True)} H–COO–CH<sub>2</sub>–CH<sub>2</sub>–CH<sub>3</sub> + H<sub>2</sub>O',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–OH</b> (<b>propan-1-ol</b>) <span class="sol-tag">[Condensación / esterificación]</span>'
            },
            {
                "lbl": "c)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–Br + <b>A</b> {arrow()} CH<sub>3</sub>–CH<sub>2</sub>–C≡N + KBr',
                "solved": f'<b>A</b> = <b>KCN</b> (cianuro de potasio) <span class="sol-tag">[Sustitución nucleófila]</span>'
            },
            {
                "lbl": "d)",
                "student": f'CH<sub>3</sub>–CO–CH<sub>2</sub>–CH<sub>3</sub> {arrow("[H] (reducción)", width_dashes=4)} <b>A</b>',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–CH(OH)–CH<sub>2</sub>–CH<sub>3</sub></b> (<b>butan-2-ol</b>) <span class="sol-tag">[RedOx / reducción de carbonilo a alcohol secundario]</span>'
            },
            {
                "lbl": "e)",
                "student": f'<b>A</b> + 5 O<sub>2</sub> {arrow()} 3 CO<sub>2</sub> + 4 H<sub>2</sub>O',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>3</sub></b> (<b>propano</b>, C<sub>3</sub>H<sub>8</sub>) <span class="sol-tag">[Combustión]</span>'
            },
            {
                "lbl": "f)",
                "student": f'<b>A</b> + HCl {arrow()} CH<sub>3</sub>–CH<sub>2</sub>–Cl + H<sub>2</sub>O',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–OH</b> (<b>etanol</b>) <span class="sol-tag">[Sustitución nucleófila del –OH por –Cl; el subproducto H<sub>2</sub>O descarta adición a eteno]</span>'
            },
            {
                "lbl": "g)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–OH {arrow("<b>A</b>", width_dashes=3)} CH<sub>3</sub>–CH=CH<sub>2</sub> + H<sub>2</sub>O',
                "solved": f'<b>A</b> = <b>H<sub>2</sub>SO<sub>4</sub> concentrado y calor</b> <span class="sol-tag">[Eliminación / deshidratación de alcohol]</span>'
            }
        ]
    },
    {
        "num": 5,
        "title": "Deduce las sustancias <b>A</b> y <b>B</b> que completan cada una de las siguientes ecuaciones químicas:",
        "items": [
            {
                "lbl": "a)",
                "student": f'CH<sub>3</sub>–COO–CH<sub>2</sub>–CH<sub>3</sub> + NaOH {arrow("calor")} <b>A</b> + <b>B</b>',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–COONa</b> (etanoato de sodio); <b>B</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–OH</b> (etanol) <span class="sol-tag">[Saponificación / hidrólisis básica de éster]</span>'
            },
            {
                "lbl": "b)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–OH + HBr {arrow()} <b>A</b> + <b>B</b>',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–Br</b> (<b>bromoetano</b>); <b>B</b> = <b>H<sub>2</sub>O</b> <span class="sol-tag">[Sustitución nucleófila de alcohol con hidrácido]</span>'
            },
            {
                "lbl": "c)",
                "student": f'<b>A</b> + CH<sub>3</sub>–CH<sub>2</sub>–OH {arrow("H<sup>+</sup>", is_rev=True)} CH<sub>3</sub>–COO–CH<sub>2</sub>–CH<sub>3</sub> + <b>B</b>',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–COOH</b> (<b>ácido etanoico</b> / acético); <b>B</b> = <b>H<sub>2</sub>O</b> <span class="sol-tag">[Condensación / esterificación]</span>'
            },
            {
                "lbl": "d)",
                "student": f'<b>A</b> + NH<sub>3</sub> {arrow("calor")} CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CONH<sub>2</sub> + <b>B</b>',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–COOH</b> (<b>ácido butanoico</b>); <b>B</b> = <b>H<sub>2</sub>O</b> <span class="sol-tag">[Condensación / amidación]</span>'
            },
            {
                "lbl": "e)",
                "student": f'CH<sub>3</sub>–COOH + NaOH {arrow()} <b>A</b> + <b>B</b>',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–COONa</b> (<b>etanoato de sodio</b> / acetato de sodio); <b>B</b> = <b>H<sub>2</sub>O</b> <span class="sol-tag">[Ácido-base / neutralización de ácido carboxílico]</span>'
            }
        ]
    },
    {
        "num": 6,
        "title": "A partir del eteno se realiza la siguiente secuencia de reacciones químicas. Escribe ajustadas las cuatro ecuaciones e indica la fórmula semidesarrollada y el nombre de los compuestos orgánicos <b>A</b>, <b>B</b>, <b>C</b> y <b>D</b>:",
        "items": [
            {
                "lbl": "a)",
                "student": f'CH<sub>2</sub>=CH<sub>2</sub> + H<sub>2</sub>O {arrow("H<sub>2</sub>SO<sub>4</sub> dil.", width_dashes=4)} <b>A</b>',
                "solved": f'CH<sub>2</sub>=CH<sub>2</sub> + H<sub>2</sub>O {arrow("H<sub>2</sub>SO<sub>4</sub> dil.", width_dashes=4)} <b>CH<sub>3</sub>–CH<sub>2</sub>–OH</b> ⟶ <b>A</b> = <b>etanol</b> <span class="sol-tag">[Adición de agua]</span>'
            },
            {
                "lbl": "b)",
                "student": f'<b>A</b> {arrow("[O] suave", width_dashes=4)} <b>B</b>',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–OH {arrow("[O] suave", width_dashes=4)} <b>CH<sub>3</sub>–CHO</b> ⟶ <b>B</b> = <b>etanal</b> <span class="sol-tag">[RedOx / oxidación suave a aldehído]</span>'
            },
            {
                "lbl": "c)",
                "student": f'<b>B</b> {arrow("KMnO<sub>4</sub> / H<sup>+</sup>", width_dashes=4)} <b>C</b>',
                "solved": f'CH<sub>3</sub>–CHO {arrow("KMnO<sub>4</sub> / H<sup>+</sup>", width_dashes=4)} <b>CH<sub>3</sub>–COOH</b> ⟶ <b>C</b> = <b>ácido etanoico</b> <span class="sol-tag">[RedOx / oxidación de aldehído a ácido]</span>'
            },
            {
                "lbl": "d)",
                "student": f'<b>C</b> + <b>A</b> {arrow("H<sup>+</sup>", is_rev=True)} <b>D</b> + H<sub>2</sub>O',
                "solved": f'CH<sub>3</sub>–COOH + CH<sub>3</sub>–CH<sub>2</sub>–OH {arrow("H<sup>+</sup>", is_rev=True)} <b>CH<sub>3</sub>–COO–CH<sub>2</sub>–CH<sub>3</sub> + H<sub>2</sub>O</b> ⟶ <b>D</b> = <b>etanoato de etilo</b> <span class="sol-tag">[Condensación / esterificación]</span>'
            }
        ]
    },
    {
        "num": 7,
        "title": "Un derivado monohalogenado saturado <b>A</b> reacciona según el esquema de cuatro transformaciones indicado abajo. Deduce razonadamente la fórmula de <b>A</b>, escribe completas las cuatro reacciones y nombra los compuestos orgánicos <b>A</b>, <b>B</b>, <b>C</b>, <b>D</b>, <b>E</b> y <b>F</b>:",
        "items": [
            {
                "lbl": "a)",
                "student": f'<b>A</b> + KOH (etanol) {arrow("calor")} <b>B</b> <i>(mayoritario)</i> + CH<sub>3</sub>–CH<sub>2</sub>–CH=CH<sub>2</sub> <i>(minoritario)</i> + KBr + H<sub>2</sub>O',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–CHBr–CH<sub>3</sub></b> (<b>2-bromobutano</b>). Al eliminar HBr con KOH/etanol rinde <b>B</b> = <b>CH<sub>3</sub>–CH=CH–CH<sub>3</sub></b> (<b>but-2-eno</b>, mayoritario, Zaitsev) y but-1-eno (minoritario) + KBr + H<sub>2</sub>O. <span class="sol-tag">[Eliminación]</span>'
            },
            {
                "lbl": "b)",
                "student": f'<b>B</b> + H<sub>2</sub> {arrow("Pt")} <b>C</b>',
                "solved": f'CH<sub>3</sub>–CH=CH–CH<sub>3</sub> + H<sub>2</sub> {arrow("Pt")} <b>CH<sub>3</sub>–CH<sub>2</sub>–CH<sub>2</sub>–CH<sub>3</sub></b> ⟶ <b>C</b> = <b>butano</b> <span class="sol-tag">[Adición / hidrogenación]</span>'
            },
            {
                "lbl": "c)",
                "student": f'<b>A</b> + NaOH (ac) {arrow()} <b>D</b> + NaBr',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CHBr–CH<sub>3</sub> + NaOH (ac) {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–CH(OH)–CH<sub>3</sub> + NaBr</b> ⟶ <b>D</b> = <b>butan-2-ol</b> <span class="sol-tag">[Sustitución nucleófila]</span>'
            },
            {
                "lbl": "d)",
                "student": f'<b>D</b> {arrow("H<sub>2</sub>SO<sub>4</sub> conc., calor", width_dashes=4)} <b>E</b> <i>(mayoritario)</i> + <b>F</b> <i>(minoritario)</i> + H<sub>2</sub>O',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–CH(OH)–CH<sub>3</sub> {arrow("H<sub>2</sub>SO<sub>4</sub> conc., calor", width_dashes=4)} <b>E</b> = <b>CH<sub>3</sub>–CH=CH–CH<sub>3</sub></b> (<b>but-2-eno</b>, mayoritario) + <b>F</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–CH=CH<sub>2</sub></b> (<b>but-1-eno</b>, minoritario) + H<sub>2</sub>O. <span class="sol-tag">[Eliminación / deshidratación]</span>'
            }
        ]
    },
    {
        "num": 8,
        "title": "Determina la fórmula semidesarrollada y el nombre sistemático del compuesto orgánico <b>A</b> en cada uno de los siguientes procesos:",
        "items": [
            {
                "lbl": "a)",
                "student": f'<b>A</b> + 2 HBr {arrow()} CH<sub>3</sub>–CHBr<sub>2</sub>',
                "solved": f'<b>A</b> = <b>CH≡CH</b> (<b>etino</b>) <span class="sol-tag">[Doble adición de HBr según Markovnikov: CH≡CH + HBr ⟶ CH<sub>2</sub>=CHBr; CH<sub>2</sub>=CHBr + HBr ⟶ CH<sub>3</sub>–CHBr<sub>2</sub>]</span>'
            },
            {
                "lbl": "b)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–COOH {arrow("LiAlH<sub>4</sub>", width_dashes=3)} <b>A</b>',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–CH<sub>2</sub>–CHO</b> (<b>propanal</b>) <span class="sol-tag">[RedOx / reducción a aldehído (también se admite reducción total a propan-1-ol)]</span>'
            },
            {
                "lbl": "c)",
                "student": f'2 <b>A</b> + 3 O<sub>2</sub> {arrow()} 2 CO<sub>2</sub> + 4 H<sub>2</sub>O',
                "solved": f'<b>A</b> = <b>CH<sub>3</sub>–OH</b> (<b>metanol</b>) <span class="sol-tag">[Combustión: el balance de átomos C<sub>2</sub>H<sub>8</sub>O<sub>2</sub> en 2 moléculas corresponde a la fórmula molecular CH<sub>4</sub>O, el metanol]</span>'
            }
        ]
    },
    {
        "num": 9,
        "title": "Completa las tres reacciones del siguiente esquema sintético con funciones nitrogenadas partiendo del cloroetano, formulando y nombrando los productos orgánicos <b>A</b>, <b>B</b> y <b>C</b>:",
        "items": [
            {
                "lbl": "a)",
                "student": f'CH<sub>3</sub>–CH<sub>2</sub>–Cl + NH<sub>3</sub> {arrow()} <b>A</b> + HCl',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–Cl + NH<sub>3</sub> {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–NH<sub>2</sub> + HCl</b> ⟶ <b>A</b> = <b>etanamina</b> (etilamina) <span class="sol-tag">[Sustitución nucleófila]</span>'
            },
            {
                "lbl": "b)",
                "student": f'<b>A</b> + HBr {arrow()} <b>B</b>',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–NH<sub>2</sub> + HBr {arrow()} <b>CH<sub>3</sub>–CH<sub>2</sub>–NH<sub>3</sub><sup>+</sup>Br<sup>–</sup></b> ⟶ <b>B</b> = <b>bromuro de etilamonio</b> <span class="sol-tag">[Ácido-base / formación de sal de amonio]</span>'
            },
            {
                "lbl": "c)",
                "student": f'<b>A</b> + CH<sub>3</sub>–CH<sub>2</sub>–COOH {arrow("calor")} <b>C</b> + H<sub>2</sub>O',
                "solved": f'CH<sub>3</sub>–CH<sub>2</sub>–NH<sub>2</sub> + CH<sub>3</sub>–CH<sub>2</sub>–COOH {arrow("calor")} <b>CH<sub>3</sub>–CH<sub>2</sub>–CONH–CH<sub>2</sub>–CH<sub>3</sub> + H<sub>2</sub>O</b> ⟶ <b>C</b> = <b><i>N</i>-etilpropanamida</b> <span class="sol-tag">[Condensación / formación de amida secundaria]</span>'
            }
        ]
    }
]

# Validar conteo exacto de 50 reacciones
total_rxns = sum(len(e["items"]) for e in exercises_data)
assert total_rxns == 50, f"Error: Se esperaban 50 reacciones, hay {total_rxns}"
print(f"[OK] Total de reacciones validadas: {total_rxns}")

def build_html(is_solved=False):
    html_items = []
    
    for ex in exercises_data:
        ex_num = ex["num"]
        ex_title = ex["title"]
        items = ex["items"]
        
        # Saltos de página estratégicos para balance perfecto de 3 páginas (18 / 18 / 14 rxns)
        # Página 1: Ejercicios 1 y 2 (18 rxns)
        # Página 2: Ejercicios 3, 4 y 5 (18 rxns)
        # Página 3: Ejercicios 6, 7, 8 y 9 (14 rxns)
        page_break_str = ""
        if ex_num in [3, 6]:
            page_break_str = '<div class="page-break"></div>\n'
        
        items_html = []
        for it in items:
            lbl = it["lbl"]
            content = it["solved"] if is_solved else it["student"]
            items_html.append(f'''
      <div class="item">
        <span class="item-label">{lbl}</span>
        <span class="item-content">{content}</span>
      </div>''')
        
        items_block = "\n".join(items_html)
        html_items.append(f'''{page_break_str}    <div class="exercise">
      <div class="exercise-title">{ex_num}. {ex_title}</div>
      <div class="items-list">
{items_block}
      </div>
    </div>''')
    
    body_content = "\n".join(html_items)
    
    doc_title = "bolsa de reacciones quimicas (resueltos)" if is_solved else "bolsa de reacciones quimicas"
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{doc_title}</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 20mm 20mm 20mm 20mm;
  }}
  * {{
    box-sizing: border-box;
  }}
  html, body {{
    font-family: 'Calibri', 'Carlito', 'Segoe UI', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.40;
    color: #000000;
    margin: 0 !important;
    padding: 0 !important;
    background: #ffffff;
  }}
  .exercise {{
    margin-bottom: 14pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .exercise-title {{
    font-weight: bold;
    margin-bottom: 5pt;
    text-align: justify;
    page-break-after: avoid;
    break-after: avoid;
  }}
  .items-list {{
    margin: 0;
    padding-left: 2px;
  }}
  .item {{
    margin-bottom: { "7.5pt" if not is_solved else "6pt" };
    display: flex;
    align-items: baseline;
    page-break-inside: avoid;
    break-inside: avoid;
    text-align: justify;
  }}
  .item-label {{
    font-weight: bold;
    display: inline-block;
    min-width: 24px;
    flex-shrink: 0;
  }}
  .item-content {{
    flex-grow: 1;
  }}
  .rxn-arrow {{
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    vertical-align: middle;
    margin: 0 4px;
    position: relative;
    top: -1.5px;
  }}
  .rxn-arrow .cond {{
    font-size: 8pt;
    line-height: 1.05;
    margin-bottom: 0px;
    white-space: nowrap;
    color: #000;
  }}
  .rxn-arrow .arr {{
    font-size: 11pt;
    line-height: 0.95;
    letter-spacing: -0.5px;
    color: #000;
  }}
  sub, sup {{
    font-size: 0.74em;
    line-height: 0;
    position: relative;
    vertical-align: baseline;
  }}
  sup {{ top: -0.45em; }}
  sub {{ bottom: -0.22em; }}
  b {{
    font-weight: 700;
  }}
  .sol-tag {{
    color: #000000;
  }}
  .sol-type {{
    color: #333333;
    font-style: italic;
  }}
  .page-break {{
    page-break-before: always !important;
    break-before: page !important;
    height: 0;
    margin: 0;
    padding: 0;
  }}
</style>
</head>
<body>
{body_content}
</body>
</html>'''
    return html

# 1. Generar HTMLs
html_student = build_html(is_solved=False)
html_solved = build_html(is_solved=True)

path_html_student = os.path.join(OUTPUT_DIR, "ejercicios_50_reacciones_organicas.temp.html")
path_html_solved = os.path.join(OUTPUT_DIR, "ejercicios_50_reacciones_organicas_resueltos.temp.html")

with open(path_html_student, "w", encoding="utf-8") as f:
    f.write(html_student)

with open(path_html_solved, "w", encoding="utf-8") as f:
    f.write(html_solved)

pdf_student = os.path.join(OUTPUT_DIR, "ejercicios_50_reacciones_organicas.pdf")
pdf_solved = os.path.join(OUTPUT_DIR, "ejercicios_50_reacciones_organicas_resueltos.pdf")

# 2. Compilar con Edge Headless
for temp_h, out_p in [(path_html_student, pdf_student), (path_html_solved, pdf_solved)]:
    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=5000",
        f"--print-to-pdf={out_p}",
        f"file:///{os.path.abspath(temp_h).replace(os.sep, '/')}"
    ]
    print(f"Compilando {os.path.basename(out_p)}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(temp_h):
        os.remove(temp_h)
    if os.path.exists(out_p):
        print(f"[OK] Generado {out_p} ({os.path.getsize(out_p)} bytes)")
    else:
        print(f"[ERROR] Fallo al generar {out_p}: {res.stderr}")

# 3. Copiar a la raíz de Clases
shutil.copy2(pdf_student, os.path.join(ROOT_DIR, "ejercicios_50_reacciones_organicas.pdf"))
shutil.copy2(pdf_solved, os.path.join(ROOT_DIR, "ejercicios_50_reacciones_organicas_resueltos.pdf"))
print("[OK] Copias sincronizadas en la raíz de Clases.")
