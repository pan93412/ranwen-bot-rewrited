from typing import Dict, NewType, Optional

i18nstruct = NewType("i18nstruct", Dict[str, str])

def i18n(string_table: i18nstruct, language_code: str, default_language: str = "zh-hans") -> Optional[str]:
    return string_table.get(language_code, string_table.get(default_language))
