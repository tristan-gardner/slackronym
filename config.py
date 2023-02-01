from key_vault import get_secret

KEY_VAULT_NAME = "KV-ROOPUSE-SLACKBOT-P"


def get_setting(name: str, default: str = None):
    try:
        val = get_secret(KEY_VAULT_NAME, name)["value"]
        return val
    except Exception:
        return default


DB_PASSWORD = get_setting("DbPassword")
DB_USER = get_setting("DbUser")
DB_HOST = get_setting("DbHost")
DB_NAME = get_setting("DbName")
