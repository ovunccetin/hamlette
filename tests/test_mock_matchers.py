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


def test__not_called__should_match__if_the_mock_not_called(fn_never_called):
    assert that(fn_never_called) >> was_not_called()


def test__not_called__should_not_match__if_the_mock_was_called(fn_called_once, fn_called_twice):
    with pytest.raises(AssertionError) as exc_info:
        assert that(fn_called_once) >> was_not_called()

    assert str(exc_info.value) == (
        f"Expected not to have been called, but <Mock name='fn_called_once' id='{id(fn_called_once)}'> was called <1> time"
    )

    with pytest.raises(AssertionError) as exc_info:
        assert that(fn_called_twice) >> was_not_called()

    assert str(exc_info.value) == (
        f"Expected not to have been called, but <Mock name='fn_called_twice' id='{id(fn_called_twice)}'> was called <2> times"
    )
