from abc import ABC, abstractmethod
from unittest.mock import Mock

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description


class BaseMockMatcher(BaseMatcher[Mock], ABC):
    """Base class for matchers that operate on Mock objects."""

    @abstractmethod
    def _matches(self, item: Mock) -> bool:
        pass

    @abstractmethod
    def describe_to(self, description: Description) -> None:
        pass

    def describe_mismatch(self, item: Mock, mismatch_description: Description) -> None:
        super().describe_mismatch(item, mismatch_description)


__all__ = [
    "BaseMockMatcher",
]
