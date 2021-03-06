"""
This type stub file was generated by pyright.
"""

from . import base
from .location import Location

class ChatLocation(base.TelegramObject):
    """
    Represents a location to which a chat is connected.

    https://core.telegram.org/bots/api#chatlocation
    """
    location: Location = ...
    address: base.String = ...
    def __init__(self, location: Location, address: base.String) -> None:
        ...
    


