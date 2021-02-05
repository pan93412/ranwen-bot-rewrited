"""
This type stub file was generated by pyright.
"""

from . import base, mixins
from .photo_size import PhotoSize

class Document(base.TelegramObject, mixins.Downloadable):
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    https://core.telegram.org/bots/api#document
    """
    file_id: base.String = ...
    file_unique_id: base.String = ...
    thumb: PhotoSize = ...
    file_name: base.String = ...
    mime_type: base.String = ...
    file_size: base.Integer = ...

