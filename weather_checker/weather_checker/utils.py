import os

from django.conf import settings


def get_credential(secret_key: str, default_value: str, secret_dir: str = None) -> str:
    """
        Get credential value from secret files

        :param secret_key: Credential Key
        :param default_value: Default value if credential not found
        :param secret_dir: Secret file directory
    """
    if not secret_dir:
        secret_dir = settings.SECRET_DIRECTORY

    try:
        with open(os.path.join(secret_dir, secret_key)) as file_secret:
            return file_secret.read()

    except FileNotFoundError:
        return default_value
