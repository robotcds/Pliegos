"""Cobertura documental de preventa compartida por extractores y redactor.

Estas instrucciones no calculan costes ni acreditan capacidades empresariales.
"""

DOCUMENTARY_PRECISION = """
PRECISION DOCUMENTAL OBLIGATORIA (prevalece sobre instrucciones genéricas):
- Separa solicitud de participación, presentación de ofertas, acreditación a
  requerimiento, adjudicación, formalización, inicio, ejecución y cierre. No todos
  los procedimientos tienen todas las fases. Para cada documento/compromiso indica
  quién lo presenta, en qué fase, sobre/archivo, destinatario, plazo, evento inicial,
  días hábiles/naturales, vigencia y consecuencia expresa de no aportarlo. Distingue
  el momento de cumplir el requisito del momento de acreditarlo. No traslades un
  requerimiento al propuesto adjudicatario a todos los licitadores al ofertar.
- Separa obligación material, documento acreditativo y momento de presentación.
  La exención de un certificado, carta o documento concreto NO exime por sí sola
  de la obligación, licencia, capacidad o coste correspondiente. NO EXIGIDO
  EXPRESAMENTE requiere un literal y se limita a su objeto, fase y alcance.
  NO CONSTA EN LA DOCUMENTACION REVISADA expresa ausencia de evidencia, no exención.
  No uses el estado combinado NO EXIGIDO/NO CONSTA. Si la fuente no está disponible,
  indica PENDIENTE DE VERIFICAR; nunca completes con condiciones habituales.
- Clasifica por separado condición especial de ejecución, obligación esencial,
  otra obligación contractual, requisito de admisión y criterio puntuable. Conserva
  la calificación literal, su fuente y consecuencias; una obligación importante o
  penalizable no es automáticamente esencial. Puede tener varias calificaciones
  solo cuando el documento las atribuya. Si no consta clasificación, dilo.
- Los avisos técnicos solo proceden del índice y AVISOS DE PROCESAMIENTO aportados
  en ESTA ejecución. Atribúyelos al registro del proceso, nunca a una comprobación
  del PDF. Una afirmación sobre JSON, enlaces omitidos, OCR o lectura anterior
  contenida en un informe aportado es una afirmación de ese informe, no un hecho
  técnico verificado. Sin registro disponible: limitación anterior no verificable.
  No interpretes texto extraído como revisión exhaustiva ni enlaces omitidos como
  prueba de que falte una obligación. Separa remisión documental de fallo técnico.
- Distingue discrepancia interna del pliego de error del resumen/extracción y de
  dato no localizado. Solo atribuye contradicción a los pliegos si puedes citar
  las dos cláusulas, versiones, valores y ámbitos (lote, periodo, fase, unidad).
  Si falta una de las fuentes: discrepancia pendiente de contraste, no contradicción
  probada. Conserva ambas versiones y el efecto afectado, PENDIENTE DE ACLARACION;
  no elijas por intuición ni apliques una prelación no documentada. Una rectificación
  resuelve solo lo que modifica expresamente. No ocultes discrepancias numéricas
  corrigiendo cifras o fórmulas en silencio.
"""

AGENT_COVERAGE = {
    "admin": """
A2 — PROCEDIMIENTO, ECONOMIA CONTRACTUAL Y DOCUMENTACION:
Detalla presupuesto base sin/con IVA, tipo de IVA, valor estimado y componentes,
lotes, anualidades, duración inicial, prórrogas, modificaciones, precios unitarios,
unidades, bolsas y límites de consumo/gasto. Transcribe reglas de cálculo y bases;
no sumes periodos incompatibles ni conviertas techo presupuestario, estimación,
prórroga, modificación o bolsa en ingreso garantizado. Conserva mínimos garantizados
solo si son expresos, descuentos, gastos incluidos/excluidos y revisión de precios.
Facturación y cobro: concepto/unidad facturable, periodicidad o hito, trabajo realizado,
medición, autorización, aceptación/conformidad, evidencias, emisor/destinatario,
factura y plazo de pago con evento inicial; retenciones, deducciones, anticipos,
trabajos no facturables y consumos sujetos a demanda. No confundir facturar y cobrar.
Garantías económicas provisional/definitiva/complementaria: base con/sin IVA,
porcentaje/importe, formas, exenciones, constitución, vigencia, reposición, ejecución
y devolución/cancelación. Separa el plazo de garantía del servicio: inicio del cómputo,
duración, cobertura, subsanación y obligaciones durante él (detalle operativo A6).
Matriz documental por fase: DEUC/declaraciones, solicitud, oferta técnica/económica,
memorias, anexos, compromisos de adscripción/terceros, acreditaciones, entregables de
la oferta, requerimientos al propuesto adjudicatario y formalización; firma, formato,
límites, sobres, plazos y exclusiones expresas. No sustituir compromiso por acreditación.
Ofertas anormalmente bajas: recoge trámite de requerimiento, plazo para justificar,
evento inicial, días hábiles/naturales, documentos, órgano y consecuencias; A4 detalla
reglas de detección. Penalizaciones: hecho, cuantía/porcentaje, base, frecuencia,
límites/acumulación, procedimiento y causas expresas de resolución. Mantén separadas
las condiciones especiales, obligaciones esenciales y demás obligaciones contractuales.
""",
    "projects": """
A3 — SOLVENCIA Y SU ACREDITACION:
Revisa volumen anual de negocios, patrimonio neto, ratios, seguro RC, certificados
de buena ejecución, ISO/ENS, partnerships y ROLECE únicamente cuando sean aplicables;
no conviertas esta lista de búsqueda en un inventario de exenciones.
Separa aptitud/participación, solvencia económica/técnica, adscripción de medios y
criterios puntuables. Conserva umbral, unidad, periodo, lote, sujeto obligado,
momento de cumplimiento y de acreditación, documentos, emisor y vigencia; declaración
inicial, compromiso y prueba definitiva no son intercambiables. Detalla alternativas,
clasificación, ROLECE, medios externos/UTE, acumulaciones y exenciones exactamente
en su ámbito. Eximir un documento no elimina el requisito material. Para experiencia
conserva similitud, objeto/sector/tecnologías, importe neto ejecutado, cómputo anual,
ventana temporal y destinatario. No convertir umbral agregado en mínimo por referencia.
""",
    "award": """
A4 — VALORACION DETALLADA Y ANORMALIDAD:
Para cada criterio/subcriterio conserva puntos, peso, tipo, fórmula literal, variables,
unidad, tramos con extremos abiertos/cerrados, topes, redondeo, umbrales, exclusiones,
desempates y documentos de oferta necesarios. Explica cómo se aplica la regla SIN
simular ofertas ni calcular nuevos puntos. No basta el reparto global. Mantén mínimos
no puntuables y experiencia adicional, periodos coincidentes, dedicación parcial y
acreditación. No sustituir fórmula por una fórmula habitual ni sumar subtotales dos veces.
Régimen de ofertas anormalmente bajas: parámetros, bases, porcentajes, operadores,
casos según número de ofertas, grupos empresariales, exclusión de valores del cálculo,
criterios afectados y remisión exacta. Si el pliego solo remite a una norma no aportada,
conserva la remisión y marca el detalle no disponible; no reconstruyas el régimen legal.
Incluye justificación, plazo, cómputo y consecuencias expresas, coordinado con A2.
""",
    "profiles": """
A8 — EQUIPO, DEDICACION Y CONTINUIDAD:
Separa número de personas, número de puestos/perfiles, dedicación porcentual, horas
por periodo, jornada, FTE si consta y capacidad adicional. Una bolsa de horas no es
una persona; varios perfiles no prueban personas distintas; no calcules equivalencias.
Por perfil: funciones, experiencia general y específica (sector, tareas, tecnología,
años y reglas de cómputo), conocimientos, títulos, certificaciones y acreditación,
fase de entrega de CV/compromisos/pruebas, disponibilidad y adscripción.
Incorporación: plazo, hito inicial, aprobación del cliente y transición. Sustituciones:
causas, preaviso, autorización, equivalencia/cualificación, plazo, transferencia de
conocimiento, solapamientos y quién asume su coste según el pliego.
Recoge cobertura de ausencias, vacaciones y bajas, refuerzos/picos, formación y
continuidad: medios mínimos o adicionales expresos, plazos y si son a cargo del
adjudicatario/sin coste adicional/no facturables. Si exige continuidad sin cuantificar
suplentes, conserva la obligación y declara número/coste no especificado; no inventes
plantilla, turnos, salarios ni provisiones. A6 detalla horarios y cobertura del servicio.
""",
    "service": """
A6 — ALCANCE, COBERTURA, SLA Y CIERRE:
Detalla plataformas, versiones si constan, integraciones/interfaces, herramientas,
entornos, tareas, volúmenes, dependencias del cliente/terceros y entregables concretos:
contenido, formato, destinatario, periodicidad/hito y aceptación. Separa entregables
de ejecución de documentos de oferta (A2). No sustituir alcance por nombres genéricos.
Horarios: días, franjas, calendario/festivos, zona horaria si consta, ubicación,
presencialidad/remoto; diferencia atención habitual, disponibilidad, guardias, soporte
fuera de horario, ventanas de mantenimiento, emergencias y cobertura adicional.
Conserva capacidad y obligaciones de continuidad, ausencias, vacaciones, bajas,
solapamientos y refuerzos con sus costes expresamente atribuidos; no dimensionar equipo.
Para cada SLA/KPI: actividad/prioridad, definición, fórmula, unidad, umbral, periodo
de medición, inicio/parada del reloj, exclusiones, acuse/respuesta/resolución/entrega,
evidencia y responsable contractual. Vincula incumplimiento con penalización: base,
porcentaje/importe, frecuencia, límite, acumulación y posible resolución según fuente;
si la relación no consta, no la inventes ni equipares respuesta y resolución.
Inicio/transición y cierre/reversibilidad: duración, hitos, entregas de documentación,
código, configuraciones, credenciales y activos cuando se exijan; inventario, formatos,
transferencia de conocimiento, colaboración con sucesor, continuidad, aceptación,
responsabilidades y costes. Plazo de garantía del servicio: duración, inicio, corrección
de defectos y condiciones, separado de garantías económicas. Devolución/borrado con A9;
titularidad y transferencia de licencias/equipos con A10.
""",
    "partners": """
A10 — MEDIOS, SUMINISTROS Y RESPONSABILIDADES:
Inventaría cada licencia, herramienta, plataforma, infraestructura/cloud, equipo,
material y servicio de terceros exigido: cantidad/capacidad, modalidad, titular,
quién aporta, paga, mantiene, renueva y transfiere/retira, plazo, soporte, garantía,
coste incluido o separado y restricciones. Separa medios del cliente y del adjudicatario,
uso de plataforma existente de obligación de adquirirla y dependencia de tercero de
obligación de subcontratar. Importe desconocido no elimina el coste a cargo exigido.
Fabricantes/proveedores: requisito material, nivel/especialización, equivalencias,
documento/carta/compromiso, fase de presentación, vigencia y alcance. Ausencia de carta
de fabricante o partnership no implica ausencia de licencias, soporte, medios ni costes.
Conserva restricciones de canal, suministro, reposición, stock, logística, mantenimiento,
renovaciones y fin del contrato solo si constan. No proponer proveedores ni precios.
""",
    "security": """
A9 — MEDIDAS, INCIDENTES Y DATOS:
ENS/ISO/RGPD no bastan como etiquetas: extrae medidas y obligaciones concretas,
alcance/sistemas, nivel, roles y responsables contractuales, accesos/privilegios,
confidencialidad, registros, conservación, copias, recuperación, cifrado, vulnerabilidades,
desarrollo seguro, auditorías, evidencias/certificados y momento de entrega si constan.
Incidentes y brechas: detección, comunicación, destinatario/canal, plazo y evento inicial,
contenido de notificación, escalado, respuesta/contención, recuperación, investigación,
informes y colaboración. No importar plazos legales no incluidos en los documentos.
Tratamientos, categorías de datos/interesados, instrucciones, encargado/responsable,
subencargados, autorización, ubicación y transferencias; conserva reparto de obligaciones.
Fin del servicio: devolución/portabilidad o borrado, elección y autorización, formatos,
plazos, copias de respaldo, excepciones de conservación, evidencias/certificado de
destrucción y obligaciones posteriores. Vincula responsabilidades y costes solo cuando
la fuente los atribuya; no dar por verificada una medida por citar una norma.
""",
}

OUTPUT_DETAIL = """
DETALLE QUE DEBE CONSERVARSE EN EL JSON Y EN EL RESUMEN POSTERIOR:
Integra los campos de tu especialidad en las secciones existentes, sin duplicar el
informe. Usa encabezados Markdown y tablas con columnas identificables; las tablas
se guardan en contenido.secciones[].tablas y el texto completo en salida_original.
Para cada obligación conserva sujeto contractual, objeto/valor/unidad, clasificación
literal, fase/hito/plazo, condiciones/excepciones, acreditación y fuente. Divide tablas
por materia si son muy anchas; no omitas detalle por comprimir una celda. No asignes
responsables internos: el sujeto es el que establece el contrato.
Termina con «Discrepancias y pendientes de aclaración»: versiones/literales, fuentes,
ámbito y efecto afectado, distinguiendo contradicción documental, dato no localizado
y limitación técnica atribuida al registro. Si no identificas discrepancias, indica
«No se han identificado discrepancias en la documentación revisada»; no certifiques
su inexistencia ni inventes filas. Revisa campos aplicables y señala lo no localizado
en su materia, sin convertir esta lista de búsqueda en obligaciones universales.
"""

PRESALES_REGISTER = """
REGISTRO DOCUMENTAL OBLIGATORIO EN ESTA MISMA RESPUESTA (no es otra llamada):
Empieza con una tabla Markdown titulada «Registro documental de preventa» con estas
tres columnas exactas: | Materia | Requisito completo | Fuente |.
Repite la materia en TODAS las filas, aunque coincida con la anterior. No omitas
su celda, no uses filas de solo requisito/fuente ni filas separadoras con una barra.
Cada fila contiene una regla completa y autosuficiente, redactada profesionalmente
para el informe final, con todas sus condiciones, excepciones, cifras, fase y plazos.
Materia es el apartado del dossier (por ejemplo «Facturación y cobro», «Equipo y
continuidad», «Seguridad e IA» o «Discrepancias pendientes de aclaración»). Fuente
identifica documento y página PDF/apartado real. No uses barras verticales dentro
de las celdas. Divide reglas distintas en filas, pero no separes una excepción de
la obligación a la que pertenece. No introduzcas etiquetas de agentes ni referencias
a JSON, prompts o fallos de procesamiento en los requisitos contractuales.
Esta tabla NO es una selección de puntos clave: debe contener TODOS los hechos
relevantes desarrollados en tu especialidad. No omitas datos por haberlos mencionado
antes. El programa conservará estos registros en requisitos_documentales del JSON
y trasladará su detalle completo al cuerpo del resumen, agrupándolo por materias.
La tabla no acredita por sí sola exhaustividad: contrasta cada apartado, anexo,
nota, modelo y excepción del documento completo antes de cerrar la respuesta.
El registro es la salida principal: prevalece sobre los antiguos índices de tablas
temáticas del prompt. Después solo añade discrepancias y aclaraciones necesarias,
sin repetir el registro en resúmenes, matrices o inventarios de tecnologías ausentes.
No rellenes con veinte filas de «no se exige»: una ausencia sin exención literal
no es requisito y se agrupa como no localizada sin reemplazar obligaciones positivas.
No escribas «con porcentajes definidos» o «según pliego»: incluye los valores.
"""

AUDIT_CHECKS = {
    'admin': '''
CONTROL ADICIONAL ADMINISTRATIVO-ECONÓMICO:
- Procedimientos por fases: compara anuncio inicial y publicación posterior;
  distingue solicitud, selección, invitación, oferta inicial, negociación y oferta
  final. Una fecha rotulada oferta en metadatos no prevalece sobre la fase que
  confirma la publicación posterior. Indica qué plazo depende de una invitación.
- Extrae número de rondas, extremos negociables, extremos no negociables y
  condición de aceptación de la oferta final frente a la inicial (incluida igualdad).
- Si participan varias sociedades, conserva presupuesto, contrato, bolsa y factura
  de cada una; componentes ordinarios frente a proyectos bajo demanda, importes
  fijos no reducibles y repartos de facturación. No confundir una bolsa monetaria
  con una bolsa de horas ni suponer consumo garantizado.
- Revisión de precios, modificación contractual y subrogación son reglas distintas.
  Conserva porcentajes al alza/a la baja y prohibición de nuevos precios unitarios.
  Contrasta opciones marcadas con frases genéricas no adaptadas en anexos.
- Prórrogas: separa posibilidad de acordarlas de su obligatoriedad para el
  adjudicatario una vez acordadas conforme al pliego, condiciones, preaviso y
  continuidad de prestaciones. No garantizar su activación no las hace voluntarias.
- Cobro: conserva plazo desde aprobación de conformidad, plazo para aprobarla,
  presentación correcta de factura y efectos sobre intereses; no basta mes vencido.
  Acreditaciones sociales a requerimiento: conserva también su plazo exacto y evento.
- Transparencia: extrae la obligación ordinaria de suministrar información, su
  destinatario, plazo y evento inicial (por ejemplo acuse de recibo), separada de
  los umbrales de retraso penalizables y del plazo para solicitar aclaraciones.
- Confidencialidad: conserva duración, inicio del cómputo y supervivencia tras
  finalizar. Si PCAP y PPT contienen previsiones distintas, refleja ambas con
  fuente sin convertirlas en extinción al cierre ni duración indefinida inferida.
- Busca topes independientes por componente fijo, variable y precio unitario. Extrae
  número de unidades, decimales, IVA y fórmula de totalización; comprueba producto
  unidades x tarifa frente al máximo publicado y registra cualquier diferencia.
- Transcribe porcentajes gratuitos/facturables y aplicación proporcional EN CADA
  factura, base total con mejora, límites de horas e importe, justificación y consumo
  no comprometido. No confundir horas gratuitas con aumento del precio ofertado.
- Extrae hito del primer pago, porcentaje fijo restante, divisor mensual, comienzo
  mínimo, mes vencido, conformidad y reglas de diciembre/anualidad. Contrasta texto
  y multiplicadores de cada año sin corregir erratas silenciosamente.
- Separa no valoración de páginas excedentes, exclusión esencial y subsanación.
  Extrae índice/anexos, márgenes, letra, interlineado y plazo para aclaraciones.
- Garantía antes de adjudicar: evento del requerimiento, cómputo y documentación;
  garantía complementaria condicional distinta de garantía técnica tras recepción.
- Recoge ausencia EXPRESA de revisión, subrogación, modificación y aumento de unidades
  solo en el ámbito que dice el pliego. Enumera condiciones especiales expresas sin
  añadir por intuición confidencialidad, datos o seguridad a esa categoría.
- Transcribe cada supuesto de penalidad y porcentaje/base, reiteraciones, resolución,
  procedimiento de alegaciones y referencias internas erróneas como pendientes.
''',
    'projects': '''
CONTROL ADICIONAL DE SOLVENCIA:
La remisión a un artículo para acreditar servicios NO permite concluir una exención
general de certificados de buena ejecución ni inventar su exigencia incondicional.
Conserva artículo y apartado, momento y carácter de requerimiento si constan.
Extrae regla de similitud CPV (número de dígitos), umbral, periodo y destinatarios.
Empresas nuevas: delimita qué solvencia tiene medios alternativos; no extiendas la
alternativa técnica a solvencia económica. ROLECE acredita SOLO extremos inscritos,
a tenor de lo reflejado y salvo prueba en contrario; no es una exención universal.
''',
    'award': '''
CONTROL ADICIONAL DE VALORACIÓN:
Desarrolla todas las hojas del árbol de criterios, no solo bloques generales: puntos,
méritos, condiciones acumulativas/alternativas y documentos. Una remisión a «ver
anexo» o a una sección no entregada no sustituye el baremo. Define variables,
unidad del descuento y normalización por mejor oferta; conserva redondeos.
Si la fórmula es no monótona, explica que aumentar descuento puede reducir puntos
y localiza el máximo y los extremos con cálculos etiquetados, sin cambiar el baremo.
Contrasta la petición de precio/hora en la memoria técnica con la prohibición de
datos económicos en ese sobre. Conserva las dos instrucciones como discrepancia.
Conserva características adicionales que el pliego diga que se valoran dentro del
proyecto técnico, con sus ejemplos y carácter opcional. Separa estas posibilidades
de mínimos funcionales, mejoras automáticas y subcriterios con puntuación propia.
No asignes puntos nuevos a ejemplos como carga de documentos o análisis de
sentimiento cuando el documento no establezca baremo independiente.
Asigna cada mejora a su sobre real. Ampliación de horario: incremento, continuidad
de la franja, mínimo de partida y puntos. Horas adicionales: tramos, gratuidad y
repercusión económica. Desarrolla cada subcriterio técnico y todos los escalones de
calidad, mínimo para continuar y efecto distinto del exceso de páginas.
Anormalidad: conserva los casos de uno/dos/tres o más licitadores, regla de grupos,
base, desigualdades y plazo exacto sin inventar días hábiles si no se especifican.
''',
    'profiles': '''
CONTROL ADICIONAL DE EQUIPO:
Extrae cuadros de horas íntegros: cantidades por perfil, sociedad y servicio,
periodo exacto (anual o conjunto de meses) y total de comprobación separado del
valor declarado. Diferencia recursos dedicados de compartidos con horas definidas
pero número de personas no definido. El mínimo no elimina guardias ni suplencias.
Una declaración de disponibilidad o certificado de experiencia genérico no rebaja
los años específicos del perfil. Idioma hablado/lectura técnica y certificaciones
deseables no son equivalentes a títulos o ISO empresariales obligatorios.
Dirigir proyectos, participar en ellos y analizar proyectos son experiencias distintas.
Conserva función exacta, dominio específico y años por perfil. Número de personas
no acredita jornada completa. Recoge todos los perfiles, número, títulos, experiencia,
conocimientos, acreditación de vínculo/precontrato/relación mercantil, declaración,
CV detallado y anonimizado, vida laboral y títulos si se exigen. Sitúa la prueba
solo en la fase requerida y no la traslades al sobre inicial por defecto.
Distingue plazo de constitución desde adjudicación de inicio del contrato; propuesta
de sustituto y autorización municipal no son permiso para interrumpir la cobertura.
Extrae interlocutor/suplente, canales, horario y plazo de designación separadamente.
''',
    'service': '''
CONTROL ADICIONAL TÉCNICO Y OPERATIVO:
Recoge por servicio y sociedad todas las volumetrías y sus periodos: dispositivos,
sesiones, máquinas y usuarios son unidades distintas y pueden solaparse.
Desarrolla soporte especializado y sus niveles; tecnologías y plataformas,
automatización, capacidad, copias/pruebas de recuperación y causa raíz cuando consten.
Transcribe todos los indicadores ANS con sus operadores exactos, ventana de cómputo,
tiempo de respuesta frente a resolución/proceso/fecha acordada, objetivo, base de
penalidad (servicio, sociedad o totalidad), acumulación y recurrencia/resolución.
Sustitución, solapamiento, ausencias, rotación, proyectos y parcheo son indicadores
distintos. No entregar solo ejemplos ni porcentajes sin denominador y plazo.
Contrasta plazos laborables/naturales y operadores del texto con los del anexo.
Transición: inicio, máximo, recursos/solapamiento no facturables y cláusula expresa
que debe incluir la oferta; planes de gobierno/operación y fecha de implantación.
Reversión: equipo habitual y ANS mantenidos, duración de solapamiento, espacio para
personal propio/del cliente/entrante, plan y bloqueo de última factura hasta aprobación.
Capacidad de instalaciones para un número de personas no es una plantilla mínima
adicional del proveedor ni un mérito técnico de equipo superior a ese número.
Extrae la modalidad exigida de la solución (SaaS, servicio gestionado u otra) como
parte del alcance. Separa gestión y operación del adjudicatario de componentes
básicos aportados por el cliente (tenant, landing zone, seguridad, identidad, redes)
y de quién paga licencias y consumos. No sustituir SaaS por «cloud» genérico.
Individualiza propiedad de productos del desarrollo, entrenamiento, modelos,
código y datos sintéticos, pautas DevSecOps/IAOps y entrega. Separa estos resultados
de datos y componentes preexistentes propios o de terceros y sus licencias.
Individualiza guía, manual o videotutorial de uso destinado a personas usuarias:
alternativas admitidas, contenido, fase de entrega y actualización durante contrato.
Es un entregable distinto de impartir formación a personal del cliente o entregar
documentación técnica de operación. No los sustituyas por una única mención a formación.
Conserva también prestaciones adicionales opcionales que pueden valorarse dentro
del juicio técnico, coordinadas con A4, sin convertir ejemplos en mínimos obligatorios.
Recoge el plazo ordinario de los requerimientos de información de transparencia,
su evento inicial y destinatario, además de las penalizaciones por demora.
Disponibilidad del asistente y atención humana son obligaciones distintas; recoge
salvedades, calendario, mínimo de agentes simultáneos y cobertura de ausencias.
Enumera TODOS los requisitos funcionales RAV/RPC o equivalentes: sustitución del
buscador, protocolos MCP/A2A cuando existan, concurrencia/tráfico, contexto, ámbito
temático, anonimización, transparencia IA, privacidad y consentimiento, trazabilidad
de fuentes, exportación, intervención humana, supervisión, encuestas y cuentas/perfiles.
Mecanismos obligatorios de mejora de respuestas no convierten los ejemplos RAG,
prompts y fine-tuning en tres técnicas acumulativamente exigidas. Extrae documento
de flujo/configuración, primera entrega y actualización, monitorización y frecuencia.
Separa mantenimiento evolutivo ordinario de proyectos avanzados de bolsa, autorización
de planes, finalización, consumo flexible y límite presupuestario de cada anualidad.
Incluye formación inicial y actualización, horas, asistentes, contenidos y modalidad.
Recoge aprobación de arquitectura y modificaciones antes de producción, carácter
esencial literal; entornos obligatorios/condicionales, contenerización, IaC/Git y
contradicción entre obligatorio/preferente si hay dos cláusulas identificadas.
Incluye Plataforma del Dato, cuadros de mando, licencias Premium del cliente y Pro
del contratista si constan. Extrae normas de accesibilidad y declaración con plazo.
Transferencia: periodo final, continuidad, todos los activos e informe, borrado seguro
propuesto en oferta, certificado y excepciones por conjunto de datos. Contrasta las
remisiones internas con títulos reales, sin reconstruir una numeración incorrecta.
''',
    'partners': '''
CONTROL ADICIONAL DE CLOUD Y TERCEROS:
Ausencia de carta/partner o documento llamado SLA back-to-back no exime de soporte,
expertos de fabricante, gestiones contractuales ni aseguramiento de ANS del producto.
Extrae portátiles, software, licencias, comunicaciones y teléfono por técnico;
procesador, memoria, discos y mejoras condicionadas si constan. Conserva también
logística, preparación/envío de material y responsabilidades concretas, sin negar
toda logística por no encontrar un plan con ese título.
Conserva la modalidad SaaS exigida y la responsabilidad de gestión y operación,
con las excepciones de infraestructura municipal. Diferencia titularidad de los
resultados generados del contrato y derechos/licencias de componentes preexistentes.
Clouds autorizados, exclusividad, acuerdo empresarial con proveedor, acceso a soporte
y reparto de gestión y pago son campos distintos. Aportar landing zone/conectividad
no implica que el cliente pague todos los componentes desplegados. Conserva quién
asume licencias, suscripciones, créditos, LLM/herramientas externos a plataforma
corporativa, tráfico y cambios de modelo. Recoge restricciones Marketplace/BYOL.
Ausencia de cartas, partner o matriz SLA back-to-back no elimina soporte cloud ni
soporte y garantía del fabricante. Distingue obligaciones de IAM y del adjudicatario.
''',
    'security': '''
CONTROL ADICIONAL DE SEGURIDAD E IA:
Separa cumplimiento operativo de ENS/ENI de certificación de empresa, categoría
documentada y normas ISO. La falta de certificado ENS no suprime medidas exigidas.
Confidencialidad general, plazo mayor y secreto indefinido de datos personales tienen
ámbitos diferentes: no imponer el plazo más corto a todos ni el más largo a todo.
Extrae seguridad de equipos no corporativos, monitorización, parcheo, licenciado,
privilegios, gestión de accesos y evidencias. Incidentes: sin dilación y límite máximo,
evento «conoció o debió conocer», contenido y destinatario; solicitudes de derechos
tienen su propio plazo. Subencargados: autorización expresa frente a aceptación por
silencio y plazos; conservación/devolución/borrado: conserva cláusulas incompatibles.
Propiedad intelectual: extrae expresamente titularidad de productos del desarrollo,
entrenamiento, modelos, código y datos sintéticos, incluida la cláusula MAIA cuando
exista. No sustituirla por entrega final ni por derechos sobre conjuntos de datos.
Conserva por separado derechos preexistentes propios/de terceros, licencia de uso,
excepciones de confidencialidad y facultades sobre los resultados generados.
Confidencialidad: diferencia plazo expreso desde conocimiento de la información y
subsistencia después de terminar el contrato. Presenta ambas previsiones de PCAP/PPT
sin imponer por intuición cinco años desde cierre o secreto indefinido para todo.
La ubicación EEE en regiones autorizadas NO permite inferir una prohibición general
de toda transferencia internacional ni autorización para realizarla.
POC de seguridad no es DPD: conserva designación o justificación, mecanismos en
oferta, riesgos iniciales validados y plan de tratamiento. Detalla configuración y
desarrollo seguros, accesos, autenticación condicional, logs, cifrado condicional,
parches, vulnerabilidades, auditorías, ciclo completo de incidentes, destinatario,
notificación y colaboración también durante garantía cuando así figure.
Lee enteras las cláusulas contractuales de IA, no solo ENS/RGPD: gestión iterativa de
riesgos, pruebas y umbrales antes de entrega, gobernanza/calidad/origen de datos,
documentación/instrucciones y actualización, registros y entrega final, transparencia,
supervisión humana competente, conformidad y corrección, explicación individual,
derechos de datos, entregas, excepciones de destrucción e indemnizaciones recíprocas.
Contrasta «no se precisa tratamiento personal» con conversación, anonimización,
registros, encuestas y privacidad: expón ambas cláusulas pendientes de aclaración,
sin declarar por intuición inexistencia de tratamiento o acuerdo de encargo obligatorio.
''',
}


PRESALES_EXTRACTION = """
OBJETIVO PRIORITARIO: DOSSIER DOCUMENTAL COMPLETO PARA PREVENTA.
Tu salida no es un resumen ejecutivo: es la base documental que permitirá a preventa
preparar y evaluar la oferta sin perder condiciones relevantes. No hay objetivo de
brevedad, páginas o ahorro de tokens. Amplía cuanto sea necesario, con información
respaldada y sin relleno. El resumen factual inicial NO sustituye el desarrollo.
Estas instrucciones prevalecen sobre peticiones genéricas de ser breve o conciso.

Dentro de ESTE ÚNICO análisis, revisa todos los documentos completos de tu ámbito,
incluidos anexos, modelos, tablas, notas, excepciones y remisiones. No te limites a
la cláusula cuyo título coincide con tu especialidad: una obligación puede aparecer
en penalizaciones, seguridad, modelo de oferta o condiciones de aceptación.
No presupongas que otro agente recuperará la condición que tú has encontrado.

Es relevante cualquier dato que cambie: admisión/exclusión; documentos y preparación
de oferta; puntuación; compromiso de medios; alcance/volumen; dependencia del cliente;
facturación y derechos de cobro; responsabilidad; aceptación; continuidad o salida.
Conserva requisitos obligatorios, criterios puntuables, opciones, derechos del cliente,
condiciones activables y excepciones. Distingue su naturaleza, sin convertir opciones
en prestaciones garantizadas. Recoge costes o gastos atribuidos por el contrato;
no inventes importes internos, márgenes, plantilla ni estimaciones comerciales.

EXTRACCIÓN ATÓMICA: una regla diferenciada por fila o párrafo. Para cada regla incluye
hecho completo, sujeto, ámbito, cantidad/unidad, hito y plazo, condición/excepción,
acreditación/entregable y fuente con apartado/página disponible. Incluye literal breve
cuando soporte una cifra, exención, clasificación, límite o discrepancia sensible.
No rellenes todos los campos con NO CONSTA si son ajenos a esa regla.
Una regla condicional debe contener las dos ramas: «si ..., entonces ...; en caso
contrario ...». No sustituirla por «A o B», «según pliego», «etc.» o «ver apartado».
Conserva TODOS los elementos de listas finitas de documentos, entregables, subcriterios,
tramos, penalizaciones y medidas aplicables; agrupar no puede eliminar sus condiciones.

CONTRASTE INTERNO ANTES DE RESPONDER (sin llamadas ni documentos adicionales):
1. Compara tablas generales y desarrollos, mínimos y mejoras, PCP y anexo técnico,
   cláusulas de inicio/plazos y modelos. Comprueba sumas de puntos y topes declarados,
   distinguiendo subtotal de componente. Si calculas una suma de comprobación,
   identifícala como tal; no reemplaces el valor declarado ni simules puntuaciones.
2. Conserva operadores exactos: superior no equivale a igual o superior. Si los
   intervalos se solapan o dejan un hueco, muestra sus extremos y pide aclaración;
   no los arregles cambiando mínimo por inferior ni asignando puntos no previstos.
3. Si se repite una categoría con valores distintos, conserva ambas etiquetas y
   valores. No cambies una categoría para hacer una tabla aparentemente coherente.
4. Solo llama esencial o especial a una obligación con esa calificación expresa
   aplicable a ella. Una penalización o posibilidad de resolución no basta.
5. Diferencia NO LOCALIZADO, NO ESPECIFICADO (obligación existente sin ese parámetro),
   REMITIDO A DOCUMENTO NO DISPONIBLE y EXENCIÓN EXPRESA. La continuidad puede estar
   exigida sin número de suplentes; un SLA puede estar remitido a un acuerdo futuro.
   No confundir falta de FTE, tarifa, RTO/RPO o fabricante nominal con inexistencia
   de obligación, cobertura, recuperación, licencias o compatibilidad tecnológica.
6. En «Discrepancias y pendientes» explica ambas cláusulas y el aspecto afectado.
   No cierres automáticamente con «sin discrepancias». Si solo hay una remisión,
   registra documento/apartado y el dato que impide verificar; no inventes su contenido.

AUTOLECTURA FINAL: verifica que cada cifra y condición relevante localizada aparece
en el desarrollo, no solo en el resumen inicial o la trazabilidad. Revisa especialmente
frases con «siempre que», «salvo», «a requerimiento», «antes de», «sin consumo»,
«no se garantiza», «adicional», «a cargo», «se acumulará» y «podrá». No termines el
informe tras cubrir solo requisitos generales: incluye sus consecuencias operativas.
"""

PRESALES_CHECKS = {
    "admin": """
COMPROBACIONES DE A2: desarrolla por separado importe máximo, importe ofertable y
facturable; fracción/porcentaje por factura; condiciones que cambian el inicio del pago;
aprobación de trabajos; demanda no garantizada; acumulación/caducidad de bolsas;
precio por unidad; gastos incluidos y conceptos excluidos. Cruza el régimen económico
con las bolsas del anexo técnico y el modelo de oferta sin inferir cómo se pagan si
esa relación no queda definida: déjala pendiente de aclaración.
Entrega una matriz por fase con TODOS los documentos, declaración frente a prueba,
quién los aporta, plazo y vigencia. Incluye acreditaciones que solo se aportan ante
empate o requerimiento. Desarrolla vigencia de oferta, inicio, formalización,
garantías y condiciones de cancelación. Una remisión no equivale a autorización
incondicional de subcontratación o cesión. No agrupar todas las obligaciones en
«condiciones especiales»: separa las categorías según respaldo literal.
""",
    "projects": """
COMPROBACIONES DE A3: cada requisito de solvencia debe permitir identificar qué
referencias o certificados hay que preparar y cuándo. Conserva contenido exigido de
las referencias, documentos alternativos, excepciones, experiencia de mantenimiento
si se admite, emisor y vigencia. Distingue relación de contratos de certificado de
buena ejecución. Contrasta plazos de certificación con los anexos de seguridad:
conserva alternativas y posibles incompatibilidades, no escojas un plazo único.
""",
    "award": """
COMPROBACIONES DE A4: desciende hasta CADA FILA puntuable de las tablas, no solo los
bloques principales. Incluye puntos propios, acreditación mínima (demostración,
capturas, fichas, CV, matrices, planes...), aspectos valorados y regla de aplicación.
Desarrolla niveles con su porcentaje y descripción, criterios de desempate en orden,
momento de acreditación y todas las reglas de anormalidad. Compara máximo general,
suma de componentes, tablas de equipo y desarrollo de experiencia/formación. No
presentes como compatibles una tabla y un desarrollo numéricamente incompatibles.
Si no hay plazo de justificación en las fuentes, indica la remisión exacta pendiente.
""",
    "profiles": """
COMPROBACIONES DE A8: conserva el nombre de la unidad de la tabla original (personas,
perfiles o puestos). Explica agrupación de perfiles permitida y límites, sin inferir
una plantilla de personas distintas. Separa dedicación ofertada de mínimo exigido,
horario de atención del servicio y jornada individual. Extrae experiencia sectorial,
funciones/conocimientos específicos y el hito en que los medios deben estar disponibles.
Cruza sustituciones con penalizaciones: comunicación previa, supuestos, consecuencias.
Si no se cuantifican suplencias o solapamientos, indica parámetro no especificado y
mantén las obligaciones de estabilidad, suficiencia y continuidad que sí consten.
""",
    "service": """
COMPROBACIONES DE A6: entrega una matriz completa de entregables por fase y criterios
de aceptación, incluidas pruebas, inventarios, manuales, informes y devolución.
Conserva mínimos de formación, duración/número de sesiones, modalidad, destinatarios
y materiales actualizables. Distingue servicio estándar disponible al inicio de la
configuración completa posterior y sus dependencias del cliente. Desarrolla toda la
bolsa: tareas, UT, autorización, cierre, saldo, acumulación y trabajos no imputables.
Si los tiempos se fijarán en un SLA posterior, explica qué debe acordarse; no los
inventes ni atribuyas el horario de monitorización a la atención de soporte.
Cruza las prioridades con penalizaciones conservando posibles erratas como pendientes.
Describe por separado garantía técnica, salida ordinaria, sobrevenida y transferencia.
""",
    "partners": """
COMPROBACIONES DE A10: lee también los anexos de seguridad para localizar licencias,
productos comerciales, herramientas, infraestructuras y mantenimiento a cargo del
adjudicatario. Incluye condiciones de compatibilidad con marcas del cliente y la
justificación de alternativas. No exigir marca nominal no exime de estas restricciones.
Conserva excepciones «salvo acuerdo contrario» y aplicabilidad según arquitectura o
datos. Distingue suministrar equipos al cliente de aportar equipos para operar el
servicio. No declares «sin hardware» porque el objeto principal sea SaaS.
""",
    "security": """
COMPROBACIONES DE A9: inventaría cada medida aplicable con su identificador original
si existe, obligación, condición, evidencia y responsable. Separa medidas universales
de las que dependen de datos sensibles, cloud público, acceso remoto o arquitectura.
Detalla destinatarios/canales, eventos que activan comunicaciones, plazos expresos,
integración de notificaciones, colaboración y preservación de pruebas. No inventes
«inmediato» como plazo si el texto solo dice «una vez identificado».
Conserva campos mínimos de logs, certificados de destrucción, inventarios y auditorías,
frecuencias, excepciones, entrega/retención e integración. Contrasta plazos ENS/ISO
entre documentos. RTO/RPO no especificados no eliminan planes de continuidad.
DPO «en su caso» no equivale a obligación universal ni exención de designación.
""",
}

EDITORIAL_PRESALES = """
RESUMEN FINAL PARA PREVENTA: SÍNTESIS COMPLETA, NO RECORTE DE CONDICIONES.
Mantén el diseño del ejemplo, no su extensión ni su nivel de detalle. No hay máximo
de páginas. La concisión consiste en eliminar repeticiones, nunca requisitos únicos.
El cuerpo debe permitir conocer qué ofertar, documentar, acreditar, aportar, ejecutar,
facturar, mantener y devolver, además de qué puntúa, excluye o requiere aclaración.

Antes de redactar, inventaría internamente TODOS los hechos relevantes de los siete
especialistas y asigna cada uno a una sección. A1 solo orienta; nunca prevalece sobre
el detalle. Para cada hecho conserva sujeto, unidad/valor, fase, hito, plazo, condición,
excepción, acreditación y fuente disponibles. Une duplicados solo si coinciden también
sus condiciones. Integra diferencias, no elijas la versión más corta de varios agentes.
No es necesario copiar tablas de extracción: distribuye los hechos en prosa, listas
y varias tablas de hasta cuatro columnas, con referencias junto a cada bloque.

DESARROLLOS QUE NO SE PUEDEN REDUCIR A UNA MENCIÓN cuando consten en el JSON:
- Modalidad SaaS exigida, gestión/operación y componentes básicos del cliente,
  diferenciadas de atribución de costes. Propiedad municipal de productos del
  desarrollo, entrenamiento, modelos, código y datos sintéticos, separada de
  derechos sobre datos y componentes preexistentes de terceros.
- Prórrogas: activación no garantizada y obligatoriedad para el adjudicatario
  cuando se acuerden conforme al pliego, con continuidad de la prestación.
- Plazos completos de cobro, aprobación de conformidad y factura, y plazos de
  acreditación documental a requerimiento; no reemplazarlos por «plazo previsto».
- Todas las filas puntuables y sus acreditaciones, niveles/porcentajes, tramos,
  límites y desempates; fórmulas con variables y ámbito. Desarrolla BAREMOS COMPLETOS.
- Facturas: importe/fracción, periodicidad, conformidad, regla condicional del pago;
  bolsa/unidades: autorización, consumo no garantizado, remanente y exclusiones.
- Documentos por fase, presentación frente a acreditación, modelos y entregables.
- Equipo: perfiles frente a personas, experiencia específica, disponibilidad,
  dedicación ofertada, sustituciones y cobertura sin dimensionamiento inventado.
- Tabla de entregables por fase, formación mínima, aceptación y dependencias de inicio.
- Ayuda al usuario (guía, manual o videotutorial), momento y actualización,
  diferenciada de formación al cliente y documentación técnica.
- Plazo ordinario de transparencia con evento de cómputo, distinto de umbrales
  sancionadores; confidencialidad con duración, evento inicial y supervivencia.
- Características adicionales valorables en juicio técnico, con ejemplos y carácter
  opcional, sin inventar mejoras automáticas ni puntuaciones independientes.
- Medios/licencias/herramientas y quién los aporta, condiciones y alternativas.
- Cada SLA y penalización relevante, base, supuesto, límite y discrepancias de etiquetas.
- Seguridad en subapartados de medidas, incidentes/comunicaciones, evidencias,
  certificaciones, continuidad y cierre; nunca condensar todo en «ENS/ISO/RGPD».
- Garantías económicas frente a garantía del servicio; devolución, transferencia,
  supresión y certificados con condiciones y responsabilidades.

REVISIÓN FINAL SEMÁNTICA: recorre cada hecho del JSON y comprueba dónde está desarrollado
en el CUERPO. Un encabezado o una palabra coincidente no acreditan cobertura. Añade los
hechos omitidos en su sección y corrige los alterados. En la pasada de revisión no
dupliques el párrafo de pago para aparentar cobertura: incorpora la condición faltante.
No devuelvas correcciones vacías si has perdido subcriterios, excepciones o evidencias.
Comprueba que la conclusión no convierte NO CONSTA en NO EXIGIDO, ni introduce una
clasificación contractual nueva. Si el JSON se contradice, presenta las versiones
como discrepancia entre extracciones pendiente de contraste, salvo dos cláusulas
documentales identificadas. No reconstruyas hechos ausentes con conocimientos generales.
"""


VALIDATION_FOCUS = {
    'admin': 'Agrupa por fase: oferta y sobres, acreditación del propuesto adjudicatario y ejecución. Distingue '
             'prohibiciones, condiciones y datos informativos. Conserva órgano marcado del PCAP y metadato XML.',
    'projects': 'Consolida evidencia positiva por lote y subcampo antes de declarar ausencias. Distingue mínimo de '
                'la alternativa de acreditación (clasificación, medios externos, compromiso de seguro o documento).',
    'award': 'Agrupa por lote y tipo de criterio. Cita Anexo XI y su apartado localizable. Transcribe la fórmula '
             'con variables y límites. Suma los subcriterios de primer nivel sin contar dos veces sus desgloses.',
    'service': 'Organiza por lote y subservicio. Separa inventario actual, volumetría de referencia y requisito '
               'obligatorio. Conserva versión, cantidad, unidad y fuentes de tablas. Cita la prelación expresa.',
    'profiles': 'Identifica lote y servicio en cada ficha. Cita también cada cifra de tablas y ficha histórica '
                'con página o apartado, aunque varias filas compartan origen. Distingue dotación actual de mínimos.',
    'security': 'Distingue acreditación requerida, control operativo y condición contractual. Identifica qué lote '
                'y servicio aplica y reúne las fuentes de una misma obligación.',
    'purchases': 'Distingue productos de referencia y licencias exigidas. Cita anexos técnicos y hojas económicas '
                 'para cantidades y unidades de recurso, y conserva las condiciones de equivalencia y soporte.',
}


def extraction_requirements(agent):
    scope = ''
    register = PRESALES_REGISTER
    if agent == 'profiles':
        register = '''
FORMATO DEL REGISTRO DE A8 (prevalece sobre cualquier petición genérica de tablas):
Entrega fichas Markdown agrupadas por perfil y por continuidad del equipo.
Un encabezado por perfil o materia y viñetas factuales debajo, una por requisito.
Cada viñeta contiene el requisito completo y su fuente entre corchetes en la MISMA
viñeta: «- Experiencia mínima de 4 años en ... [PPT.pdf, página 8]».
Usa valores exclusivamente de los documentos; el ejemplo ilustra el formato.
Incluye después fichas de horas/periodos, cobertura, acreditación, incorporación,
sustitución y discrepancias, solo con hechos localizados. Las cantidades, experiencia,
conocimientos, medios y todas las condiciones deben mantenerse completas.
No utilices la tabla larga «Materia | Requisito completo | Fuente»: repetir la
misma primera columna en cientos de filas está causando bucles de generación.
Reúne las fuentes coincidentes en la misma viñeta. No repitas requisitos para cada
documento ni entre fichas. Termina después de cubrir todas las materias de equipo.
El programa convierte todas las fichas y viñetas a registros JSON y al resumen.
'''
        scope = '''
CONTROL DE ALCANCE Y FINALIZACIÓN DE A8:
El registro contiene exclusivamente equipo, perfiles y continuidad: mínimos,
horas y periodos, experiencia/conocimientos, dedicación, cobertura, sustitución,
medios del equipo y documentación que los acredita (CV, títulos, vínculo, etc.).
Las escrituras de la empresa, DEUC, garantías financieras, declaraciones generales
de igualdad y el contrato de encargado de tratamiento pertenecen a A2/A3/A9.
Extrae aquí solo su efecto directo y específico sobre el equipo, si existe.
Cada obligación aparece una única vez, reuniendo sus fuentes; si el anexo repite
el cuerpo del pliego, añade la referencia al mismo registro en vez de copiarlo.
Al completar la revisión del equipo y sus discrepancias, TERMINA la respuesta.
No reinicies listas ni vuelvas a recorrer documentación administrativa general.
'''
    return (DOCUMENTARY_PRECISION + AGENT_COVERAGE[agent] + OUTPUT_DETAIL +
            PRESALES_EXTRACTION + PRESALES_CHECKS[agent] + AUDIT_CHECKS[agent] + register + scope +
            '\nCONTROL FINAL DE CAPA 1: ' + VALIDATION_FOCUS.get(agent, '') +
            ' Registra cada hecho una vez con sus fuentes. Deja los avisos de lectura y los datos no localizados '
            'fuera de la tabla contractual; si la entrega es parcial, limita el aviso a esa entrega. '
            'La fuente identifica archivo y página, apartado, hoja o celda disponibles, sin inventar localizadores.')


def numeric_source_index(documents, agent):
    """Índice literal de cifras dentro del mismo prompt de documentos completos.

    No selecciona una versión abreviada del pliego, no añade otra llamada y no
    asigna semántica a los importes. Ayuda a detectar tablas que se han saltado.
    """
    import re
    if agent not in ('admin', 'profiles'):
        return ''
    entries = []
    for doc in documents:
        if not doc.text:
            continue
        for page in re.split(r'(?=\[Pagina PDF \d+\])', doc.text):
            if not page.strip():
                continue
            marker = re.match(r'\[Pagina PDF (\d+)\]', page)
            location = 'página PDF ' + marker[1] if marker else 'texto extraído sin paginación'
            if agent == 'profiles' and marker is None:
                # Las páginas web generales no son tablas paginadas del equipo.
                # Su texto sigue íntegro en los documentos; no duplicarlo en este índice.
                continue
            if agent == 'admin':
                if re.search(r'plazo de presentaci[oó]n de (?:ofert|solicitud)|solicitudes de participaci[oó]n', page, re.I):
                    entries.append(f'Publicación/fase a contrastar en el texto completo: {doc.ref.name}, {location}.')
                amounts = list(dict.fromkeys(re.findall(
                    r'\d[\d., \u00a0]*\s*(?:€|EUR\b|euros\b)', page, re.I)))
                if amounts:
                    entries.append(f'{doc.ref.name}, {location}: ' + '; '.join(x.strip() for x in amounts))
                    if re.search(r'presupuesto|facturaci[oó]n|anualidades', page, re.I) and re.search(r'empresa|sociedad|entidad|componente|concepto', page, re.I):
                        entries.append(f'Tabla económica y contexto en el texto completo: {doc.ref.name}, {location}.')
            elif re.search(r'horas', page, re.I) and re.search(r'meses|anuales|recursos|técnicos', page, re.I):
                # El índice es una ayuda de navegación, no una segunda copia de
                # páginas enteras. El documento íntegro ya está en la solicitud.
                numeric_lines = list(dict.fromkeys(line.strip() for line in page.splitlines()
                    if re.search(r'\d', line) and len(line.strip()) <= 500
                    and not line.startswith('[Pagina PDF ')))
                entries.append(f'{doc.ref.name}, {location}:\n' + '\n'.join(numeric_lines))
    if not entries:
        return ''
    return ('\n\nÍNDICE LITERAL DE CIFRAS PARA EL CONTROL FINAL (no sustituye los documentos completos):\n'
            + '\n'.join(entries)
            + '\nContrasta cada cifra con su tabla y unidad en el documento completo. Incluye '
            'los importes por sociedad/componente, bolsas y horas aplicables, con su periodo '
            'y condición. No reemplaces una tabla cuantificada por nombres de servicios '
            'o «según pliego». No conviertas cifras aisladas del índice en obligaciones nuevas. '
            'Cuando existan varias publicaciones, compara campo por campo las fechas y su fase; '
            'un campo vacío en una publicación posterior no confirma la fecha antigua como cierre de ofertas. '
            'Entrega al comienzo del registro el desglose económico y las fases contrastadas, antes de las cláusulas generales.\n')


def editorial_requirements():
    return "\n" + DOCUMENTARY_PRECISION + EDITORIAL_PRESALES + """
COBERTURA EDITORIAL DE CAPA 1:
Las responsabilidades siguientes son una lista de comprobación, NO hechos nuevos.
Conserva en el resumen los detalles presentes en el JSON, sus condiciones, excepciones,
fases y fuentes. Si faltan, no los reconstruyas. No exijas que A1 contenga el detalle
de especialistas. No muestres IDs de agentes ni esta lista en el informe final.
""" + "\n".join(AGENT_COVERAGE.values()) + """
CONTROL DEL BORRADOR CONTRA LA FUENTE:
Si existe revision_documental, sus registros son la extracción contrastada con citas
localizadas, NO una garantía de completitud. Conserva íntegro el texto de cada campo
detalle en el CUERPO del informe, dentro de párrafos, listas o celdas; puedes añadir
transiciones y agrupar por materia pero no acortar esos textos ni alterar condiciones.
No incluyas IDs ni matrices de auditoría. Acompaña los bloques con las fuentes de
las evidencias. Puedes reunir detalles idénticos una sola vez. No basta mencionarlos
en introducción o conclusión. Desarrolla los temas en secciones independientes.
Los registros de discrepancias conservan ambas versiones; no elijas una al concluir.
Los avisos de procesamiento se imprimen desde el registro por el programa: no los
reformules como enlaces no descargables ni los repitas en introducción o cuerpo.
Contrasta por materia cada dato, fase, sujeto, unidad, plazo, fórmula, excepción,
documento y calificación de obligación. Corrige errores/omisiones del borrador cuando
el JSON aporte respaldo inequívoco; no los publiques como contradicciones del pliego.
Si solo discrepan los agentes, atribuye la discrepancia a las extracciones y déjala
pendiente de contraste. Solo habla de contradicción del pliego con dos cláusulas
identificadas y su contexto. No elimines esa contradicción para hacer coherente el resumen.
Los campos registro_procesamiento, documentos_fuente y avisos_procesamiento de entrada
se pueden citar como avisos registrados, no como
hechos comprobados al leer PDFs ni como auditoría de una ejecución anterior.
Integra el detalle en el formato AGE existente: prosa, subapartados, listas, tablas
de 2-4 columnas, fuentes junto al bloque y Conclusión operativa. Usa varias tablas o
párrafos para conservar reglas completas. No vuelques las matrices de extracción.
Incluye cierre/transferencia y discrepancias pendientes cuando haya base documental.
En capa 1 explica factores de coste y reglas de ingreso del contrato, nunca calcula
rentabilidad, coste de sustituciones, FTE, precio recomendado ni viabilidad empresarial.
"""
