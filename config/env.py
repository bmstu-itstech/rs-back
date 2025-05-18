import os
from dotenv import load_dotenv


load_dotenv()


class EnvIsNotDefined(Exception):
    def __init__(self, key: str):
        super().__init__(f'environment variable {key} is not defined')


def env_required(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise EnvIsNotDefined(key)
    return value


def env_with_default(key: str, default: str = '') -> str:
    return os.getenv(key, default)


def env_with_default_bool(key: str, default: str = '') -> str:
    return os.getenv(key, default) == 'True'


def env_list_with_default(key: str, default: str = '') -> str:
    return [
        host.strip() for host in os.getenv(key, default).split() if host.strip()
    ]
