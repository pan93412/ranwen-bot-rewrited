"""
This type stub file was generated by pyright.
"""

import typing
from . import base

class KeyboardButtonPollType(base.TelegramObject):
    """
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    https://core.telegram.org/bots/api#keyboardbuttonpolltype
    """
    type: base.String = ...
    def __init__(self, type: , = ...) -> None:
        ...
    


class ReplyKeyboardMarkup(base.TelegramObject):
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    https://core.telegram.org/bots/api#replykeyboardmarkup
    """
    keyboard: , = ...
    resize_keyboard: base.Boolean = ...
    one_time_keyboard: base.Boolean = ...
    selective: base.Boolean = ...
    def __init__(self, keyboard: , = ..., resize_keyboard: base.Boolean = ..., one_time_keyboard: base.Boolean = ..., selective: base.Boolean = ..., row_width: base.Integer = ...) -> None:
        ...
    
    @property
    def row_width(self):
        ...
    
    @row_width.setter
    def row_width(self, value):
        ...
    
    def add(self, *args):
        """
        Add buttons

        :param args:
        :return: self
        :rtype: :obj:`types.ReplyKeyboardMarkup`
        """
        ...
    
    def row(self, *args):
        """
        Add row

        :param args:
        :return: self
        :rtype: :obj:`types.ReplyKeyboardMarkup`
        """
        ...
    
    def insert(self, button):
        """
        Insert button to last row

        :param button:
        :return: self
        :rtype: :obj:`types.ReplyKeyboardMarkup`
        """
        ...
    


class KeyboardButton(base.TelegramObject):
    """
    This object represents one button of the reply keyboard.
    For simple text buttons String can be used instead of this object to specify text of the button.
    Optional fields request_contact, request_location, and request_poll are mutually exclusive.
    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016.
    Older clients will ignore them.
    Note: request_poll option will only work in Telegram versions released after 23 January, 2020.
    Older clients will receive unsupported message.

    https://core.telegram.org/bots/api#keyboardbutton
    """
    text: base.String = ...
    request_contact: base.Boolean = ...
    request_location: base.Boolean = ...
    request_poll: KeyboardButtonPollType = ...
    def __init__(self, text: base.String, request_contact: base.Boolean = ..., request_location: base.Boolean = ..., request_poll: KeyboardButtonPollType = ..., **kwargs) -> None:
        ...
    


class ReplyKeyboardRemove(base.TelegramObject):
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    https://core.telegram.org/bots/api#replykeyboardremove
    """
    remove_keyboard: base.Boolean = ...
    selective: base.Boolean = ...
    def __init__(self, selective: base.Boolean = ...) -> None:
        ...
    


