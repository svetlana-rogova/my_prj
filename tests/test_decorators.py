from src.decorators import log


def test_log():
    @log(filename=None)
    def add(a, b):
        return a + b

    assert add(1, 2) == 3

    @log(filename=None)
    def add(a, b):
        return a / b

    assert add(1, 0) == "Ошибка в программе, проверьте введенные значения"
