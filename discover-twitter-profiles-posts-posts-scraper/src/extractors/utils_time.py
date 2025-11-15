from datetime import datetime, timezone

def utc_timestamp() -> str:
    """Returns current UTC timestamp ISO formatted."""
    return datetime.now(timezone.utc).isoformat()