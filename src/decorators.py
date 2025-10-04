import logging
from functools import wraps


def log(filename=None):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    if not logger.handlers:
        if filename:
            handler = logging.FileHandler(filename, encoding="utf-8")
        else:
            handler = logging.StreamHandler()
        logger.addHandler(handler)

    def my_decorator(func):
        @wraps(func)
        def wrappers(*args, **kwargs):
            logger.info("Начало работы программы")
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.exception("%s error: %s. Inputs:  %s,  %s", func.__name__, e, args, kwargs)
                print("Программа упала с ошибкой")
                logger.info("Окончание работы программы")
            else:
                logger.info(f"Результат работы функции {func.__name__}:{result}")
                logger.info("Окончание работы программы")
                return result

        return wrappers

    return my_decorator
