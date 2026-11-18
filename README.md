# Sistema de Monitoreo Agrario para el Altiplano Cundiboyacense

**Formulación y Evaluación de Proyectos** · Universidad Distrital Francisco José de Caldas
Docente: Diego Andrés García Sánchez

Equipo: Julian David Cabrera Barragán, Andrés Felipe Carvajal Forero, Angelo Alejandro Ibáñez Hernández, Juan Felipe Chibuque López y Joan Francisco Gómez.

Guía de estudio para la sustentación: archivos del proyecto, 10 preguntas probables con su respuesta y qué leer para cada parte de la presentación.

---

## Archivos del proyecto

| Archivo | Para qué sirve |
|---|---|
| `Trabajo Final - Formulacion y Evaluacion - Monitoreo Agrario.pdf` | Documento final en APA 7, 95 páginas. Es la fuente principal de estudio. |
| `Trabajo Final - Formulacion y Evaluacion - Monitoreo Agrario.docx` | Mismo documento en Word, editable. |
| `Presentacion - Monitoreo Agrario.html` | Presentación de 25 diapositivas. Se abre en el navegador: flechas para avanzar, **F** pantalla completa, **O** vista general. |
| `Flujo de Caja - Monitoreo Agrario.xlsx` | Flujo de caja del proyecto y del inversionista con fórmulas, más la matriz de riesgos. Si se cambia un dato de la hoja **Supuestos**, todo se recalcula. |
| `modelo_financiero/` | Modelo en Python, resultados e informes de investigación con la fuente de cada cifra. |

> **Nota sobre las páginas:** los números de página citados abajo son los que aparecen impresos en la esquina superior derecha del PDF. Coinciden con el número de página que muestra el lector de PDF.

---

## Cifras clave para memorizar

| Concepto | Valor |
|---|---|
| Área de papa en los 16 municipios objetivo (2025) | 61.353 ha |
| Mercado total / disponible / potencial de adopción | 31.865 / 18.131 / 3.989 predios |
| Predios monitoreados 2028 → 2032 → 2037 | 143 → 1.486 → 2.562 |
| Precio del Plan Predio (2027) | $72.000 al mes (alternativa recomendada: $78.000) |
| Costo de materiales por sensor | ≈ $1.800 |
| Inversión inicial (año 0) | $387,8 millones |
| Déficit acumulado máximo (2030) | $1.342,5 millones |
| TMAR del proyecto | 19,58 % |
| Caso base: VPN / TIR / B/C | −$167,6 M / 16,9 % / 0,85 |
| Alternativa C ($78.000): VPN / TIR | +$72,1 M / 20,7 % |
| Inversionista (caso base): VPN / TIR / costo del capital propio | −$72,0 M / 19,0 % / 20,38 % |
| Decisión | Ajustar y ejecutar por etapas |

---

## 10 preguntas y respuestas

### 1. ¿Qué problema resuelve el proyecto y cómo se demuestra que existe?

Los pequeños y medianos productores de papa, hortalizas y leche del Altiplano Cundiboyacense deciden cuándo sembrar, regar y proteger sus cultivos de las heladas sin información medida en su propia parcela. Solo tienen boletines climáticos mensuales y regionales, casi no reciben asistencia técnica y están muy expuestos a eventos climáticos.

El documento lo sustenta con cifras de fuentes oficiales y de prensa:
- **Producción:** en 2025 se sembraron 115.941 ha de papa entre Boyacá y Cundinamarca, y 61.353 ha en los 16 municipios objetivo (UPRA, 2026).
- **Heladas:** las de 2020 afectaron más de 43.000 ha y a más de 12.000 productores en 59 municipios de Boyacá (El Tiempo, 2020). Para 2024 la prensa reportó 94.111 ha afectadas (Boyacá Sie7e Días, 2026).
- **Asistencia técnica:** solo el 4,3 % de las unidades productivas de Boyacá y el 9,1 % de las de Cundinamarca recibieron asistencia técnica según el censo agropecuario (DANE). Hoy solo el 22 % de los productores del país la recibe de forma permanente.
- **Costos:** producir una hectárea de papa cuesta entre $24,8 millones (UPRA, Centro Boyacá, 2023) y $35–38 millones (estimaciones nacionales de 2025–2026). Además, la papa sufre daño crítico entre −1 °C y −2 °C (FAO).

La pregunta problema es si es viable una empresa que ofrezca monitoreo agroclimático de bajo costo a escala de predio con sensores de papel biodegradables.

### 2. ¿En qué consiste la solución y cuál es el papel del sensor de papel?

Es un **servicio por suscripción**: el productor no compra equipos. Tiene cuatro componentes:
1. **Sensores de papel biodegradables.** Se imprimen por serigrafía con tinta de carbono sobre papel de celulosa y se encapsulan con cera de abejas. Miden la humedad y la temperatura del suelo y, al terminar su vida útil, se degradan en el suelo.
2. **Nodo lector reutilizable**, entregado en comodato. Usa un microcontrolador ESP32 con radio LoRa de 915 MHz, mide la temperatura del aire para detectar heladas y funciona con panel solar.
3. **Red LoRaWAN** de 16 gateways con salida 4G, en la banda de uso libre de 915–928 MHz con el plan de canales AU915.
4. **Plataforma en la nube** que envía alertas por WhatsApp o SMS en tres niveles: prealerta a +1 °C, alerta a 0 °C y alerta crítica a −2 °C.

El sensor de papel es el elemento diferenciador porque es un consumible barato, de unos $1.800 en materiales, que se cambia tres veces al año. La evidencia científica muestra que dura 113 días en campo (Zaccarin et al., 2025).

### 3. ¿Cómo se calculó el tamaño del mercado (TAM, SAM y potencial de adopción)?

No hay un censo reciente de productores por municipio, así que el mercado se estimó con supuestos explícitos:
- **Mercado total (TAM) = 31.865 predios.** Se sumaron los productores de papa estimados (61.353 ha ÷ 3 ha por productor = 20.451) y el 60 % de las 19.023 fincas bovinas del censo del ICA de 2026. El otro 40 % se descontó por traslape, es decir, fincas que también siembran papa.
- **Mercado disponible (SAM) = 18.131.** Es el TAM por el 56,9 % de hogares rurales con internet (DANE, 2025).
- **Potencial de adopción (m) = 3.989.** Es el SAM por el 22 % de productores con asistencia técnica permanente. Ese porcentaje se usó como techo de adopción.

### 4. ¿Por qué se usó el modelo de Bass y qué resultados dio?

Porque el servicio es nuevo y no tiene historial de ventas, así que no se puede proyectar con series de tiempo. El modelo de Bass es un modelo para innovaciones que separa dos tipos de adopción:
- La **innovación** (p = 0,03): adopción por promoción y asistencia técnica.
- La **imitación** (q = 0,38): adopción porque los vecinos ya lo usan.

Ambos coeficientes son promedios de un metaanálisis (Sultan et al., 1990). Se le sumaron los convenios institucionales, de 150 a 350 predios por año, y un abandono del 10 % anual.

**Resultado:** los predios monitoreados pasan de 143 en 2028 a 1.486 en 2032 y a 2.562 en 2037. Los ingresos crecen de $89,7 M a $3.003 M.

Como complemento, una regresión lineal del área de papa entre 2019 y 2025 dio un crecimiento de 989 ha por año, con R² = 0,575 y un error de validación (MAPE) del 0,48 %. Por eso el mercado total se dejó constante, que es lo conservador.

### 5. ¿Por qué se eligió Tunja y cómo se dimensionó la capacidad?

**Localización.** En una matriz de factores ponderados, Tunja obtuvo 8,30 puntos, frente a 6,85 de Duitama y 6,45 de Zipaquirá. Las razones:
- Está en el centro de la zona papera: Villapinzón queda a 51 km y Duitama a 57 km.
- El arriendo es más barato: $13.333 a $22.000 por m² al mes, frente a $28.077 en Bogotá.
- Tiene talento disponible en la UPTC.
- Está cerca de la Gobernación y de Fedepapa.

**Capacidad.** Se analizaron tres frentes:
- **Laboratorio:** el cuello de botella es el encapsulado manual, de 60 sensores por hora. La capacidad efectiva es de unos 90.700 sensores al año y la utilización queda por debajo del 20 %, porque los equipos más pequeños que existen ya superan la demanda.
- **Campo:** cada técnico hace 8 visitas al día durante 200 días al año. Los técnicos pasan de 1 a 5 a lo largo del horizonte.
- **Red:** el despliegue se hace por etapas: 8 gateways en 2027, 4 en 2029 y 4 en 2030.

### 6. ¿Cuánto se invierte, cómo se financia y por qué se necesita más dinero del que dice la inversión inicial?

**Inversión inicial: $387,8 millones** en el segundo semestre de 2027. Incluye activos fijos (laboratorio, cómputo, gateways y nodos del piloto), intangibles (desarrollo de la plataforma y marca), gastos preoperativos y $79 millones de capital de trabajo.

**Financiación del año 0:**

| Fuente | Monto | Participación |
|---|---|---|
| Capital semilla del Fondo Emprender (70 SMMLV) | $133,6 M | 34 % |
| Crédito al 22,58 % E. A. a 5 años | $96,9 M | 25 % |
| Aportes de los socios | $157,2 M | 41 % |

El capital de trabajo se calculó con el método del periodo de desfase (60 días). Ese método no muestra las pérdidas operativas de los primeros años. El flujo acumulado del proyecto llega a **−$1.342,5 millones en 2030**, unas 3,5 veces la inversión inicial. Por eso los socios deben conseguir una ronda de capital semilla adicional para cubrir el arranque.

### 7. ¿Cómo se determinó la tasa de descuento (TMAR)?

Con el modelo CAPM ajustado por riesgo país, con datos de Damodaran (2026):

1. **Costo del capital en dólares:** Ke = rf + β × PRM + PRP = 5,10 % + 0,85 × 4,23 % + 2,85 % = **11,55 %**.
   - rf (tasa libre de riesgo): bono del Tesoro de EE. UU. a 10 años, 5,10 %.
   - β: beta desapalancada de 0,85, promedio de los sectores de electrónica, agricultura y servicios de información.
   - PRM: prima de mercado de 4,23 %.
   - PRP: prima de riesgo país de Colombia, 2,85 %.
2. **Conversión a pesos:** se ajusta por el diferencial de inflación esperada (5,19 % en Colombia y 2,4 % en EE. UU.), lo que da **14,58 %**.
3. **Prima por tamaño y etapa temprana:** se suman 5 puntos, lo que da una **TMAR de 19,58 %** nominal en pesos.

Para el inversionista, la beta se ajusta por la deuda: una relación deuda/capital de 0,33 da una beta de 1,03 y un costo del capital propio de **20,38 %**. El costo promedio ponderado de capital (WACC) es de 18,96 %.

### 8. ¿Cuáles son los resultados de la evaluación financiera y qué significan?

**Caso base (precio de $72.000):**
- VPN de **−$167,6 M**.
- TIR de **16,9 %**, menor que la TMAR de 19,58 %.
- TIR modificada de 17,6 % y relación beneficio-costo de 0,85.
- Recuperación simple en 7,8 años; la recuperación descontada no ocurre dentro del horizonte.
- **Flujo del inversionista:** VPN de −$72,0 M y TIR de 19,0 %, frente a un costo del capital propio de 20,38 %.

**Cronología del negocio:** el EBITDA es positivo desde 2030, el flujo neto desde 2031, el flujo acumulado desde 2035, y el impuesto de renta se paga desde 2033 gracias a la compensación de pérdidas fiscales.

**Interpretación:** el negocio sí genera caja, pero tarda en compensar las pérdidas del arranque. Por eso el caso base es **marginal**: crea valor a tasas menores (VPN de +$140,5 M al 15 %), pero no a la exigida. Con un precio de $78.000 (alternativa C), el VPN es de +$72,1 M y la TIR de 20,7 %.

**Punto de equilibrio en 2032:** 1.030 predios, frente a 1.332 proyectados.

### 9. ¿Cuáles son los riesgos y variables más críticos del proyecto?

La **matriz de riesgos** usa la escala de la matriz SGC-MT-002 (probabilidad × impacto, de 1 a 5 cada uno). Los riesgos altos son:
- R1, disposición a pagar menor que el precio (nivel 16).
- R10, falta de capital para el arranque (15).
- R2, adopción lenta (12).
- R3, convenios no firmados (12).
- R8, alza del costo laboral (12).

La **sensibilidad** se midió moviendo cada variable ±20 %:
- **Precio:** el VPN va de −$759,6 M a +$399,5 M.
- **Adopción:** el VPN va de −$462,2 M a +$91,9 M.
- **Nivel salarial:** el VPN va de +$101,7 M a −$386,6 M.
- El costo del sensor de papel casi no mueve el resultado: el diferenciador no es la fuente de riesgo económico.

**Valores críticos** con los que el VPN es cero: precio de $76.194 o techo de adopción de 25,1 %.

**Escenarios:**

| Escenario | VPN | TIR |
|---|---|---|
| Pesimista | −$1.202 M | — |
| Base | −$167,6 M | 16,9 % |
| Optimista | +$608 M | 28,5 % |

### 10. ¿Cuál es la decisión final y bajo qué condiciones?

**Ajustar y ejecutar por etapas.** No se recomienda ejecutar el caso base tal como está, porque no remunera el capital a la TMAR. Se recomienda la **alternativa C** (modelo híbrido con precio de $78.000), siempre que el piloto de 50 predios en 2027 cumpla tres condiciones:
1. Una vida útil del sensor de al menos 100 días en los suelos del altiplano.
2. Que al menos el 30 % de 150 productores encuestados acepte pagar $78.000 al mes (encuesta del Anexo A).
3. Al menos un convenio institucional firmado y la ronda de capital semilla cerrada antes de 2028.

Si no se cumplen, el proyecto se aplaza y se reformula. También se comparó la alternativa A, de venta solo directa y sin convenios, y destruye valor: VPN de −$836 M.

---

## Guía de estudio por apartado de la presentación

### 01 · Problema

| | |
|---|---|
| **Qué estudiar** | Contexto agrícola del altiplano, cifras de heladas, baja asistencia técnica, costos de producción de la papa, brecha de conectividad y pregunta problema. Diferenciar el problema de la solución: el enunciado lo exige. |
| **PDF** | Resumen ejecutivo (p. 10); 1.3 Planteamiento del problema (pp. 12–14); 1.4 Justificación en sus seis dimensiones (pp. 14–15); 2.2 Necesidad del mercado (p. 19). |
| **Presentación** | Diapositivas 3 y 4. |
| **Pregunta clave** | ¿Por qué un boletín agroclimático mensual no resuelve el problema? |

### 02 · Solución

| | |
|---|---|
| **Qué estudiar** | Componentes del sistema (sensor, nodo, gateway, plataforma, alerta), cómo funciona el sensor de papel, evidencia científica, umbrales de helada, propuesta de valor y diferencias con las alternativas. |
| **PDF** | 1.2 Descripción de la idea (pp. 11–12); 1.8 Producto o servicio (p. 17); 1.9 Propuesta de valor y Tabla 1 (pp. 17–18); 4.2 Descripción técnica y Tabla 9 (pp. 32–33); 2.7 Competidores y Tabla 5 (pp. 22–23). |
| **Presentación** | Diapositivas 5, 6 y 7. |
| **Pregunta clave** | ¿Qué gana el productor frente a comprar un sensor Watermark o una estación Davis? |

### 03 · Mercado

| | |
|---|---|
| **Qué estudiar** | Segmentación; cálculo del mercado total, disponible y potencial (y sus supuestos); análisis de precios; modelo de negocio; regresión lineal; modelo de Bass (fórmula y parámetros); convenios institucionales; validación por MAPE. |
| **PDF** | Capítulo 2 completo (pp. 19–25), en especial 2.5 con las Tablas 3 y 4 (pp. 20–21) y 2.9 Precios (pp. 23–24). Capítulo 3 completo (pp. 26–31): 3.5 Selección de la técnica (p. 27), 3.6 Aplicación con la Figura 1 (pp. 27–28), Tabla 7 (p. 29), Tabla 8 (p. 30) y 3.10 Validación (p. 31). Anexo C (p. 91). |
| **Presentación** | Diapositivas 8, 9 y 10. |
| **Pregunta clave** | ¿Por qué no se usó una serie de tiempo para proyectar la demanda del servicio? |

### 04 · Estudio técnico

| | |
|---|---|
| **Qué estudiar** | Capacidad instalada, efectiva y utilización; matriz de localización; proceso en 10 pasos; equipos y lista de materiales del nodo; costo del sensor; personal y organigrama; cronograma; requisitos legales (ANE, Ley 1581, RAEE, páramos, ICA). |
| **PDF** | Capítulo 4 completo (pp. 32–41): Tabla 10 Capacidad (p. 33), Tabla 11 Localización (p. 34), Figura 3 Proceso (p. 36), Tablas 12–14 Equipos y materiales (pp. 37–38), Tabla 15 Personal (p. 38), Figura 4 Organigrama (p. 39), Figura 5 Cronograma (p. 40) y Tabla 16 Requisitos legales (p. 40). |
| **Presentación** | Diapositivas 11, 12, 13 y 22. |
| **Pregunta clave** | ¿Por qué el laboratorio tiene baja utilización y no es un problema? |

### 05 · Inversiones

| | |
|---|---|
| **Qué estudiar** | Clasificación de las inversiones (fijas, intangibles, diferidas, capital de trabajo); presupuesto del año 0; método del periodo de desfase; diferencia entre ese método y el déficit acumulado máximo; depreciación en línea recta (art. 137 ET); valor residual por el método contable; estructura de financiación. |
| **PDF** | Capítulo 5 completo (pp. 42–46): Tablas 17–20 (pp. 42–43), Tabla 21 Capital de trabajo (p. 44), 5.9 Necesidades de efectivo (p. 45), Tabla 22 Depreciación (p. 45) y Tabla 23 (p. 46). Sección 7.10 Financiación y Tabla 34 (p. 56). Anexos E y F (pp. 92–93). |
| **Excel** | Hojas Inversiones, Capital de trabajo y Financiación. |
| **Presentación** | Diapositiva 14. |
| **Pregunta clave** | ¿Por qué se necesitan $1.342 M si la inversión inicial es de $388 M? |

### 06 · Flujos y evaluación

| | |
|---|---|
| **Qué estudiar** | Supuestos financieros; costos fijos y variables; impuestos (renta del 35 % con compensación de pérdidas, ICA del 9 por mil, por qué no se eligió el régimen SIMPLE); estructura del flujo del proyecto; flujo del inversionista y su diferencia con el del proyecto; cálculo de la TMAR; VPN, TIR, TIRM, B/C, recuperación y punto de equilibrio; comparación de las alternativas A, B y C. |
| **PDF** | Capítulo 6 (pp. 47–52), en especial la Tabla 24 Supuestos (p. 47), 6.10 Impuestos (pp. 50–51) y la Tabla 31 Estado de resultados (p. 51). Capítulo 7 completo (pp. 53–58): Tablas 32–33 Flujo del proyecto (pp. 54–55), Tablas 35–36 Flujo del inversionista (p. 57) y 7.12 Diferencias (p. 57). Capítulo 8 completo (pp. 59–63): Tabla 38 Tasa de descuento (p. 59), 8.4–8.8 Indicadores (pp. 60–61) y Tabla 40 Alternativas (p. 62). Anexo I (pp. 94–95). |
| **Excel** | Hojas Flujo Proyecto, Flujo Inversionista y Resumen. Ejercicio recomendado: cambiar el precio en Supuestos a 78.000 y ver cómo cambia el VPN. |
| **Presentación** | Diapositivas 15 a 18. |
| **Pregunta clave** | ¿Por qué la TIR es de 16,9 % y aun así el proyecto no se acepta? |

### 07 · Riesgos

| | |
|---|---|
| **Qué estudiar** | Escala de la matriz SGC-MT-002; los 12 riesgos y su tratamiento; variables críticas; escenarios pesimista, base y optimista; sensibilidad de ±10 % y ±20 % y diagrama de tornado; valores críticos (precio de $76.194 y techo de 25,1 %); efecto de la Ley de Rescate Económico. |
| **PDF** | Capítulo 9 completo (pp. 64–68): Tabla 41 Matriz de riesgos (p. 64), 9.4 Riesgos financieros (p. 65), Tabla 42 Escenarios (p. 66), Tabla 43 Sensibilidad (pp. 66–67), Figura 9 Tornado (p. 67) y 9.9 Medidas (pp. 67–68). Anexo J (p. 95). |
| **Excel** | Hoja Matriz de Riesgos, con su mapa de calor. |
| **Presentación** | Diapositivas 19, 20 y 21. El simulador de precio de la diapositiva 19 permite mostrar la sensibilidad en vivo. |
| **Pregunta clave** | ¿Por qué el costo del sensor de papel casi no afecta la rentabilidad? |

### 08 · Decisión

| | |
|---|---|
| **Qué estudiar** | Síntesis de mercado, técnica y finanzas; criterios de aceptación; la decisión de "ajustar y ejecutar por etapas"; las tres condiciones del piloto; cumplimiento de los objetivos; limitaciones del análisis. |
| **PDF** | Capítulo 10 completo (pp. 69–71), en especial la Tabla 44 Resumen de indicadores (p. 70) y 10.8 Decisión final (p. 71). Capítulo 11 (pp. 72–73), con la Tabla 45 Cumplimiento de objetivos (p. 72) y 11.5 Limitaciones (p. 73). Anexo A Encuesta (p. 89). |
| **Presentación** | Diapositivas 23 y 24. |
| **Pregunta clave** | ¿Qué pasa si el piloto no cumple las condiciones? |

---

## Supuestos que conviene saber defender

Son decisiones del equipo, no datos oficiales. Si el jurado pregunta, hay que explicar por qué se escogieron y mostrar su efecto en la sensibilidad:
- Productor promedio con 3 ha de papa sembradas al año.
- Techo de adopción del 22 %.
- Abandono del 10 % anual.
- Convenios institucionales de 150 a 350 predios por año.
- Prima por tamaño de 5 puntos en la TMAR.
- Incremento del SMMLV del 9 % en 2027.
- TRM de $3.550 y factor de importación de 1,35.

Todos aparecen en la Tabla 24 (p. 47) y en la hoja Supuestos del Excel, con su fuente.
