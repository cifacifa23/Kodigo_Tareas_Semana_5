# Kodigo_Tareas_Semana_5
El estudiante deberá crear desde cero una API utilizando FastAPI, que sirva como base para la integración de un agente de IA personalizado. La API deberá exponer uno o más endpoints simples que representen una funcionalidad clara (por ejemplo: procesamiento de texto, análisis de prompts, validación de entradas o generación controlada de respuestas)


# 🤖 AI Agent Refactoring: Architecture Based on Custom Skills

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/IDE-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![Architecture](https://img.shields.io/badge/Pattern-Modular%20Agent%20Skills-brightgreen)](#arquitectura-de-la-solución)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Proyecto Académico:** AI for Developers  
> **Autor:** Carlos Isaac Flores Aparicio  
> **Objetivo:** Refactorizar un flujo de agente de IA desde un enfoque monolítico hacia una arquitectura modular, extensible y declarativa basada en **Skills personalizadas** (`skill.md`).

---

## 📌 1. Diagnóstico del Proyecto Anterior (Monolítico)

En implementaciones preliminares, el flujo de procesamiento presentaba problemas habituales de acoplamiento:

* **Lógica Acoplada:** Las reglas de negocio (limpieza de datos, conversiones de divisa y detección de anomalías) se encontraban incrustadas en el mismo bloque donde se configuraba el agente.
* **Rigidez:** Incorporar una nueva capacidad requería modificar directamente el script principal, aumentando el riesgo de errores colaterales.
* **Falta de Abstracción Declarativa:** Las instrucciones para el LLM no contaban con metadatos estandarizados, impidiendo que el agente descubriera o invocara herramientas de forma autónoma.

---

## 🏛️ 2. Arquitectura de la Solución

El proyecto fue rediseñado bajo un patrón de **Inyección de Dependencias y Skills Declarativas**:

```text
proyecto-agente-skills/
│
├── .gitignore                   # Exclusión de entornos virtuales y cachés
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación técnica completa
├── main.py                      # Punto de entrada y orquestación
│
├── data/
│   └── test_transactions.json   # Dataset heterogéneo de prueba
│
├── agents/
│   ├── __init__.py
│   └── custom_agent.py          # Clase orquestadora desacoplada
│
└── skills/
    ├── loader.py                # Parseador de metadatos YAML/Markdown
    ├── auditor_metricas/        # Skill de auditoría financiera
    │   ├── skill.md             # Especificación declarativa
    │   └── logic.py             # Ejecución determinista
    └── normalizador_datos/      # Skill de saneamiento de datos
        ├── skill.md             # Especificación declarativa
        └── logic.py             # Ejecución determinista
