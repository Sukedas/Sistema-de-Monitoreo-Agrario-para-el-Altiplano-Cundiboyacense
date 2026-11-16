# Investigación técnica, de costos, legal y de localización
## Proyecto: Sistema de Monitoreo Agrario para el Altiplano Cundiboyacense con sensores de papel biodegradables

Fecha de consulta de todas las fuentes: **15 de noviembre de 2026** (salvo que se indique otra fecha de publicación).

**Convención de verificación**

| Marca | Significado |
|---|---|
| **[V]** | Página o documento abierto y leído (WebFetch, API o PDF descargado). La cifra viene de ese texto. |
| **[S]** | Cifra vista solo en el fragmento del buscador; la página no se pudo abrir (bloqueo 403/429). Hay que confirmarla antes de citarla como definitiva. |
| **NO ENCONTRADO** | No se halló una fuente verificable. Se propone un sustituto (proxy). |

Tasas de cambio: no se fijaron. Se reportan los precios en la moneda original (USD, EUR, COP).

---

## A. Evidencia científica

### A1. Sensor capacitivo con acople inductivo impreso sobre sustrato biodegradable (Penn, 2025) [V]
- **Cifra:** funcionó en campo hasta **113 días**. Rango de lectura inalámbrica de **hasta 10 cm** en aire y en suelo seco. Respondió a la humedad a **hasta 5 cm de profundidad**. Se enterraron 5 sensores.
- **Cita:** "The sensors' ability to respond to changes in soil moisture over long periods of time (i.e. up to 113 days) is demonstrated." / "interrogation range up to 10 cm in air and dry soil".
- **Fabricación:** tinta conductora aplicada por serigrafía sobre sustrato de papel biodegradable "to minimize sensor costs". Lectura con analizador vectorial de redes (VNA).
- **Costo por unidad y exactitud:** el resumen no los reporta (NO ENCONTRADO).
- **URL:** https://iot4ag.us/?p=2264 (resumen). Metadatos tomados de Crossref: https://api.crossref.org/works?query.title=Inductively+Coupled+Capacitive+Soil+Moisture+Sensors+Printed+on+a+Biodegradable+Substrate
- **APA:** Zaccarin, A.-M., Peddada, N., Machold, M., Turner, K. T., & Olsson, R. H., III. (2025). Inductively coupled capacitive soil moisture sensors printed on a biodegradable substrate: Characterization and long-term testing. *Smart Agricultural Technology, 11*, 101052. https://doi.org/10.1016/j.atech.2025.101052

### A2. Sensores de humedad sobre sustrato celulósico (CNF) (IEEE Sensors Journal, 2024; conferencia IEEE Sensors 2022) [V]
- **Hallazgos:** los sensores capacitivos se serigrafiaron sobre "fully biodegradable paper substrate infiltrated with cellulose nanofibrils (CNFs)". Responden a la humedad del suelo y a la humedad relativa, con "fast response times in both air and soil". La calidad de las pistas es "comparable to traces printed on polyimide".
- **Degradación y costo:** el resumen no los cuantifica.
- **Nota sobre "IEEE 2023":** el artículo de revista salió en línea en 2023 (DOI jsen.2023) y en el número de marzo de 2024. La versión de conferencia es de 2022.
- **URL:** https://iot4ag.us/?p=1891 ; Crossref: https://api.crossref.org/works?query.title=Fabrication+and+Characterization+of+Soil+Moisture+Sensors+on+a+Biodegradable+Cellulose-Based+Substrate
- **APA:**
  - Zaccarin, A.-M., Iyer, G. M., Olsson, R. H., & Turner, K. T. (2024). Fabrication and characterization of soil moisture sensors on a biodegradable, cellulose-based substrate. *IEEE Sensors Journal, 24*(6), 7235–7243. https://doi.org/10.1109/JSEN.2023.3299430
  - Iyer, G. M., Zaccarin, A.-M., Olsson, R. H., & Turner, K. T. (2022). Fabrication and characterization of cellulose-based materials for biodegradable soil moisture sensors. En *2022 IEEE Sensors* (pp. 1–4). IEEE. https://doi.org/10.1109/SENSORS52175.2022.9967089

### A3. Osaka University: "sensing fertilizer" inalámbrico de nanopapel (Kasuga et al.) [V]
- **Materiales:** "nanopaper substrate, a natural wax protective coating, a carbon heater, and tin conductive lines". Se usa estaño en lugar de plata o cobre porque es menos probable que dañe las plantas.
- **Desempeño:** al pasar la humedad del suelo de 5 % a 30 %, la eficiencia de transmisión cae de ~46 % a ~3 %. La lectura se hace con cámara térmica. Demostración con **12 sensores en 0,4 m × 0,6 m**.
- **Fin de vida:** al final de la temporada el sensor se incorpora al suelo con la labranza. Los microorganismos degradan la mayor parte y el sustrato libera componentes fertilizantes. No se publica un tiempo de degradación en días.
- **Fecha:** nota de prensa del 17 oct. 2023. El artículo está en el vol. 8 (2024).
- **URL:** https://resou.osaka-u.ac.jp/en/research/2023/20231017_1 ; Crossref: https://api.crossref.org/works/10.1002/adsu.202300314
- **APA:** Kasuga, T., Mizui, A., Koga, H., & Nogi, M. (2024). Wirelessly powered sensing fertilizer for precision and sustainable agriculture. *Advanced Sustainable Systems, 8*(1), 2300314. https://doi.org/10.1002/adsu.202300314
- **Implicación regulatoria:** si el sensor se ofrece también como fuente de nutrientes, podría entrar en el régimen ICA de fertilizantes (ver C13).

### A4. TU Delft: sensor de humedad biodegradable alimentado por baterías de papel cargadas por bacterias [V]
- **Hallazgo:** se trata de una **tesis doctoral** (defensa el 24 feb. 2026), no de un artículo de revista. Propone alimentar el sensor con celdas de combustible microbianas de suelo (SMFC), con "current production being directly proportional to the soil moisture", dirigido a "smallholder farmers of developing countries".
- **Cifras de potencia, voltaje o degradación:** el resumen no las da. Habría que revisar el PDF completo de 57 MB (NO ENCONTRADO en el resumen).
- **Aclaración:** las "bacteria-powered paper batteries" más citadas en la prensa son de Binghamton University (S. Choi), no de TU Delft. No se verificaron.
- **URL:** https://repository.tudelft.nl/record/uuid:69b9f541-e7ec-41ca-a6f2-b53efb1da9d4
- **APA:** Meshram, S. M. (2026). *Design of biodegradable soil moisture sensor powered by bacteria charged paper batteries* [Tesis doctoral, Delft University of Technology]. TU Delft Repository. https://doi.org/10.4233/uuid:69b9f541-e7ec-41ca-a6f2-b53efb1da9d4

### A5. Revisión "Low-cost, off-grid, biodegradable in situ autonomous soil moisture sensing systems" (2024) [V]
- **Cita:** los sensores "may be expensive and require batteries or other energy sources". La brecha que identifica es la de "challenges in combining low-cost, off-grid, and biodegradable soil moisture sensing". La elección del sistema es un compromiso entre desempeño, factibilidad operativa y biodegradabilidad.
- **URL:** https://repository.tudelft.nl/record/uuid:96ae7bf5-9f85-4029-b99d-02375f328e47
- **APA:** Meshram, S. M. M., Adla, S., Jourdin, L., & Pande, S. (2024). Review of low-cost, off-grid, biodegradable in situ autonomous soil moisture sensing systems. *Computers and Electronics in Agriculture, 225*, 109289. https://doi.org/10.1016/j.compag.2024.109289

### A6. Nature Communications 2026: verificación [V]
- **Resultado:** el artículo existe, pero **no** trata de "cellulose sensors for precision agriculture". Es una **revisión** sobre tecnologías de impresión (inyección de tinta, serigrafía, aerosol jet, impresión 3D, escritura láser) para monitorear la salud de los cultivos. Publicado en línea el 24 ene. 2026, vol. 17. El artículo 2009 aparece en el listado del buscador [S]. El DOI está confirmado en Crossref.
- **URL:** https://api.crossref.org/works?query.title=Printing+technologies+for+monitoring+crop+health
- **APA:** Panáček, D., Kupka, V., Nalepa, M.-A., Dědek, I., Álvarez-Diduk, R., Olenik, S., Flauzino, J., Zdražil, J., Jakubec, P., Zdražil, L., Spíchal, L., Sonigara, K. K., Zbořil, R., Pumera, M., Merkoçi, A., Wang, J., De Diego, N., Güder, F., & Otyepka, M. (2026). Printing technologies for monitoring crop health. *Nature Communications, 17*, 2009. https://doi.org/10.1038/s41467-026-68778-6

### A7. Degradación controlada y encapsulado de cera (CU Boulder, 2021) [V]
- **Diseño:** "rapidly degrading substrate and electrode are encapsulated in a slowly degrading wax blend". La cera "controls degradation time". El sensor responde "predictably and stably until the encapsulation is breached" y después falla rápido. Esto da un límite claro de vida útil, pensado para durar una temporada de cultivo.
- **Cifras de días y costo:** no están en la nota del laboratorio (NO ENCONTRADO; revisar el texto completo).
- **URL:** https://www.colorado.edu/lab/whiting/2021/02/04/paper-published-acs-sustainable-chemistry-and-engineering ; Crossref: https://api.crossref.org/works/10.1021/acssuschemeng.0c07615
- **APA:** Sui, Y., Atreya, M., Dahal, S., Gopalakrishnan, A., Khosla, R., & Whiting, G. L. (2021). Controlled biodegradation of an additively fabricated capacitive soil moisture sensor. *ACS Sustainable Chemistry & Engineering, 9*(6), 2486–2495. https://doi.org/10.1021/acssuschemeng.0c07615

### A8. Sensores impresos en PHBV para actividad microbiana del suelo (2026) [V]
- **Cifras:** circuito de **carbono impreso sobre PHBV**. Lecturas **cada 30 min durante 7 semanas** bajo sequía e inundación simuladas. Los autores los describen como "extremely low-cost", sin dar una cifra.
- **URL:** https://www.lancaster.ac.uk/news/degradable-sensors-reveal-hidden-soil-secrets-by-being-nibbled-on-by-microbes (11 jun. 2026)
- **APA:** Fry, E. L., Sharpe, T. J., Atreya, M., Whiting, G. L., & Quinton, J. N. (2026). Printed PHBV-based sensors as a real-time proxy for soil microbial decomposer activity during drought and flood recovery. *European Journal of Soil Science, 77*(3), e70358. https://doi.org/10.1111/ejss.70358

### A9. Costo unitario de un sensor impreso biodegradable: proxy [V]
- **Costo de sensores de suelo de papel o celulosa:** NO ENCONTRADO en las fuentes A1–A8.
- **Proxy:** sensor electroquímico con tinta de carbono serigrafiada sobre acetato de celulosa, "each sensor costs 0.077 cents" (FAPESP, 13 may. 2026). Es otra aplicación (plaguicidas) y la cifra cubre solo materiales e impresión.
- **URL:** https://agencia.fapesp.br/biodegradable-sensors-attached-to-plants-detect-pesticides-in-three-minutes/58067
- **APA:** Teixeira, S. C., Gomes, N. O., Machado, S. A. S., de Oliveira, T. V., Soares, N. F. F., & Raymundo-Pereira, P. A. (2026). Biodegradable wearable sensors for rapid non-destructive analysis of pesticides on plants and foods. *Biosensors and Bioelectronics: X, 29*, 100758. https://doi.org/10.1016/j.biosx.2026.100758

### A10. Heladas: temperaturas críticas para la papa [V]
- **FAO, Tabla 4.5** ("critical damage temperatures", Ventskevich, 1958), papa: **germinación −2 / −3 °C; floración −1 / −2 °C; fructificación −1 / −2 °C**.
- **FAO, Tabla 4.4** (temperatura de congelación más alta): papa, cosecha temprana y tardía, **−0,8 °C**.
- **Advertencia de la fuente:** los valores de campo pueden ser algo más altos, así que deben usarse como guía y no como umbrales exactos.
- **Recomendación de diseño (análisis propio):** prealerta a **≤ +1 °C**, alerta a **≤ 0 °C** y alerta crítica a **≤ −2 °C**, medidas a la altura del dosel.
- **URL:** https://www.fao.org/4/y7223e/y7223e0a.htm
- **APA:** Snyder, R. L., & de Melo-Abreu, J. P. (2005). *Frost protection: Fundamentals, practice and economics* (Vol. 1, Environment and Natural Resources Series No. 10). Food and Agriculture Organization of the United Nations. https://www.fao.org/4/y7223e/y7223e00.htm
- **Contexto regional [S], no abierto:**
  - Circular de la Gobernación de Boyacá: las zonas a ≥ 2.500 m s. n. m. son propicias para heladas; un evento afectó 59 municipios y unas 48.000 ha. El año no es claro. https://www.boyaca.gov.co/wp-content/uploads/2020/12/324.CIRCULAR-GOB-BOYACÁ-HELADAS_V3.pdf
  - UPRA (ene. 2024): papa con 6.225 ha cultivadas y 6.156 ha vulnerables (23 % del área vulnerable). https://upra.gov.co/es-co/Documents/fenomeno_nino/20240125_Heladas-Enero-2024.pdf (devolvió 404 al abrirlo).

---

## B. Precios de equipos y materiales

### B1. Tintas conductoras
| Ítem | Precio | Fecha | Fuente | Estado |
|---|---|---|---|---|
| Pasta de carbono termoestable (140 °C, 50 Ω/sq/25 µm; curado 30–60 min) | **€47 / 100 g; €90 / 250 g** | consulta 15-nov-2026 | https://shop.nanografi.com/new-materials/carbon-paste-140-100-ohm-sqr-25-m | [V] |
| NovaCentrix HPR-059, tinta de negro de carbono base agua para serigrafía (0,7–0,9 Ω·cm, curado mín. 100 °C) | **USD 100 / 100 g** | 15-nov-2026 | https://novacentrix.com/product/hpr-059-carbon-black | [V] |
| Pasta de plata flexible para serigrafía, Sigma-Aldrich 901769 (comparación) | **USD 149 / 25 g; USD 373 / 100 g** | dato actualizado 30-abr-2026 | https://www.chemicalbook.com/Price/CB25542136.htm | [V] |

- **Lectura:** la plata cuesta unas **3,7 a 7 veces** más por gramo que el carbono. Esto respalda el diseño sin plata (y el uso de estaño, como en A3).
- **APA:**
  - Nanografi. (s. f.). *Carbon paste (140 ℃, 50 ohm/sqr/25 µm)*. Recuperado el 15 de noviembre de 2026, de https://shop.nanografi.com/new-materials/carbon-paste-140-100-ohm-sqr-25-m
  - NovaCentrix. (s. f.). *HPR-059 carbon black ink*. Recuperado el 15 de noviembre de 2026, de https://novacentrix.com/product/hpr-059-carbon-black
  - ChemicalBook. (2026). *Silver conductive ink: Price* [Lista de precios Sigma-Aldrich 901769]. Recuperado el 15 de noviembre de 2026, de https://www.chemicalbook.com/Price/CB25542136.htm

### B2. Sustratos y recubrimientos
| Ítem | Precio | Fuente | Estado |
|---|---|---|---|
| Papel filtro Whatman grado 1, 460×570 mm, 100 hojas | USD 258,30 (Sigma) / USD 254,18 (Labfilterz) | https://www.sigmaaldrich.com/US/en/product/aldrich/wha1001917 ; https://labfilterz.com/collections/whatman/products/whatman-filter-sheets-460-x-570mm-grade-1-100-pk-pn-1001-917 | [S] (429/timeout) |
| Hidrogel de nanofibra de celulosa (CNF), 1 % p/p | USD 545 / 500 mL | https://store.nanochemazone.com/product-category/nanoparticles/nanocellulose/cellulose-nanofiber/ | [S] (403) |
| Cera de abejas y goma laca (Colombia) | **NO ENCONTRADO** | Proxy: cotizar con proveedores apícolas o Fedeapicultores. Referencia internacional [S]: cera de grado farmacéutico, promedio USD 20,91/kg (12 meses a may-2026), https://pharmaoffer.com/es/api-excipient-supplier/transactions/beeswax | — |

### B3. Equipos de producción
| Ítem | Precio | Fecha | Fuente | Estado |
|---|---|---|---|---|
| Impresora manual de esténcil/serigrafía de precisión 3040 (área 250×400 mm, repetibilidad ±0,01 mm) | Página muestra "Sale price" **USD 880** y "Regular price" USD 544,88 (inconsistente) | 15-nov-2026 | https://vxb.com/products/solder-paste-printer-for-smt-pcb-stencil-printing | [V] |
| Misma clase 3040 (Walmart/eBay) | USD 314,40–354,10 | — | https://www.walmart.com/ip/15529423948 ; https://www.ebay.com/itm/135434833263 | [S] |
| Máquina de serigrafía semiautomática (Colombia) | **NO ENCONTRADO** | — | Proxy: impresora manual de precisión de esta tabla, o cotizar con distribuidores en Bogotá | — |
| Cortadora láser CO₂ 50 W VEVOR (20×12 in) | USD 1.899,90 (VEVOR) / USD 1.785,90 (Best Buy) | — | https://www.bestbuy.com/product/vevor-50w-co2-laser-engraver-20x12in-co2-laser-engraver-cutter-machine-with-4-way-pass-air-assist-engraving-cutting-machine/JJGHKKV345 | [S] (timeout) |
| Horno de secado de laboratorio 300 °C (Memmert UN30, usado, Valle del Cauca) | COP 6.000.000 | — | https://www.equipnet.com/memmert-un30-drying-oven-listid-1047493/ | [S] (403) |
| Horno nuevo, cámara climática, balanza de precisión | **NO ENCONTRADO** con precio público | — | Proxy: el horno usado de esta tabla; para lo demás, cotizar con distribuidores (VWR muestra "consulta de precio") | — |

### B4. Electrónica del nodo, sensores de referencia e instrumentos (Colombia, Electronilab, COP con IVA) [V]
Fuente: API pública de la tienda https://electronilab.co (WooCommerce Store API), consultada el 15-nov-2026.

| Ítem | Precio COP | URL |
|---|---|---|
| ESP32-S3 N16R8 DevKitC | 38.900 | https://electronilab.co/tienda/board-esp32-s3-n16r8-devkitc-ch340-wifi-bluetooth-usb-c-dual-sin-soldar/ |
| TTGO LoRa32 V2.1 ESP32 SX1276 915 MHz | 131.900 | https://electronilab.co/tienda/ttgo-lora32-v2-1-esp32-oled/ |
| TTGO T-Beam V1.2 (ESP32 + LoRa 915 + GPS) | 229.900 | https://electronilab.co/tienda/ttgo-t-beam-v1-2-esp32-wifi-bluetooth-gps-neo-6m-lora-900-mhz/ |
| Módulo LoRa E220-900T22D (868–915 MHz) | 37.500 | https://electronilab.co/tienda/modulo-transceptor-lora-e220-900t22d-868mhz-915mhz-22dbm-5km/ |
| Antena 915 MHz 3 dBi SMA | 21.900 | https://electronilab.co/tienda/antena-rf-915mhz-lora-omnidireccional-3dbi-sma/ |
| Panel solar 1,8 W 12 V 110×110 mm | 39.500 | https://electronilab.co/tienda/panel-solar-12v/ |
| Panel solar 5 V 291 mA (~1,5 W), agotado | 28.900 | https://electronilab.co/tienda/panel-solar-3w/ |
| Cargador Li-ion TP4056 USB-C | 5.500 | https://electronilab.co/tienda/modulo-cargador-bateria-de-lipo-1a-usb-c-5v-tp4056/ |
| BMS 1S 18650 | 3.900 | https://electronilab.co/tienda/modulo-bms-de-carga-y-proteccion-baterias-litio-18650-1s-2/ |
| Sensor capacitivo de humedad de suelo (referencia comercial) | 15.900 | https://electronilab.co/tienda/sensor-de-humedad-de-suelo-capacitivo-higrometro/ |
| Adafruit STEMMA, sensor capacitivo de suelo I2C | 39.900 | https://electronilab.co/tienda/adafruit-stemma-sensor-de-humedad-de-suelo-capacitivo-i2c/ |
| SHT41, temperatura y humedad del aire | 31.900 | https://electronilab.co/tienda/sht41-sensor-de-temperatura-y-humedad-sensirion/ |
| DS18B20, sonda de temperatura | 9.900 | https://electronilab.co/tienda/sensor-de-temperatura-ds18b20-tipo-sonda/ |
| Lector/grabador NFC PN532 13,56 MHz | 42.700 | https://electronilab.co/tienda/modulo-rfid-nfc-pn532-13-56mhz-lector-grabador/ |
| Etiqueta NFC industrial NTAG213 | 2.900 | https://electronilab.co/tienda/etiqueta-nfc-de-proximidad-tag-pps-industrial-rfid-13-56-mhz-ntag213/ |
| Lector NFC USB ACR1552U (agotado) | 335.300 | https://electronilab.co/tienda/acr1552u-lector-y-escritor-rfid-nfc-usb-13-56mhz/ |
| Multímetro Aneng M118A | 73.900 | https://electronilab.co/tienda/multimetro-digital-aneng-an8008-true-rms/ |
| Probador LCR-TC1 (proxy de medidor LCR) | 89.900 | https://electronilab.co/tienda/probador-multicomponentes-tester-lcr-tc1-esr/ |
| Osciloscopio USB Hantek 6022BE (agotado) | 605.900 | https://electronilab.co/tienda/osciloscopio-usb-hantek-6022be-20mhz-48msas/ |

- **APA:** Electronilab. (2026). *Catálogo de productos* [Tienda en línea]. Recuperado el 15 de noviembre de 2026, de https://electronilab.co/tienda/
- **Sin precio encontrado:** batería LiFePO4, celda 18650 suelta, caja IP65 y lector NFC portátil de mano (**NO ENCONTRADO**). Proxy para el lector portátil: PN532 + ESP32 + batería, o un teléfono Android con NFC.

### B5. Módulos LoRa/LoRaWAN, gateways y sensores comerciales (USD)
| Ítem | Precio | Fuente | Estado |
|---|---|---|---|
| Heltec WiFi LoRa 32 V4.3 (ESP32-S3 + SX1262) | **USD 17,90** | https://heltec.org/project/wifi-lora-32-v4/ | [V] (API tienda, 15-nov-2026) |
| RAK3172-9 (915 MHz), DigiKey | **USD 10,27 (1 u.); 8,917 (10 u.); 7,802 (100 u.)** | https://www.digikey.com/en/products/detail/rakwireless-technology-limited/RAK3172-9-SM-NI/17138034 | [V] |
| RAK7268V2 WisGate Edge Lite 2 (sin LTE) | USD 139 (variantes hasta USD 219) | https://store.rakwireless.com/collections/wisgate-edge/products/wisgate-edge-lite-2-rak7268-rak7268c | [S] (429) |
| RAK7268CV2 US915 con LTE (Rokland) | USD 234 | https://store.rokland.com/collections/helium-accessories/products/rak-wireless-wisgate-edge-lite-2-indoor-gateway-for-lorawan-rak7268c-us915 | [S] |
| RAK7289 WisGate Edge Pro | **NO ENCONTRADO** | Proxy: Milesight UG65 | — |
| Dragino LPS8N 915 MHz | USD 170 (Robotshop) | https://robotshop.com/products/lps8n-indoor-lorawan-gateway-915-mhz-north-america | [S] (429) |
| Milesight UG65-915M (sin celular) | USD 555 (Embedded Works) / USD 467,50 (MCCI) | https://embeddedworks.net/product/sens820 | [S] (403) |
| Milesight UG65 con 4G | USD 690 | https://embeddedworks.net/product/sens732/ | [S] |
| Dragino LSE01 US915 (sensor de suelo comercial) | USD 149,99 | https://embeddedworks.net/product/sens607 | [S] (403) |
| RAK4631 WisBlock | **NO ENCONTRADO** (429) | Proxy: Heltec V4.3 | — |

- **APA:**
  - DigiKey. (2026). *RAK3172-9-SM-NI* [Página de producto]. Recuperado el 15 de noviembre de 2026, de https://www.digikey.com/en/products/detail/rakwireless-technology-limited/RAK3172-9-SM-NI/17138034
  - Heltec Automation. (2026). *WiFi LoRa 32 (V4)*. Recuperado el 15 de noviembre de 2026, de https://heltec.org/project/wifi-lora-32-v4/

### B6. Nube, mensajería y conectividad [V]
| Servicio | Cifra | Fecha | URL |
|---|---|---|---|
| AWS Lightsail (Linux, IPv4) | **USD 12/mes** (2 GB, 2 vCPU, 60 GB SSD, 3 TB); **USD 24/mes** (4 GB, 80 GB, 4 TB); USD 7/mes (1 GB) | 15-nov-2026 | https://aws.amazon.com/lightsail/pricing/ |
| DigitalOcean Droplets Basic | USD 6/mes (1 GiB); USD 12 (2 GiB/1 vCPU); USD 24 (4 GiB/2 vCPU) | 15-nov-2026 | https://www.digitalocean.com/pricing/droplets |
| The Things Stack Cloud | **Discovery: €0**, hasta 10 dispositivos y 10 gateways. **Standard: €171/mes** (anual) para 11–1.000 dispositivos, gateways ilimitados | 15-nov-2026 | https://www.thethingsindustries.com/stack/plans/ |
| AWS IoT Core for LoRaWAN | **USD 2,30 por millón de mensajes**. MQTT: USD 1 por millón | 15-nov-2026 | https://aws.amazon.com/iot-core/pricing/ |
| ChirpStack | Software libre (sin licencia). Costo real = VPS (Lightsail o DigitalOcean) | — | Proxy |
| SMS a Colombia, Twilio | **USD 0,0592 por segmento** | 15-nov-2026 | https://www.twilio.com/en-us/sms/pricing/co |
| SMS Hablame (Colombia) | **NO ENCONTRADO**. La web no publica tarifas ("sin recargas mínimas, sin vencimiento de saldo") | 15-nov-2026 | https://www.hablame.co/ |
| WhatsApp Business (Meta), Colombia | **Marketing USD 0,0125; utility USD 0,0008; authentication USD 0,0008** por mensaje entregado. Tarifario vigente desde el 1-oct-2026 | 15-nov-2026 | https://leadsales.io/en/tools/whatsapp-api-pricing-calculator/ (cita el tarifario de Meta) |
| Modelo de cobro de Meta | Cobro por mensaje desde el **1-jul-2025**. Utility y authentication para Colombia subieron el 1-oct-2025 | 15-nov-2026 | https://developers.facebook.com/docs/whatsapp/pricing/ |
| SIM IoT en Colombia (Telnyx) | **USD 0,0625/MB + USD 1 por SIM**. Sin cargo mensual mínimo | 15-nov-2026 | https://telnyx.com/sim-cards/colombia |
| Plan M2M Claro/Movistar/Tigo | **NO ENCONTRADO** (se negocia con el área empresarial) | — | Proxy: Telnyx, o paquete prepago Claro (T&C de jun-2026; tabla mal alineada, no confiable) |
| Portátil (Colombia 2026) | **NO ENCONTRADO** (Alkosto/Ktronix no muestran precios al abrirlas) | — | Proxy: cotizar en tienda; dejar como supuesto del estudio |

- **Ejemplo de cálculo de alertas (análisis propio):** 1.000 alertas de helada al mes por WhatsApp "utility" costarían 1.000 × 0,0008 = **USD 0,80**. Por SMS Twilio costarían **USD 59,20**. WhatsApp sale unas 74 veces más barato.
- **Volumen LoRaWAN (análisis propio):** 500 nodos × 96 mensajes/día × 30 días = 1,44 millones de mensajes/mes, unos **USD 3,3/mes** en AWS IoT Core for LoRaWAN.
- **APA:**
  - Amazon Web Services. (2026a). *Amazon Lightsail pricing*. Recuperado el 15 de noviembre de 2026, de https://aws.amazon.com/lightsail/pricing/
  - Amazon Web Services. (2026b). *AWS IoT Core pricing*. Recuperado el 15 de noviembre de 2026, de https://aws.amazon.com/iot-core/pricing/
  - DigitalOcean. (2026). *Droplet pricing*. Recuperado el 15 de noviembre de 2026, de https://www.digitalocean.com/pricing/droplets
  - The Things Industries. (2026). *The Things Stack plans*. Recuperado el 15 de noviembre de 2026, de https://www.thethingsindustries.com/stack/plans/
  - Twilio. (2026). *SMS pricing in Colombia*. Recuperado el 15 de noviembre de 2026, de https://www.twilio.com/en-us/sms/pricing/co
  - Meta. (2026). *Pricing on the WhatsApp Business Platform*. Recuperado el 15 de noviembre de 2026, de https://developers.facebook.com/docs/whatsapp/pricing/
  - Leadsales. (2026). *WhatsApp API pricing calculator*. Recuperado el 15 de noviembre de 2026, de https://leadsales.io/en/tools/whatsapp-api-pricing-calculator/
  - Telnyx. (2026). *IoT SIM cards for Colombia*. Recuperado el 15 de noviembre de 2026, de https://telnyx.com/sim-cards/colombia

---

## C. Marco legal y regulatorio (Colombia)

### C1. Espectro para LoRa (uso libre 915–928 MHz) [V]
- **Resolución ANE 105 de 2020**, "Por medio de la cual se planea y atribuye el espectro radioeléctrico en Colombia".
  - El **Título 4 y el Anexo 1** fijan las bandas de uso libre.
  - **Art. 4.1.2:** el uso conforme al Anexo 1 no requiere "el permiso de uso del espectro".
  - **Art. 4.1.3:** los equipos deben cumplir estándares o tener certificado de homologación.
  - **Art. 4.1.4:** el uso libre no puede causar interferencia ni reclamar protección.
- **MinTIC (nov. 2022):** la banda **915–928 MHz** está listada para "dispositivos de salto en frecuencia, modulación digital o híbridos". El Anexo 1 tiene modificaciones posteriores (Res. ANE 148 de 2020, 469 de 2020, 647 de 2021, 148 de 2022 y 737 de 2022).
- **Resolución ANE 000028 del 26-ene-2026** (Diario Oficial 53.390, 6-feb-2026): modifica la Res. 105 de 2020 y el CNABF en 902–928 MHz. Reconoce el "despliegue masivo de dispositivos de uso libre en el segmento superior (915-928 MHz)".
- **Hallazgo de diseño (inferencia propia; verificar con LoRa Alliance RP002):**
  - TTN lista a Colombia con el plan **US902-928**.
  - Los canales de subida de US915 (902,3–914,9 MHz) quedan **fuera** de 915–928 MHz.
  - Se recomienda configurar gateways y nodos en **AU915-928** (subidas desde 915,2 MHz), o confirmar con la ANE que 902–915 MHz está habilitado para uso libre.
- **URL:**
  - https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_ane_0105_2020.htm
  - https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_ane_0028_2026.htm
  - https://www.mintic.gov.co/portal/715/articles-273358_memorias_05.pdf
  - https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/
- **APA:**
  - Agencia Nacional del Espectro. (2020). *Resolución 105 de 2020, por medio de la cual se planea y atribuye el espectro radioeléctrico en Colombia*. https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_ane_0105_2020.htm
  - Agencia Nacional del Espectro. (2026). *Resolución 000028 de 2026, por la cual se modifica la Resolución 105 de 2020 y se actualiza el Cuadro Nacional de Atribución de Bandas de Frecuencias*. Diario Oficial 53.390. https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_ane_0028_2026.htm
  - Ministerio de Tecnologías de la Información y las Comunicaciones. (2022). *Uso libre del espectro radioeléctrico* [Presentación]. https://www.mintic.gov.co/portal/715/articles-273358_memorias_05.pdf
  - The Things Network. (s. f.). *Frequency plans by country*. Recuperado el 15 de noviembre de 2026, de https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/

### C2. Homologación CRC [V]
- La **Resolución CRC 6129 de 2020** "subrogó el Título VII de la Resolución 5050 de 2016" (régimen de homologación de equipos terminales).
- La **Circular CRC 155 de 2024** (21-mar-2024) actualizó las normas técnicas para equipos terminales móviles, teléfonos fijos y satelitales. Fue **derogada por la Circular CRC 162 de 2025**.
- **Aplicabilidad a gateways y nodos LoRa:** no queda explícita; el régimen apunta a ETM. Para los nodos: cumplimiento de las condiciones de uso libre del Anexo 1 (art. 4.1.3 de la Res. 105). Para los gateways con 4G (son equipos con módem celular e IMEI): verificar homologación CRC.
- **URL:** https://normograma.mintic.gov.co/mintic/compilacion/docs/circular_crc_0155_2024.htm
- **APA:** Comisión de Regulación de Comunicaciones. (2024). *Circular 155 de 2024* [Derogada por la Circular 162 de 2025]. https://normograma.mintic.gov.co/mintic/compilacion/docs/circular_crc_0155_2024.htm

### C3. RETIE [S]
- **Resolución MinEnergía 40117 del 2-abr-2024** (DO 52.716): nuevo RETIE. Las disposiciones transitorias se modificaron con la Res. 40304 de 2025 y la Res. 40284 de 2026.
- **Relevancia:** aplica a la instalación eléctrica del laboratorio, no a los nodos de baja tensión alimentados por baterías.
- **URL:** https://www.minenergia.gov.co/es/misional/energia-electrica-2/reglamentos-tecnicos/reglamento-t%C3%A9cnico-de-instalaciones-eléctricas-retie/

### C4. Protección de datos [V]
- **Ley 1581 de 2012** (17-oct-2012; DO 48.587), "Por la cual se dictan disposiciones generales para la protección de datos personales". Art. 25: el RNBD "es el directorio público de las bases de datos sujetas a Tratamiento".
- **Decreto 1377 de 2013** (27-jun-2013; DO 48.834), reglamenta parcialmente la Ley 1581. Está compilado en el **Decreto 1074 de 2015, sección 2.2.2.25**.
- **Umbral RNBD:** el **Decreto 090 de 2018** obliga a inscribir las bases de datos a las sociedades con **activos totales > 100.000 UVT**.
  - Con la UVT 2026 = $52.374, el umbral es de **$5.237.400.000** (cálculo propio).
  - Una startup por debajo de ese umbral no inscribe en el RNBD, pero **sí** debe cumplir la Ley 1581 (política de tratamiento y autorización de los agricultores).
  - Las bases creadas después de los plazos deben inscribirse "dentro de los dos (2) meses posteriores a su establecimiento o creación".
- **URL:**
  - https://normograma.mintic.gov.co/mintic/compilacion/docs/ley_1581_2012.htm
  - https://normograma.mintic.gov.co/mintic/compilacion/docs/decreto_1377_2013.htm
  - https://www.asuntoslegales.com.co/analisis/catalina-herrera-von-norden-530696/cambios-en-el-registro-nacional-de-bases-de-datos-2596772
- **APA:**
  - Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales*. Diario Oficial 48.587. https://normograma.mintic.gov.co/mintic/compilacion/docs/ley_1581_2012.htm
  - Ministerio de Comercio, Industria y Turismo. (2013). *Decreto 1377 de 2013, por el cual se reglamenta parcialmente la Ley 1581 de 2012*. Diario Oficial 48.834. https://normograma.mintic.gov.co/mintic/compilacion/docs/decreto_1377_2013.htm
  - Herrera Von Norden, C. (2018, 7 de febrero). Cambios en el Registro Nacional de Bases de Datos. *Asuntos Legales*. https://www.asuntoslegales.com.co/analisis/catalina-herrera-von-norden-530696/cambios-en-el-registro-nacional-de-bases-de-datos-2596772

### C5. RAEE: Ley 1672 de 2013 [V]
- Ley del 19-jul-2013 (DO 48.856), sobre la política de gestión integral de los Residuos de Aparatos Eléctricos y Electrónicos.
- **Art. 6, obligaciones del productor:**
  - Establecer y financiar "un sistema de recolección y gestión ambientalmente segura de los residuos".
  - "Aceptar la devolución de los RAEE por parte del usuario final, sin costo alguno".
  - Informar al consumidor cómo devolver los residuos.
- **Aplica a:** los nodos y gateways reutilizables. Los sensores de papel, si no llevan componentes electrónicos, en principio quedan fuera.
- **URL:** https://normograma.mintic.gov.co/mintic/compilacion/docs/ley_1672_2013.htm
- **APA:** Congreso de la República de Colombia. (2013). *Ley 1672 de 2013, por la cual se establecen los lineamientos para la adopción de una política pública de gestión integral de Residuos de Aparatos Eléctricos y Electrónicos (RAEE)*. Diario Oficial 48.856. https://normograma.mintic.gov.co/mintic/compilacion/docs/ley_1672_2013.htm

### C6. Páramos: Ley 1930 de 2018 [V]
- Ley del 27-jul-2018 (DO 50.667).
- **Art. 5, num. 5:** "Se prohíbe el uso de maquinaria pesada en el desarrollo de actividades agropecuarias".
- **Art. 5, num. 11:** la fumigación y aspersión química "deberá eliminarse paulatinamente en el marco de la reconversión".
- **Art. 10:** permite continuar "actividades agropecuarias de bajo impacto".
- **Relevancia:** el monitoreo con sensores biodegradables apoya la reconversión y las buenas prácticas en zonas de páramo (por ejemplo, Rabanal y Guerrero).
- **URL:** https://jurinfo.jep.gov.co/Normograma/Compilacion/docs/ley_1930_2018.htm
- **APA:** Congreso de la República de Colombia. (2018). *Ley 1930 de 2018, por medio de la cual se dictan disposiciones para la gestión integral de los páramos en Colombia*. Diario Oficial 50.667. https://jurinfo.jep.gov.co/Normograma/Compilacion/docs/ley_1930_2018.htm

### C7. Sociedad SAS: Ley 1258 de 2008 [V]
- Ley del 5-dic-2008 (DO 47.194).
- **Art. 1:** la SAS "podrá constituirse por una o varias personas naturales o jurídicas", con responsabilidad hasta el monto de los aportes.
- **Art. 5:** se crea "mediante contrato o acto unilateral que conste en documento privado" (sin escritura pública).
- **URL:** https://normas.cra.gov.co/Gestor/Docs/ley_1258_2008.htm
- **APA:** Congreso de la República de Colombia. (2008). *Ley 1258 de 2008, por medio de la cual se crea la sociedad por acciones simplificada*. Diario Oficial 47.194. https://normas.cra.gov.co/Gestor/Docs/ley_1258_2008.htm

### C8. Emprendimiento: Ley 2069 de 2020 [V]
- Ley del 31-dic-2020 (DO 51.544).
- **Art. 3:** modifica el art. 230 de la Ley 223 de 1995. Para las microempresas (Decreto 957 de 2019), el impuesto departamental de registro queda así:
  - **0,3 %–0,6 %** para actos sin cuantía de capital.
  - **0,1 %–0,2 %** para actos de constitución de capital o prima.
  - "no se les podrán adicionar sobretasas o recargos de ningún tipo".
- **URL:** https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_2069_2020.htm
- **APA:** Congreso de la República de Colombia. (2020). *Ley 2069 de 2020, por medio de la cual se impulsa el emprendimiento en Colombia*. Diario Oficial 51.544. https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_2069_2020.htm

### C9. Registro mercantil 2026 (tabla nacional Confecámaras, aplica en Tunja y Bogotá) [V]
- **Base legal:** Decreto 1074 de 2015, modificado por el **Decreto 045 del 30-ene-2024**. Las tarifas se expresan en **UVB** (art. 313 de la Ley 2294 de 2023, PND 2022–2026).
- **Matrícula o renovación de persona jurídica:**
  - Activos de $0 a $78.715.000: **$24.220 + 8.477 × (activos / $1.000.000)**.
  - Activos de $78.715.000 a $302.750.000: $575.225 + 4.238,5 × (activos − 78.715.000)/1.000.000.
  - Tope: $12.110.000.
- **Matrícula de establecimiento en la misma jurisdicción:** $48.400 para activos ≤ $78.715.000.
- **Otros cobros:** inscripción de actos y documentos **6 UVB = $73.000**; libros 2 UVB = $24.200.
- **Ejemplo (cálculo propio):** SAS con activos de $50.000.000 paga 24.220 + 423.850 = **$448.070**.
- **Pendiente:** hay un proyecto de decreto de MinCIT del 19-oct-2026 que modificaría las tarifas.
- **URL:** https://www.camaramedellin.com.co/Portals/0/Documentos/2026/Tarifas_2026_CCMA.pdf ; https://www.cchuila.org/wp-content/uploads/Tarifas2026CCHweb.pdf
- **APA:** Confecámaras. (2026). *Tarifas del registro mercantil año 2026* [Publicado por la Cámara de Comercio de Medellín para Antioquia]. https://www.camaramedellin.com.co/Portals/0/Documentos/2026/Tarifas_2026_CCMA.pdf

### C10. Impuesto de renta y régimen SIMPLE [V]
- **Ley 2277 de 2022, art. 10:** modifica el art. 240 del Estatuto Tributario. Tarifa general para personas jurídicas: **35 %**.
- **Ley 2277 de 2022, art. 44:** modifica el art. 908 del ET. El grupo que incluye "actividades industriales, incluidas las de agro-industria, mini-industria y micro-industria; actividades de telecomunicaciones" tiene estas tarifas SIMPLE consolidadas:

  | Ingresos brutos anuales | Tarifa |
  |---|---|
  | 0–6.000 UVT | 1,6 % |
  | 6.000–15.000 UVT | 2,0 % |
  | 15.000–30.000 UVT | 3,5 % |
  | 30.000–100.000 UVT | 4,5 % |

- **Servicios profesionales y de consultoría:** la tabla vigente cambió tras la **Sentencia C-540 de 2023**, que revivió las tarifas de la Ley 2155 de 2021. No se extrajo la tabla (**NO ENCONTRADO**).
- **Actividades múltiples:** el **Concepto DIAN 015659 de 2026** (7-sep-2026) indica que se aplica "la tarifa SIMPLE consolidada más alta".
- **UVT 2026: $52.374**, Resolución DIAN 000238 del 15-dic-2025.
- **Ley 2010 de 2019:** no se consultó. La tarifa vigente es la de la Ley 2277.
- **URL:**
  - https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=199883
  - https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_15659_2026.htm
  - https://incp.org.co/publicaciones/infoincp-publicaciones/impuestos/2025/12/dian-fijo-en-52-374-en-valor-de-la-uvt-para-el-ano-gravable-2026/ [S]
- **APA:**
  - Congreso de la República de Colombia. (2022). *Ley 2277 de 2022, por medio de la cual se adopta una reforma tributaria para la igualdad y la justicia social*. https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=199883
  - Dirección de Impuestos y Aduanas Nacionales. (2026). *Concepto 015659 (int 1578) de 2026*. https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_15659_2026.htm

### C11. ICA [V]/[S]
- **Bogotá:** el **Acuerdo 1084 de 2026** (aprobado el 8-oct-2026) reemplaza la tabla del art. 3 del Acuerdo 65 de 2002.
  - Tarifas residuales: **10 por mil (servicios)** y **11 por mil (comerciales e industriales)**.
  - Las aplican los declarantes anuales desde el **1-ene-2027**.
  - El ICA consolidado en el SIMPLE para el numeral 2 del art. 908 queda en **14 por mil**.
  - Da exenciones a nuevas inversiones en electrónica, TIC e investigación científica. [V] Cuatrecasas (oct-2026).
- **Tunja:** **4,5 por mil** (Acuerdo 031 de 2005, que subió del 4 por mil del Acuerdo 034 de 1998). El dato viene de un fallo judicial sobre el año gravable 2012. [S] https://www.ramajudicial.gov.co/documents/2216525/23294578/_00620150015901-.PDF/e2e6f977-2490-4ca4-bf9e-658a82ccac0a
  - La tarifa vigente en 2026 para industria o servicios es **NO ENCONTRADO**. Proxy: el rango legal para actividades industriales es de 2 a 7 por mil (Ley 1819, art. 342, según la SDH Bogotá) [S]. Confirmar con la Secretaría de Hacienda de Tunja.
- **APA:** Cuatrecasas. (2026). *Legal Flash: Bogotá aprueba nueva reforma tributaria: Acuerdo 1084 de 2026*. https://www.cuatrecasas.com/resources/bogota-reforma-tributaria-txt-6ad788361244a900148682.pdf

### C12. Depreciación fiscal: ET art. 137 [V]
- **Tasas máximas anuales:**

  | Activo | Tasa anual |
  |---|---|
  | Construcciones y edificaciones | 2,22 % |
  | Maquinaria y equipos | 10 % |
  | Muebles y enseres | 10 % |
  | Equipo eléctrico | 10 % |
  | Equipo médico-científico | 12,5 % |
  | Envases, empaques y herramientas | 20 % |
  | Equipo de computación | 20 % |
  | Redes de procesamiento de datos | 20 % |
  | Equipo de comunicación | 20 % |
  | Flota terrestre | 10 % |

- La tabla del ET fue modificada por el art. 82 de la **Ley 1819 de 2016**. El art. 1.2.1.18.4 del DUR 1625 de 2016 trata la vida útil de activos adquiridos desde 1989.
- **URL:** https://actualicese.com/estatutotributario/137-2/
- **APA:** Actualícese. (s. f.). *Estatuto Tributario, artículo 137: Limitación a la deducción por depreciación*. Recuperado el 15 de noviembre de 2026, de https://actualicese.com/estatutotributario/137-2/

### C13. ICA (Instituto Colombiano Agropecuario) [V]
- La **Resolución ICA 00150 del 21-ene-2003** adopta el Reglamento Técnico de **Fertilizantes y Acondicionadores de Suelos**. El ICA debe "otorgar el registro y ejercer el control legal y técnico de los fertilizantes y acondicionadores de suelos".
- **Conclusión (análisis):** un sensor que solo mide no es fertilizante ni acondicionador, así que **no requiere registro ICA**. Si se comercializa con una función fertilizante declarada (como el "sensing fertilizer" de A3), sí podría requerirlo.
- **Pendiente:** verificar la vigencia y las modificaciones de la Res. 150 de 2003 en el normograma ICA.
- **URL:** https://compilacionmsf.ica.gov.co:4443/compilacion/docs/pdf/resolucion_ica_0150_2003.pdf
- **APA:** Instituto Colombiano Agropecuario. (2003). *Resolución 00150 de 2003, por la cual se adopta el Reglamento Técnico de Fertilizantes y Acondicionadores de Suelos para Colombia*. https://compilacionmsf.ica.gov.co:4443/compilacion/docs/pdf/resolucion_ica_0150_2003.pdf

### C14. Normas de biodegradabilidad [V]
| Norma | Título | Fecha |
|---|---|---|
| **ISO 17556:2019** | Plastics — Determination of the ultimate aerobic biodegradability of plastic materials in soil by measuring the oxygen demand in a respirometer or the amount of carbon dioxide evolved | 30-abr-2019 (confirmada en 2024 [S]) |
| **ISO 14855-1:2012** | Determination of the ultimate aerobic biodegradability of plastic materials under controlled composting conditions — Method by analysis of evolved carbon dioxide — Part 1: General method | 26-nov-2012 |
| **EN 17033:2018** | Plastics — Biodegradable mulch films for use in agriculture and horticulture — Requirements and test methods | 16-abr-2018 (confirmada el 21-nov-2023) |
| **ISO 23517:2021** | Plastics — Soil biodegradable materials for mulch films for use in agriculture and horticulture — Requirements and test methods regarding biodegradation, ecotoxicity and control of constituents | 23-jul-2021 |
| NTC 5167 [S] | Norma colombiana para materiales orgánicos usados como fertilizantes y acondicionadores de suelo. Versión 2022 según una tesis de UTadeo. **No es una norma de biodegradabilidad** | Título oficial NO ENCONTRADO |

- **Recomendación:** usar **ISO 17556** (biodegradación en suelo) como método de ensayo, y **ISO 23517 / EN 17033** como marco de requisitos y ecotoxicidad por analogía.
- **URL:** https://genorma.com/en/standards/iso-17556-2019 ; https://genorma.com/en/standards/iso-14855-1-2012/amp ; https://genorma.com/en/standards/en-17033-2018 ; https://genorma.com/en/standards/iso-23517-2021
- **APA:**
  - International Organization for Standardization. (2019). *Plastics — Determination of the ultimate aerobic biodegradability of plastic materials in soil by measuring the oxygen demand in a respirometer or the amount of carbon dioxide evolved* (ISO Standard No. 17556:2019).
  - International Organization for Standardization. (2012). *Determination of the ultimate aerobic biodegradability of plastic materials under controlled composting conditions — Method by analysis of evolved carbon dioxide — Part 1: General method* (ISO Standard No. 14855-1:2012).
  - International Organization for Standardization. (2021). *Plastics — Soil biodegradable materials for mulch films for use in agriculture and horticulture — Requirements and test methods regarding biodegradation, ecotoxicity and control of constituents* (ISO Standard No. 23517:2021).
  - European Committee for Standardization. (2018). *Plastics — Biodegradable mulch films for use in agriculture and horticulture — Requirements and test methods* (EN 17033:2018).

---

## D. Factores de localización

### D1. Arriendo de bodegas
| Ciudad | Cifra | Fecha | Fuente | Estado |
|---|---|---|---|---|
| Tunja (barrio Obrero) | 150 m², $2.000.000/mes con administración, **≈ $13.333/m²** | publicado 17-oct-2026 | https://www.fincaraiz.com.co/bodega-en-arriendo-en-tunja/194418092 | [V] |
| Tunja (Mezopotamia) | 560 m², $12.320.000 + administración $470.905, **≈ $22.000/m²** | sin fecha | https://www.ciencuadras.com/inmueble/bodega-en-arriendo-en-mezopotamia-tunja-3296607 | [V] |
| Duitama (Centro) | 2.650 m², $35.000.000, **≈ $13.200/m²** | sin fecha | https://www.ciencuadras.com/inmueble/bodega-en-arriendo-en-centro-duitama-3362158 | [S] |
| Bogotá y Sabana (promedio de mercado) | **$28.077/m²/mes**, vacancia 0,9 %, +17 % en 12 meses (Cushman & Wakefield, MarketBeat Industrial Q2) | artículo del 1-sep-2026 | https://www.portafolio.co/negocios/empresas/bodegas-en-bogota-tocan-minimos-historicos-de-vacancia-con-solo-0-9-y-disparan-17-los-arriendos-en-un-ano-501574 | [V] |

- Los cálculos por m² son propios. Las cifras de Tunja son precios de oferta, no un índice de mercado.
- **Lectura:** en Tunja o Duitama el m² cuesta entre 20 % y 50 % menos que el promedio de Bogotá.
- **APA:** Monsalve Martínez, M. C. (2026, 1 de septiembre). Bodegas en Bogotá tocan mínimos históricos de vacancia con solo 0,9 % y disparan 17 % los arriendos en un año. *Portafolio*. https://www.portafolio.co/negocios/empresas/bodegas-en-bogota-tocan-minimos-historicos-de-vacancia-con-solo-0-9-y-disparan-17-los-arriendos-en-un-ano-501574

### D2. Distancias por carretera desde Tunja [V]
Calculadas con el enrutador OSRM sobre OpenStreetMap el 15-nov-2026, entre los centros urbanos (coordenadas aproximadas).

| Ruta | Distancia | Tiempo |
|---|---|---|
| Tunja–Paipa | 42,5 km | ~59 min |
| Tunja–Villapinzón | 51,1 km | ~51 min |
| Tunja–Duitama | 56,5 km | ~76 min |
| Tunja–Sogamoso | 72,2 km | ~96 min |
| Tunja–Zipaquirá | 115,7 km | ~112 min |
| Tunja–Bogotá | 138,6 km | ~135 min |
| Bogotá–Villapinzón | 87,5 km | — |

- **Contraste [S]:** Travelandtime da Tunja–Duitama 49 km y Tunja–Sogamoso 52 km, probablemente distancias aproximadas.
- **Lectura:** Tunja queda en el centro de gravedad de la zona papera (Villapinzón, Ventaquemada, Duitama y Sogamoso a menos de 75 km).
- **APA:** Project OSRM. (2026). *OSRM routing service* [Servicio de enrutamiento sobre datos de OpenStreetMap]. Recuperado el 15 de noviembre de 2026, de https://router.project-osrm.org

### D3. Universidades [S]
- **UPTC (Tunja):** ofrece Ingeniería Electrónica e Ingeniería Agronómica según documentos de inducción de 2025. Tiene sede en Sogamoso.
- **Universidad de Cundinamarca:** Ingeniería Agronómica (SNIES 1928) e Ingeniería Electrónica (SNIES 4086) en Fusagasugá. La primera tiene ampliación a Facatativá y la segunda a Soacha. Tiene extensión en Zipaquirá.
- **URL:** https://www.ucundinamarca.edu.co/gaceta/phocadownload/academico_acuerdos/2025/ACUERDO_CA_036.pdf ; https://moodle.uptc.edu.co/servicios/pluginfile.php/11740/mod_resource/content/1/JORNADA%20INDUCCIÓN%202025.pdf
- **Verificar en SNIES** antes de citar.

### D4. Tarifa de energía eléctrica, sector no residencial [V]
| Operador | Mes | Tipo de usuario | Tarifa ($/kWh) |
|---|---|---|---|
| **EBSA (Boyacá)** | **dic-2025** | Comercial/industrial NT1, activos EBSA | **1.063,4994** |
| EBSA | dic-2025 | NT1, activos del usuario | 964,1340 |
| EBSA | dic-2025 | NT2 | 884,4554 |
| **Enel (Bogotá)** | **ago-2026** | Industrial y comercial con contribución, NT1, propiedad Enel | **1.036,3262** |
| Enel | ago-2026 | NT1, propiedad del cliente | 977,3813 |
| Enel | ago-2026 | NT2 (11,4–13,2 kV) | 865,7615 |
| Enel | ago-2026 | Industrial sin contribución, NT1 | 863,6052 |

- **Faltante:** la tarifa EBSA de 2026 es **NO ENCONTRADO**. Proxy: dic-2025.
- **URL:** https://boyaca7dias.com.co/wp-content/uploads/2025/12/Aviso-Tarifas-Ebsa-DICIEMBRE.pdf ; https://www.enel.com.co/content/dam/enel-co/español/personas/1-17-1/2026/pliego%20tarifario%20digital%20_agosto_2026.pdf
- **APA:**
  - Empresa de Energía de Boyacá. (2025). *Información sobre tarifas de energía eléctrica aplicables a consumos en el mercado regulado de Boyacá: diciembre 2025*. https://boyaca7dias.com.co/wp-content/uploads/2025/12/Aviso-Tarifas-Ebsa-DICIEMBRE.pdf
  - Enel Colombia. (2026). *Pliego tarifario de energía eléctrica: agosto 2026*. https://www.enel.com.co/content/dam/enel-co/español/personas/1-17-1/2026/pliego%20tarifario%20digital%20_agosto_2026.pdf

---

## Vacíos principales (NO ENCONTRADO)
1. Costo unitario y tiempo de degradación en días de los sensores de papel en suelo. Proxy: USD 0,00077 por sensor de acetato de celulosa (A9). La vida funcional demostrada es de 113 días (A1).
2. Exactitud en % VWC de los sensores biodegradables (los resúmenes no la reportan).
3. Precios en Colombia de máquina de serigrafía semiautomática, horno nuevo, cámara climática, balanza, portátil, cera de abejas, goma laca, LiFePO4 y caja IP65.
4. Plan M2M de Claro, Movistar o Tigo, y tarifa de Hablame.
5. Precios de RAK7289 y RAK4631 (la tienda RAK bloqueó el acceso con 429).
6. Tarifa ICA vigente de Tunja en 2026.
7. Tabla SIMPLE vigente para servicios profesionales tras la C-540 de 2023.
8. Tarifa EBSA de 2026.

---

## Lista consolidada de referencias (APA 7, orden alfabético)

Actualícese. (s. f.). *Estatuto Tributario, artículo 137: Limitación a la deducción por depreciación*. Recuperado el 15 de noviembre de 2026, de https://actualicese.com/estatutotributario/137-2/

Agencia Nacional del Espectro. (2020). *Resolución 105 de 2020, por medio de la cual se planea y atribuye el espectro radioeléctrico en Colombia*. https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_ane_0105_2020.htm

Agencia Nacional del Espectro. (2026). *Resolución 000028 de 2026, por la cual se modifica la Resolución 105 de 2020 y se actualiza el Cuadro Nacional de Atribución de Bandas de Frecuencias*. Diario Oficial 53.390. https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_ane_0028_2026.htm

Amazon Web Services. (2026a). *Amazon Lightsail pricing*. Recuperado el 15 de noviembre de 2026, de https://aws.amazon.com/lightsail/pricing/

Amazon Web Services. (2026b). *AWS IoT Core pricing*. Recuperado el 15 de noviembre de 2026, de https://aws.amazon.com/iot-core/pricing/

ChemicalBook. (2026). *Silver conductive ink: Price* [Lista de precios Sigma-Aldrich 901769]. Recuperado el 15 de noviembre de 2026, de https://www.chemicalbook.com/Price/CB25542136.htm

Comisión de Regulación de Comunicaciones. (2024). *Circular 155 de 2024* [Derogada por la Circular 162 de 2025]. https://normograma.mintic.gov.co/mintic/compilacion/docs/circular_crc_0155_2024.htm

Confecámaras. (2026). *Tarifas del registro mercantil año 2026*. Cámara de Comercio de Medellín para Antioquia. https://www.camaramedellin.com.co/Portals/0/Documentos/2026/Tarifas_2026_CCMA.pdf

Congreso de la República de Colombia. (2008). *Ley 1258 de 2008, por medio de la cual se crea la sociedad por acciones simplificada*. Diario Oficial 47.194. https://normas.cra.gov.co/Gestor/Docs/ley_1258_2008.htm

Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales*. Diario Oficial 48.587. https://normograma.mintic.gov.co/mintic/compilacion/docs/ley_1581_2012.htm

Congreso de la República de Colombia. (2013). *Ley 1672 de 2013, por la cual se establecen los lineamientos para la adopción de una política pública de gestión integral de Residuos de Aparatos Eléctricos y Electrónicos (RAEE)*. Diario Oficial 48.856. https://normograma.mintic.gov.co/mintic/compilacion/docs/ley_1672_2013.htm

Congreso de la República de Colombia. (2018). *Ley 1930 de 2018, por medio de la cual se dictan disposiciones para la gestión integral de los páramos en Colombia*. Diario Oficial 50.667. https://jurinfo.jep.gov.co/Normograma/Compilacion/docs/ley_1930_2018.htm

Congreso de la República de Colombia. (2020). *Ley 2069 de 2020, por medio de la cual se impulsa el emprendimiento en Colombia*. Diario Oficial 51.544. https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_2069_2020.htm

Congreso de la República de Colombia. (2022). *Ley 2277 de 2022, por medio de la cual se adopta una reforma tributaria para la igualdad y la justicia social*. https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=199883

Cuatrecasas. (2026). *Legal Flash: Bogotá aprueba nueva reforma tributaria: Acuerdo 1084 de 2026*. https://www.cuatrecasas.com/resources/bogota-reforma-tributaria-txt-6ad788361244a900148682.pdf

DigiKey. (2026). *RAK3172-9-SM-NI* [Página de producto]. Recuperado el 15 de noviembre de 2026, de https://www.digikey.com/en/products/detail/rakwireless-technology-limited/RAK3172-9-SM-NI/17138034

DigitalOcean. (2026). *Droplet pricing*. Recuperado el 15 de noviembre de 2026, de https://www.digitalocean.com/pricing/droplets

Dirección de Impuestos y Aduanas Nacionales. (2026). *Concepto 015659 (int 1578) de 2026*. https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_15659_2026.htm

Electronilab. (2026). *Catálogo de productos* [Tienda en línea]. Recuperado el 15 de noviembre de 2026, de https://electronilab.co/tienda/

Empresa de Energía de Boyacá. (2025). *Información sobre tarifas de energía eléctrica aplicables a consumos en el mercado regulado de Boyacá: diciembre 2025*. https://boyaca7dias.com.co/wp-content/uploads/2025/12/Aviso-Tarifas-Ebsa-DICIEMBRE.pdf

Enel Colombia. (2026). *Pliego tarifario de energía eléctrica: agosto 2026*. https://www.enel.com.co/content/dam/enel-co/español/personas/1-17-1/2026/pliego%20tarifario%20digital%20_agosto_2026.pdf

European Committee for Standardization. (2018). *Plastics — Biodegradable mulch films for use in agriculture and horticulture — Requirements and test methods* (EN 17033:2018).

Fry, E. L., Sharpe, T. J., Atreya, M., Whiting, G. L., & Quinton, J. N. (2026). Printed PHBV-based sensors as a real-time proxy for soil microbial decomposer activity during drought and flood recovery. *European Journal of Soil Science, 77*(3), e70358. https://doi.org/10.1111/ejss.70358

Heltec Automation. (2026). *WiFi LoRa 32 (V4)*. Recuperado el 15 de noviembre de 2026, de https://heltec.org/project/wifi-lora-32-v4/

Herrera Von Norden, C. (2018, 7 de febrero). Cambios en el Registro Nacional de Bases de Datos. *Asuntos Legales*. https://www.asuntoslegales.com.co/analisis/catalina-herrera-von-norden-530696/cambios-en-el-registro-nacional-de-bases-de-datos-2596772

Instituto Colombiano Agropecuario. (2003). *Resolución 00150 de 2003, por la cual se adopta el Reglamento Técnico de Fertilizantes y Acondicionadores de Suelos para Colombia*. https://compilacionmsf.ica.gov.co:4443/compilacion/docs/pdf/resolucion_ica_0150_2003.pdf

International Organization for Standardization. (2012). *Determination of the ultimate aerobic biodegradability of plastic materials under controlled composting conditions — Method by analysis of evolved carbon dioxide — Part 1: General method* (ISO Standard No. 14855-1:2012).

International Organization for Standardization. (2019). *Plastics — Determination of the ultimate aerobic biodegradability of plastic materials in soil by measuring the oxygen demand in a respirometer or the amount of carbon dioxide evolved* (ISO Standard No. 17556:2019).

International Organization for Standardization. (2021). *Plastics — Soil biodegradable materials for mulch films for use in agriculture and horticulture — Requirements and test methods regarding biodegradation, ecotoxicity and control of constituents* (ISO Standard No. 23517:2021).

Iyer, G. M., Zaccarin, A.-M., Olsson, R. H., & Turner, K. T. (2022). Fabrication and characterization of cellulose-based materials for biodegradable soil moisture sensors. En *2022 IEEE Sensors* (pp. 1–4). IEEE. https://doi.org/10.1109/SENSORS52175.2022.9967089

Kasuga, T., Mizui, A., Koga, H., & Nogi, M. (2024). Wirelessly powered sensing fertilizer for precision and sustainable agriculture. *Advanced Sustainable Systems, 8*(1), 2300314. https://doi.org/10.1002/adsu.202300314

Leadsales. (2026). *WhatsApp API pricing calculator*. Recuperado el 15 de noviembre de 2026, de https://leadsales.io/en/tools/whatsapp-api-pricing-calculator/

Meshram, S. M. (2026). *Design of biodegradable soil moisture sensor powered by bacteria charged paper batteries* [Tesis doctoral, Delft University of Technology]. TU Delft Repository. https://doi.org/10.4233/uuid:69b9f541-e7ec-41ca-a6f2-b53efb1da9d4

Meshram, S. M. M., Adla, S., Jourdin, L., & Pande, S. (2024). Review of low-cost, off-grid, biodegradable in situ autonomous soil moisture sensing systems. *Computers and Electronics in Agriculture, 225*, 109289. https://doi.org/10.1016/j.compag.2024.109289

Meta. (2026). *Pricing on the WhatsApp Business Platform*. Recuperado el 15 de noviembre de 2026, de https://developers.facebook.com/docs/whatsapp/pricing/

Ministerio de Comercio, Industria y Turismo. (2013). *Decreto 1377 de 2013, por el cual se reglamenta parcialmente la Ley 1581 de 2012*. Diario Oficial 48.834. https://normograma.mintic.gov.co/mintic/compilacion/docs/decreto_1377_2013.htm

Ministerio de Tecnologías de la Información y las Comunicaciones. (2022). *Uso libre del espectro radioeléctrico* [Presentación]. https://www.mintic.gov.co/portal/715/articles-273358_memorias_05.pdf

Monsalve Martínez, M. C. (2026, 1 de septiembre). Bodegas en Bogotá tocan mínimos históricos de vacancia con solo 0,9 % y disparan 17 % los arriendos en un año. *Portafolio*. https://www.portafolio.co/negocios/empresas/bodegas-en-bogota-tocan-minimos-historicos-de-vacancia-con-solo-0-9-y-disparan-17-los-arriendos-en-un-ano-501574

Nanografi. (s. f.). *Carbon paste (140 ℃, 50 ohm/sqr/25 µm)*. Recuperado el 15 de noviembre de 2026, de https://shop.nanografi.com/new-materials/carbon-paste-140-100-ohm-sqr-25-m

NovaCentrix. (s. f.). *HPR-059 carbon black ink*. Recuperado el 15 de noviembre de 2026, de https://novacentrix.com/product/hpr-059-carbon-black

Panáček, D., Kupka, V., Nalepa, M.-A., Dědek, I., Álvarez-Diduk, R., Olenik, S., Flauzino, J., Zdražil, J., Jakubec, P., Zdražil, L., Spíchal, L., Sonigara, K. K., Zbořil, R., Pumera, M., Merkoçi, A., Wang, J., De Diego, N., Güder, F., & Otyepka, M. (2026). Printing technologies for monitoring crop health. *Nature Communications, 17*, 2009. https://doi.org/10.1038/s41467-026-68778-6

Project OSRM. (2026). *OSRM routing service* [Servicio de enrutamiento sobre datos de OpenStreetMap]. Recuperado el 15 de noviembre de 2026, de https://router.project-osrm.org

Snyder, R. L., & de Melo-Abreu, J. P. (2005). *Frost protection: Fundamentals, practice and economics* (Vol. 1, Environment and Natural Resources Series No. 10). Food and Agriculture Organization of the United Nations. https://www.fao.org/4/y7223e/y7223e00.htm

Sui, Y., Atreya, M., Dahal, S., Gopalakrishnan, A., Khosla, R., & Whiting, G. L. (2021). Controlled biodegradation of an additively fabricated capacitive soil moisture sensor. *ACS Sustainable Chemistry & Engineering, 9*(6), 2486–2495. https://doi.org/10.1021/acssuschemeng.0c07615

Teixeira, S. C., Gomes, N. O., Machado, S. A. S., de Oliveira, T. V., Soares, N. F. F., & Raymundo-Pereira, P. A. (2026). Biodegradable wearable sensors for rapid non-destructive analysis of pesticides on plants and foods. *Biosensors and Bioelectronics: X, 29*, 100758. https://doi.org/10.1016/j.biosx.2026.100758

Telnyx. (2026). *IoT SIM cards for Colombia*. Recuperado el 15 de noviembre de 2026, de https://telnyx.com/sim-cards/colombia

The Things Industries. (2026). *The Things Stack plans*. Recuperado el 15 de noviembre de 2026, de https://www.thethingsindustries.com/stack/plans/

The Things Network. (s. f.). *Frequency plans by country*. Recuperado el 15 de noviembre de 2026, de https://www.thethingsnetwork.org/docs/lorawan/frequencies-by-country/

Twilio. (2026). *SMS pricing in Colombia*. Recuperado el 15 de noviembre de 2026, de https://www.twilio.com/en-us/sms/pricing/co

Zaccarin, A.-M., Iyer, G. M., Olsson, R. H., & Turner, K. T. (2024). Fabrication and characterization of soil moisture sensors on a biodegradable, cellulose-based substrate. *IEEE Sensors Journal, 24*(6), 7235–7243. https://doi.org/10.1109/JSEN.2023.3299430

Zaccarin, A.-M., Peddada, N., Machold, M., Turner, K. T., & Olsson, R. H., III. (2025). Inductively coupled capacitive soil moisture sensors printed on a biodegradable substrate: Characterization and long-term testing. *Smart Agricultural Technology, 11*, 101052. https://doi.org/10.1016/j.atech.2025.101052
