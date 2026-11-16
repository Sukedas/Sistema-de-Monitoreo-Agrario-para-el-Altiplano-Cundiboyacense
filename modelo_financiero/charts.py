# -*- coding: utf-8 -*-
import json, sys, os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = sys.argv[1]
o = json.load(open(os.path.join(OUT, 'model_out.json'), encoding='utf8'))
b = o['base']
plt.rcParams.update({'font.family': 'Times New Roman', 'font.size': 11, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.dpi': 150})
C1, C2, C3, C4 = '#1b4332', '#40916c', '#95d5b2', '#b08900'
YEARS = list(range(2027, 2038))

def save(name):
    plt.tight_layout(); plt.savefig(os.path.join(OUT, name), dpi=170); plt.close()

def mill(v): return [x / 1e6 for x in v]

# 1. Serie de papa y regresión
yrs = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
boy = [49208, 49735, 46506, 46718, 48336, 46668, 48477]
cun = [61553, 61270, 63160, 62855, 67618, 67274, 67464]
tot = np.array(boy) + np.array(cun)
x = np.array(yrs)
bb, aa = np.polyfit(x, tot, 1)
pred = aa + bb * x
r2 = 1 - ((tot - pred) ** 2).sum() / ((tot - tot.mean()) ** 2).sum()
# validación: ajuste 2019-2023, prueba 2024-2025
b2, a2 = np.polyfit(x[:5], tot[:5], 1)
p_test = a2 + b2 * x[5:]
mape = float(np.mean(np.abs((tot[5:] - p_test) / tot[5:])))
fut = np.arange(2026, 2038)
proj = aa + bb * fut
reg = dict(a=float(aa), b=float(bb), r2=float(r2), mape=mape, p_test=p_test.tolist(), real_test=tot[5:].tolist(),
           tot=tot.tolist(), proj={int(y): float(v) for y, v in zip(fut, proj)}, cagr=float((tot[-1] / tot[0]) ** (1 / 6) - 1))
json.dump(reg, open(os.path.join(OUT, 'reg.json'), 'w'))
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.bar(x - 0.2, boy, 0.4, color=C2, label='Boyacá')
ax.bar(x + 0.2, cun, 0.4, color=C1, label='Cundinamarca')
ax.plot(x, tot / 2, 'o', color=C4, label='Total / 2')
ax.plot(np.concatenate([x, fut]), (aa + bb * np.concatenate([x, fut])) / 2, '--', color=C4, label='Tendencia lineal / 2')
ax.set_ylabel('Hectáreas sembradas'); ax.legend(frameon=False, fontsize=9, ncol=2); ax.set_xticks(list(range(2019, 2038, 2)))
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f"{v:,.0f}".replace(',', '.')))
save('fig_papa.png')

# 2. Proyección de usuarios
m = b['mercado']
t = np.arange(0, 11)
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.bar(YEARS, m['new'], color=C3, label='Nuevos suscriptores directos (Bass)')
ax.plot(YEARS, m['active'], 'o-', color=C2, label='Suscriptores directos activos (fin de año)')
ax.plot(YEARS, m['inst'], 's--', color=C4, label='Predios en convenios institucionales')
ax.plot(YEARS, m['active_tot'], 'o-', color=C1, lw=2, label='Total de predios monitoreados')
ax.set_ylabel('Predios'); ax.legend(frameon=False, fontsize=9); ax.set_xticks(YEARS)
save('fig_demanda.png')

# 3. Ingresos y costos
p = b['pyg']
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.bar(np.array(YEARS) - 0.2, mill(p['ingresos']), 0.4, color=C1, label='Ingresos')
ax.bar(np.array(YEARS) + 0.2, mill(p['costos_op']), 0.4, color=C3, label='Costos y gastos operativos')
ax.plot(YEARS, mill(p['ebitda']), 'o-', color=C4, label='EBITDA')
ax.axhline(0, color='k', lw=0.6); ax.set_ylabel('Millones de COP corrientes'); ax.legend(frameon=False, fontsize=9)
ax.set_xticks(YEARS)
save('fig_ingresos.png')

# 4. Flujo de caja
fig, ax = plt.subplots(figsize=(7.2, 3.6))
cols = [C2 if v >= 0 else '#b5651d' for v in b['fc']]
ax.bar(YEARS, mill(b['fc']), color=cols, label='Flujo neto del proyecto')
ax.plot(YEARS, mill(b['fca']), 'o-', color=C1, label='Flujo acumulado')
ax.axhline(0, color='k', lw=0.6); ax.set_ylabel('Millones de COP corrientes'); ax.legend(frameon=False, fontsize=9)
ax.set_xticks(YEARS)
save('fig_flujo.png')

# 5. Tornado
base_v = b['ind']['vpn'] / 1e6
rows = []
for s in o['sens']:
    lo, hi = s['res']['-0.2']['vpn'] / 1e6, s['res']['0.2']['vpn'] / 1e6
    rows.append((s['var'], lo, hi))
rows.sort(key=lambda r: abs(r[2] - r[1]))
fig, ax = plt.subplots(figsize=(7.2, 3.8))
for i, (lab, lo, hi) in enumerate(rows):
    ax.barh(i, lo - base_v, left=base_v, color='#b5651d', height=0.6)
    ax.barh(i, hi - base_v, left=base_v, color=C2, height=0.6)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=9)
ax.axvline(base_v, color='k', lw=0.8); ax.axvline(0, color='grey', lw=0.6, ls=':')
ax.set_xlabel('VPN (millones de COP)')
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color='#b5651d', label='Variable −20 %'), Patch(color=C2, label='Variable +20 %')], frameon=False, fontsize=9, loc='lower right')
save('fig_tornado.png')

# 6. Escenarios / alternativas
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.2))
sc = o['escenarios']
names = ['pesimista', 'base', 'optimista']
axs[0].bar(['Pesimista', 'Base', 'Optimista'], [sc[k]['ind']['vpn'] / 1e6 for k in names], color=['#b5651d', C3, C2])
axs[0].axhline(0, color='k', lw=0.6); axs[0].set_title('VPN por escenario', fontsize=10); axs[0].set_ylabel('Millones de COP')
al = o['alts']
axs[1].bar(['A: directa', 'B: híbrida', 'C: híbrida\najustada'], [al[k]['ind']['vpn'] / 1e6 for k in 'ABC'], color=['#b5651d', C3, C2])
axs[1].axhline(0, color='k', lw=0.6); axs[1].set_title('VPN por alternativa', fontsize=10)
save('fig_escenarios.png')

# 7. Diagrama de flujo del proceso
def box(ax, x, y, w, h, txt, fc='#e9f5ee', ec=C1, fs=8.5, shape='round'):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"{shape},pad=0.02,rounding_size=0.08" if shape == 'round' else 'square,pad=0.02', fc=fc, ec=ec, lw=1.1))
    ax.text(x, y, txt, ha='center', va='center', fontsize=fs, wrap=True)
def arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='->', color='#333', lw=1))
fig, ax = plt.subplots(figsize=(7.2, 6.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 12); ax.axis('off')
steps_l = ["1. Recepción e inspección de insumos\n(papel, tinta de carbono, cera)",
           "2. Serigrafía de electrodos\nsobre lámina de papel",
           "3. Curado en horno\n(100–140 °C, 30–60 min)",
           "4. Corte láser y encapsulado\ncon cera biodegradable",
           "5. Control de calidad\n(capacitancia, continuidad)"]
steps_r = ["6. Alistamiento de kits por ruta\n(sensores + nodo en comodato)",
           "7. Instalación en predio\n(nodo, sensores a 5–10 cm, alta en plataforma)",
           "8. Lectura cada 15 min y envío\nLoRaWAN → gateway 4G → nube",
           "9. Análisis y alertas\n(helada ≤ 0 °C, déficit hídrico) por WhatsApp/SMS",
           "10. Reposición cada ~4 meses;\nsensor usado se incorpora al suelo"]
ys = [10.8, 8.6, 6.4, 4.2, 2.0]
for i, s in enumerate(steps_l):
    box(ax, 2.6, ys[i], 4.6, 1.5, s)
    if i: arrow(ax, 2.6, ys[i - 1] - 0.78, 2.6, ys[i] + 0.78)
for i, s in enumerate(steps_r):
    box(ax, 7.6, ys[i], 4.4, 1.5, s, fc='#fdf6e3', ec=C4)
    if i: arrow(ax, 7.6, ys[i - 1] - 0.78, 7.6, ys[i] + 0.78)
arrow(ax, 4.95, ys[4], 5.35, ys[0])
ax.text(2.6, 0.95, 'Si no cumple: reproceso o descarte (merma prevista del 10 %)', fontsize=8, ha='center', color='#7a1f1f')
ax.text(5.3, 7.4, 'Lotes\naprobados', fontsize=7.5, ha='left', color='#333')
arrow(ax, 7.6, ys[4] - 0.78, 7.6, 0.6); ax.text(7.6, 0.35, 'Ciclo de servicio (retorna al paso 6)', ha='center', fontsize=8)
ax.text(2.6, 11.85, 'Producción de sensores (laboratorio, Tunja)', ha='center', fontsize=9.5, weight='bold', color=C1)
ax.text(7.6, 11.85, 'Prestación del servicio (campo y plataforma)', ha='center', fontsize=9.5, weight='bold', color=C4)
save('fig_proceso.png')

# 8. Organigrama
fig, ax = plt.subplots(figsize=(7.2, 3.2)); ax.set_xlim(0, 12); ax.set_ylim(0.8, 5.8); ax.axis('off')
box(ax, 6, 5.2, 3.6, 0.8, 'Asamblea de accionistas', fc='#ffffff')
box(ax, 6, 4.0, 3.8, 0.8, 'Gerencia general y comercial')
arrow(ax, 6, 4.8, 6, 4.42)
box(ax, 10.3, 4.0, 2.8, 0.8, 'Contador externo\n(honorarios)', fc='#ffffff', fs=7.5)
ax.plot([7.9, 8.9], [4.0, 4.0], ls=':', color='#555')
areas = [(1.6, 'Área técnica (I+D)\nIng. electrónico(a)\nDesarrollador(a) IoT'), (4.6, 'Producción\nTécnico(a) de\nproducción'),
         (7.4, 'Operaciones de campo\nIng. agrónomo(a)\nTécnicos(as) de campo'), (10.4, 'Comercial y admón.\nAsesores(as) comerciales\nAuxiliar admón. y contable')]
ax.plot([1.6, 10.4], [3.0, 3.0], color='#333', lw=1)
ax.plot([6, 6], [3.58, 3.0], color='#333', lw=1)
for xx, txt in areas:
    ax.plot([xx, xx], [3.0, 2.55], color='#333', lw=1)
    box(ax, xx, 1.75, 2.7, 1.5, txt, fs=7.8)
save('fig_organigrama.png')

# 9. Cronograma (Gantt) jul-dic 2027 + arranque
acts = [("Constitución SAS, RUT, cuentas y Fondo Emprender", 0, 1),
        ("Adecuación del laboratorio y compra de equipos", 0.5, 2),
        ("Ajuste del diseño del sensor y del nodo (prototipos)", 0.5, 3),
        ("Ensayos de biodegradabilidad y calibración", 2, 4),
        ("Desarrollo de plataforma, firmware y alertas", 1, 5),
        ("Instalación de 8 gateways LoRaWAN", 3, 4.5),
        ("Piloto en 50 predios (Ventaquemada, Villapinzón, Siachoque)", 4, 6.5),
        ("Convenios con asociaciones y PDEA/EPSEA", 3, 6),
        ("Lanzamiento comercial y arranque de operación", 6, 7)]
fig, ax = plt.subplots(figsize=(7.2, 3.6))
for i, (n, s, e) in enumerate(acts):
    ax.barh(i, e - s, left=s, color=C2 if e <= 6 else C4, height=0.55)
ax.set_yticks(range(len(acts))); ax.set_yticklabels([a[0] for a in acts], fontsize=8.2); ax.invert_yaxis()
ax.set_xticks(range(0, 8)); ax.set_xticklabels(['jul-27', 'ago', 'sep', 'oct', 'nov', 'dic', 'ene-28', 'feb'], fontsize=8.5)
ax.grid(axis='x', ls=':', alpha=.6)
save('fig_cronograma.png')
print('ok', reg)
