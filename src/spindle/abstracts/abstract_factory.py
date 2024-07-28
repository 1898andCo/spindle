from spindle.interfaces.factory_interface import IParserFactory
from spindle.interfaces.parser_interface import IParser
from spindle.interfaces.processor_interface import IProcessor
from spindle.interfaces.handler_interface import IHandler
from abc import abstractmethod

__All__ = ['AbstractParserFactory']


class AbstractParserFactory(IParserFactory):
    def create_parser(self, *args, **kwargs) -> IParser:
        parser = self._create_parser(*args, **kwargs)
        return parser

    def create_processor(self, *args, **kwargs) -> IProcessor:
        processor = self._create_processor(*args, **kwargs)
        return processor

    def create_handler(self, *args, **kwargs) -> IHandler:
        handler = self._create_handler(*args, **kwargs)
        return handler

    @abstractmethod
    def _create_parser(self, *args, **kwargs) -> IParser:
        pass

    @abstractmethod
    def _create_processor(self, *args, **kwargs) -> IProcessor:
        pass

    @abstractmethod
    def _create_handler(self, *args, **kwargs) -> IHandler:
        pass
