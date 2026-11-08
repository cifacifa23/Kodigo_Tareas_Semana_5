from typing import List, Dict, Any

def run_normalization(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    normalized = []
    eur_to_usd = 1.08

    for item in records:
        amount = item.get("amount", 0.0)
        currency = item.get("currency", "USD").upper()
        raw_status = item.get("status", "PENDING").upper()

        # Conversión de divisa
        if currency == "EUR":
            amount = round(amount * eur_to_usd, 2)
            currency = "USD"

        # Validación de estado
        if amount <= 0:
            status = "INVALID"
        elif raw_status in ["COMPLETED", "PENDING", "FAILED"]:
            status = raw_status
        else:
            status = "PENDING"

        normalized.append({
            "id": item.get("id"),
            "amount": amount,
            "currency": currency,
            "status": status
        })

    return normalized