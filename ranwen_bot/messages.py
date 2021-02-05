from typing import cast
from .exceptions.DeveloperError import DeveloperError
from .i18n import i18n, i18nstruct

_help_message = cast(i18nstruct, {
    "zh-hans": (
        ">> 帮助\n"
        "/help  帮助\n"
        "/blackjack  21点\n"
        "/horse  赛马\n"
        "/dice  骰子\n"
        "/bet 金额|百分比|sh  下注 (不支持小数)\n"
        "例: /bet 10 或 /bet 10%\n"
    ),
    "zh-hant": (
        ">> 說明\n"
        "/help  說明\n"
        "/blackjack  21點\n"
        "/horse  賽馬\n"
        "/dice  骰子\n"
        "/bet 金額|百分比|sh  下注（不支援小數點）\n"
        "例如：/bet 10 或 /bet 10%\n"
    )
})

def get_message(messages: i18nstruct, language: str) -> str:
    message = i18n(messages, language)

    if message == None:
        raise DeveloperError("There are nothing even the default language.", "help_message()")

    return message or ""

def help_message(language: str) -> str:
    return get_message(_help_message, language)