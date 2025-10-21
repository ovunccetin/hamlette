from unittest.mock import Mock

from hamcrest.core.description import Description

from ._base import BaseMockMatcher


class WasNotCalled(BaseMockMatcher):
    """Matcher that checks if a Mock has not been called."""

    def _matches(self, item: Mock) -> bool:
        return item.call_count == 0

    def describe_to(self, description: Description) -> None:
        description.append_text("not to have been called")

    def describe_mismatch(self, item: Mock, mismatch_description: Description) -> None:
        count: int = item.call_count
        mismatch_description \
            .append_text(str(item)) \
            .append_text(" was called ") \
            .append_description_of(count) \
            .append_text(" time" if count == 1 else " times")


def not_called() -> WasNotCalled:
    """
    Matches if a Mock has not been called.

    It has an alias: `was_not_called` for convenience.

    Examples:
        assert that(mock) >> not_called()
        assert that(mock) >> was_not_called()
    """
    return WasNotCalled()


# Aliases
was_not_called = not_called

__all__ = [
    "not_called",
    "was_not_called",
]
