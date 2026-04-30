from typing import Any

LOGGING_FILE = open("babi_logging.txt", "w")


def log(*args: Any, **kwargs: Any) -> None:
    print(*args, **kwargs, flush=True, file=LOGGING_FILE)
