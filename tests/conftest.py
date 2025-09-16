import pytest


@pytest.fixture
def standard_number():
    return "7000792289606361"


@pytest.fixture
def short_number():
    return ""


@pytest.fixture
def word():
    return "python"


@pytest.fixture
def long_number():
    return "70007922896063617000792289606361"
