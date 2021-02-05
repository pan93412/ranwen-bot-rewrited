"""
This type stub file was generated by pyright.
"""

import typing
from . import base
from .photo_size import PhotoSize

class UserProfilePhotos(base.TelegramObject):
    """
    This object represent a user's profile pictures.

    https://core.telegram.org/bots/api#userprofilephotos
    """
    total_count: base.Integer = ...
    photos: , = ...


