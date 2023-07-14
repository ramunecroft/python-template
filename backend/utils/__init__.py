import logging
import os
from pathlib import Path

from rich.logging import RichHandler


def get_envfile():
    env_variables = ["DEVELOPMENT", "PRODUCTION"]
    for env in env_variables:
        print(env)
        if os.environ.get(env):
            print(f".env.{env.lower()}")
            env_file_path = str(
                (Path(__file__).resolve().parents[2] / "f.env.{env.lower()}")
            )
            return env_file_path
    return None


def setup_logger(name: str, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        # Set RichHandler to handle the log
        rich_handler = RichHandler()
        rich_handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s - %(module)s - %(funcName)s - %(message)s",
            )
        )

        logger.addHandler(rich_handler)
        logger.setLevel(level)

    return logger
