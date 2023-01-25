from key_vault import get_secret


def get_setting(name: str, default: str = None):
    try:
        val = get_secret(name)["value"]
        return val
    except Exception:
        return default


DB_PASSWORD = get_setting("DB_PASSWORD")
DB_USER = get_setting("DB_USER")
DB_HOST = get_setting("DB_HOST")
DB_NAME = get_setting("DB_NAME")
