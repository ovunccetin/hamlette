from unittest.mock import Mock

from hamcrest.core.description import Description

from ._base import BaseMockMatcher


class IsNeverCalled(BaseMockMatcher):
    """Matcher that checks if a Mock has never been called."""

    def _matches(self, item: Mock) -> bool:
        return item.call_count == 0

    def describe_to(self, description: Description) -> None:
        description.append_text("to have never been called")

    def describe_mismatch(self, item: Mock, mismatch_description: Description) -> None:
        count: int = item.call_count
        mismatch_description \
            .append_text(str(item)) \
            .append_text(" was called ") \
            .append_description_of(count) \
            .append_text(" time" if count == 1 else " times")


def never_called() -> IsNeverCalled:
    """
    Matches if a Mock has never been called.

    It has aliases like `not_called` and `was_never_called`.

    Examples:
        assert that(mock) >> never_called()
        assert that(mock) >> not_called()
        assert that(mock) >> was_never_called()
    """
    return IsNeverCalled()


# Aliases
not_called = never_called
was_never_called = never_called

__all__ = [
    "never_called",
    "was_never_called",
    "not_called",
]
