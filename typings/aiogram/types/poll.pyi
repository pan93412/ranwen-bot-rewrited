"""
This type stub file was generated by pyright.
"""

import datetime
import typing
from . import base
from .user import User
from ..utils import helper

class PollOption(base.TelegramObject):
    """
    This object contains information about one answer option in a poll.

    https://core.telegram.org/bots/api#polloption
    """
    text: base.String = ...
    voter_count: base.Integer = ...


class PollAnswer(base.TelegramObject):
    """
    This object represents an answer of a user in a non-anonymous poll.
    
    https://core.telegram.org/bots/api#pollanswer
    """
    poll_id: base.String = ...
    user: User = ...
    option_ids: , = ...


class Poll(base.TelegramObject):
    """
    This object contains information about a poll.
    
    https://core.telegram.org/bots/api#poll
    """
    id: base.String = ...
    question: base.String = ...
    options: , = ...
    total_voter_count: base.Integer = ...
    is_closed: base.Boolean = ...
    is_anonymous: base.Boolean = ...
    type: base.String = ...
    allows_multiple_answers: base.Boolean = ...
    correct_option_id: base.Integer = ...
    explanation: base.String = ...
    explanation_entities: base.String = ...
    open_period: base.Integer = ...
    close_date: datetime.datetime = ...
    def parse_entities(self, as_html=...):
        ...
    
    @property
    def md_explanation(self) -> str:
        """
        Explanation formatted as markdown.

        :return: str
        """
        ...
    
    @property
    def html_explanation(self) -> str:
        """
        Explanation formatted as HTML

        :return: str
        """
        ...
    


class PollType(helper.Helper):
    mode = ...
    REGULAR = ...
    QUIZ = ...


