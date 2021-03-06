"""
This type stub file was generated by pyright.
"""

import typing
from . import base
from .passport_file import PassportFile

class EncryptedPassportElement(base.TelegramObject):
    """
    Contains information about documents or other Telegram Passport elements shared with the bot by the user.

    https://core.telegram.org/bots/api#encryptedpassportelement
    """
    type: base.String = ...
    data: base.String = ...
    phone_number: base.String = ...
    email: base.String = ...
    files: , = ...
    front_side: PassportFile = ...
    reverse_side: PassportFile = ...
    selfie: PassportFile = ...


