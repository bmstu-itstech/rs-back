import os
from pathlib import Path
from dotenv import load_dotenv
from typing import List


class EnvIsNotDefined(Exception):
    def __init__(self, key: str):
        super().__init__(f'environment variable {key} is not defined')


def load_env():
    env_path = Path(__file__).parent.parent / '.env'
    if not env_path.exists():
        env_path = Path(__file__).parent / '.env'

    load_dotenv(env_path, override=True)


load_env()


def env_required(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise EnvIsNotDefined(key)
    return value


def env_with_default(key: str, default: str = '') -> str:
    return os.getenv(key, default)


def env_with_default_bool(key: str, default: str = '') -> str:
    return os.getenv(key, default) == 'True'


def env_with_default_int(key: str, default: int = 0) -> int:
    try:
        return int(os.getenv(key, default))
    except Exception:
        return default


def env_list_with_default(key: str, default: str = '') -> List[str]:
    return [
        value.strip() for value in os.getenv(key, default).split() if value.strip()
    ]
