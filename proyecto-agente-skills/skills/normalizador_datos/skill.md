---
name: transaction-data-normalizer
description: "Normaliza registros crudos de transacciones. Se activa cuando se solicita limpiar datos, convertir divisas o estandarizar estados."
license: MIT
metadata:
  author: Carlos Flores
  version: "1.0.0"
argument-hint: "[records-list]"
---

# Transaction Data Normalizer

## Directivas:
1. Asegurar que los estados sean siempre en mayúsculas: `COMPLETED`, `PENDING` o `FAILED`.
2. Convertir registros en EUR a USD usando factor 1.08.
3. Marcar registros con montos menores o iguales a 0 con el estado `INVALID`.