import pytest


@pytest.fixture(autouse=True)
def single_line_messages(monkeypatch):
    monkeypatch.setenv("HAMLETTE_SINGLE_LINE", "1")
