"""
Storages implementing adding and getting redirect link
"""

from abc import abstractmethod
from typing import Protocol


class Storage(Protocol):
    @abstractmethod
    def get(self, source: str) -> str | None:
        raise NotImplementedError

    @abstractmethod
    def set(self, source: str, destination: str) -> None:
        raise NotImplementedError


class DictStorage(Storage):
    def __init__(self, *, default_destination: str = None):
        self._collection: dict[str, str] = dict()
        self._default_destination = default_destination

    def get(self, source: str) -> str | None:
        if source not in self._collection:
            return self._default_destination
        return self._collection[source]

    def set(self, source: str, destination: str) -> None:
        self._collection[source] = destination
