# -*- coding: utf-8 -*-
"""Libro de Excel con flujo de caja del proyecto y del inversionista (fórmulas vivas)."""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.chart import BarChart, LineChart, Reference

OUT = sys.argv[1]
N = 10
COLS = [get_column_letter(2 + t) for t in range(N + 1)]  # B..L = año 0..10
YEARS = [2027 + t for t in range(N + 1)]
FONT = 'Arial'
BLUE = Font(name=FONT, color='0000FF', size=10)
BLACK = Font(name=FONT, color='000000', size=10)
GREEN = Font(name=FONT, color='008000', size=10)
BOLD = Font(name=FONT, bold=True, size=10)
HDR = Font(name=FONT, bold=True, color='FFFFFF', size=10)
TITLE = Font(name=FONT, bold=True, size=14, color='1B4332')
HFILL = PatternFill('solid', fgColor='1B4332')
SFILL = PatternFill('solid', fgColor='E9F5EE')
YFILL = PatternFill('solid', fgColor='FFFF00')
TOTFILL = PatternFill('solid', fgColor='D8EFE1')
thin = Side(style='thin', color='9AA8A0')
TOP = Border(top=thin)
COP = '#,##0;(#,##0);"-"'
PCT = '0.0%;(0.0%);"-"'
PCT2 = '0.00%'
NUM = '#,##0;(#,##0);"-"'
DEC = '#,##0.00'
DEC4 = '0.0000'

wb = Workbook()

def title(ws, text, sub=None):
    ws['A1'] = text; ws['A1'].font = TITLE
    if sub:
        ws['A2'] = sub; ws['A2'].font = Font(name=FONT, italic=True, size=9, color='5B6B62')
    ws.sheet_view.showGridLines = False

def year_header(ws, r, label='Concepto (COP corrientes)'):
    ws[f'A{r}'] = label
    for t, c in enumerate(COLS):
        ws[f'{c}{r}'] = f'{YEARS[t]}'
        ws[f'{c}{r + 1}'] = f'Año {t}'
    ws[f'M{r}'] = 'Nota / fuente'
    for c in ['A'] + COLS + ['M']:
        for rr in (r, r + 1):
            ws[f'{c}{rr}'].font = HDR; ws[f'{c}{rr}'].fill = HFILL
            ws[f'{c}{rr}'].alignment = Alignment(horizontal='center' if c != 'A' else 'left')

def section(ws, r, text):
    ws[f'A{r}'] = text; ws[f'A{r}'].font = BOLD
    for c in ['A'] + COLS + ['M']:
        ws[f'{c}{r}'].fill = SFILL

def yrow(ws, r, label, fn, fmt=COP, font=BLACK, note=None, bold=False, total=False):
    ws[f'A{r}'] = label; ws[f'A{r}'].font = BOLD if bold else Font(name=FONT, size=10)
    for t, c in enumerate(COLS):
        v = fn(t, c)
        ws[f'{c}{r}'] = v
        ws[f'{c}{r}'].number_format = fmt
        f = font
        if bold: f = Font(name=FONT, bold=True, color=font.color.rgb if font.color else '000000', size=10)
        ws[f'{c}{r}'].font = f
        if total:
            ws[f'{c}{r}'].fill = TOTFILL; ws[f'{c}{r}'].border = TOP
    if total:
        ws[f'A{r}'].fill = TOTFILL; ws[f'A{r}'].border = TOP
    if note:
        ws[f'M{r}'] = note; ws[f'M{r}'].font = Font(name=FONT, size=9, italic=True, color='5B6B62')
    return r

def widths(ws, a=46, y=15, m=60):
    ws.column_dimensions['A'].width = a
    for c in COLS: ws.column_dimensions[c].width = y
    ws.column_dimensions['M'].width = m
    ws.freeze_panes = 'B5'

# =====================================================================  SUPUESTOS
S = wb.active; S.title = 'Supuestos'
title(S, 'Supuestos del modelo', 'Celdas en azul = datos de entrada editables; negro = fórmulas; verde = vínculos a otras hojas. Fondo amarillo = supuestos clave del equipo.')
for c, h in zip('ABCD', ['Supuesto', 'Valor', 'Unidad', 'Fuente o justificación']):
    S[f'{c}4'] = h; S[f'{c}4'].font = HDR; S[f'{c}4'].fill = HFILL
S.column_dimensions['A'].width = 52; S.column_dimensions['B'].width = 16; S.column_dimensions['C'].width = 16; S.column_dimensions['D'].width = 95
REF = {}
scal = [
    ('h', 'Macroeconomía y laboral'),
    ('smmlv26', 'SMMLV 2026', 1750905, 'COP/mes', 'Decreto 1469 de 2025 y Decreto 0159 de 2026 (Muñoz Paredes, 2026; Colorado, 2026)'),
    ('aux26', 'Auxilio de transporte 2026', 249095, 'COP/mes', 'Decreto 1470 de 2025'),
    ('inc27', 'Incremento SMMLV 2027', 0.09, '%', 'Supuesto del equipo; propuestas gremiales 8,5 %–9,5 % (Morales Herrera, 2026a)', 'Y'),
    ('increal', 'Incremento real SMMLV desde 2028 (sobre inflación)', 0.01, 'p. p.', 'Supuesto del equipo'),
    ('carga', 'Carga prestacional del empleador', 0.3835, '%', 'Gerencie.com (2026): empresa exonerada art. 114-1 ET, riesgo I'),
    ('cargaux', 'Carga sobre auxilio de transporte', 0.1766, '%', 'Cesantías, intereses y prima sobre el auxilio'),
    ('trm', 'TRM 2027', 3550, 'COP/USD', 'Supuesto con BBVA Research (2026) y Bancolombia (Delgado Gómez, 2026); TRM 14-nov-2026 = 3.316,70', 'Y'),
    ('audusd', 'Tasa USD por AUD', 0.65, 'USD/AUD', 'Supuesto del equipo (conversión del precio del gateway)', 'Y'),
    ('impf', 'Factor de importación (flete, arancel, IVA)', 1.35, 'x', 'Supuesto del equipo'),
    ('h', 'Impuestos'),
    ('tax', 'Impuesto de renta', 0.35, '%', 'Ley 2277 de 2022, art. 10 (art. 240 ET)'),
    ('ica', 'ICA Tunja (servicios)', 0.009, '%', 'Acuerdo Municipal 0029 de 2020, art. 145 (Concejo Municipal de Tunja, 2020)'),
    ('gmf', 'Gravamen a los movimientos financieros', 0.004, '%', 'Art. 872 ET'),
    ('gmfsh', 'Proporción de pagos gravados con GMF', 0.5, '%', 'Supuesto del equipo'),
    ('h', 'Mercado'),
    ('papaha', 'Área de papa sembrada 2025 en los 16 municipios', 61353, 'ha', 'UPRA (2026), EVA 2019–2025'),
    ('haprod', 'Área sembrada por productor al año', 3, 'ha', 'Supuesto; 80,3 % de predios de Boyacá < 3 ha (UPRA, 2024a)', 'Y'),
    ('trasl', 'Traslape fincas bovinas con productores de papa', 0.4, '%', 'Supuesto del equipo'),
    ('conect', 'Hogares rurales con internet', 0.569, '%', 'DANE (2026b), ECV 2025'),
    ('techo', 'Techo de adopción (sobre SAM)', 0.22, '%', '22 % de productores con asistencia técnica permanente (Castro, 2025b)', 'Y'),
    ('bp', 'Coeficiente de innovación p (Bass)', 0.03, '', 'Sultan, Farley y Lehmann (1990)'),
    ('bq', 'Coeficiente de imitación q (Bass)', 0.38, '', 'Sultan, Farley y Lehmann (1990)'),
    ('churn', 'Abandono anual de suscriptores', 0.10, '%', 'Supuesto del equipo', 'Y'),
    ('piloto', 'Predios del piloto (2027)', 50, 'predios', 'Supuesto del equipo'),
    ('convpil', 'Conversión de predios piloto a clientes', 0.6, '%', 'Supuesto del equipo'),
    ('h', 'Precios (pesos de 2027, antes de IVA)'),
    ('precio', 'Precio de lista Plan Predio', 72000, 'COP/mes', 'Sección 2.9 del documento. Alternativa recomendada C: 78.000', 'Y'),
    ('descas', 'Descuento por asociación', 0.15, '%', 'Estrategia comercial'),
    ('shas', 'Proporción de clientes vía asociación', 0.5, '%', 'Supuesto del equipo'),
    ('fee', 'Cargo de instalación', 120000, 'COP', 'Estrategia comercial'),
    ('descinst', 'Descuento en convenios institucionales', 0.10, '%', 'Estrategia comercial'),
    ('b2gp', 'Precio por contrato de información territorial', 40000000, 'COP', 'Supuesto del equipo'),
    ('h', 'Parámetros técnicos y costos unitarios'),
    ('nodos', 'Nodos por predio', 1, 'u.', 'Estudio técnico'),
    ('spn', 'Sensores por nodo', 2, 'u.', 'Estudio técnico'),
    ('ciclos', 'Ciclos de reposición al año', 3, 'ciclos', 'Vida útil 113 días (Zaccarin et al., 2025)'),
    ('scrap', 'Merma de producción', 0.10, '%', 'Supuesto del equipo'),
    ('smat', 'Materiales por sensor (precios 2026)', 1800, 'COP', 'Tinta NovaCentrix, papel Tisch Scientific, cera Anthophila SAS'),
    ('visita', 'Costo por visita de campo (2026)', 15000, 'COP', 'Supuesto del equipo (transporte y viáticos)', 'Y'),
    ('vpp', 'Visitas por predio al año', 3, 'visitas', 'Una por ciclo de reposición'),
    ('comis', 'Comisión a asociaciones', 0.05, '%', 'Sobre el recaudo de clientes vía asociación'),
    ('msg', 'Mensajería por predio', 0.035, 'USD/mes', 'WhatsApp utilidad USD 0,0008 (Meta, 2026); SMS USD 0,0592 (Twilio, 2026)'),
    ('nrep', 'Reposición anual de nodos (vida 5 años)', 0.20, '%', 'Supuesto del equipo'),
    ('bom', 'Costo del nodo lector (precios 2026)', 304100, 'COP', 'Lista de materiales, Electronilab (2026) y supuestos'),
    ('gwaud', 'Gateway Milesight UG65 4G AU915', 702.24, 'AUD', 'Ocean Controls (s. f.)'),
    ('gwinst', 'Instalación por gateway (2026)', 600000, 'COP', 'Supuesto del equipo'),
    ('gwsim', 'Datos móviles por gateway', 20, 'USD/mes', 'Telnyx (2026)'),
    ('cloud', 'Servidor en la nube', 58, 'USD/mes', 'Amazon Web Services (2026)'),
    ('arr', 'Arriendo bodega 150 m² en Tunja (2026)', 2000000, 'COP/mes', 'Fincaraíz (2026)'),
    ('kwh', 'Consumo de energía', 400, 'kWh/mes', 'Supuesto del equipo'),
    ('tkwh', 'Tarifa de energía EBSA', 1063.5, 'COP/kWh', 'Empresa de Energía de Boyacá (2025)'),
    ('serv', 'Agua, internet, telefonía y aseo', 600000, 'COP/mes', 'Supuesto del equipo'),
    ('seg', 'Seguros', 3000000, 'COP/año', 'Supuesto del equipo'),
    ('mlab', 'Mantenimiento del laboratorio', 2500000, 'COP/año', 'Supuesto del equipo'),
    ('mkt1', 'Mercadeo años 1 a 3', 24000000, 'COP/año', 'Supuesto del equipo'),
    ('mkt2', 'Mercadeo desde el año 4', 18000000, 'COP/año', 'Supuesto del equipo'),
    ('cont', 'Honorarios del contador', 900000, 'COP/mes', 'Supuesto del equipo'),
    ('vdia', 'Visitas por técnico al día', 8, 'visitas', 'Estudio técnico'),
    ('dias', 'Días de campo al año', 200, 'días', 'Estudio técnico'),
    ('desf', 'Días de desfase (capital de trabajo)', 60, 'días', 'Método del periodo de desfase'),
    ('pre', 'Fracción del año 0 (semestre preoperativo)', 0.5, 'año', 'Julio a diciembre de 2027'),
    ('h', 'Inversión inicial (precios 2026 o USD)'),
    ('printer', 'Impresora de esténcil 3040', 544.88, 'USD', 'VXB Bearings (s. f.)'),
    ('laser', 'Cortadora láser CO2 50 W', 1899.90, 'USD', 'VEVOR (s. f.)'),
    ('oven', 'Horno Memmert UN30 nuevo', 2161, 'USD', 'TEquipment (s. f.)'),
    ('bal', 'Balanza, congelador de pruebas y mesa ESD', 7000000, 'COP', 'Supuesto del equipo'),
    ('instr', 'Instrumentos (multímetro, LCR, osciloscopio, soldadura)', 1569700, 'COP', 'Electronilab (2026) y supuesto'),
    ('lapt', 'Portátil', 3500000, 'COP', 'Supuesto del equipo'),
    ('nlapt', 'Número de portátiles', 5, 'u.', 'Estudio técnico'),
    ('mueb', 'Muebles y enseres', 7000000, 'COP', 'Supuesto del equipo'),
    ('adec', 'Adecuación del laboratorio', 10000000, 'COP', 'Supuesto del equipo'),
    ('marca', 'Registro de marca, licencias y dominio', 2500000, 'COP', 'Supuesto del equipo'),
    ('const', 'Constitución SAS y registros', 1200000, 'COP', 'Confecámaras (2026)'),
    ('legal', 'Asesoría legal (datos y comodato)', 4000000, 'COP', 'Supuesto del equipo'),
    ('ensayo', 'Ensayos ISO 17556 y calibración', 9000000, 'COP', 'Supuesto del equipo'),
    ('capac', 'Capacitación de productores', 5000000, 'COP', 'Supuesto del equipo'),
    ('lanz', 'Lanzamiento comercial', 12000000, 'COP', 'Supuesto del equipo'),
    ('pcap', 'Nómina preoperativa capitalizada como intangible', 0.6, '%', 'Supuesto del equipo'),
    ('h', 'Tasa de descuento y financiación'),
    ('rf', 'Tasa libre de riesgo (UST 10 años)', 0.051, '%', 'FRED (2026), 12-nov-2026'),
    ('b1', 'Beta desapalancada Electronics (General)', 0.94, '', 'Damodaran (2026b)'),
    ('b2', 'Beta desapalancada Farming/Agriculture', 0.85, '', 'Damodaran (2026b)'),
    ('b3', 'Beta desapalancada Information Services', 0.76, '', 'Damodaran (2026b)'),
    ('erp', 'Prima de riesgo de mercado maduro', 0.0423, '%', 'Damodaran (2026a)'),
    ('crp', 'Prima de riesgo país Colombia', 0.0285, '%', 'Damodaran (2026a)'),
    ('pico', 'Inflación esperada Colombia dic-2027', 0.0519, '%', 'Encuesta BanRep (Alape Gamez, 2026)'),
    ('pius', 'Inflación esperada EE. UU. 2027', 0.024, '%', 'BBVA Research (2026)'),
    ('prima', 'Prima por tamaño y etapa temprana', 0.05, '%', 'Supuesto del equipo', 'Y'),
    ('fsmm', 'Capital semilla Fondo Emprender', 70, 'SMMLV', 'Acuerdo SENA 3 de 2026 (5 o más empleos)'),
    ('lsh', 'Proporción financiada con crédito', 0.25, '%', 'Supuesto del equipo'),
    ('lrate', 'Tasa del crédito', 0.2258, '% E. A.', 'IBC productivo rural nov-2026 (Acosta, 2026)'),
    ('lterm', 'Plazo del crédito', 5, 'años', 'Supuesto del equipo'),
]
r = 5
for it in scal:
    if it[0] == 'h':
        S[f'A{r}'] = it[1]; S[f'A{r}'].font = BOLD
        for c in 'ABCD': S[f'{c}{r}'].fill = SFILL
        r += 1; continue
    k, lab, val, unit, src = it[:5]
    S[f'A{r}'] = lab; S[f'B{r}'] = val; S[f'C{r}'] = unit; S[f'D{r}'] = src
    S[f'B{r}'].font = BLUE
    if len(it) > 5: S[f'B{r}'].fill = YFILL
    if unit in ('%', '% E. A.', 'p. p.'): S[f'B{r}'].number_format = '0.00%'
    elif isinstance(val, float) and val < 100: S[f'B{r}'].number_format = '0.00'
    else: S[f'B{r}'].number_format = '#,##0'
    for c in 'ACD': S[f'{c}{r}'].font = Font(name=FONT, size=10)
    REF[k] = f'Supuestos!$B${r}'
    r += 1
# derivados
r += 1; S[f'A{r}'] = 'Valores derivados'; S[f'A{r}'].font = BOLD
for c in 'ABCD': S[f'{c}{r}'].fill = SFILL
r += 1
der = [
    ('betau', 'Beta desapalancada promedio', f'=AVERAGE({REF["b1"]},{REF["b2"]},{REF["b3"]})', '0.000'),
    ('keusd', 'Costo del capital en USD (CAPM con riesgo país)', f'={REF["rf"]}+B{r}*{REF["erp"]}+{REF["crp"]}', PCT2),
    ('kecop', 'Costo del capital en COP', f'=(1+B{r+1})*(1+{REF["pico"]})/(1+{REF["pius"]})-1', PCT2),
    ('tmar', 'TMAR del proyecto (nominal en COP)', f'=B{r+2}+{REF["prima"]}', PCT2),
    ('pn', 'Precio neto mensual directo', f'={REF["precio"]}*(1-{REF["descas"]}*{REF["shas"]})', '#,##0'),
    ('pconv', 'Precio mensual en convenio', f'={REF["precio"]}*(1-{REF["descinst"]})', '#,##0'),
    ('fx', 'Tasa de importación (TRM × factor)', f'={REF["trm"]}*{REF["impf"]}', '#,##0'),
    ('spp', 'Sensores por predio al año (con merma)', f'={REF["nodos"]}*{REF["spn"]}*{REF["ciclos"]}*(1+{REF["scrap"]})', '0.00'),
]
for k, lab, f, fmt in der:
    S[f'A{r}'] = lab; S[f'B{r}'] = f; S[f'B{r}'].number_format = fmt; S[f'B{r}'].font = BLACK
    S[f'A{r}'].font = Font(name=FONT, size=10); REF[k] = f'Supuestos!$B${r}'; r += 1

# per-year inputs
r += 1
YR0 = r
S[f'A{r}'] = 'Supuestos por año'
for t, c in enumerate(COLS):
    S[f'{c}{r}'] = f'{YEARS[t]}'
for c in ['A'] + COLS:
    S[f'{c}{r}'].font = HDR; S[f'{c}{r}'].fill = HFILL
for c in COLS: S.column_dimensions[c].width = max(S.column_dimensions[c].width or 0, 14)
S.column_dimensions['B'].width = 16
r += 1
infl = [0.052, 0.042, 0.037, 0.035, 0.034] + [0.034] * 6
peryear = [
    ('infl', 'Inflación anual', infl, PCT, 'Construida con BanRep, encuesta de expectativas y FMI'),
    ('b2g', 'Contratos de información territorial', [0, 0, 1] + [2] * 8, NUM, 'Supuesto del equipo'),
    ('conv', 'Predios en convenios institucionales', [0, 0, 150, 250, 300] + [350] * 6, NUM, 'Supuesto del equipo (PDEA Cundinamarca: 5.020 productores)'),
    ('gwnew', 'Gateways nuevos', [8, 0, 4, 4] + [0] * 7, NUM, 'Despliegue por etapas'),
    ('gwrep', 'Gateways de reposición', [0, 0, 0, 0, 0, 8, 0, 4, 4, 0, 0], NUM, 'Vida útil de 5 años'),
]
PY = {}
for k, lab, vals, fmt, note in peryear:
    S[f'A{r}'] = lab; S[f'A{r}'].font = Font(name=FONT, size=10)
    for t, c in enumerate(COLS):
        S[f'{c}{r}'] = vals[t]; S[f'{c}{r}'].font = BLUE; S[f'{c}{r}'].number_format = fmt
    S[f'M{r}'] = note; S[f'M{r}'].font = Font(name=FONT, size=9, italic=True)
    PY[k] = r; r += 1
S[f'A{r}'] = 'Índice de precios (base 2026 = 1)'
for t, c in enumerate(COLS):
    prev = '1' if t == 0 else f'{COLS[t-1]}{r}'
    S[f'{c}{r}'] = f'={prev}*(1+{c}{PY["infl"]})'; S[f'{c}{r}'].number_format = DEC4
PY['idx'] = r; r += 1
S[f'A{r}'] = 'Índice de precios (base 2027 = 1)'
for c in COLS:
    S[f'{c}{r}'] = f'={c}{PY["idx"]}/$B${PY["idx"]}'; S[f'{c}{r}'].number_format = DEC4
PY['pidx'] = r; r += 1
S[f'A{r}'] = 'SMMLV'
for t, c in enumerate(COLS):
    S[f'{c}{r}'] = f'={REF["smmlv26"]}*(1+{REF["inc27"]})' if t == 0 else f'={COLS[t-1]}{r}*(1+{c}{PY["infl"]}+{REF["increal"]})'
    S[f'{c}{r}'].number_format = COP
PY['sm'] = r; r += 1
S[f'A{r}'] = 'Auxilio de transporte'
for t, c in enumerate(COLS):
    S[f'{c}{r}'] = f'={REF["aux26"]}*(1+{REF["inc27"]})' if t == 0 else f'={COLS[t-1]}{r}*(1+{c}{PY["infl"]}+{REF["increal"]})'
    S[f'{c}{r}'].number_format = COP
PY['aux'] = r; r += 1
S[f'A{r}'] = 'Factor de duración del año (año 0 = semestre)'
for t, c in enumerate(COLS):
    S[f'{c}{r}'] = f'={REF["pre"]}' if t == 0 else 1; S[f'{c}{r}'].number_format = '0.0'
PY['k0'] = r; r += 1
S[f'A{r}'] = 'Índice 2027 sobre 2026'; S[f'B{r}'] = f'=$B${PY["idx"]}'; S[f'B{r}'].number_format = DEC4
REF['i27'] = f'Supuestos!$B${r}'
SY = lambda key, c: f'Supuestos!{c}${PY[key]}'

# =====================================================================  DEMANDA
D = wb.create_sheet('Demanda')
title(D, 'Mercado y proyección de la demanda', 'Modelo de difusión de Bass (Bass, 1969) más convenios institucionales.')
D['A4'] = 'Municipio'; D['B4'] = 'Fincas bovinas 2026 (ICA)'
for c in 'AB': D[f'{c}4'].font = HDR; D[f'{c}4'].fill = HFILL
fincas = {"Chocontá": 1782, "Zipaquirá": 1113, "Villapinzón": 1656, "Cogua": 1060, "Tausa": 1101, "Ventaquemada": 1738, "Toca": 1293, "Cómbita": 1286, "Duitama": 868, "Siachoque": 1466, "Sogamoso": 1443, "Firavitoba": 813, "Tunja": 867, "Tibasosa": 738, "Soracá": 958, "Samacá": 841}
rr = 5
for k, v in fincas.items():
    D[f'A{rr}'] = k; D[f'B{rr}'] = v; D[f'B{rr}'].font = BLUE; D[f'B{rr}'].number_format = NUM; rr += 1
D[f'A{rr}'] = 'Total fincas bovinas'; D[f'B{rr}'] = f'=SUM(B5:B{rr-1})'; D[f'A{rr}'].font = BOLD; D[f'B{rr}'].number_format = NUM
FB = f'Demanda!$B${rr}'
rr += 2
mk = [
    ('prod', 'Productores de papa estimados', f'={REF["papaha"]}/{REF["haprod"]}'),
    ('tam', 'Mercado total (TAM)', f'=B{rr}+{FB}*(1-{REF["trasl"]})'),
    ('sam', 'Mercado disponible (SAM)', f'=B{rr+1}*{REF["conect"]}'),
    ('m', 'Potencial de adopción (m)', f'=B{rr+2}*{REF["techo"]}'),
]
for k, lab, f in mk:
    D[f'A{rr}'] = lab; D[f'B{rr}'] = f; D[f'B{rr}'].number_format = NUM; D[f'A{rr}'].font = Font(name=FONT, size=10)
    REF[k] = f'Demanda!$B${rr}'; rr += 1
rr += 1
year_header(D, rr, 'Proyección (predios)'); rr += 2
DR = {}
def drow(key, label, fn, fmt=NUM, note=None, total=False):
    global rr
    yrow(D, rr, label, fn, fmt, note=note, total=total); DR[key] = rr; rr += 1
drow('t', 't (años)', lambda t, c: t, '0')
drow('F', 'F(t) acumulada de Bass', lambda t, c: 0 if t == 0 else f'=(1-EXP(-({REF["bp"]}+{REF["bq"]})*{c}{DR["t"]}))/(1+({REF["bq"]}/{REF["bp"]})*EXP(-({REF["bp"]}+{REF["bq"]})*{c}{DR["t"]}))', DEC4, 'F(t) = [1−e^(−(p+q)t)] / [1+(q/p)e^(−(p+q)t)]')
drow('cum', 'Adoptantes acumulados', lambda t, c: f'={REF["m"]}*{c}{DR["F"]}')
drow('new', 'Nuevos suscriptores directos', lambda t, c: 0 if t == 0 else f'={c}{DR["cum"]}-{COLS[t-1]}{DR["cum"]}')
drow('act', 'Suscriptores directos activos (fin de año)', lambda t, c: 0 if t == 0 else f'={COLS[t-1]}{rr}*(1-{REF["churn"]})+{c}{DR["new"]}')
drow('avgd', 'Suscriptores directos promedio del año', lambda t, c: 0 if t == 0 else (f'=({COLS[t-1]}{DR["act"]}+{c}{DR["act"]})/2+{REF["piloto"]}*{REF["convpil"]}/2' if t == 1 else f'=({COLS[t-1]}{DR["act"]}+{c}{DR["act"]})/2'), NUM, 'Año 1 incluye la conversión del piloto')
drow('conv', 'Predios en convenios institucionales', lambda t, c: f'={SY("conv", c)}', NUM)
drow('convnew', 'Aumento de predios en convenio', lambda t, c: 0 if t == 0 else f'=MAX({c}{DR["conv"]}-{COLS[t-1]}{DR["conv"]},0)')
drow('avg', 'Total predios promedio atendidos', lambda t, c: f'={c}{DR["avgd"]}+{c}{DR["conv"]}', NUM, total=True)
drow('acttot', 'Total predios monitoreados (fin de año)', lambda t, c: f'={c}{DR["act"]}+{c}{DR["conv"]}', NUM, total=True)
drow('sens', 'Sensores fabricados', lambda t, c: f'={REF["piloto"]}*{REF["nodos"]}*{REF["spn"]}*2*(1+{REF["scrap"]})' if t == 0 else f'={c}{DR["avg"]}*{REF["spp"]}')
drow('vis', 'Visitas de campo', lambda t, c: f'={REF["piloto"]}*3' if t == 0 else f'={c}{DR["avg"]}*{REF["vpp"]}+{c}{DR["new"]}+{c}{DR["convnew"]}')
drow('tec', 'Técnicos de campo requeridos', lambda t, c: 1 if t == 0 else f'=MAX(1,ROUNDUP({c}{DR["vis"]}/({REF["vdia"]}*{REF["dias"]}),0))', NUM)
drow('nodos', 'Nodos lectores comprados', lambda t, c: f'={REF["piloto"]}*{REF["nodos"]}' if t == 0 else
     (f'=(MAX({c}{DR["new"]}-{REF["piloto"]}*{REF["convpil"]},0)+{c}{DR["convnew"]})*{REF["nodos"]}' if t == 1 else
      f'=(MAX({c}{DR["new"]},0)+{c}{DR["convnew"]})*{REF["nodos"]}+{COLS[t-1]}{DR["acttot"]}*{REF["nodos"]}*{REF["nrep"]}'), NUM, 'Nuevos predios + reposición del 20 % de la base instalada')
drow('gwcum', 'Gateways en operación', lambda t, c: f'={SY("gwnew", c)}' if t == 0 else f'={COLS[t-1]}{rr}+{SY("gwnew", c)}')
widths(D)
DY = lambda key, c: f'Demanda!{c}{DR[key]}'

# =====================================================================  INGRESOS
I = wb.create_sheet('Ingresos')
title(I, 'Proyección de ingresos', 'Precios de 2027 indexados con la inflación proyectada (índice base 2027).')
year_header(I, 4); ri = 6; IR = {}
def irow(key, label, fn, fmt=COP, note=None, total=False):
    global ri
    yrow(I, ri, label, fn, fmt, note=note, total=total); IR[key] = ri; ri += 1
irow('pl', 'Precio de lista mensual', lambda t, c: f'={REF["precio"]}*{SY("pidx", c)}', COP)
irow('pn', 'Precio neto mensual directo', lambda t, c: f'={REF["pn"]}*{SY("pidx", c)}', COP)
irow('pc', 'Precio mensual en convenio', lambda t, c: f'={REF["pconv"]}*{SY("pidx", c)}', COP)
irow('sus', 'Ingresos por suscripción directa', lambda t, c: 0 if t == 0 else f'={DY("avgd", c)}*{c}{IR["pn"]}*12', note='Predios directos promedio × precio neto × 12')
irow('conv', 'Ingresos por convenios de cobertura', lambda t, c: 0 if t == 0 else f'={DY("conv", c)}*{c}{IR["pc"]}*12')
irow('inst', 'Ingresos por cargos de instalación', lambda t, c: 0 if t == 0 else f'={DY("new", c)}*{REF["fee"]}*{SY("pidx", c)}')
irow('b2g', 'Ingresos por información territorial', lambda t, c: 0 if t == 0 else f'={SY("b2g", c)}*{REF["b2gp"]}*{SY("pidx", c)}')
irow('tot', 'Total ingresos operacionales', lambda t, c: f'=SUM({c}{IR["sus"]}:{c}{IR["b2g"]})', total=True)
widths(I)
IY = lambda key, c: f'Ingresos!{c}{IR[key]}'

# =====================================================================  PERSONAL
Pp = wb.create_sheet('Personal')
title(Pp, 'Costo de personal', 'Costo anual = (salario × (1 + carga) + auxilio × (1 + carga auxilio) si salario ≤ 2 SMMLV) × 12 × personas × fracción del año.')
roles = [
    ("Gerente general y comercial", 'fijo', 3800000, [1] * 11),
    ("Ingeniero(a) electrónico(a) I+D", 'fijo', 3064000, [1] * 11),
    ("Desarrollador(a) IoT y plataforma", 'fijo', 3354000, [1] * 11),
    ("Ingeniero(a) agrónomo(a)", 'fijo', 3103000, [0] + [1] * 10),
    ("Técnico(a) de producción", 'smm', 1.25, [1] * 11),
    ("Asesor(a) comercial", 'smm', 1.35, [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]),
    ("Auxiliar administrativo(a) y contable", 'smm', 1.15, [0] + [1] * 10),
    ("Técnico(a) de campo", 'smm', 1.2, None),
]
Pp['A4'] = 'Cargo'; Pp['N4'] = 'Base salarial'; Pp['O4'] = 'Tipo'
for c in ['A', 'N', 'O']: Pp[f'{c}4'].font = HDR; Pp[f'{c}4'].fill = HFILL
rp = 5; PR = {'cant': [], 'sal': [], 'cost': []}
year_header(Pp, rp, 'Personas por cargo'); rp += 2
for name, tp, val, cant in roles:
    Pp[f'A{rp}'] = name; Pp[f'N{rp}'] = val; Pp[f'N{rp}'].font = BLUE; Pp[f'O{rp}'] = 'COP 2027 (indexado al SMMLV)' if tp == 'fijo' else 'Múltiplo del SMMLV'
    Pp[f'N{rp}'].number_format = '#,##0.00' if tp == 'smm' else '#,##0'
    for t, c in enumerate(COLS):
        if cant is None:
            Pp[f'{c}{rp}'] = f'={DY("tec", c)}'; Pp[f'{c}{rp}'].font = GREEN
        else:
            Pp[f'{c}{rp}'] = cant[t]; Pp[f'{c}{rp}'].font = BLUE
        Pp[f'{c}{rp}'].number_format = NUM
    PR['cant'].append((rp, tp)); rp += 1
rp += 1; section(Pp, rp, 'Salario básico mensual'); rp += 1
for (rc, tp), (name, _, _, _) in zip(PR['cant'], roles):
    Pp[f'A{rp}'] = name
    for t, c in enumerate(COLS):
        Pp[f'{c}{rp}'] = f'=$N${rc}*{SY("sm", c)}/$B${PY["sm"]}'.replace('$B$', 'Supuestos!$B$') if tp == 'fijo' else f'=$N${rc}*{SY("sm", c)}'
        Pp[f'{c}{rp}'].number_format = COP
    PR['sal'].append(rp); rp += 1
rp += 1; section(Pp, rp, 'Costo anual total (incluye prestaciones)'); rp += 1
first = rp
for (rc, tp), rs, (name, _, _, _) in zip(PR['cant'], PR['sal'], roles):
    Pp[f'A{rp}'] = name
    for t, c in enumerate(COLS):
        Pp[f'{c}{rp}'] = (f'=({c}{rs}*(1+{REF["carga"]})+IF({c}{rs}<=2*{SY("sm", c)},{SY("aux", c)}*(1+{REF["cargaux"]}),0))*12*{c}{rc}*{SY("k0", c)}')
        Pp[f'{c}{rp}'].number_format = COP
    rp += 1
yrow(Pp, rp, 'Total nómina', lambda t, c: f'=SUM({c}{first}:{c}{rp-1})', total=True); PRT = rp; rp += 1
yrow(Pp, rp, 'Honorarios del contador', lambda t, c: f'={REF["cont"]}*12*{SY("pidx", c)}*{SY("k0", c)}'); PRC = rp; rp += 1
widths(Pp); Pp.column_dimensions['N'].width = 14; Pp.column_dimensions['O'].width = 28
NOM = lambda c: f'Personal!{c}{PRT}'; CONT = lambda c: f'Personal!{c}{PRC}'

# =====================================================================  COSTOS
Cs = wb.create_sheet('Costos')
title(Cs, 'Costos y gastos operativos', 'En el año 0 (semestre preoperativo) los costos se registran como inversión diferida.')
year_header(Cs, 4); rc = 6; CR = {}
def crow(key, label, fn, note=None, total=False, fmt=COP):
    global rc
    yrow(Cs, rc, label, fn, fmt, note=note, total=total); CR[key] = rc; rc += 1
section(Cs, rc, 'Costos variables'); rc += 1
crow('csu', 'Costo unitario del sensor', lambda t, c: f'={REF["smat"]}*{REF["i27"]}*{SY("pidx", c)}')
crow('sens', 'Materiales de sensores', lambda t, c: f'={DY("sens", c)}*{c}{CR["csu"]}')
crow('vis', 'Visitas de campo', lambda t, c: f'={DY("vis", c)}*{REF["visita"]}*{REF["i27"]}*{SY("pidx", c)}')
crow('com', 'Comisiones a asociaciones', lambda t, c: f'={IY("sus", c)}*{REF["shas"]}*{REF["comis"]}')
crow('msg', 'Mensajería (WhatsApp y SMS)', lambda t, c: 0 if t == 0 else f'={DY("avg", c)}*{REF["msg"]}*12*{REF["trm"]}*{SY("pidx", c)}')
crow('ica', 'ICA', lambda t, c: f'={IY("tot", c)}*{REF["ica"]}')
crow('var', 'Subtotal costos variables', lambda t, c: f'=SUM({c}{CR["sens"]}:{c}{CR["ica"]})', total=True)
section(Cs, rc, 'Costos fijos'); rc += 1
crow('nom', 'Nómina', lambda t, c: f'={NOM(c)}', note='Hoja Personal')
crow('cont', 'Honorarios del contador', lambda t, c: f'={CONT(c)}')
crow('sim', 'Datos móviles de gateways', lambda t, c: f'={DY("gwcum", c)}*{REF["gwsim"]}*12*{REF["trm"]}*{SY("pidx", c)}*{SY("k0", c)}')
crow('nube', 'Servidor en la nube', lambda t, c: f'={REF["cloud"]}*12*{REF["trm"]}*{SY("pidx", c)}*{SY("k0", c)}')
crow('arr', 'Arriendo', lambda t, c: f'={REF["arr"]}*12*{REF["i27"]}*{SY("pidx", c)}*{SY("k0", c)}')
crow('ene', 'Energía', lambda t, c: f'={REF["kwh"]}*12*{REF["tkwh"]}*{REF["i27"]}*{SY("pidx", c)}*{SY("k0", c)}')
crow('serv', 'Agua, internet y telefonía', lambda t, c: f'={REF["serv"]}*12*{SY("pidx", c)}*{SY("k0", c)}')
crow('mkt', 'Mercadeo', lambda t, c: 0 if t == 0 else f'=IF({c}{DR["t"]}<=3,{REF["mkt1"]},{REF["mkt2"]})*{SY("pidx", c)}'.replace(f'{c}{DR["t"]}', f'Demanda!{c}{DR["t"]}'))
crow('seg', 'Seguros', lambda t, c: f'={REF["seg"]}*{SY("pidx", c)}*{SY("k0", c)}')
crow('mlab', 'Mantenimiento del laboratorio', lambda t, c: 0 if t == 0 else f'={REF["mlab"]}*{SY("pidx", c)}')
crow('fix', 'Subtotal costos fijos', lambda t, c: f'=SUM({c}{CR["nom"]}:{c}{CR["mlab"]})', total=True)
crow('genfix', 'Gastos generales fijos (sin nómina ni honorarios)', lambda t, c: f'=SUM({c}{CR["sim"]}:{c}{CR["mlab"]})')
crow('op', 'Total costos y gastos operativos', lambda t, c: 0 if t == 0 else f'={c}{CR["var"]}+{c}{CR["fix"]}', total=True, note='Año 0: 0 (se capitaliza como inversión)')
widths(Cs)
CY = lambda key, c: f'Costos!{c}{CR[key]}'

# =====================================================================  INVERSIONES
V = wb.create_sheet('Inversiones')
title(V, 'Inversiones, depreciación y valor en libros', 'Depreciación en línea recta según tasas máximas del art. 137 del Estatuto Tributario.')
year_header(V, 4, 'Inversión por activo (COP corrientes)')
V['N4'] = 'Categoría'; V['O4'] = 'Vida útil'; V['N5'] = ''; V['O5'] = 'años'
for cc in ['N', 'O']:
    for rr_ in (4, 5): V[f'{cc}{rr_}'].font = HDR; V[f'{cc}{rr_}'].fill = HFILL
rv = 6
assets = []
def asset(label, cat, life, fn):
    global rv
    yrow(V, rv, label, fn); V[f'N{rv}'] = cat; V[f'O{rv}'] = life; V[f'O{rv}'].font = BLUE
    assets.append(rv); rv += 1
only0 = lambda expr: (lambda t, c: f'={expr}' if t == 0 else 0)
fx = REF['fx']; i27 = REF['i27']
section(V, rv, 'Activos fijos'); rv += 1
asset('Impresora de esténcil/serigrafía 3040', 'Maquinaria y equipo', 10, only0(f'{REF["printer"]}*{fx}'))
asset('Cortadora láser CO2 50 W', 'Maquinaria y equipo', 10, only0(f'{REF["laser"]}*{fx}'))
asset('Horno de secado Memmert UN30', 'Maquinaria y equipo', 10, only0(f'{REF["oven"]}*{fx}'))
asset('Balanza, congelador de pruebas y mesa ESD', 'Maquinaria y equipo', 10, only0(f'{REF["bal"]}*{i27}'))
asset('Instrumentos de laboratorio', 'Maquinaria y equipo', 10, only0(f'{REF["instr"]}*{i27}'))
asset('Equipos de cómputo', 'Equipo de cómputo', 5, lambda t, c: f'={REF["nlapt"]}*{REF["lapt"]}*{i27}' if t == 0 else 0)
asset('Reposición de equipos de cómputo', 'Equipo de cómputo', 5, lambda t, c: f'={REF["nlapt"]}*{REF["lapt"]}*{i27}*{SY("pidx", c)}' if t == 5 else 0)
asset('Muebles y enseres', 'Muebles y enseres', 10, only0(f'{REF["mueb"]}*{i27}'))
asset('Adecuación del laboratorio', 'Adecuaciones', 5, only0(f'{REF["adec"]}*{i27}'))
asset('Gateways LoRaWAN 4G (nuevos y reposición)', 'Equipo de comunicación', 5, lambda t, c: f'=({SY("gwnew", c)}+{SY("gwrep", c)})*({REF["gwaud"]}*{REF["audusd"]}*{fx}+{REF["gwinst"]}*{i27})*{SY("pidx", c)}')
asset('Nodos lectores en comodato', 'Equipo de comunicación', 5, lambda t, c: f'={DY("nodos", c)}*{REF["bom"]}*{i27}*{SY("pidx", c)}')
section(V, rv, 'Intangibles'); rv += 1
asset('Desarrollo de plataforma, firmware y app', 'Intangibles', 5, only0(f'({NOM("B")}+{CONT("B")})*{REF["pcap"]}'))
asset('Registro de marca, licencias y dominio', 'Intangibles', 5, only0(f'{REF["marca"]}*{i27}'))
section(V, rv, 'Gastos preoperativos diferidos'); rv += 1
asset('Constitución SAS y registros', 'Diferidos', 5, only0(f'{REF["const"]}*{i27}'))
asset('Asesoría legal', 'Diferidos', 5, only0(f'{REF["legal"]}*{i27}'))
asset('Ensayos de biodegradabilidad y calibración', 'Diferidos', 5, only0(f'{REF["ensayo"]}*{i27}'))
asset('Piloto en 50 predios (sensores y visitas)', 'Diferidos', 5, only0(f'{CY("sens", "B")}+{CY("vis", "B")}'))
asset('Capacitación de productores', 'Diferidos', 5, only0(f'{REF["capac"]}*{i27}'))
asset('Lanzamiento comercial', 'Diferidos', 5, only0(f'{REF["lanz"]}*{i27}'))
asset('Nómina preoperativa no capitalizada y honorarios', 'Diferidos', 5, only0(f'({NOM("B")}+{CONT("B")})*(1-{REF["pcap"]})'))
asset('Gastos generales del semestre preoperativo', 'Diferidos', 5, only0(f'{CY("genfix", "B")}'))
yrow(V, rv, 'Total inversión en activos', lambda t, c: '=' + '+'.join(f'{c}{a}' for a in assets), total=True); VTOT = rv; rv += 2
# Depreciación: por activo, depreciación del año t = suma sobre años de compra s<t con t-s<=vida de inv[s]/vida
section(V, rv, 'Depreciación y amortización anual por activo'); rv += 1
deps = []
for a in assets:
    V[f'A{rv}'] = '= "Dep. " & A' + str(a)
    for t, c in enumerate(COLS):
        if t == 0:
            V[f'{c}{rv}'] = 0
        else:
            terms = [f'IF({t}-{s}<=$O${a},{COLS[s]}{a}/$O${a},0)' for s in range(t)]
            V[f'{c}{rv}'] = '=' + '+'.join(terms)
        V[f'{c}{rv}'].number_format = COP
    deps.append(rv); rv += 1
yrow(V, rv, 'Total depreciación y amortización', lambda t, c: '=' + '+'.join(f'{c}{d}' for d in deps), total=True); VDEP = rv; rv += 2
section(V, rv, 'Valor en libros al cierre de 2037'); rv += 1
V[f'A{rv}'] = 'Activo'; V[f'B{rv}'] = 'Inversión total'; V[f'C{rv}'] = 'Depreciación acumulada'; V[f'D{rv}'] = 'Valor en libros'
for cc in 'ABCD': V[f'{cc}{rv}'].font = BOLD
rv += 1; vls = []
for a, dd in zip(assets, deps):
    V[f'A{rv}'] = f'=A{a}'; V[f'B{rv}'] = f'=SUM(B{a}:L{a})'; V[f'C{rv}'] = f'=SUM(B{dd}:L{dd})'; V[f'D{rv}'] = f'=B{rv}-C{rv}'
    for cc in 'BCD': V[f'{cc}{rv}'].number_format = COP
    vls.append(rv); rv += 1
V[f'A{rv}'] = 'Valor residual total (método contable)'; V[f'D{rv}'] = f'=SUM(D{vls[0]}:D{vls[-1]})'; V[f'D{rv}'].number_format = COP
V[f'A{rv}'].font = BOLD; V[f'D{rv}'].font = BOLD; VVL = f'Inversiones!$D${rv}'
widths(V, a=50); V.column_dimensions['N'].width = 24; V.column_dimensions['O'].width = 10

# =====================================================================  CAPITAL DE TRABAJO
K = wb.create_sheet('Capital de trabajo')
title(K, 'Capital de trabajo', 'Método del periodo de desfase: capital requerido para el año t+1 = costo operativo del año t+1 ÷ 365 × días de desfase.')
year_header(K, 4); rk = 6
yrow(K, rk, 'Costo operativo del año siguiente', lambda t, c: f'={CY("op", COLS[t+1])}' if t < N else 0); K1 = rk; rk += 1
yrow(K, rk, 'Costo operativo diario', lambda t, c: f'={c}{K1}/365'); K2 = rk; rk += 1
yrow(K, rk, 'Capital de trabajo requerido', lambda t, c: f'={c}{K2}*{REF["desf"]}'); K3 = rk; rk += 1
yrow(K, rk, 'Inversión (incremento) en capital de trabajo', lambda t, c: (f'={c}{K3}' if t == 0 else (f'={c}{K3}-{COLS[t-1]}{K3}' if t < N else 0)), total=True); KINV = rk; rk += 1
yrow(K, rk, 'Recuperación del capital de trabajo', lambda t, c: f'=SUM(B{KINV}:K{KINV})' if t == N else 0); KREC = rk; rk += 1
widths(K)

# =====================================================================  FLUJO DEL PROYECTO
F = wb.create_sheet('Flujo Proyecto')
title(F, 'Flujo de caja del proyecto (sin financiación)', 'Estructura: ingresos − costos − GMF = EBITDA − depreciación = EBIT − impuesto + depreciación − inversiones − capital de trabajo + valores de rescate.')
year_header(F, 4); rf_ = 6; FR = {}
def frow(key, label, fn, fmt=COP, note=None, total=False, font=BLACK):
    global rf_
    yrow(F, rf_, label, fn, fmt, note=note, total=total, font=font); FR[key] = rf_; rf_ += 1
section(F, rf_, 'Estado de resultados'); rf_ += 1
frow('ing', 'Ingresos operacionales', lambda t, c: f'={IY("tot", c)}', font=GREEN)
frow('var', '(−) Costos variables', lambda t, c: 0 if t == 0 else f'=-{CY("var", c)}', font=GREEN)
frow('fix', '(−) Costos y gastos fijos', lambda t, c: 0 if t == 0 else f'=-{CY("fix", c)}', font=GREEN)
frow('gmf', '(−) Gravamen a los movimientos financieros', lambda t, c: 0 if t == 0 else f'=-{REF["gmf"]}*{REF["gmfsh"]}*({CY("op", c)}+Inversiones!{c}{VTOT})', note='4 por mil sobre el 50 % de pagos')
frow('ebitda', 'EBITDA', lambda t, c: 0 if t == 0 else f'=SUM({c}{FR["ing"]}:{c}{FR["gmf"]})', total=True)
frow('dep', '(−) Depreciación y amortización', lambda t, c: f'=-Inversiones!{c}{VDEP}', font=GREEN)
frow('ebit', 'Utilidad operacional (EBIT)', lambda t, c: f'={c}{FR["ebitda"]}+{c}{FR["dep"]}', total=True)
frow('lossp', 'Pérdida fiscal acumulada al inicio', lambda t, c: 0 if t <= 1 else f'={COLS[t-1]}{rf_+2}', note='Art. 147 ET: compensación de pérdidas')
frow('base', 'Base gravable después de compensar', lambda t, c: 0 if t == 0 else f'=MAX(0,{c}{FR["ebit"]}-{c}{FR["lossp"]})')
frow('lossf', 'Pérdida fiscal acumulada al cierre', lambda t, c: 0 if t == 0 else f'=MAX(0,{c}{FR["lossp"]}-{c}{FR["ebit"]})')
frow('tax', '(−) Impuesto de renta', lambda t, c: f'=-{c}{FR["base"]}*{REF["tax"]}')
frow('net', 'Utilidad neta', lambda t, c: f'={c}{FR["ebit"]}+{c}{FR["tax"]}', total=True)
section(F, rf_, 'Flujo de caja'); rf_ += 1
frow('adddep', '(+) Depreciación y amortización', lambda t, c: f'=-{c}{FR["dep"]}')
frow('inv', '(−) Inversión en activos', lambda t, c: f'=-Inversiones!{c}{VTOT}', font=GREEN)
frow('gmf0', '(−) GMF de la inversión inicial', lambda t, c: f'=-{REF["gmf"]}*{REF["gmfsh"]}*Inversiones!{c}{VTOT}' if t == 0 else 0)
frow('kt', '(−) Inversión en capital de trabajo', lambda t, c: f"=-'Capital de trabajo'!{c}{KINV}", font=GREEN)
frow('rec', '(+) Recuperación del capital de trabajo', lambda t, c: f"='Capital de trabajo'!{c}{KREC}", font=GREEN)
frow('vl', '(+) Valor residual (valor en libros)', lambda t, c: f'={VVL}' if t == N else 0, font=GREEN)
frow('fc', 'FLUJO NETO DEL PROYECTO', lambda t, c: f'={c}{FR["net"]}+SUM({c}{FR["adddep"]}:{c}{FR["vl"]})', total=True)
frow('fca', 'Flujo acumulado', lambda t, c: f'={c}{FR["fc"]}' if t == 0 else f'={COLS[t-1]}{rf_}+{c}{FR["fc"]}')
frow('fd', 'Factor de descuento a la TMAR', lambda t, c: f'=1/(1+{REF["tmar"]})^Demanda!{c}{DR["t"]}', DEC4)
frow('vp', 'Valor presente del flujo', lambda t, c: f'={c}{FR["fc"]}*{c}{FR["fd"]}')
frow('vpa', 'Valor presente acumulado', lambda t, c: f'={c}{FR["vp"]}' if t == 0 else f'={COLS[t-1]}{rf_}+{c}{FR["vp"]}')
frow('pbs', 'Auxiliar recuperación simple', lambda t, c: '' if t == 0 else f'=IF(AND({COLS[t-1]}{FR["fca"]}<0,{c}{FR["fca"]}>=0),Demanda!{COLS[t-1]}{DR["t"]}+(-{COLS[t-1]}{FR["fca"]})/{c}{FR["fc"]},"")', '0.00')
frow('pbd', 'Auxiliar recuperación descontada', lambda t, c: '' if t == 0 else f'=IF(AND({COLS[t-1]}{FR["vpa"]}<0,{c}{FR["vpa"]}>=0),Demanda!{COLS[t-1]}{DR["t"]}+(-{COLS[t-1]}{FR["vpa"]})/{c}{FR["vp"]},"")', '0.00')
rf_ += 1; section(F, rf_, 'Indicadores de evaluación'); rf_ += 1
FC = f'B{FR["fc"]}:L{FR["fc"]}'
ind = [
    ('TMAR', f'={REF["tmar"]}', PCT2),
    ('VPN', f'=B{FR["fc"]}+NPV({REF["tmar"]},C{FR["fc"]}:L{FR["fc"]})', COP),
    ('TIR', f'=IRR({FC})', PCT2),
    ('TIR modificada (reinversión a la TMAR)', f'=MIRR({FC},{REF["tmar"]},{REF["tmar"]})', PCT2),
    ('Relación beneficio/costo', f'=SUMIF(B{FR["vp"]}:L{FR["vp"]},">0")/-SUMIF(B{FR["vp"]}:L{FR["vp"]},"<0")', '0.00'),
    ('Periodo de recuperación simple (años)', f'=IF(COUNT(C{FR["pbs"]}:L{FR["pbs"]})=0,"No se recupera",MIN(C{FR["pbs"]}:L{FR["pbs"]}))', '0.00'),
    ('Periodo de recuperación descontado (años)', f'=IF(COUNT(C{FR["pbd"]}:L{FR["pbd"]})=0,"No se recupera en el horizonte",MIN(C{FR["pbd"]}:L{FR["pbd"]}))', '0.00'),
    ('Necesidad máxima de financiación (déficit acumulado)', f'=-MIN(B{FR["fca"]}:L{FR["fca"]})', COP),
    ('VPN sin valor residual', f'=B{rf_+1}-{VVL}/(1+{REF["tmar"]})^10', COP),
]
FIND = {}
for lab, f, fmt in ind:
    F[f'A{rf_}'] = lab; F[f'B{rf_}'] = f; F[f'B{rf_}'].number_format = fmt; F[f'B{rf_}'].font = BOLD
    F[f'A{rf_}'].font = BOLD; FIND[lab] = f"'Flujo Proyecto'!$B${rf_}"; rf_ += 1
F[f'C{FIND["VPN"].split("$")[-1]}'] = '=IF(B' + FIND['VPN'].split('$')[-1] + '>0,"Viable: VPN > 0","No viable a la TMAR: VPN < 0")'
widths(F)

# =====================================================================  FINANCIACIÓN
Fi = wb.create_sheet('Financiación')
title(Fi, 'Estructura de financiación y amortización del crédito')
rfi = 4
fin = [
    ('inv0', 'Inversión inicial total (año 0)', f"=-'Flujo Proyecto'!B{FR['fc']}"),
    ('fondo', 'Capital semilla Fondo Emprender', f'={REF["fsmm"]}*{SY("sm", "B")}'),
    ('deuda', 'Crédito', f'={REF["lsh"]}*B{rfi}'),
    ('aporte', 'Aportes de los socios', f'=B{rfi}-B{rfi+1}-B{rfi+2}'),
    ('cuota', 'Cuota anual fija', f'=PMT({REF["lrate"]},{REF["lterm"]},-B{rfi+2})'),
]
for k, lab, f in fin:
    Fi[f'A{rfi}'] = lab; Fi[f'B{rfi}'] = f; Fi[f'B{rfi}'].number_format = COP; Fi[f'A{rfi}'].font = Font(name=FONT, size=10)
    Fi[f'C{rfi}'] = f'=IF(B$4=0,0,B{rfi}/B$4)' if k in ('fondo', 'deuda', 'aporte') else None
    if k in ('fondo', 'deuda', 'aporte'): Fi[f'C{rfi}'].number_format = PCT
    REF[k] = f'Financiación!$B${rfi}'; rfi += 1
rfi += 1
year_header(Fi, rfi, 'Tabla de amortización'); rfi += 2; FIR = {}
def firow(key, label, fn, total=False):
    global rfi
    yrow(Fi, rfi, label, fn, COP, total=total); FIR[key] = rfi; rfi += 1
firow('si', 'Saldo inicial', lambda t, c: 0 if t == 0 else (f'={REF["deuda"]}' if t == 1 else f'={COLS[t-1]}{rfi+4}'))
firow('int', 'Intereses', lambda t, c: f'={c}{FIR["si"]}*{REF["lrate"]}')
firow('cuota', 'Cuota', lambda t, c: 0 if t == 0 else f'=IF(Demanda!{c}{DR["t"]}<={REF["lterm"]},{REF["cuota"]},0)')
firow('am', 'Abono a capital', lambda t, c: f'={c}{FIR["cuota"]}-{c}{FIR["int"]}')
firow('sf', 'Saldo final', lambda t, c: f'={REF["deuda"]}' if t == 0 else f'={c}{FIR["si"]}-{c}{FIR["am"]}', total=True)
widths(Fi)

# =====================================================================  FLUJO DEL INVERSIONISTA
G = wb.create_sheet('Flujo Inversionista')
title(G, 'Flujo de caja del inversionista (capital propio)', 'Incluye el crédito, el capital semilla, los intereses (deducibles) y la amortización. Se descuenta con el costo del capital propio apalancado.')
year_header(G, 4); rg = 6; GR = {}
def grow(key, label, fn, fmt=COP, note=None, total=False, font=BLACK):
    global rg
    yrow(G, rg, label, fn, fmt, note=note, total=total, font=font); GR[key] = rg; rg += 1
PF = lambda key, c: f"'Flujo Proyecto'!{c}{FR[key]}"
section(G, rg, 'Estado de resultados con financiación'); rg += 1
grow('ebit', 'Utilidad operacional (EBIT)', lambda t, c: f'={PF("ebit", c)}', font=GREEN)
grow('int', '(−) Intereses del crédito', lambda t, c: f'=-Financiación!{c}{FIR["int"]}', font=GREEN)
grow('uai', 'Utilidad antes de impuestos', lambda t, c: f'={c}{GR["ebit"]}+{c}{GR["int"]}', total=True)
grow('lossp', 'Pérdida fiscal acumulada al inicio', lambda t, c: 0 if t <= 1 else f'={COLS[t-1]}{rg+2}')
grow('base', 'Base gravable', lambda t, c: 0 if t == 0 else f'=MAX(0,{c}{GR["uai"]}-{c}{GR["lossp"]})')
grow('lossf', 'Pérdida fiscal acumulada al cierre', lambda t, c: 0 if t == 0 else f'=MAX(0,{c}{GR["lossp"]}-{c}{GR["uai"]})')
grow('tax', '(−) Impuesto de renta', lambda t, c: f'=-{c}{GR["base"]}*{REF["tax"]}')
grow('net', 'Utilidad neta', lambda t, c: f'={c}{GR["uai"]}+{c}{GR["tax"]}', total=True)
section(G, rg, 'Flujo de caja del inversionista'); rg += 1
grow('dep', '(+) Depreciación y amortización', lambda t, c: f'={PF("adddep", c)}', font=GREEN)
grow('inv', '(−) Inversión en activos y GMF inicial', lambda t, c: f'={PF("inv", c)}+{PF("gmf0", c)}', font=GREEN)
grow('kt', '(−) Capital de trabajo', lambda t, c: f'={PF("kt", c)}', font=GREEN)
grow('desem', '(+) Desembolso del crédito', lambda t, c: f'={REF["deuda"]}' if t == 0 else 0, font=GREEN)
grow('fondo', '(+) Capital semilla Fondo Emprender', lambda t, c: f'={REF["fondo"]}' if t == 0 else 0, font=GREEN)
grow('am', '(−) Amortización del crédito', lambda t, c: f'=-Financiación!{c}{FIR["am"]}', font=GREEN)
grow('rec', '(+) Recuperación de capital de trabajo y valor residual', lambda t, c: f'={PF("rec", c)}+{PF("vl", c)}', font=GREEN)
grow('fci', 'FLUJO DEL INVERSIONISTA', lambda t, c: f'={c}{GR["net"]}+SUM({c}{GR["dep"]}:{c}{GR["rec"]})', total=True)
grow('fcia', 'Flujo acumulado del inversionista', lambda t, c: f'={c}{GR["fci"]}' if t == 0 else f'={COLS[t-1]}{rg}+{c}{GR["fci"]}')
grow('aport', 'Aportes de capital requeridos de los socios', lambda t, c: f'=MAX(0,-{c}{GR["fci"]})', note='Año 0: aporte inicial; años siguientes: aportes adicionales para cubrir flujos negativos')
grow('dist', 'Excedentes disponibles para los socios', lambda t, c: f'=MAX(0,{c}{GR["fci"]})')
grow('fd', 'Factor de descuento al costo del capital propio', lambda t, c: f'=1/(1+$B${rg+10})^Demanda!{c}{DR["t"]}', DEC4)
grow('vp', 'Valor presente', lambda t, c: f'={c}{GR["fci"]}*{c}{GR["fd"]}')
grow('vpa', 'Valor presente acumulado', lambda t, c: f'={c}{GR["vp"]}' if t == 0 else f'={COLS[t-1]}{rg}+{c}{GR["vp"]}')
grow('pbs', 'Auxiliar recuperación simple', lambda t, c: '' if t == 0 else f'=IF(AND({COLS[t-1]}{GR["fcia"]}<0,{c}{GR["fcia"]}>=0),Demanda!{COLS[t-1]}{DR["t"]}+(-{COLS[t-1]}{GR["fcia"]})/{c}{GR["fci"]},"")', '0.00')
grow('pbd', 'Auxiliar recuperación descontada', lambda t, c: '' if t == 0 else f'=IF(AND({COLS[t-1]}{GR["vpa"]}<0,{c}{GR["vpa"]}>=0),Demanda!{COLS[t-1]}{DR["t"]}+(-{COLS[t-1]}{GR["vpa"]})/{c}{GR["vp"]},"")', '0.00')
rg += 1; section(G, rg, 'Costo del capital propio e indicadores'); rg += 1
start = rg
gi = [
    ('Relación deuda / capital propio (D/E)', f'={REF["deuda"]}/({REF["aporte"]}+{REF["fondo"]})', '0.000'),
    ('Beta apalancada (Hamada)', f'={REF["betau"]}*(1+(1-{REF["tax"]})*B{start})', '0.000'),
    ('Costo del capital propio apalancado (Ke)', f'=(1+{REF["rf"]}+B{start+1}*{REF["erp"]}+{REF["crp"]})*(1+{REF["pico"]})/(1+{REF["pius"]})-1+{REF["prima"]}', PCT2),
    ('WACC', f'=({REF["aporte"]}+{REF["fondo"]})/{REF["inv0"]}*B{start+2}+{REF["deuda"]}/{REF["inv0"]}*{REF["lrate"]}*(1-{REF["tax"]})', PCT2),
]
for lab, f, fmt in gi:
    G[f'A{rg}'] = lab; G[f'B{rg}'] = f; G[f'B{rg}'].number_format = fmt; G[f'A{rg}'].font = BOLD; G[f'B{rg}'].font = BOLD; rg += 1
KE = f'$B${start+2}'
# fix discount factor reference to Ke cell
for t, c in enumerate(COLS):
    G[f'{c}{GR["fd"]}'] = f'=1/(1+{KE})^Demanda!{c}{DR["t"]}'
FCI = f'B{GR["fci"]}:L{GR["fci"]}'
gi2 = [
    ('VPN del inversionista', f'=B{GR["fci"]}+NPV({KE},C{GR["fci"]}:L{GR["fci"]})', COP),
    ('TIR del inversionista', f'=IRR({FCI})', PCT2),
    ('TIR modificada del inversionista', f'=MIRR({FCI},{KE},{KE})', PCT2),
    ('Relación beneficio/costo', f'=SUMIF(B{GR["vp"]}:L{GR["vp"]},">0")/-SUMIF(B{GR["vp"]}:L{GR["vp"]},"<0")', '0.00'),
    ('Periodo de recuperación simple (años)', f'=IF(COUNT(C{GR["pbs"]}:L{GR["pbs"]})=0,"No se recupera",MIN(C{GR["pbs"]}:L{GR["pbs"]}))', '0.00'),
    ('Periodo de recuperación descontado (años)', f'=IF(COUNT(C{GR["pbd"]}:L{GR["pbd"]})=0,"No se recupera en el horizonte",MIN(C{GR["pbd"]}:L{GR["pbd"]}))', '0.00'),
    ('Total aportes de capital de los socios (años 0 a 10)', f'=SUM(B{GR["aport"]}:L{GR["aport"]})', COP),
    ('Total excedentes para los socios', f'=SUM(B{GR["dist"]}:L{GR["dist"]})', COP),
    ('VPN del proyecto descontado al WACC', f"='Flujo Proyecto'!B{FR['fc']}+NPV(B{start+3},'Flujo Proyecto'!C{FR['fc']}:L{FR['fc']})", COP),
]
GIND = {}
for lab, f, fmt in gi2:
    G[f'A{rg}'] = lab; G[f'B{rg}'] = f; G[f'B{rg}'].number_format = fmt; G[f'A{rg}'].font = BOLD; G[f'B{rg}'].font = BOLD
    GIND[lab] = f"'Flujo Inversionista'!$B${rg}"; rg += 1
G[f'A{rg+1}'] = 'Lectura: el inversionista aporta el capital del año 0 neto de crédito y capital semilla, y además debe cubrir los flujos negativos de los primeros años de operación (fila "Aportes de capital requeridos").'
G[f'A{rg+1}'].font = Font(name=FONT, italic=True, size=9)
widths(G)

# =====================================================================  RESUMEN
R = wb.create_sheet('Resumen', 0)
title(R, 'BioSens Altiplano: resumen del flujo de caja', 'Sistema de Monitoreo Agrario para el Altiplano Cundiboyacense · Formulación y Evaluación de Proyectos · Universidad Distrital Francisco José de Caldas')
R['A4'] = 'Indicador'; R['B4'] = 'Proyecto'; R['C4'] = 'Inversionista'; R['D4'] = 'Criterio'
for c in 'ABCD': R[f'{c}4'].font = HDR; R[f'{c}4'].fill = HFILL
rows = [
    ('Tasa de descuento', FIND['TMAR'], f"'Flujo Inversionista'!{KE}", 'TMAR / Ke', PCT2),
    ('VPN (COP)', FIND['VPN'], GIND['VPN del inversionista'], '> 0', COP),
    ('TIR', FIND['TIR'], GIND['TIR del inversionista'], '> tasa de descuento', PCT2),
    ('TIR modificada', FIND['TIR modificada (reinversión a la TMAR)'], GIND['TIR modificada del inversionista'], '> tasa de descuento', PCT2),
    ('Relación beneficio/costo', FIND['Relación beneficio/costo'], GIND['Relación beneficio/costo'], '> 1', '0.00'),
    ('Recuperación simple (años)', FIND['Periodo de recuperación simple (años)'], GIND['Periodo de recuperación simple (años)'], '≤ 10', '0.00'),
    ('Recuperación descontada (años)', FIND['Periodo de recuperación descontado (años)'], GIND['Periodo de recuperación descontado (años)'], '≤ 10', '0.00'),
]
r = 5
for lab, a, b, crit, fmt in rows:
    R[f'A{r}'] = lab; R[f'B{r}'] = f'={a}'; R[f'C{r}'] = f'={b}'; R[f'D{r}'] = crit
    for c in 'BC': R[f'{c}{r}'].number_format = fmt; R[f'{c}{r}'].font = GREEN
    r += 1
r += 1
R[f'A{r}'] = 'Inversión inicial'; R[f'B{r}'] = f'={REF["inv0"]}'; R[f'B{r}'].number_format = COP; r += 1
R[f'A{r}'] = 'Necesidad máxima de financiación del proyecto'; R[f'B{r}'] = f"={FIND['Necesidad máxima de financiación (déficit acumulado)']}"; R[f'B{r}'].number_format = COP; r += 1
R[f'A{r}'] = 'Aportes totales de capital de los socios'; R[f'C{r}'] = f"={GIND['Total aportes de capital de los socios (años 0 a 10)']}"; R[f'C{r}'].number_format = COP; r += 1
R[f'A{r}'] = 'Decisión según VPN del proyecto'; R[f'B{r}'] = f'=IF({FIND["VPN"]}>0,"Aceptar","Ajustar: VPN negativo a la TMAR")'; r += 2
R[f'A{r}'] = 'Prueba la alternativa recomendada: cambie Supuestos › Precio de lista Plan Predio de 72.000 a 78.000 y todo el libro se recalcula.'
R[f'A{r}'].font = Font(name=FONT, italic=True, size=10, color='C0622B'); r += 2
# tabla de flujos para gráfico
R[f'A{r}'] = 'Año'; R[f'B{r}'] = 'Flujo del proyecto'; R[f'C{r}'] = 'Flujo acumulado del proyecto'; R[f'D{r}'] = 'Flujo del inversionista'
for c in 'ABCD': R[f'{c}{r}'].font = HDR; R[f'{c}{r}'].fill = HFILL
h = r; r += 1
for t, c in enumerate(COLS):
    R[f'A{r}'] = str(YEARS[t]); R[f'B{r}'] = f"='Flujo Proyecto'!{c}{FR['fc']}"; R[f'C{r}'] = f"='Flujo Proyecto'!{c}{FR['fca']}"; R[f'D{r}'] = f"='Flujo Inversionista'!{c}{GR['fci']}"
    for cc in 'BCD': R[f'{cc}{r}'].number_format = COP; R[f'{cc}{r}'].font = GREEN
    r += 1
ch = BarChart(); ch.type = 'col'; ch.title = 'Flujo de caja del proyecto y del inversionista (COP)'
ch.add_data(Reference(R, min_col=2, min_row=h, max_row=r - 1), titles_from_data=True)
ch.add_data(Reference(R, min_col=4, min_row=h, max_row=r - 1), titles_from_data=True)
ch.set_categories(Reference(R, min_col=1, min_row=h + 1, max_row=r - 1))
ln = LineChart(); ln.add_data(Reference(R, min_col=3, min_row=h, max_row=r - 1), titles_from_data=True)
ch += ln
ch.height = 9; ch.width = 22; ch.roundedCorners = False; ch.legend.position = 'b'; ch.legend.overlay = False
ch.x_axis.delete = False; ch.y_axis.delete = False; ch.y_axis.numFmt = '#,##0'
try:
    ch.title.overlay = False
except Exception:
    pass
R.add_chart(ch, 'F4')
R.column_dimensions['A'].width = 48; R.column_dimensions['B'].width = 20; R.column_dimensions['C'].width = 22; R.column_dimensions['D'].width = 22
R.sheet_view.showGridLines = False

# =====================================================================  MATRIZ DE RIESGOS
X = wb.create_sheet('Matriz de Riesgos')
title(X, 'Matriz de riesgos y oportunidades del proyecto', 'Escala de la matriz SGC-MT-002: probabilidad 1 (rara) a 5 (casi cierta); impacto 1 (insignificante) a 5 (catastrófico). Nivel = probabilidad × impacto: 1–4 bajo, 5–9 medio (moderado), 10–25 alto.')
hdr = ['No.', 'Proceso / componente', 'Tipo de riesgo', 'Factor', 'Riesgo', 'Causas', 'Consecuencias', 'Probabilidad (1-5)', 'Impacto (1-5)', 'Nivel inherente', 'Valoración', 'Controles / tratamiento', 'Opción de manejo', 'Responsable', 'Indicador de seguimiento', 'Probabilidad residual', 'Impacto residual', 'Nivel residual', 'Valoración residual', 'Frecuencia de monitoreo']
for j, h_ in enumerate(hdr):
    cell = X.cell(row=4, column=j + 1, value=h_); cell.font = HDR; cell.fill = HFILL; cell.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
X.row_dimensions[4].height = 42
risks = [
    ('Comercial', 'Mercado', 'Externo', 'Disposición a pagar menor que el precio supuesto', 'Ingreso bajo de pequeños productores; servicio nuevo sin referencia de precio', 'Menores ingresos; VPN negativo', 4, 4, 'Encuesta de disposición a pagar en el piloto; precio escalonado; venta vía asociaciones', 'Reducir la probabilidad', 'Gerencia', '% de encuestados que aceptan $78.000', 3, 3, 'Trimestral'),
    ('Comercial', 'Mercado', 'Externo', 'Adopción lenta o abandono alto', 'Baja cultura digital; desconfianza en tecnología nueva', 'Menos predios activos; punto de equilibrio tardío', 3, 4, 'Demostraciones en finca; casos de éxito; contratos anuales', 'Reducir la probabilidad', 'Comercial', 'Predios activos y tasa de abandono', 2, 4, 'Mensual'),
    ('Comercial', 'Mercado', 'Externo', 'No se firman convenios institucionales', 'Restricción presupuestal de gobernaciones y EPSEA; cambios de gobierno', 'Pérdida de 150 a 350 predios por año', 3, 4, 'Postulación temprana a PDEA y mesas agroclimáticas; diversificar entre los dos departamentos', 'Compartir el riesgo', 'Gerencia', 'Convenios firmados', 2, 4, 'Trimestral'),
    ('Producción', 'Técnico', 'Interno', 'Vida útil del sensor menor a 110 días', 'Suelos ácidos, fríos y húmedos del altiplano', 'Cuarto ciclo de reposición; más visitas', 3, 3, 'Ensayos de campo en el piloto; ajuste del espesor de la cera', 'Reducir la probabilidad', 'I+D', 'Días promedio de funcionamiento', 2, 3, 'Por lote'),
    ('Producción', 'Técnico', 'Interno', 'Exactitud insuficiente de la humedad medida', 'Variabilidad del papel y de la tinta', 'Alertas erradas; pérdida de confianza', 3, 3, 'Calibración por tipo de suelo; validación con sensor de referencia', 'Reducir el impacto', 'I+D', 'Error frente a sensor de referencia', 2, 3, 'Por lote'),
    ('Operación de campo', 'Operativo', 'Externo', 'Robo o daño de nodos', 'Equipos expuestos en campo', 'Reposición no presupuestada', 4, 2, 'Comodato con responsabilidad del productor; diseño discreto; seguro', 'Transferir el riesgo', 'Operaciones', 'Nodos perdidos por año', 3, 2, 'Mensual'),
    ('Red', 'Regulatorio', 'Externo', 'Plan de frecuencias no conforme u homologación', 'Canales US915 fuera de la banda libre 915–928 MHz', 'Sanción o interferencias', 1, 4, 'Configurar AU915; consulta previa a la ANE', 'Evitar el riesgo', 'I+D', 'Concepto de la ANE', 1, 2, 'Única'),
    ('Administración', 'Financiero', 'Externo', 'Aumento del salario mínimo o de la carga laboral', 'Decreto del SMMLV; proyecto de Ley de Rescate Económico', 'Mayor nómina (≈ 70 % de los costos)', 4, 3, 'Escalar la nómina con la demanda; indexar precios', 'Reducir el impacto', 'Gerencia', 'Nómina / ingresos', 3, 3, 'Anual'),
    ('Compras', 'Financiero', 'Externo', 'Devaluación del peso', 'TRM volátil', 'Hardware importado más caro', 3, 2, 'Compras anticipadas; proveedores nacionales', 'Reducir el impacto', 'Administración', 'TRM de compra frente a la presupuestada', 2, 2, 'Trimestral'),
    ('Finanzas', 'Liquidez', 'Interno', 'Falta de capital para el déficit del arranque', 'Flujos negativos 2027–2030', 'Cierre de la empresa antes del punto de equilibrio', 3, 5, 'Ronda de capital semilla antes de 2028; Fondo Emprender; pagos anuales anticipados', 'Reducir la probabilidad', 'Gerencia', 'Meses de caja disponible', 2, 4, 'Mensual'),
    ('Servicio', 'Climático', 'Externo', 'Eventos fuera del alcance del sistema (granizo, inundación)', 'Variabilidad climática', 'Reclamos de clientes', 3, 2, 'Comunicar el alcance; integrar alertas del IDEAM', 'Aceptar el riesgo', 'Agronomía', 'Reclamos por evento', 3, 1, 'Por evento'),
    ('Producción', 'Ambiental', 'Interno', 'Residuos de tinta o cera en el suelo', 'Composición de los materiales', 'Daño ambiental y reputacional', 1, 3, 'Tinta de carbono sin plata; ensayos ISO 17556 e ISO 23517; recolección RAEE de nodos', 'Evitar el riesgo', 'I+D', 'Resultado de ensayos de ecotoxicidad', 1, 2, 'Anual'),
]
lev = lambda cell: f'=IF({cell}>=10,"Alto",IF({cell}>=5,"Moderado","Bajo"))'
for i, rk_ in enumerate(risks):
    rr_ = 5 + i
    vals = [f'R{i+1}', rk_[0], rk_[1], rk_[2], rk_[3], rk_[4], rk_[5], rk_[6], rk_[7], f'=H{rr_}*I{rr_}', lev(f'J{rr_}'), rk_[8], rk_[9], rk_[10], rk_[11], rk_[12], rk_[13], f'=P{rr_}*Q{rr_}', lev(f'R{rr_}'), rk_[14]]
    for j, v in enumerate(vals):
        cell = X.cell(row=rr_, column=j + 1, value=v); cell.font = Font(name=FONT, size=9, color='0000FF' if j in (7, 8, 15, 16) else '000000')
        cell.alignment = Alignment(wrap_text=True, vertical='top', horizontal='center' if j in (0, 7, 8, 9, 10, 15, 16, 17, 18) else 'left')
    X.row_dimensions[rr_].height = 48
last = 4 + len(risks)
red = PatternFill('solid', fgColor='E8A48A'); yel = PatternFill('solid', fgColor='F3D38B'); grn = PatternFill('solid', fgColor='BFE3CC')
for col in ('J', 'R'):
    X.conditional_formatting.add(f'{col}5:{col}{last}', CellIsRule(operator='greaterThanOrEqual', formula=['10'], fill=red))
    X.conditional_formatting.add(f'{col}5:{col}{last}', CellIsRule(operator='between', formula=['5', '9'], fill=yel))
    X.conditional_formatting.add(f'{col}5:{col}{last}', CellIsRule(operator='lessThan', formula=['5'], fill=grn))
for j, w in enumerate([6, 16, 12, 10, 34, 34, 30, 12, 11, 10, 12, 42, 18, 14, 28, 12, 11, 10, 12, 14]):
    X.column_dimensions[get_column_letter(j + 1)].width = w
X.freeze_panes = 'F5'
# mapa de calor
hr = last + 3
X[f'B{hr}'] = 'Mapa de calor (número de riesgos inherentes por celda)'; X[f'B{hr}'].font = BOLD
pl = ['Casi cierta (5)', 'Probable (4)', 'Posible (3)', 'Improbable (2)', 'Rara (1)']
for k, p in enumerate(range(5, 0, -1)):
    rr_ = hr + 1 + k
    X[f'B{rr_}'] = pl[k]; X[f'B{rr_}'].font = BOLD
    for i_ in range(1, 6):
        col = get_column_letter(2 + i_)
        cell = X[f'{col}{rr_}']
        cell.value = f'=COUNTIFS($H$5:$H${last},{p},$I$5:$I${last},{i_})'
        s_ = p * i_; cell.fill = red if s_ >= 10 else yel if s_ >= 5 else grn
        cell.alignment = Alignment(horizontal='center', vertical='center'); cell.font = Font(name=FONT, bold=True, size=11)
    X.row_dimensions[rr_].height = 26
for i_, n_ in enumerate(['Insignificante (1)', 'Menor (2)', 'Moderado (3)', 'Mayor (4)', 'Catastrófico (5)']):
    c_ = X[f'{get_column_letter(3 + i_)}{hr + 6}']; c_.value = n_; c_.font = BOLD; c_.alignment = Alignment(horizontal='center', wrap_text=True)
X.sheet_view.showGridLines = False

wb.save(OUT)
print('saved', OUT)
