"""
This type stub file was generated by pyright.
"""

from . import base

class ChatPermissions(base.TelegramObject):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.

    https://core.telegram.org/bots/api#chatpermissions
    """
    can_send_messages: base.Boolean = ...
    can_send_media_messages: base.Boolean = ...
    can_send_polls: base.Boolean = ...
    can_send_other_messages: base.Boolean = ...
    can_add_web_page_previews: base.Boolean = ...
    can_change_info: base.Boolean = ...
    can_invite_users: base.Boolean = ...
    can_pin_messages: base.Boolean = ...
    def __init__(self, can_send_messages: base.Boolean = ..., can_send_media_messages: base.Boolean = ..., can_send_polls: base.Boolean = ..., can_send_other_messages: base.Boolean = ..., can_add_web_page_previews: base.Boolean = ..., can_change_info: base.Boolean = ..., can_invite_users: base.Boolean = ..., can_pin_messages: base.Boolean = ..., **kwargs) -> None:
        ...
    


