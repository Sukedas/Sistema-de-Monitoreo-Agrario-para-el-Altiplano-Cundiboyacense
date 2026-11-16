# Insumos macrofinancieros verificados para la evaluación financiera
**Proyecto:** servicio de monitoreo agroclimático con sensores de papel biodegradables (Boyacá / Cundinamarca)
**Fecha de corte de la investigación:** 15 de noviembre de 2026
**Regla aplicada:** cada cifra proviene de una página abierta durante la búsqueda. Si no se encontró, se indica **NO ENCONTRADO** y se da el mejor sustituto con su fuente. Las cifras marcadas como *(cálculo propio)* son operaciones aritméticas sobre datos citados, no datos de la fuente.

> **Advertencia de contexto (nov. 2026):** el entorno macro de 2026 es atípico frente a lo que suele traer la literatura de formulación de proyectos: inflación de 6,30 % (oct. 2026), tasa BanRep 12,25 %, SMMLV +23 %, S&P rebajó a Colombia a BB- y está en trámite un proyecto de reforma tributaria ("Ley de Rescate Económico", radicado el 29-oct-2026) que, si se aprueba, cambia la tarifa de renta y la exoneración de aportes desde 2027. Se recomienda modelar escenarios.

---

## 1. Salario mínimo, auxilio de transporte y UVT

| Concepto | Valor | Norma / fecha | Fuente |
|---|---|---|---|
| SMMLV 2026 | **$1.750.905** | Decreto 1469 del 29-dic-2025 (vigente desde 1-ene-2026) | Muñoz Paredes (2026) |
| Auxilio de transporte 2026 | **$249.095** | Decreto 1470 del 29-dic-2025 | Muñoz Paredes (2026) |
| SMMLV 2025 | **$1.423.500** | — | Muñoz Paredes (2026); Colorado (2026) |
| Auxilio de transporte 2025 | **$200.000** | — | Muñoz Paredes (2026) |
| Incremento SMMLV 2026 | **23 %** (+$327.405) | — | Muñoz Paredes (2026); Colorado (2026) |
| Incremento auxilio 2026 | **24,5 %** | — | Muñoz Paredes (2026) |
| Tope para recibir auxilio (2 SMMLV) | **$3.501.810** | — | Murcia (2026) |
| UVT 2026 | **$52.374** | Resolución DIAN 000238 del 15-dic-2025 | Actualícese (2025a) |
| UVT 2025 | **$49.799** | — | Actualícese (2025a) |

**Citas cortas:**
- "El salario mínimo legal mensual (SMMLV) para 2026 se fijó en $1.750.905" … "Ambas medidas rigen a partir del 1° de enero de 2026" (Muñoz Paredes, 2026).
- UVT: "El valor de la UVT para el próximo año será de $52.374; un incremento del 5,17 % frente al valor vigente para 2025" (Actualícese, 2025a).

**Situación jurídica del SMMLV 2026 (importante):**
- El Consejo de Estado **suspendió provisionalmente** el Decreto 1469 de 2025: "se trata de una medida cautelar temporal que no prejuzga la validez definitiva del Decreto 1469 de 2025" (Quiroga Rubio, 2026, 16 de febrero).
- MinTrabajo expidió el **Decreto transitorio 0159 del 19-feb-2026**, que mantiene $1.750.905 y $249.095; "la vigencia del decreto estará sujeta al momento en el que se dicte una sentencia sobre el proceso de nulidad" (Colorado, 2026, 20 de febrero).
- Nota de consistencia: El Tiempo y La República (Murcia) reportan 23,7 %, pero 1.750.905 / 1.423.500 = 1,2300 → **23,0 %** *(cálculo propio)*; se recomienda usar 23 %.

**SMMLV 2027 (en discusión, no decretado):** propuestas reportadas al 3-nov-2026: CUT 38,5 % (→ $2.424.003); Corficolombiana 8,0 % (→ $1.890.977, con inflación esperada 6,8 % + productividad 1,2 %); Fenalco "no más de 9 %"; gremios 8,5 %–9,5 %. Primer plazo legal de concertación: 15-dic; si no hay acuerdo, el Gobierno decreta antes del 30-dic (Morales Herrera, 2026a). **Sugerencia para el modelo:** escenario base 8–10 % para 2027 *(supuesto, no dato)*.

---

## 2. Carga laboral (factor prestacional) y jornada

### 2.1 Porcentajes a cargo del empleador (Gerencie.com, modificado 28-sep-2026)

| Concepto | % sobre salario | Observación |
|---|---|---|
| Salud (empleador) | 8,5 % | **Exonerable** art. 114-1 ET (trabajadores < 10 SMMLV, empleador persona jurídica) |
| Pensión (empleador) | 12 % | — |
| ARL riesgo I | 0,522 % | Riesgo II 1,044 %; III 2,436 %; IV 4,35 %; V 6,96 % |
| Caja de compensación | 4 % | No exonerable |
| ICBF | 3 % | Exonerable art. 114-1 |
| SENA | 2 % | Exonerable art. 114-1 |
| Cesantías | 8,33 % | Base incluye auxilio de transporte |
| Intereses sobre cesantías | 1 % | 12 % anual × 8,33 % |
| Prima de servicios | 8,33 % | Base incluye auxilio de transporte |
| Vacaciones | 4,17 % | Sin auxilio de transporte |
| Dotación | sin % legal | "La dotación no tiene porcentaje" (aplica a quienes devengan hasta 2 SMMLV; 3 entregas/año, art. 230 CST — referencia normativa, no verificada en página) |

**Totales reportados por la fuente:** prestaciones 21,83 % (con vacaciones); carga total empleador exonerado **38,36 %**; sin exoneración "cerca del **51,86 %**" (Gerencie.com, 2026a).

Umbral de exoneración 2026: 10 SMMLV = **$17.509.050** *(cálculo propio: 10 × 1.750.905)*.

**Factor prestacional recomendado para el modelo (cálculo propio con los % anteriores, riesgo I):**
- Empresa exonerada (régimen ordinario, salarios < 10 SMMLV): 12 + 0,522 + 4 + 21,83 = **38,35 %** sobre salario (+ auxilio de transporte para ≤ 2 SMMLV, que a su vez carga 17,66 % de cesantías, intereses y prima).
- Empresa no exonerada: **51,85 %**.
- Ejemplo trabajador de 1 SMMLV 2026: 1.750.905 × 1,3835 + 249.095 × 1,1766 ≈ **$2.715.500/mes** de costo total (sin dotación) *(cálculo propio)*.

**Cambio propuesto (no vigente) en el proyecto de Ley de Rescate Económico (desde 1-ene-2027):** la exoneración total solo para salarios hasta 2 SMMLV (≈ $3,5 millones); entre 2 y 3 SMMLV el empleador pagaría 6 % (1 % SENA, 1 % ICBF, 4 % salud); por encima de 3 SMMLV pagaría el 13,5 % completo (Brigard Urrutia, 2026; González Vargas, 2026). Para un ingeniero de $4–6 millones esto suma +$240.000 a +$810.000/mes según el ejemplo de Brigard Urrutia (2026).

### 2.2 Jornada laboral (Ley 2101 de 2021)
- Desde el **15 de julio de 2026** la jornada máxima es **42 horas semanales**: "Desde este miércoles 15 de julio de 2026, la jornada laboral máxima en Colombia queda en 42 horas semanales" (Suárez, 2026).
- Calendario: 47 h (jul-2023), 46 h (jul-2024), 44 h (jul-2025), 42 h (jul-2026). Sin reducción del salario mensual.
- Implicación: valor hora ordinaria 2026 con 42 h/sem ≈ salario / (42 × 30/7 = 180 h) *(cálculo propio)*.

---

## 3. Salarios de referencia (COP/mes, salario base)

**Advertencia:** no se encontraron cifras específicas para Tunja/Boyacá en ninguna plataforma consultada (**NO ENCONTRADO** a nivel Tunja). Se usan promedios nacionales de Indeed Colombia (avisos de los últimos 36 meses) y, donde existe, Bogotá. Algunos promedios de Indeed están por debajo del SMMLV 2026 porque incluyen avisos de años anteriores; en el modelo, **ningún salario puede ser menor a $1.750.905**.

| Cargo | Promedio Colombia | Bogotá | n | Actualizado | Fuente |
|---|---|---|---|---|---|
| Ingeniero electrónico | $2.811.405 | no muestra | 49 | 1-oct-2026 | Indeed (2026a) |
| Ingeniero de sistemas | $2.606.418 | $2.703.123 | 124 | 28-oct-2026 | Indeed (2026b) |
| Desarrollador de software | $3.076.944 | no muestra | 399 | 5-nov-2026 | Indeed (2026c) |
| Ingeniero agrónomo | $2.846.342 | $4.762.229 (n=5) | 34 | 5-nov-2026 | Indeed (2026d) |
| Técnico agropecuario | dato no confiable ($29,7 M/mes, n=2) | $22.172.964/año (≈ $1.847.747/mes, cálculo propio) | 2 | 21-sep-2026 | Indeed (2026e) |
| Operario / auxiliar de producción | $1.419.545 (< SMMLV → usar SMMLV) | no muestra | ≈2.800 | 7-nov-2026 | Indeed (2026f) |
| Asesor / gestor comercial | $1.706.668 | $1.728.117 | ≈4.200 | 8-nov-2026 | Indeed (2026g) |
| Contador (empleado) | $2.700.349 | no muestra (Funza $3.131.629) | ≈1.200 | 6-nov-2026 | Indeed (2026h) |
| Auxiliar administrativo (proxy "administrador") | $1.672.236 | $1.675.505 | ≈1.500 | 8-nov-2026 | Indeed (2026i) |

**Rangos por seniority (software):** Michael Page, *Guía Salarial Tecnología 2026*: "los profesionales senior en desarrollo de software pueden alcanzar ingresos mensuales de hasta $23 millones" (Lorduy, 2026). No se obtuvieron rangos junior/mid verificados de Michael Page/Hays: **NO ENCONTRADO** (los rangos de blogs como JobRise o Colombia Move no se abrieron, solo aparecieron en buscador).

**OLE (recién graduados, cohorte 2022 que ingresó al mercado en 2023):** en TIC el 65,6 % gana más de 2,5 SMMLV y el 34 % más de 4 SMMLV; en Ingeniería, Industria y Construcción el 32,4 % gana más de 2,5 SMMLV; en Administración, Derecho y Finanzas el 32,4 % gana entre 1,5 y 2,5 SMMLV; Agropecuario tiende a rangos bajos (Barona, 2026). No hay cifra por programa (electrónica, agronomía) → **NO ENCONTRADO**.

**Contador por prestación de servicios:** **NO ENCONTRADO** (honorarios). Proxy: salario promedio de contador empleado $2.700.349 (Indeed, 2026h); para una startup un contador externo parcial suele pactarse como fracción de ese valor *(supuesto)*.

**Sugerencia para el modelo (Boyacá, supuesto razonado):** ingeniero electrónico/sistemas junior ≈ 1,6–1,8 SMMLV ($2,8–3,1 M); mid ≈ $4–5 M; agrónomo ≈ $2,8 M; técnico agropecuario ≈ 1,05–1,1 SMMLV; operario = 1 SMMLV; asesor comercial = 1 SMMLV + comisiones.

---

## 4. Impuestos

### 4.1 Renta personas jurídicas
- **35 %** año gravable 2026 (art. 240 ET, modificado por art. 10 Ley 2277 de 2022): "Para el año gravable 2026, la tarifa general del impuesto de renta para personas jurídicas será del 35 %" (Actualícese, 2025b).
- **Tasa mínima de tributación (TTD) 15 %:** hoy aplica a la generalidad de contribuyentes del régimen ordinario (Brigard Urrutia, 2026, p. 4).
- **Proyecto Ley de Rescate Económico (radicado 29-oct-2026, NO es ley):** renta 33 % en 2027 y 31 % desde 2028; TTD solo para multinacionales con ingresos ≥ EUR 750 millones; RUGE 20 % para nuevas inversiones (Brigard Urrutia, 2026; González Vargas, 2026). "El proyecto apenas inicia su trámite en el Congreso y su contenido puede cambiar" (Brigard Urrutia, 2026, p. 2).

### 4.2 Régimen SIMPLE (art. 908 ET, tarifa consolidada sobre ingresos brutos anuales)

| Ingresos brutos (UVT) | En pesos 2026 (cálculo propio) | Grupo 2: comercio, industria, servicios técnicos, telecomunicaciones y "demás actividades" | Grupo 3: servicios profesionales, consultoría y científicos |
|---|---|---|---|
| 0 – < 6.000 | hasta $314.244.000 | 1,6 % | 5,9 % |
| 6.000 – < 15.000 | hasta $785.610.000 | 2,0 % | 7,3 % |
| 15.000 – < 30.000 | hasta $1.571.220.000 | 3,5 % | 12 % |
| 30.000 – < 100.000 | hasta $5.237.400.000 | 4,5 % | 14,5 % |

Grupo 1 (tiendas, minimercados, peluquerías): 1,2 %–5,6 %. Grupo de expendio de comidas/transporte: 3,1 %–4,5 %. Con dos o más actividades se aplica la tarifa más alta (parágrafo 5) (Contadia, s.f.-a). La tarifa SIMPLE ya incluye el ICA consolidado municipal. La Corte Constitucional revisó el parágrafo 5 en la Sentencia C-121 de 2026 (resultado no verificado).
*Implicación:* un servicio de monitoreo agroclimático con hardware propio podría clasificarse en Grupo 2 (servicios técnicos / telecomunicaciones / demás actividades); si la DIAN lo considera consultoría profesional, Grupo 3. La DIAN señala que "prevalece la actividad realmente desarrollada sobre el código CIIU" (Concepto 016144 de 2026, solo visto en buscador).

### 4.3 IVA
- Tarifa general **19 %** (Brigard Urrutia, 2026, p. 9).
- **Computadores personales** de escritorio o portátiles de hasta 50 UVT: **excluidos** (art. 424 num. 5 ET). Tope 2026 ≈ $2.619.000 (50 × 52.374 = $2.618.700): "5. Los computadores personales de escritorio o portátiles, cuyo valor no exceda de cincuenta (50) UVT" (Gerencie.com, 2026b).
- **Hosting y computación en la nube: excluidos** (art. 476 num. 21 ET): "21. Suministro de páginas web, servidores (hosting), computación en la nube (cloud computing)"; el contribuyente debe verificar que el servicio cumpla las características esenciales de cloud computing (DIAN, Oficio 13566 de 2026, 3-ago-2026).
- **Servicio de monitoreo/datos agroclimáticos (SaaS):** no se encontró exclusión específica → **gravado al 19 %** salvo que encaje en "computación en la nube" (num. 21). Interpretación a validar con contador.
- **Sensores / dispositivos electrónicos:** no se encontró exclusión específica (**NO ENCONTRADO**) → asumir 19 %.
- **Proyecto Ley de Rescate:** pasaría a 19 % "Hosting, nube y software para contenidos digitales" (hoy excluido) al entrar en vigencia y "Computadores y celulares" (hoy excluidos) desde 2028 (Brigard Urrutia, 2026, p. 9).

### 4.4 GMF (4 × 1.000)
- Tarifa 4 por mil (art. 872 ET). Exención 2026 de 350 UVT mensuales = **$18.330.900** (Actualícese, 2025c). La deducibilidad del 50 % del GMF pagado (art. 115 ET) no se verificó en página abierta (**NO VERIFICADO**).

### 4.5 ICA Tunja
- Tarifa específica de Tunja: **NO ENCONTRADO** (no se halló el acuerdo vigente del Concejo de Tunja).
- Proxy legal: para actividades de servicios el ICA "va del 2 al 10 por mil según el artículo 33 de la ley 14 de 1983" (Gerencie.com, 2026c). Referencia comparativa: Bogotá redujo consultoría jurídica/contable de 8,66 a 8 por mil (Acuerdo 1084 de 2026; solo en buscador). **Sugerencia:** usar 7–10 por mil para servicios en el modelo y verificar con la Secretaría de Hacienda de Tunja. Si la empresa se acoge al SIMPLE, el ICA va incluido en la tarifa consolidada.

### 4.6 Retención en la fuente
- No se recopilaron tarifas 2026 verificadas (**NO ENCONTRADO**). Referencias habituales (servicios generales 4 %/6 %, honorarios 10 %/11 %) deben validarse en la tabla DIAN 2026.

### 4.7 Depreciación fiscal (art. 137 ET, tasas máximas anuales; vida útil = 1/tasa, cálculo propio)

| Activo | Tasa máx. anual | Vida útil equivalente |
|---|---|---|
| Construcciones y edificaciones | 2,22 % | 45 años |
| Acueducto, planta y redes | 2,50 % | 40 años |
| Maquinaria y equipo | 10 % | 10 años |
| Muebles y enseres | 10 % | 10 años |
| Equipo eléctrico | 10 % | 10 años |
| Flota y equipo de transporte terrestre (vehículos) | 10 % | 10 años |
| Equipo médico-científico | 12,5 % | 8 años |
| Envases, empaques y herramientas | 20 % | 5 años |
| **Equipo de computación** | **20 %** | **5 años** |
| Redes de procesamiento de datos | 20 % | 5 años |
| Equipo de comunicación | 20 % | 5 años |

Fuente: Contadia (s.f.-b). La tasa contable puede ser menor, nunca mayor que la fiscal (DIAN, Oficio 1931 de 2025, citado por la fuente).

---

## 5. Inflación

| Indicador | Valor | Fecha | Fuente |
|---|---|---|---|
| IPC Colombia 2025 (anual, dic.) | **5,10 %** | 8-ene-2026 | Pérez Godoy (2026) |
| IPC 12 meses octubre 2026 | **6,30 %** | Boletín 9-nov-2026 | DANE (2026) |
| IPC mensual oct. 2026 / año corrido | 0,20 % / 5,94 % | 9-nov-2026 | DANE (2026) |
| IPC sept. 2026 / inflación básica sin alimentos ni regulados | 6,29 % / 6,03 % | 30-oct-2026 | Banco de la República (2026b) |
| Meta BanRep | **3 %** (rango ±1 p.p.) | — | Morales Herrera (2026b); Banco de la República (2026b) |

**Proyecciones:**
- **BanRep IPM octubre 2026:** sin cifra puntual publicada en la nota; "la inflación continúe aumentando durante lo que resta de 2026", moderándose en 2027 y acercándose a 3 % en 2028 (Banco de la República, 2026a, 4 de noviembre). Pronóstico del equipo técnico para 2027: **4,8 %** (Morales Herrera, 2026b, citando las minutas de oct-2026).
- **IPM enero 2026 (antecedente):** 6,3 % fin de 2026 y 3,7 % en 2027 (Delgado Gómez, 2026a, 3 de febrero) — superado por datos posteriores.
- **Encuesta mensual de expectativas BanRep (oct-2026):** cierre 2026 **6,85 %**; diciembre 2027 **5,19 %** (Alape Gamez, 2026, 18 de octubre). Encuesta sept-2026: 5 años (ago-2031) ≈ **3,4 %** (Delgado Gómez, 2026b, 17 de septiembre).
- **FMI WEO octubre 2026 (promedio anual):** 6 % en 2026 y 5,7 % en 2027; PIB 2,2 % (2026) y 2,3 % (2027); desempleo 9 % y 10 % (Redacción Vanguardia, 2026a, 13 de octubre). 2028–2031: **NO ENCONTRADO** en página abierta.
- **BBVA Research (jun-2026):** inflación cierre 2026 ≈ 7,0 %, 2027 5,6 %; PIB 2,6 % / 2,1 %; inflación EE. UU. promedio 3,5 % (2026) y 2,4 % (2027) (BBVA Research, 2026).

**Senda sugerida para el modelo 2027–2031 (supuesto construido con las fuentes):** 2027: 5,2 %; 2028: 4,2 %; 2029: 3,7 %; 2030: 3,5 %; 2031: 3,4 %.

---

## 6. Tasas de interés

| Indicador | Valor | Fecha | Fuente |
|---|---|---|---|
| Tasa de intervención BanRep | **12,25 %** (vigente desde 1-oct-2026; mantenida 30-oct-2026, votación 4–3) | 4-nov-2026 | Banco de la República (2026a); Morales Herrera (2026b) |
| Expectativa tasa BanRep | 12,50 % a cierre de 2026; primer recorte jun-2027; ≈ 11,00 % en dic-2027 | 18-oct-2026 | Alape Gamez (2026) |
| IBR 3 meses (nominal) | **11,543 %** | 25-sep-2026 | González V. (2026) |
| DTF 90 días | **10,38 % E.A.** (semana 28-sep a 4-oct-2026) | 28-sep-2026 | González V. (2026) |
| Desaparición de la DTF | desde 1-ene-2027 el mercado migra al IBR | 17-jun-2026 | Rico Muñoz (2026) |
| Interés bancario corriente consumo y ordinario | **18,89 % E.A.** | nov-2026 | Acosta (2026) |
| **Tasa de usura consumo y ordinario** | **28,34 % E.A.** (Res. SFC 1707 de 2026, vigente 1–30 nov-2026) | 30-oct-2026 | Acosta (2026) |
| Usura productivo de mayor monto | 42,35 % E.A. (IBC 28,23 %) | nov-2026 | Acosta (2026) |
| Usura productivo rural | 33,87 % E.A. (IBC 22,58 %) | nov-2026 | Acosta (2026) |
| Usura productivo urbano | 59,87 % E.A. (IBC 39,91 %) | nov-2026 | Acosta (2026) |
| Usura popular productivo rural / urbano | 66,90 % / 88,44 % E.A. | nov-2026 | Acosta (2026) |
| TES pesos 10 años | "por encima de 13 %" (titular 21-oct-2026); TES "cercanos al 13 %" en sept-2026 | oct-2026 | La República (2026); Ruiz Clavijo (2026) |
| US Treasury 10 años | **5,10 %** | 12-nov-2026 | FRED (2026) |
| T-bond usado por Damodaran | 4,94 % | 1-nov-2026 | Damodaran (2026f) |

- IBR y DTF de noviembre 2026: **NO ENCONTRADO** (el portal de BanRep bloqueó el acceso automatizado); usar los valores de fin de septiembre como proxy.
- Rendimiento exacto del TES 2036: **NO ENCONTRADO**; proxy ≈ 13 %.
- Tasas promedio efectivamente cobradas a pymes en 2026: **NO ENCONTRADO**. Proxy: entre el IBC productivo rural (22,58 %) y el productivo de mayor monto (28,23 %) para crédito empresarial; consumo/ordinario IBC 18,89 %.

---

## 7. Tasa de cambio (COP/USD)

| Indicador | Valor | Fecha | Fuente |
|---|---|---|---|
| TRM vigente | **$3.301,91** | 13-nov-2026 | Dólar-Colombia.com (2026) |
| TRM promedio 2026 | **NO ENCONTRADO** dato oficial. Proxy: estimación promedio anual Bancolombia **$3.420** | 11-oct-2026 | Delgado Gómez (2026c) |
| Tasa de cambio "justa" según Bancolombia | ≈ $3.600 | 11-oct-2026 | Delgado Gómez (2026c) |
| BBVA Research | promedio 2026 ≈ $3.628; promedio 2027 **$3.698** | 12-jun-2026 | BBVA Research (2026) |

Nota: otras proyecciones (Citi $3.746 en 2027, BTG $3.530, Credicorp ≈ $3.600 dic-2027, Bancolombia $3.331 promedio 2027) aparecieron solo en resultados de búsqueda y no se verificaron en página abierta. **Supuesto sugerido 2027:** $3.450–3.700.

---

## 8. Tasa de descuento (CAPM / WACC)

### 8.1 Damodaran (enero 2026, con actualizaciones)
| Insumo | Valor | Fecha | Fuente |
|---|---|---|---|
| ERP madura (mature market) | **4,23 %** | 1-ene-2026 | Damodaran (2026c, 2026d) |
| T-bond EE. UU. a 1-ene-2026 | 4,18 % | 1-ene-2026 | Damodaran (2026c) |
| ERP madura actualizada | 4,20 % (jul-2026); ERP implícita S&P 500 **4,41 %** con T-bond 4,94 % (1-nov-2026) | 15-jul-2026 / nov-2026 | Damodaran (2026e, 2026f) |
| Colombia: calificación Moody's | **Baa3** | 5-ene-2026 | Damodaran (2026a) |
| Colombia: default spread | **1,87 %** | 5-ene-2026 | Damodaran (2026a) |
| Colombia: country risk premium (CRP) | **2,85 %** | 5-ene-2026 | Damodaran (2026a) |
| Colombia: ERP total | **7,08 %** | 5-ene-2026 | Damodaran (2026a) |
| S&P Colombia | rebajada de BB a **BB-** (perspectiva estable) | 8-abr-2026 | Redacción Vanguardia (2026b) |

La actualización de CRP de julio 2026 existe, pero la cifra de Colombia no se pudo extraer (**NO ENCONTRADO**); dada la rebaja de S&P, el CRP de Colombia probablemente es mayor que 2,85 % (inferencia).

**Betas por industria (EE. UU., enero 2026):**

| Industria | N.º empresas | Beta apalancada | D/E | Tasa impuesto efectiva | Beta desapalancada | Desapalancada corregida por caja |
|---|---|---|---|---|---|---|
| Electronics (General) | 114 | 0,97 | 11,01 % | 8,04 % | 0,90 | **0,94** |
| Farming/Agriculture | 35 | 1,13 | 51,85 % | 6,29 % | 0,81 | **0,85** |
| Software (System & Application) | 309 | 1,28 | 5,58 % | 5,51 % | 1,23 | **1,25** |
| Information Services | 15 | 0,92 | 33,17 % | 18,16 % | 0,74 | **0,76** |
| Computer Services | 64 | 1,09 | 25,10 % | 10,53 % | 0,92 | **0,96** |
| Semiconductor | 66 | 1,52 | 2,59 % | 5,11 % | 1,49 | 1,50 |
| Total Market | 5.994 | 0,91 | 35,17 % | 8,30 % | 0,72 | 0,76 |

Fuente: Damodaran (2026b). La tabla de betas de mercados emergentes (betaemerg.html) devolvió error 404: **NO ENCONTRADO**.

**Ejemplo ilustrativo (cálculo propio, no dato de fuente):** beta desapalancada promedio de Electronics, Farming e Information Services = (0,94 + 0,85 + 0,76)/3 ≈ 0,85; reapalancada con D/E = 0 (startup sin deuda) = 0,85. Ke (USD) = 5,10 % + 0,85 × 4,41 % + 2,85 % ≈ 11,7 %. Conversión a COP con diferencial de inflación 2027 (Colombia 5,19 % / EE. UU. 2,4 %): Ke (COP) ≈ (1,117 × 1,0519 / 1,024) − 1 ≈ **14,7 %** nominal. Muchas guías añaden prima por tamaño/startup (3–10 p.p.), de modo que una tasa de 18–25 % nominal en COP es defendible para una startup agrotech en etapa temprana (supuesto).

### 8.2 Tasa social de descuento (DNP, para MGA)
- Resolución DNP **1092 de 2022**: "Para los proyectos de inversión del sector público en general se estableció una Tasa del **9 %** efectiva anual" (DNP, 2022). Para proyectos ambientales la tasa depende del horizonte. No se encontró norma posterior que la modifique.

---

## 9. Fuentes de financiación

### 9.1 Fondo Emprender (SENA) — Acuerdo 3 de 2026 (marzo 2026, reglamento interno vigente; derogó el Acuerdo 7 de 2025)
- Capital semilla **condonable**, artículo 13 (iniciativas individuales): **hasta 42 SMMLV** (1 empleo), **56 SMMLV** (3 empleos), **70 SMMLV** (5 o más empleos). Asociativas de aprendices/egresados: 200–499 SMMLV; asociaciones campesinas: 500–1.100 SMMLV. El SMMLV que se usa es el vigente a la apertura de la convocatoria (SENA, 2026).
- En pesos 2026: 42 SMMLV = $73.538.010; 56 = $98.050.680; 70 = $122.563.350 *(cálculo propio)*.
- Condonación (art. 30–31): se cumple con empleo generado, ejecución presupuestal del 100 %, transferencia de experiencias y eventos de mercadeo (SENA, 2026).
- Convocatorias 2026: 12 convocatorias por más de $282.000 millones; abiertas desde el 2-mar-2026, con cierres entre el 6 y el 30-abr-2026 (Villamil, 2026). **Ya cerradas** a nov-2026; esperar convocatorias 2027.

### 9.2 Finagro
- **LTPS 2026 (Circular 20 de 2026, 2-abr-2026):** tasa de redescuento **IBR − 3,0 %** para pequeño y mediano productor y enfoque asociativo; IBR para gran productor; IBR − 3,5 % para cadena de valor horizontal; "Tasa de interés nominal: **No tiene techo**". Prioriza "Tecnologías de eficiencia hídrica y energética" y reducción de GEI (Finagro, 2026a). Plazo y gracia: **NO ENCONTRADO** en la infografía.
- **ICR 2026 (Circular Externa 27 de 2026, 13-abr-2026):** reconocimiento **40 %** pequeño productor de ingresos bajos; **30 %** pequeño productor; **30 %** enfoques étnico colectivo, asociativo y cadena de valor horizontal; **25 %** mediano productor. Vigente hasta el 31-dic-2026 o hasta agotar recursos (Finagro, 2026b). *Relevancia:* el ICR lo recibe el **productor** que invierte (p. ej., en tecnología/riego) con crédito Finagro; puede reducir el precio efectivo del servicio o hardware para los clientes si la inversión es un destino habilitado (verificar en el Manual de Servicios, Título 3).
- LEC 2026 específica para tecnología agropecuaria: **NO ENCONTRADO**.

### 9.3 Bancóldex
- **Línea Impacto Inclusivo 2026** (13-may-2026): cupo $100.000 millones; para empresas de mujeres o jóvenes (hasta 28 años) y adultos mayores de 50; plazo hasta 3 años en capital de trabajo y 5 años en modernización; **gracia hasta 3 meses**; montos máximos: microempresa $300 M, pyme $800 M, microfinanzas $70 M; vigente hasta 31-dic-2026. Tasa: **no publicada** en la nota (Acosta Argote, 2026).

### 9.4 iNNpulsa / MinCiencias
- Convocatoria agrotech vigente con montos: **NO ENCONTRADO** (los boletines 2026 de iNNpulsa solo muestran programas generales ya cerrados, como Aldea+).
- MinCiencias: **NO ENCONTRADO** convocatoria 2026 específica; existen beneficios tributarios CTeI vía CNBT (sin datos 2026 verificados).

### 9.5 Crédito comercial típico
- Tasas promedio efectivamente cobradas a pymes en 2026: **NO ENCONTRADO**. Proxy: IBC productivo de mayor monto 28,23 % E.A.; IBC productivo rural 22,58 %; consumo y ordinario 18,89 % (nov-2026, Acosta, 2026). Para microcrédito, el equivalente regulatorio es el "popular productivo" (IBC 44,60 % rural / 58,96 % urbano).

---

## 10. Costos de constitución de la empresa

### 10.1 Cámara de Comercio (tarifas nacionales 2026, Decreto 1074 de 2015 modificado por el Decreto 045 de 2024; aplican igual en Tunja)
| Concepto | Tarifa 2026 |
|---|---|
| Matrícula mercantil (activos hasta $78.715.000) | $24.220 + 8.477 × (activos / $1.000.000) |
| Matrícula (activos $78,7 M – $302,75 M) | $575.225 + 4.238,5 × (activos − $78.715.000)/$1.000.000 |
| Inscripción de actos y documentos (p. ej., constitución) | 6 UVB = **$73.000** |
| Inscripción de libros | 2 UVB = $24.200 |
| Matrícula de establecimiento (misma jurisdicción, activos hasta $78,7 M) | $48.400 |
| Certificado de existencia y representación legal | $12.100 |
| Certificado de matrícula | $6.100 |
| Formulario RUES | $8.500 |

Fuente: Cámara de Comercio del Huila y Confecámaras (2026). Ejemplo: SAS con activos de $50 M → matrícula ≈ $24.220 + 8.477 × 50 = **$448.070** *(cálculo propio)*. MinCIT publicó el 19-oct-2026 un proyecto de decreto para modificar estas tarifas (solo visto en buscador).

### 10.2 Impuesto de registro (departamental, Boyacá)
- Tarifa específica de Boyacá: **NO ENCONTRADO**.
- Rango legal (art. 230 Ley 223 de 1995): actos con cuantía en Cámara de Comercio **entre 0,3 % y 0,7 %** (base: capital suscrito / social); actos sin cuantía **entre 2 y 4 salarios mínimos diarios** (Gerencie.com, 2026d). **Sugerencia:** usar 0,7 % del capital suscrito como escenario conservador.

### 10.3 Honorarios
- Honorarios de abogado/contador para constitución: **NO ENCONTRADO** (sin fuente verificable). Una SAS puede constituirse por documento privado sin notaría.

---

## 11. Resumen de vacíos (NO ENCONTRADO)
1. ICA de Tunja (tarifa por mil vigente).
2. Impuesto de registro de Boyacá (tarifa exacta).
3. Salarios específicos para Tunja/Boyacá y para el técnico agropecuario (dato de Indeed no confiable).
4. Honorarios del contador por prestación de servicios.
5. IBR/DTF de noviembre de 2026 (último dato: fin de septiembre).
6. TES 2036 exacto (proxy: "por encima de 13 %").
7. TRM promedio 2026 oficial (proxy: Bancolombia $3.420).
8. CRP de Colombia de Damodaran (jul-2026) y betas de mercados emergentes.
9. FMI 2028–2031; IPM oct-2026 con cifras puntuales.
10. Convocatorias agrotech vigentes de iNNpulsa y MinCiencias; LEC Finagro de tecnología; plazos y gracia de LTPS.
11. Tasas promedio de colocación a pymes en 2026.
12. Tabla de retención en la fuente 2026.

---

## Referencias (APA 7, orden alfabético)

Acosta, J. (2026, 30 de octubre). *Créditos de consumo tendrán nuevo tope de usura en noviembre: Superfinanciera lo certificó en 28,34 % efectivo anual*. Portafolio. https://www.portafolio.co/economia/finanzas/creditos-de-consumo-tendran-nuevo-tope-de-usura-en-noviembre-superfinanciera-lo-certifico-en-28-34-efectivo-anual-505461

Acosta Argote, C. (2026, 13 de mayo). *Bancóldex lanzó una línea de crédito por $100.000 millones para emprendedores*. La República. https://www.larepublica.co/finanzas/bancoldex-lanzo-una-linea-de-credito-por-100-000-millones-para-emprendedores-4391643

Actualícese. (2025a, 17 de diciembre). *DIAN fijó el nuevo valor de la UVT para 2026*. https://actualicese.com/dian-fijo-el-nuevo-valor-de-la-uvt-para-2026/

Actualícese. (2025b, 4 de diciembre). *Tarifa general del impuesto de renta 2026 para personas jurídicas*. https://actualicese.com/tarifa-general-del-impuesto-de-renta-2026-para-personas-juridicas/

Actualícese. (2025c, 17 de diciembre). *Transacciones exentas del GMF en 2026*. https://actualicese.com/transacciones-exentas-del-gmf-en-2026/

Alape Gamez, C. D. (2026, 18 de octubre). *Expectativas de inflación que no ceden*. La República. https://www.larepublica.co/analisis/carlos-david-alape-gamez-3820864/expectativas-de-inflacion-que-no-ceden-4505502

Banco de la República. (2026a, 4 de noviembre). *Informe de Política Monetaria, octubre de 2026*. https://banrep.gov.co/es/noticias/informe-politica-monetaria-octubre-2026

Banco de la República. (2026b, 30 de octubre). *Anexo estadístico, Informe de Política Monetaria: Indicadores económicos con cifras a septiembre de 2026* [Presentación]. https://banrep.gov.co/sites/default/files/paginas/anexo-estadistico-octubre-2026.pdf

Barona, L. (2026, 6 de marzo). *Lista de las cinco carreras con salarios más altos y bajos para recién graduados en Colombia 2026*. El País. https://www.elpais.com.co/colombia/lista-de-las-cinco-carreras-con-salarios-mas-altos-y-bajos-para-recien-graduados-en-colombia-2026-esta-la-suya-0613.html

BBVA Research. (2026). *Situación Colombia. Junio 2026*. https://www.bbvaresearch.com/wp-content/uploads/2026/06/20260626_TextoSC_Junio2026.pdf

Brigard Urrutia. (2026, 30 de octubre). *Ley de Rescate Económico: lo clave de la nueva reforma tributaria* [Newsflash tributario]. https://www.bu.com.co/sites/default/files/2026-11/Newsflash_Ley_Rescate_Economico_ES.pdf

Cámara de Comercio del Huila y Confecámaras. (2026). *Tarifas vigentes 2026* [Documento PDF]. https://www.cchuila.org/wp-content/uploads/Tarifas2026CCHweb.pdf

Colorado, J. C. (2026, 20 de febrero). *MinTrabajo publicó decreto transitorio que mantiene mínimo de $1,75 millones en 2026*. La República. https://www.larepublica.co/economia/mintrabajo-publico-decreto-transitorio-que-mantiene-minimo-de-1-75-millones-en-2026-4331878

Contadia. (s.f.-a). *Artículo 908. Tarifa* [Estatuto Tributario]. Recuperado el 15 de noviembre de 2026, de https://www.contadia.com/estatuto-tributario/articulo-908-tarifa

Contadia. (s.f.-b). *Artículo 137. Limitación a la deducción por depreciación* [Estatuto Tributario]. Recuperado el 15 de noviembre de 2026, de https://www.contadia.com/estatuto-tributario/articulo-137-limitacion-a-la-deduccion-por-depreciacion

Damodaran, A. (2026a). *Country default spreads and risk premiums* [Conjunto de datos]. NYU Stern School of Business. Recuperado el 15 de noviembre de 2026, de https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html

Damodaran, A. (2026b). *Betas by sector (US)* [Conjunto de datos]. NYU Stern School of Business. Recuperado el 15 de noviembre de 2026, de https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html

Damodaran, A. (2026c, 23 de enero). *Data update 2 for 2026: Equities get tested and pass again*. Musings on Markets. https://aswathdamodaran.blogspot.com/2026/01/data-update-2-for-2026-equities-get.html

Damodaran, A. (2026d, 1 de febrero). *Data update 4 for 2026: The global perspective!* Musings on Markets. https://aswathdamodaran.blogspot.com/2026/02/data-update-4-for-2026-global.html

Damodaran, A. (2026e, 15 de julio). *Country risk: Drivers, measures and investment implications – The 2026 edition!* Musings on Markets. https://aswathdamodaran.blogspot.com/2026/07/country-risk-drivers-measures-and.html

Damodaran, A. (2026f). *Damodaran Online* [Página de inicio; ERP implícita al 1 de noviembre de 2026]. Recuperado el 15 de noviembre de 2026, de https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm

Delgado Gómez, P. (2026a, 3 de febrero). *BanRep ajusta al alza sus proyecciones de inflación y refuerza la postura restrictiva en tasas para 2026*. Valora Analitik. https://www.valoraanalitik.com/banrep-ajusta-al-alza-sus-proyecciones-de-inflacion-y-refuerza-la-postura-restrictiva-en-tasas-para-2026/

Delgado Gómez, P. (2026b, 17 de septiembre). *Proyección de inflación para cierre de 2026 en Colombia es la más alta en tres años: encuesta BanRep*. Valora Analitik. https://www.valoraanalitik.com/?p=612480

Delgado Gómez, P. (2026c, 11 de octubre). *[Proyecciones de la tasa de cambio en Colombia y estimación promedio anual de Bancolombia]*. Valora Analitik. https://www.valoraanalitik.com/?p=616778

Departamento Administrativo Nacional de Estadística. (2026, 9 de noviembre). *Boletín técnico: Índice de Precios al Consumidor (IPC), octubre 2026*. https://www.dane.gov.co/files/operaciones/IPC/oct2026/bol-IPC-oct2026.pdf

Departamento Nacional de Planeación. (2022). *Adopción de la Tasa Social de Descuento para la evaluación de proyectos de inversión* [Revista Jurídica, Edición 2]. https://dnp.gov.co/publicaciones/Revista-Juridica/Paginas/Adopción-de-la-Tasa-Social-de-Descuento-para-la-evaluación-de-proyectos-de-inversión.aspx

Dirección de Impuestos y Aduanas Nacionales. (2026, 3 de agosto). *Oficio 13566 de 2026* [Concepto]. https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_13566_2026.htm

Dólar-Colombia.com. (2026, 13 de noviembre). *Dólar TRM hoy en Colombia: 13 de noviembre de 2026*. https://www.dolar-colombia.com/2026-11-13

Federal Reserve Bank of St. Louis. (2026). *Market yield on U.S. Treasury securities at 10-year constant maturity, quoted on an investment basis (DGS10)* [Conjunto de datos]. FRED. Recuperado el 15 de noviembre de 2026, de https://fred.stlouisfed.org/series/DGS10

Finagro. (2026a, 2 de abril). *Circular No. 20 de 2026: Línea Especial de Redescuento para la Transformación Productiva y Sostenible – LTPS 2026* [Infografía]. https://www.finagro.com.co/sites/default/files/field_tst_pdf_attached/node/2026-04/Infografia_Circular20.pdf

Finagro. (2026b, 13 de abril). *Circular Externa No. 27 de 2026: Incentivo a la Capitalización Rural ICR 2026*. https://www.finagro.com.co/sites/default/files/notifications/2026-05/Circular%20Externa%20No.%2027%20de%202026.pdf

Gerencie.com. (2026a, 28 de septiembre). *Porcentajes de prestaciones sociales y seguridad social*. https://www.gerencie.com/porcentajes-prestaciones-sociales.html

Gerencie.com. (2026b, 20 de septiembre). *Computadores excluidos de IVA*. https://www.gerencie.com/computadores-excluidos-de-iva.html

Gerencie.com. (2026c, 3 de octubre). *ICA en el ejercicio de profesiones liberales*. https://www.gerencie.com/ica-en-el-ejercicio-de-profesiones-liberales.html

Gerencie.com. (2026d, 3 de octubre). *Impuesto de registro*. https://www.gerencie.com/impuesto-de-registro.html

González V., M. (2026, 28 de septiembre). *DTF sube a 10,38 %: qué significa para los CDT tras la Junta del BanRep*. Rankia. https://www.rankia.co/blog/mejores-cdts/7487546-dtf-sube-10-38-cdt-junta-banrep

González Vargas, J. A. (2026, 30 de octubre). *Empresas pagarían menos impuesto de renta pero más costos de nómina con el proyecto de la Ley de Rescate*. Portafolio. https://www.portafolio.co/economia/impuestos/empresas-pagarian-menos-impuesto-de-renta-pero-mas-costos-de-nomina-con-el-proyecto-de-la-ley-de-rescate-505425

Indeed. (2026a). *Sueldo de ingeniero/a electrónico/a en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/ingeniero-electronico/salaries

Indeed. (2026b). *Sueldo de ingeniero/a en sistemas en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/ingeniero-de-sistemas/salaries

Indeed. (2026c). *Sueldo de desarrollador/a de software en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/desarrollador-de-software/salaries

Indeed. (2026d). *Sueldo de ingeniero agrónomo en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/ingeniero-agronomo/salaries

Indeed. (2026e). *Sueldo de técnico/a agropecuario/a en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/tecnico-agropecuario/salaries

Indeed. (2026f). *Sueldo de operario/a de producción en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/auxiliar-de-produccion/salaries

Indeed. (2026g). *Sueldo de gestor/a comercial en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/asesor-comercial/salaries

Indeed. (2026h). *Sueldo de contable en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/contador/salaries

Indeed. (2026i). *Sueldo de auxiliar administrativo/a en Colombia*. Recuperado el 15 de noviembre de 2026, de https://co.indeed.com/career/administrador/salaries

La República. (2026). *TES* [Sección de noticias]. Recuperado el 15 de noviembre de 2026, de https://www.larepublica.co/tes

Lorduy, J. (2026, 14 de abril). *Salarios en tecnología en Colombia 2026: cuánto ganan perfiles en inteligencia artificial, datos y software*. Portafolio. https://www.portafolio.co/tecnologia/salarios-en-tecnologia-en-colombia-2026-cuanto-ganan-perfiles-en-inteligencia-artificial-datos-y-software-491946

Morales Herrera, N. C. (2026a, 3 de noviembre). *Aumento del salario mínimo en Colombia para 2027: las propuestas de ajuste van desde el 8 % al 38,5 %*. Portafolio. https://www.portafolio.co/economia/aumento-del-salario-minimo-2027-propuestas-van-del-8-al-38-505643

Morales Herrera, N. C. (2026b, 5 de noviembre). *Banco de la República mantiene la tasa en 12,25 % con voto dividido*. Portafolio. https://www.portafolio.co/economia/banco-de-la-republica-mantiene-la-tasa-en-12-25-con-voto-dividido-505819

Muñoz Paredes, C. F. (2026, 3 de enero). *Aumento del salario mínimo en Colombia 2026: esto es lo que debe saber – decretos 1469 y 1470 de 2025*. Consultorsalud. https://consultorsalud.com/aumento-del-salario-minimo-en-colombia-2026/

Murcia, J. D. (2026, 20 de febrero). *Todo lo que debe saber sobre el salario mínimo de 2026 que decretó el Gobierno*. La República. https://www.larepublica.co/economia/todo-lo-que-debe-saber-sobre-el-salario-minimo-de-2026-que-decreto-el-gobierno-4331996

Pérez Godoy, M. C. (2026, 8 de enero). *Inflación en Colombia cerró el 2025 en 5,10 %: cifra fue menor a la de 2024*. Valora Analitik. https://www.valoraanalitik.com/inflacion-en-colombia-en-2025/

Quiroga Rubio, L. (2026, 16 de febrero). *Salario mínimo 2026: diez preguntas y respuestas para entender la suspensión del decreto y su impacto en los trabajadores*. El Tiempo. https://www.eltiempo.com/economia/sectores/salario-minimo-2026-diez-preguntas-y-respuestas-para-entender-la-suspension-del-decreto-y-su-impacto-en-los-trabajadores-3532351

Redacción Vanguardia. (2026a, 13 de octubre). *FMI: economía colombiana crecerá lento, inflación y desempleo preocupan*. Vanguardia. https://www.vanguardia.com/economia/2026/10/13/fmi-economia-colombiana-crecera-lento-inflacion-y-desempleo-preocupan/

Redacción Vanguardia. (2026b, 8 de abril). *S&P rebajó calificación de Colombia a BB- por su situación fiscal*. Vanguardia. https://www.vanguardia.com/economia/2026/04/08/sp-rebajo-calificacion-de-colombia-a-bb-por-su-situacion-fiscal/

Rico Muñoz, A. (2026, 17 de junio). *Qué significa el fin de la DTF y por qué el IBR la reemplazará desde 2027*. La República. https://www.larepublica.co/finanzas/que-significa-el-fin-de-la-dtf-y-por-que-el-ibr-la-reemplazara-desde-2027-4416769

Ruiz Clavijo, L. J. (2026, 9 de octubre). *Los TES en pesos regresaron a tasas cercanas al 13 % y abrieron oportunidades de compra para bancos y extranjeros*. Portafolio. https://www.portafolio.co/economia/los-tes-en-pesos-regresaron-a-tasas-cercanas-al-13-y-abrieron-oportunidades-de-compra-para-bancos-y-extranjeros-504170

Servicio Nacional de Aprendizaje. (2026). *Acuerdo 3 de 2026, por el cual se establece el Reglamento Interno del Fondo Emprender*. Normograma. https://normograma.com/keralty/compilacion/docs/acuerdo_sena_0003_2026.htm

Suárez, M. C. (2026, 15 de julio). *A quiénes sí y a quiénes no les aplica la reducción de la jornada laboral desde hoy en Colombia*. Bloomberg Línea. https://www.bloomberglinea.com/latinoamerica/colombia/a-quienes-si-y-a-quienes-no-les-aplica-la-reduccion-de-la-jornada-laboral-desde-hoy-en-colombia/

Villamil, M. (2026, 17 de marzo). *Más de $282.000 millones para emprendedores: SENA abre 12 convocatorias en Colombia con capital semilla*. Infobae. https://www.infobae.com/colombia/2026/03/17/mas-de-282000-millones-para-emprendedores-sena-abre-12-convocatorias-en-colombia-con-capital-semilla/

---
*Notas sobre las referencias:* (1) Los títulos de Gerencie.com (2026a), Rankia y Valora Analitik (2026c) se reconstruyeron a partir de la URL o del contenido, porque la página no expuso el titular exacto; verifíquelos antes de entregar. (2) Varias fechas de actualización de Gerencie y Actualícese son inconsistentes dentro de la misma página; se usó la fecha de "modificado" visible.
