from abc import ABC, abstractmethod
from typing import Dict, List
from .visitable_interface import IVisitable

__All__ = ['IParser']


class IParser(IVisitable):
    """
    Interface for parsers.

    This abstract base class defines the contract for parser implementations.
    It inherits from IVisitable, suggesting that parser objects can be visited.
    """

    @abstractmethod
    def parse(self) -> Dict[str, List[str]]:
        """
        Parses content.

        This abstract method must be implemented by concrete parser classes.

        Returns:
            Dict[str, List[str]]: A dictionary where keys are likely file names or identifiers,
                                  and values are lists of strings representing parsed content.
        """
        pass
