# Refactorización de Agente de IA: Arquitectura Modular basada en Skills

**Autor:** Carlos Isaac Flores Aparicio  
**Materia:** AI for Developers  
**Entorno de desarrollo:** Visual Studio Code / Python 3  

---

## 1. Diagnóstico del Proyecto Anterior (Monolítico)
En versiones anteriores, el procesamiento de entradas y las decisiones del agente se encontraban fuertemente acoplados:
* **Lógica acoplada:** Las reglas de negocio (limpieza de cadenas, normalización de monedas y filtrado de anomalías) se ejecutaban en el mismo script o bloque donde se definía la personalidad del agente.
* **Falta de extensibilidad:** Agregar una nueva capacidad requería modificar la función principal de ejecución, elevando el riesgo de efectos colaterales.
* **Rigidez de prompts:** Las instrucciones operativas estaban incrustadas en cadenas de texto fijas, impidiendo su versionado o reutilización como herramientas independientes.

---

## 2. Arquitectura de la Solución Refactorizada
Se aplicó un patrón modular inspirado en arquitecturas de **Agent Skills declarativas** y desacoplamiento de componentes:

* **Estructura Declarativa (`skill.md`):** Cada skill define en su archivo Markdown metadatos en formato YAML Frontmatter (`name`, `description`, `argument-hint`) e instrucciones de negocio directas para el modelo.
* **Separación de responsabilidades:**
  * `skills/`: Contiene módulos aislados e independientes.
  * `loader.py`: Parsea dinámicamente los metadatos de las skills y asocia la lógica ejecutable.
  * `agents/custom_agent.py`: Actúa exclusivamente como orquestador; no contiene lógica dura de cálculo o normalización.
* **Inyección dinámica:** El agente registra capacidades a través del método `.register_skill()` sin conocer la implementación interna de cada una.

---

## 3. Catálogo de Skills Implementadas

| Skill Name | Archivo de Especificación | Entradas | Salidas Clave | Responsabilidad |
| :--- | :--- | :--- | :--- | :--- |
| `transaction-data-normalizer` | `skills/normalizador_datos/skill.md` | Lista de transacciones en bruto | Lista normalizada en USD | Valida integridad de campos, unifica divisa (EUR $\rightarrow$ USD) y marca estados inválidos. |
| `transaction-anomaly-auditor` | `skills/auditor_metricas/skill.md` | Lista de transacciones limpias | Totales, promedios, valores atípicos y veredicto | Aplica reglas de negocio financiero para auditar montos que excedan el umbral establecido. |

---

## 4. Archivos de Entrada (`data/`)
* **`test_transactions.json`**: Contiene un conjunto balanceado de transacciones heterogéneas que ponen a prueba:
  * Registros normales en USD.
  * Conversión de monedas internacionales (EUR).
  * Montos anómalos superiores al umbral ($2,300.50 y $15,000.00).
  * Datos con anomalías de negocio (montos negativos $\le 0$).

---

## 5. Instrucciones de Instalación y Ejecución

1. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .\.venv\Scripts\Activate.ps1