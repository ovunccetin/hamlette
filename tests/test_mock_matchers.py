from unittest.mock import Mock

import pytest

from hamlette import that
from hamlette.mock import *


@pytest.fixture
def fn_never_called() -> Mock:
    return Mock(name="fn_never_called")


@pytest.fixture
def fn_called_once() -> Mock:
    mock = Mock(name="fn_called_once")
    mock()
    return mock


@pytest.fixture
def fn_called_twice() -> Mock:
    mock = Mock(name="fn_called_twice")
    mock()
    mock()
    return mock


def test__never_called__should_match__if_the_mock_not_called(fn_never_called):
    assert that(fn_never_called) >> never_called()


def test__never_called__should_not_match__if_the_mock_was_called(fn_called_once, fn_called_twice):
    with pytest.raises(AssertionError) as exc_info:
        assert that(fn_called_once) >> never_called()

    assert str(exc_info.value) == (
        f"Expected to have never been called, but <Mock name='fn_called_once' id='{id(fn_called_once)}'> was called <1> time"
    )

    with pytest.raises(AssertionError) as exc_info:
        assert that(fn_called_twice) >> never_called()

    assert str(exc_info.value) == (
        f"Expected to have never been called, but <Mock name='fn_called_twice' id='{id(fn_called_twice)}'> was called <2> times"
    )


def test__never_called__should_have_aliases():
    assert never_called is was_never_called
    assert never_called is not_called
