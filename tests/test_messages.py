import unittest
from typing import cast

from ranwen_bot import i18nstruct
from ranwen_bot.exceptions import DeveloperError
from ranwen_bot.messages import get_message


class TestMessages(unittest.TestCase):
    structure: i18nstruct
    wrong_structure: i18nstruct

    def setUp(self):
        self.structure = cast(i18nstruct, {
            "zh-hans": "a",
            "zh-hant": "A",
        })

        self.wrong_structure = cast(i18nstruct, {})

    def test_with_correct_target(self):
        self.assertEqual(get_message(self.structure, "zh-hant"), "A")

    def test_with_correct_default(self):
        self.assertEqual(get_message(self.structure, "en-us"), "a")
    
    def test_with_all_wrong(self):
        self.assertRaises(DeveloperError, lambda: get_message(self.wrong_structure, "zh-hans"))
