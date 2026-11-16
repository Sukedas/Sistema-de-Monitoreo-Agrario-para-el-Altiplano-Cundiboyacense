# -*- coding: utf-8 -*-
"""Modelo financiero - Sistema de Monitoreo Agrario Altiplano Cundiboyacense.
Cifras en pesos colombianos (COP) corrientes. Año 0 = 2027 (6 meses preoperativos,
jul-dic 2027); años 1..10 = 2028..2037.
"""
import json, math, copy, sys

N = 10
PRE = 0.5
YEARS = [2027 + t for t in range(N + 1)]

BASE = dict(
    infl={2027: 0.052, 2028: 0.042, 2029: 0.037, 2030: 0.035, 2031: 0.034, **{y: 0.034 for y in range(2032, 2038)}},
    smmlv_2026=1_750_905, aux_2026=249_095,
    smmlv_2027_inc=0.09, smmlv_real_inc=0.01,
    trm=3_550, import_factor=1.35,
    carga_prest=0.3835, carga_aux=0.1766,
    tax_rate=0.35, ica=0.009,
    papa_ha_2025=61_353, ha_por_productor=3.0, traslape_bov=0.40,
    conect=0.569, techo_adop=0.22, bass_p=0.03, bass_q=0.38, churn=0.10,
    precio_mes_2027=72_000, desc_asoc=0.15, share_asoc=0.50, inst_fee_2027=120_000,
    b2g_contracts={1: 0, 2: 1, **{t: 2 for t in range(3, N + 1)}}, b2g_price_2027=40_000_000,
    nodos_por_predio=1, sensores_por_nodo=2, ciclos=3, scrap=0.10,
    sensor_mat_2026=1_800, visita_2026=15_000, visitas_por_predio=3, comision_asoc=0.05,
    msg_predio_mes_usd=0.035, nodo_reposicion=0.20,
    gw_usd=702.24 * 0.65, gw_install_2026=600_000, gw_sim_usd_mes=20.0,
    gw_plan={0: 8, 2: 4, 3: 4}, gw_rep={5: 8, 7: 4, 8: 4},
    cloud_usd_mes=58, piloto_predios=50, arriendo_2026=2_000_000,
    inst_predios={0: 0, 1: 0, 2: 150, 3: 250, 4: 300, **{t: 350 for t in range(5, N + 1)}}, inst_desc=0.10,
    loan_share=0.25, loan_rate=0.2258, loan_term=5,
)

BOM_NODO_2026 = [
    ("Microcontrolador ESP32-S3", 38_900, "Electronilab (2026)"),
    ("Módulo LoRa E220-900T22D (915 MHz)", 37_500, "Electronilab (2026)"),
    ("Antena 915 MHz 3 dBi", 21_900, "Electronilab (2026)"),
    ("Panel solar 1,8 W", 39_500, "Electronilab (2026)"),
    ("Cargador TP4056 y protección BMS 1S", 9_400, "Electronilab (2026)"),
    ("Sensor de aire SHT41 (temperatura para helada)", 31_900, "Electronilab (2026)"),
    ("Celda Li-ion 18650", 15_000, "Supuesto del equipo"),
    ("Lector de acople inductivo (bobina y convertidor de impedancia)", 45_000, "Supuesto del equipo"),
    ("Caja IP65, estaca y tornillería", 40_000, "Supuesto del equipo"),
    ("Circuito impreso, ensamble y prueba", 25_000, "Supuesto del equipo"),
]

# cargo, tipo, salario (COP 2027 o múltiplo SMMLV), cantidades año 0..10
ROLES = [
    ("Gerente general y comercial (socio fundador)", 'fijo', 3_800_000, [1] * 11),
    ("Ingeniero(a) electrónico(a): I+D de sensores y nodos", 'fijo', round(2_811_405 * 1.09, -3), [1] * 11),
    ("Desarrollador(a) IoT y de plataforma", 'fijo', round(3_076_944 * 1.09, -3), [1] * 11),
    ("Ingeniero(a) agrónomo(a): agroclima y soporte", 'fijo', round(2_846_342 * 1.09, -3), [0] + [1] * 10),
    ("Técnico(a) de producción de sensores", 'smm', 1.25, [1] * 11),
    ("Asesor(a) comercial", 'smm', 1.35, [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]),
    ("Auxiliar administrativo(a) y contable", 'smm', 1.15, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
]


def npv(rate, cf):
    return sum(v / (1 + rate) ** t for t, v in enumerate(cf))


def irr(cf):
    f = lambda r: npv(r, cf)
    lo, hi = -0.95, 3.0
    if f(lo) * f(hi) > 0:
        return None
    for _ in range(300):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0: hi = mid
        else: lo = mid
    return (lo + hi) / 2


def indicators(cf, rate):
    acc = 0; pb = None
    for t, x in enumerate(cf):
        prev = acc; acc += x
        if t > 0 and acc >= 0 and pb is None and x > 0:
            pb = t - 1 + (-prev) / x
    accd = 0; pbd = None
    for t, x in enumerate(cf):
        xd = x / (1 + rate) ** t; prev = accd; accd += xd
        if t > 0 and accd >= 0 and pbd is None and xd > 0:
            pbd = t - 1 + (-prev) / xd
    ben = sum(x / (1 + rate) ** t for t, x in enumerate(cf) if x > 0)
    cost = sum(-x / (1 + rate) ** t for t, x in enumerate(cf) if x < 0)
    n = len(cf) - 1
    fv = sum(x * (1 + rate) ** (n - t) for t, x in enumerate(cf) if x > 0)
    tirm = (fv / cost) ** (1 / n) - 1 if cost > 0 and fv > 0 else None
    return dict(vpn=npv(rate, cf), tir=irr(cf), pb=pb, pbd=pbd, bc=ben / cost if cost else None, tirm=tirm)


def build(P):
    P = copy.deepcopy(P)
    r = dict(P=P)
    idx = {2026: 1.0}
    for y in YEARS: idx[y] = idx[y - 1] * (1 + P['infl'][y])
    sm = {2026: P['smmlv_2026']}; aux = {2026: P['aux_2026']}
    for y in YEARS:
        g = P['smmlv_2027_inc'] if y == 2027 else P['infl'][y] + P['smmlv_real_inc']
        sm[y] = sm[y - 1] * (1 + g); aux[y] = aux[y - 1] * (1 + g)
    r.update(idx=idx, smmlv=sm, aux=aux)
    pidx = lambda t: idx[YEARS[t]] / idx[2027]
    k0 = lambda t: PRE if t == 0 else 1.0   # año 0 dura 6 meses

    # ---------- mercado
    fincas = {"Chocontá": 1782, "Zipaquirá": 1113, "Villapinzón": 1656, "Cogua": 1060, "Tausa": 1101,
              "Ventaquemada": 1738, "Toca": 1293, "Cómbita": 1286, "Duitama": 868, "Siachoque": 1466,
              "Sogamoso": 1443, "Firavitoba": 813, "Tunja": 867, "Tibasosa": 738, "Soracá": 958, "Samacá": 841}
    fb = sum(fincas.values())
    prod_papa = P['papa_ha_2025'] / P['ha_por_productor']
    tam = prod_papa + fb * (1 - P['traslape_bov'])
    sam = tam * P['conect']
    m = sam * P['techo_adop']
    p, q = P['bass_p'], P['bass_q']
    F = lambda t: (1 - math.exp(-(p + q) * t)) / (1 + (q / p) * math.exp(-(p + q) * t))
    cum = [0] + [m * F(t) for t in range(1, N + 1)]
    new = [0] + [cum[t] - cum[t - 1] for t in range(1, N + 1)]
    active = [0]
    for t in range(1, N + 1): active.append(active[-1] * (1 - P['churn']) + new[t])
    avg = [0] + [(active[t - 1] + active[t]) / 2 for t in range(1, N + 1)]
    avg[1] += P['piloto_predios'] * 0.6 / 2   # predios piloto que se convierten (60 %)
    inst = [P['inst_predios'][t] for t in range(N + 1)]
    inst_new = [0] + [max(inst[t] - inst[t - 1], 0) for t in range(1, N + 1)]
    avg_b2c = avg[:]
    avg = [avg_b2c[t] + inst[t] for t in range(N + 1)]
    active_tot = [active[t] + inst[t] for t in range(N + 1)]
    r['mercado'] = dict(inst=inst, inst_new=inst_new, avg_b2c=avg_b2c, active_tot=active_tot, fincas=fincas, fincas_bov=fb, prod_papa=prod_papa, tam=tam, sam=sam, m=m,
                        F=[F(t) for t in range(N + 1)], cum=cum, new=new, active=active, avg=avg)

    # ---------- ingresos
    pn = P['precio_mes_2027'] * (1 - P['desc_asoc'] * P['share_asoc'])
    ing_sus = [0] + [avg_b2c[t] * pn * 12 * pidx(t) for t in range(1, N + 1)]
    ing_conv = [0] + [inst[t] * P['precio_mes_2027'] * (1 - P['inst_desc']) * 12 * pidx(t) for t in range(1, N + 1)]
    ing_inst = [0] + [new[t] * P['inst_fee_2027'] * pidx(t) for t in range(1, N + 1)]
    ing_b2g = [0] + [P['b2g_contracts'][t] * P['b2g_price_2027'] * pidx(t) for t in range(1, N + 1)]
    ingresos = [ing_sus[t] + ing_conv[t] + ing_inst[t] + ing_b2g[t] for t in range(N + 1)]
    r['ingresos'] = dict(conv=ing_conv, sus=ing_sus, inst=ing_inst, b2g=ing_b2g, total=ingresos, precio_neto_mes=pn)

    # ---------- cantidades físicas
    spp = P['nodos_por_predio'] * P['sensores_por_nodo'] * P['ciclos'] * (1 + P['scrap'])
    sensores = [P['piloto_predios'] * P['nodos_por_predio'] * P['sensores_por_nodo'] * 2 * (1 + P['scrap'])] + \
               [avg[t] * spp for t in range(1, N + 1)]
    visitas = [P['piloto_predios'] * 3] + [avg[t] * P['visitas_por_predio'] + new[t] + inst_new[t] for t in range(1, N + 1)]
    r['fisico'] = dict(sensores=sensores, visitas=visitas, spp=spp)

    # ---------- personal
    def costo(s, y):
        tot = s * (1 + P['carga_prest'])
        if s <= 2 * sm[y]: tot += aux[y] * (1 + P['carga_aux'])
        return tot * 12
    roles = [list(x) for x in ROLES]
    tec = [1]
    for t in range(1, N + 1): tec.append(max(1, math.ceil(visitas[t] / (8 * 200))))
    roles.append(["Técnico(a) de campo", 'smm', 1.2, tec])
    personal = []; nomina = [0.0] * (N + 1)
    for name, tp, val, cant in roles:
        row = dict(cargo=name, cant=cant, salario=[], costo=[])
        for t in range(N + 1):
            y = YEARS[t]
            s = val * sm[y] / sm[2027] if tp == 'fijo' else val * sm[y]
            c = costo(s, y) * cant[t] * k0(t)
            row['salario'].append(s); row['costo'].append(c); nomina[t] += c
        personal.append(row)
    contador = [900_000 * 12 * pidx(t) * k0(t) for t in range(N + 1)]
    r.update(personal=personal, nomina=nomina, contador=contador, tecnicos=tec)

    # ---------- costos de operación
    fx = P['trm'] * P['import_factor']
    c_sens_u = P['sensor_mat_2026'] * idx[2027]
    C = {}
    C['sensores'] = [sensores[t] * c_sens_u * pidx(t) for t in range(N + 1)]
    C['visitas'] = [visitas[t] * P['visita_2026'] * idx[2027] * pidx(t) for t in range(N + 1)]
    C['comision'] = [ing_sus[t] * P['share_asoc'] * P['comision_asoc'] for t in range(N + 1)]
    C['mensajeria'] = [0] + [avg[t] * P['msg_predio_mes_usd'] * 12 * P['trm'] * pidx(t) for t in range(1, N + 1)]
    gw_cum = []; acc = 0
    for t in range(N + 1): acc += P['gw_plan'].get(t, 0); gw_cum.append(acc)
    C['sim'] = [gw_cum[t] * P['gw_sim_usd_mes'] * 12 * P['trm'] * pidx(t) * k0(t) for t in range(N + 1)]
    C['nube'] = [P['cloud_usd_mes'] * 12 * P['trm'] * pidx(t) * k0(t) for t in range(N + 1)]
    C['arriendo'] = [P['arriendo_2026'] * 12 * idx[2027] * pidx(t) * k0(t) for t in range(N + 1)]
    C['energia'] = [400 * 12 * 1_063.5 * idx[2027] * pidx(t) * k0(t) for t in range(N + 1)]
    C['servicios'] = [600_000 * 12 * pidx(t) * k0(t) for t in range(N + 1)]
    C['marketing'] = [0] + [(24_000_000 if t <= 3 else 18_000_000) * pidx(t) for t in range(1, N + 1)]
    C['seguros'] = [3_000_000 * pidx(t) * k0(t) for t in range(N + 1)]
    C['mant_lab'] = [0] + [2_500_000 * pidx(t) for t in range(1, N + 1)]
    C['ica'] = [ingresos[t] * P['ica'] for t in range(N + 1)]
    r['costos'] = C; r['c_sens_u'] = c_sens_u; r['gw_cum'] = gw_cum
    VAR_KEYS = ['sensores', 'visitas', 'comision', 'mensajeria', 'ica']
    FIX_KEYS = ['sim', 'nube', 'arriendo', 'energia', 'servicios', 'marketing', 'seguros', 'mant_lab']
    r['VAR_KEYS'] = VAR_KEYS; r['FIX_KEYS'] = FIX_KEYS

    # ---------- inversiones
    nodo_cost = sum(c for _, c, _ in BOM_NODO_2026)
    nodo_u = nodo_cost * idx[2027]
    gw_u = P['gw_usd'] * fx + P['gw_install_2026'] * idx[2027]
    inv = []
    def add(con, cat, t, val, vida, grupo):
        inv.append(dict(concepto=con, cat=cat, t=t, valor=val, vida=vida, grupo=grupo))
    usd = lambda v: v * fx
    I27 = idx[2027]
    add("Impresora de esténcil/serigrafía de precisión 3040", "Maquinaria y equipo", 0, usd(544.88), 10, 'fijo')
    add("Cortadora láser CO2 de 50 W", "Maquinaria y equipo", 0, usd(1_899.90), 10, 'fijo')
    add("Horno de secado y curado Memmert UN30 (32 L, nuevo)", "Maquinaria y equipo", 0, usd(2_161), 10, 'fijo')
    add("Balanza analítica, congelador adaptado para pruebas de helada y mesa antiestática", "Maquinaria y equipo", 0, 7_000_000 * I27, 10, 'fijo')
    add("Instrumentos: multímetro, medidor LCR, osciloscopio USB y estación de soldadura", "Maquinaria y equipo", 0, (73_900 + 89_900 + 605_900 + 800_000) * I27, 10, 'fijo')
    add("Equipos de cómputo (5 portátiles)", "Equipo de cómputo", 0, 5 * 3_500_000 * I27, 5, 'fijo')
    add("Reposición de equipos de cómputo (5 portátiles)", "Equipo de cómputo", 5, 5 * 3_500_000 * I27 * pidx(5), 5, 'fijo')
    add("Muebles y enseres (oficina y laboratorio)", "Muebles y enseres", 0, 7_000_000 * I27, 10, 'fijo')
    add("Adecuación del laboratorio (instalación eléctrica RETIE, extracción, piso antiestático)", "Adecuaciones", 0, 10_000_000 * I27, 5, 'fijo')
    for t, n in P['gw_plan'].items():
        add(f"Gateways LoRaWAN 4G (AU915), instalados ({n} u.)", "Equipo de comunicación", t, n * gw_u * pidx(t), 5, 'red')
    for t, n in P['gw_rep'].items():
        add(f"Reposición de gateways ({n} u.)", "Equipo de comunicación", t, n * gw_u * pidx(t), 5, 'red')
    nodos_inst = [P['piloto_predios'] * P['nodos_por_predio']]
    for t in range(1, N + 1):
        nuevos = max(new[t] - (P['piloto_predios'] * 0.6 if t == 1 else 0), 0)
        rep = active_tot[t - 1] * P['nodos_por_predio'] * P['nodo_reposicion'] if t > 1 else 0
        nodos_inst.append((nuevos + inst_new[t]) * P['nodos_por_predio'] + rep)
    for t in range(N + 1):
        add(f"Nodos lectores en comodato ({nodos_inst[t]:.0f} u.)", "Equipo de comunicación", t, nodos_inst[t] * nodo_u * pidx(t), 5, 'nodos')
    nom0 = nomina[0] + contador[0]
    add("Desarrollo de plataforma, firmware y aplicación (60 % de la nómina preoperativa)", "Intangibles", 0, nom0 * 0.60, 5, 'intangible')
    add("Registro de marca, licencias y dominio", "Intangibles", 0, 2_500_000 * I27, 5, 'intangible')
    gen0 = sum(C[k][0] for k in FIX_KEYS)
    pre = [
        ("Constitución de la SAS, registro mercantil e impuesto de registro", 1_200_000 * I27),
        ("Asesoría legal: política de datos (Ley 1581 de 2012) y contrato de comodato", 4_000_000 * I27),
        ("Ensayos de biodegradabilidad (ISO 17556) y calibración en laboratorio externo", 9_000_000 * I27),
        ("Piloto en 50 predios: sensores y visitas", C['sensores'][0] + C['visitas'][0]),
        ("Capacitación de productores y asociaciones", 5_000_000 * I27),
        ("Lanzamiento comercial con asociaciones", 12_000_000 * I27),
        ("Nómina preoperativa no capitalizada (40 %) y honorarios", nom0 * 0.40),
        ("Gastos generales del semestre preoperativo", gen0),
    ]
    for con, val in pre:
        add(con, "Gastos preoperativos (diferidos)", 0, val, 5, 'diferido')
    r.update(inv=inv, nodos_inst=nodos_inst, nodo_u=nodo_u, gw_u=gw_u, nodo_2026=nodo_cost, bom=BOM_NODO_2026)
    inv_t = [sum(d['valor'] for d in inv if d['t'] == t) for t in range(N + 1)]

    # ---------- depreciación y valor en libros
    dep = [0.0] * (N + 1); vl = 0.0; rows = []
    for d in inv:
        a = d['valor'] / d['vida']; row = dict(d, anual=a, dep=[0.0] * (N + 1))
        for t in range(d['t'] + 1, N + 1):
            if t - d['t'] <= d['vida']: row['dep'][t] = a; dep[t] += a
        row['vl'] = d['valor'] - sum(row['dep']); vl += row['vl']; rows.append(row)
    r.update(dep=dep, dep_rows=rows, vl_final=vl)

    # ---------- costos operativos totales y capital de trabajo
    costos_op = [sum(C[k][t] for k in VAR_KEYS + FIX_KEYS) + nomina[t] + contador[t] for t in range(N + 1)]
    costos_op[0] = 0.0  # año 0: todo se registra como inversión/diferido
    desfase = 60
    req = [costos_op[t + 1] / 365 * desfase for t in range(N)] + [0]
    kt_inv = []; prev = 0
    for t in range(N):
        kt_inv.append(req[t] - prev); prev = req[t]
    kt_inv.append(0)
    kt_rec = sum(kt_inv)
    r['kt'] = dict(req=req, inv=kt_inv, rec=kt_rec, desfase=desfase)

    gmf = [0.004 * 0.5 * (costos_op[t] + inv_t[t]) for t in range(N + 1)]
    ebitda = [ingresos[t] - costos_op[t] - gmf[t] for t in range(N + 1)]
    ebitda[0] = 0.0
    ebit = [ebitda[t] - dep[t] for t in range(N + 1)]

    def taxes(base_list):
        tx = [0.0] * (N + 1); loss = 0.0
        for t in range(1, N + 1):
            b = base_list[t] - loss
            if b > 0: tx[t] = b * P['tax_rate']; loss = 0
            else: loss = -b
        return tx
    tax = taxes(ebit)
    net = [ebit[t] - tax[t] for t in range(N + 1)]
    fc = [0.0] * (N + 1)
    fc[0] = -inv_t[0] - gmf[0] - kt_inv[0]
    for t in range(1, N + 1): fc[t] = net[t] + dep[t] - inv_t[t] - kt_inv[t]
    fc[N] += kt_rec + vl
    fca = []; a = 0
    for v in fc: a += v; fca.append(a)
    r['pyg'] = dict(ingresos=ingresos, costos_op=costos_op, gmf=gmf, ebitda=ebitda, dep=dep, ebit=ebit, tax=tax,
                    net=net, inv_t=inv_t)
    r['fc'] = fc; r['fca'] = fca

    # ---------- tasa de descuento (CAPM, Damodaran 2026)
    rf, erp, crp = 0.0510, 0.0423, 0.0285
    beta_u = (0.94 + 0.85 + 0.76) / 3
    pi_co, pi_us = 0.0519, 0.024
    ke_usd = rf + beta_u * erp + crp
    ke_cop = (1 + ke_usd) * (1 + pi_co) / (1 + pi_us) - 1
    prima = 0.05
    tmar = ke_cop + prima
    r['tasa'] = dict(rf=rf, beta_u=beta_u, erp=erp, crp=crp, ke_usd=ke_usd, ke_cop=ke_cop, prima=prima, tmar=tmar,
                     pi_co=pi_co, pi_us=pi_us)
    r['ind'] = indicators(fc, tmar)

    # ---------- financiación
    inv0 = -fc[0]
    fondo = 70 * sm[2027]
    deuda = P['loan_share'] * inv0
    aporte = inv0 - fondo - deuda
    i_d = P['loan_rate']; T = P['loan_term']
    cuota = deuda * i_d / (1 - (1 + i_d) ** -T)
    saldo = deuda; rows = []; inte = [0.0] * (N + 1); amo = [0.0] * (N + 1)
    for t in range(1, T + 1):
        it = saldo * i_d; am = cuota - it
        rows.append(dict(t=t, saldo_ini=saldo, interes=it, amort=am, cuota=cuota, saldo_fin=saldo - am))
        inte[t] = it; amo[t] = am; saldo -= am
    tax_i = taxes([ebit[t] - inte[t] for t in range(N + 1)])
    fci = [0.0] * (N + 1)
    fci[0] = fc[0] + deuda + fondo
    for t in range(1, N + 1):
        fci[t] = (ebit[t] - inte[t] - tax_i[t]) + dep[t] - inv_t[t] - kt_inv[t] - amo[t]
    fci[N] += kt_rec + vl
    de = deuda / (aporte + fondo)
    beta_l = beta_u * (1 + (1 - P['tax_rate']) * de)
    ke_l = (1 + rf + beta_l * erp + crp) * (1 + pi_co) / (1 + pi_us) - 1 + prima
    wacc = (aporte + fondo) / inv0 * ke_l + deuda / inv0 * i_d * (1 - P['tax_rate'])
    r['fin'] = dict(inv0=inv0, fondo=fondo, deuda=deuda, aporte=aporte, i_d=i_d, cuota=cuota, amort_rows=rows,
                    intereses=inte, amort=amo, tax_i=tax_i, fci=fci, de=de, beta_l=beta_l, ke_l=ke_l, wacc=wacc,
                    ind=indicators(fci, ke_l), ind_wacc=indicators(fc, wacc))

    # ---------- punto de equilibrio (año de régimen: año 5 y año 10)
    pe = {}
    for t in (5, N):
        precio_anual = pn * 12 * pidx(t)
        var_u = (spp * c_sens_u + P['visitas_por_predio'] * P['visita_2026'] * idx[2027]
                 + P['msg_predio_mes_usd'] * 12 * P['trm']) * pidx(t) + precio_anual * (P['share_asoc'] * P['comision_asoc'] + P['ica'])
        rep_nodo = P['nodos_por_predio'] * P['nodo_reposicion'] * nodo_u * pidx(t)
        mc = precio_anual - var_u - rep_nodo
        fijos = sum(C[k][t] for k in FIX_KEYS) + nomina[t] + contador[t] + dep[t] - ing_b2g[t]
        pe[t] = dict(precio=precio_anual, var_u=var_u, rep_nodo=rep_nodo, mc=mc, fijos=fijos, predios=fijos / mc,
                     ingreso_pe=fijos / mc * precio_anual, activos=active[t], avg=avg[t])
    r['pe'] = pe
    return r


def run_all():
    base = build(BASE); tmar = base['tasa']['tmar']
    out = dict(base=base)
    pes = copy.deepcopy(BASE); pes.update(techo_adop=0.16, precio_mes_2027=62_000, churn=0.14, sensor_mat_2026=3_000,
                                          b2g_contracts={1: 0, 2: 0, **{t: 1 for t in range(3, N + 1)}})
    opt = copy.deepcopy(BASE); opt.update(techo_adop=0.28, precio_mes_2027=75_000, churn=0.07,
                                          b2g_contracts={1: 1, 2: 2, **{t: 3 for t in range(3, N + 1)}})
    sc = {}
    for k, P in [('pesimista', pes), ('base', BASE), ('optimista', opt)]:
        rr = build(P)
        sc[k] = dict(ind=indicators(rr['fc'], tmar), fc=rr['fc'], active=rr['mercado']['active'],
                     ingresos=rr['pyg']['ingresos'], techo=P['techo_adop'], precio=P['precio_mes_2027'],
                     churn=P['churn'], sensor=P['sensor_mat_2026'], b2g=P['b2g_contracts'][5])
    out['escenarios'] = sc
    sens = []
    def var(label, f):
        res = {}
        for d in (-0.2, -0.1, 0.1, 0.2):
            P = copy.deepcopy(BASE); f(P, 1 + d); rr = build(P)
            ind = indicators(rr['fc'], tmar)
            res[str(d)] = dict(vpn=ind['vpn'], tir=ind['tir'])
        sens.append(dict(var=label, res=res))
    var("Precio de la suscripción", lambda P, k: P.update(precio_mes_2027=BASE['precio_mes_2027'] * k))
    var("Demanda (techo de adopción del mercado)", lambda P, k: P.update(techo_adop=BASE['techo_adop'] * k))
    var("Costo de materiales del sensor de papel", lambda P, k: P.update(sensor_mat_2026=BASE['sensor_mat_2026'] * k))
    var("Costo por visita de campo", lambda P, k: P.update(visita_2026=BASE['visita_2026'] * k))
    var("Inversión en hardware importado (TRM y factor de importación)", lambda P, k: P.update(import_factor=BASE['import_factor'] * k))
    var("Nivel salarial", lambda P, k: P.update(smmlv_2027_inc=(1 + BASE['smmlv_2027_inc']) * k - 1))
    var("Tasa de abandono (churn)", lambda P, k: P.update(churn=BASE['churn'] * k))
    out['sens'] = sens
    alts = {}
    A = copy.deepcopy(BASE); A.update(inst_predios={t: 0 for t in range(N + 1)}, b2g_contracts={t: 0 for t in range(1, N + 1)})
    Cc = copy.deepcopy(BASE); Cc.update(precio_mes_2027=78_000)
    for k, P in [('A', A), ('B', BASE), ('C', Cc)]:
        rr = build(P)
        alts[k] = dict(ind=indicators(rr['fc'], tmar), fc=rr['fc'], fca=rr['fca'], ingresos=rr['pyg']['ingresos'],
                       ind_inv=rr['fin']['ind'], fci=rr['fin']['fci'], ke_l=rr['fin']['ke_l'],
                       maxdef=min(rr['fca']))
    out['alts'] = alts
    def solve(key, lo, hi, scale=1):
        for _ in range(60):
            mid = (lo + hi) / 2; P = copy.deepcopy(BASE); P[key] = mid
            v = indicators(build(P)['fc'], tmar)['vpn']
            if v > 0: hi = mid
            else: lo = mid
        return hi
    out['precio_vpn0'] = solve('precio_mes_2027', 10_000, 200_000)
    out['techo_vpn0'] = solve('techo_adop', 0.01, 0.9)
    P = copy.deepcopy(BASE); P['tax_rate'] = 0.32
    out['vpn_tax32'] = indicators(build(P)['fc'], tmar)['vpn']
    P = copy.deepcopy(BASE); P['carga_prest'] = 0.3835 + 0.06
    out['vpn_rescate_nomina'] = indicators(build(P)['fc'], tmar)['vpn']
    # tasas alternativas
    out['vpn_tasas'] = {f"{x:.2f}": npv(x, base['fc']) for x in (0.09, 0.12, 0.15, tmar, 0.25, 0.30)}
    return out


if __name__ == '__main__':
    out = run_all(); b = out['base']; m = b['mercado']
    f = lambda x: f"{x/1e6:,.1f}"
    print('TAM', round(m['tam']), 'SAM', round(m['sam']), 'm', round(m['m']))
    print('new', [round(x) for x in m['new']]); print('active', [round(x) for x in m['active']]); print('avg', [round(x) for x in m['avg']])
    print('nodo', b['nodo_2026'], round(b['nodo_u']), 'gw', round(b['gw_u']), 'tec', b['tecnicos'])
    for k in ['ingresos', 'costos_op', 'ebitda', 'ebit', 'tax', 'inv_t']:
        print(k, [f(x) for x in b['pyg'][k]])
    print('nomina', [f(x) for x in b['nomina']])
    print('kt', [f(x) for x in b['kt']['inv']], 'VL', f(b['vl_final']))
    print('FC', [f(x) for x in b['fc']]); print('FCA', [f(x) for x in b['fca']])
    print('tasa', {k: round(v, 4) for k, v in b['tasa'].items()})
    print('IND', b['ind'])
    fi = b['fin']; print('inv0', f(fi['inv0']), 'fondo', f(fi['fondo']), 'deuda', f(fi['deuda']), 'aporte', f(fi['aporte']), 'ke_l', round(fi['ke_l'], 4), 'wacc', round(fi['wacc'], 4))
    print('FCI', [f(x) for x in fi['fci']], fi['ind'])
    for t, v in b['pe'].items(): print('PE', t, {k: round(x) for k, x in v.items()})
    for k, v in out['escenarios'].items(): print(k, {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v['ind'].items()})
    for s in out['sens']: print(s['var'], {k: f(v['vpn']) for k, v in s['res'].items()})
    print('precio0', round(out['precio_vpn0']), 'techo0', round(out['techo_vpn0'], 4), 'tax32', f(out['vpn_tax32']), 'nom', f(out['vpn_rescate_nomina']))
    print('vpn_tasas', {k: f(v) for k, v in out['vpn_tasas'].items()})
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else 'model_out.json', 'w', encoding='utf8'), ensure_ascii=False, default=float)
