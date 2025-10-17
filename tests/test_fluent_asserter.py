import pytest

from hamlette import *


def test_rshift_operator_success():
    assert that(10) >> greater_than(5)
    assert that(10) >> less_than(20)


def test_rshift_operator_failure():
    with pytest.raises(AssertionError) as e:
        assert that(10) >> greater_than(15)


def test_comparison_operators_success():
    assert that(10) == 10
    assert that(10) != 5
    assert that(10) > 5
    assert that(10) >= 10
    assert that(10) < 20
    assert that(10) <= 10


def test_comparison_operators_failure():
    with pytest.raises(AssertionError):
        assert that(10) == 5

    with pytest.raises(AssertionError):
        assert that(10) != 10

    with pytest.raises(AssertionError):
        assert that(10) > 15

    with pytest.raises(AssertionError):
        assert that(10) >= 15

    with pytest.raises(AssertionError):
        assert that(10) < 5

    with pytest.raises(AssertionError):
        assert that(10) <= 5


def test_single_line_error_message_with_reason(monkeypatch):
    monkeypatch.setenv("HAMLETTE_SINGLE_LINE", "1")

    with pytest.raises(AssertionError) as exc:
        # Pass reason on the matcher side
        assert that("hi") >> (has_length(3), "length check")

    msg = str(exc.value)
    assert "length check. " in msg
    assert "Expected " in msg and ", but " in msg
    assert "\n" not in msg  # single-line only


def test_multiline_error_message_with_reason(monkeypatch):
    monkeypatch.setenv("HAMLETTE_SINGLE_LINE", "0")
    
    with pytest.raises(AssertionError) as exc:
        assert that("hi") >> (has_length(3), "length check")

    msg = str(exc.value)
    assert "length check" in msg
    assert "Expected:" in msg
    assert "but:" in msg
    assert "\n" in msg  # multi-line formatting
