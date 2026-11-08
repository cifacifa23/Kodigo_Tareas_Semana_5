from typing import List, Dict, Any

def run_audit(records: List[Dict[str, Any]], threshold: float = 1000.0) -> Dict[str, Any]:
    valid_records = [r for r in records if r.get("status") != "INVALID"]
    amounts = [r["amount"] for r in valid_records]

    total = sum(amounts)
    avg = total / len(amounts) if amounts else 0.0
    outliers = [r for r in valid_records if r["amount"] > threshold]

    return {
        "total_records": len(records),
        "valid_records_count": len(valid_records),
        "total_amount_usd": round(total, 2),
        "average_amount_usd": round(avg, 2),
        "outliers_found": len(outliers),
        "outliers": outliers,
        "audit_verdict": "REVISION_REQUERIDA" if len(outliers) > 0 else "APROBADO"
    }