"""
This type stub file was generated by pyright.
"""

import typing
from .filters import AbstractFilter
from ..handler import Handler

class FiltersFactory:
    """
    Filters factory
    """
    def __init__(self, dispatcher) -> None:
        ...
    
    def bind(self, callback: ,, validator: , = ..., event_handlers: , = ..., exclude_event_handlers: , = ...):
        """
        Register filter

        :param callback: callable or subclass of :obj:`AbstractFilter`
        :param validator: custom validator.
        :param event_handlers: list of instances of :obj:`Handler`
        :param exclude_event_handlers: list of excluded event handlers (:obj:`Handler`)
        """
        ...
    
    def unbind(self, callback: ,):
        """
        Unregister filter

        :param callback: callable of subclass of :obj:`AbstractFilter`
        """
        ...
    
    def resolve(self, event_handler, *custom_filters, **full_config) -> ,:
        """
        Resolve filters to filters-set

        :param event_handler:
        :param custom_filters:
        :param full_config:
        :return:
        """
        ...
    

