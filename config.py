import os

KEY_VAULT_NAME = "KV-ROOPUSE-SLACKBOT-P"


def get_setting(name: str, default: str = None):
    return os.getenv(name, default)


DB_PASSWORD = get_setting("DbPassword")
DB_USER = get_setting("DbUser")
DB_HOST = get_setting("DbHost")
DB_NAME = get_setting("DbName")
