---
name: transaction-anomaly-auditor
description: "Audita transacciones normalizadas, calcula métricas operativas y detecta importes atípicos sobre un umbral."
license: MIT
metadata:
  author: Carlos Flores
  version: "1.0.0"
argument-hint: "[threshold-amount]"
---

# Transaction Anomaly Auditor

## Directivas:
1. Calcular el total monetario y el promedio por transacción.
2. Identificar registros individuales que superen el umbral configurado ($1,000.00 por defecto).
3. Determinar el estado general de la auditoría: `APROBADO` o `REVISION_REQUERIDA`.