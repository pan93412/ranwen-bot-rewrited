"""
This type stub file was generated by pyright.
"""

from . import base

class Dice(base.TelegramObject):
    """
    This object represents a dice with random value from 1 to 6.
    (Yes, we're aware of the “proper” singular of die.
    But it's awkward, and we decided to help it change. One dice at a time!)
    
    https://core.telegram.org/bots/api#dice
    """
    emoji: base.String = ...
    value: base.Integer = ...


class DiceEmoji:
    DICE = ...
    DART = ...
    BASKETBALL = ...
    FOOTBALL = ...
    SLOT_MACHINE = ...


