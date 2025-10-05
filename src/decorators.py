import logging
from functools import wraps
from typing import Any


def log(filename=None):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        if filename:
            handler = logging.FileHandler(filename, encoding="utf-8")
        else:
            handler = logging.StreamHandler()
        logger.addHandler(handler)

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info("Начало работы программы")
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.exception("%s error: %s. Inputs:  %s,  %s", func.__name__, e, args, kwargs)
                logger.info("Окончание работы программы")
                return "Ошибка в программе, проверьте введенные значения"
            else:
                logger.info(f"Результат работы функции {func.__name__}:{result}")
                logger.info("Окончание работы программы")
                return result
        return wrapper

    return my_decorator
