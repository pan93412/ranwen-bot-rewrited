from typing import cast
import unittest
from ranwen_bot import i18nstruct, i18n

class TestI18n(unittest.TestCase):
    structure: i18nstruct

    def setUp(self):
        self.structure = cast(i18nstruct, {
            "zh-hans": "a",
            "zh-hant": "A",
        })

    def test_with_correct_target(self):
        self.assertEqual(i18n(self.structure, "zh-hans"), "A")

    def test_with_correct_default(self):
        self.assertEqual(i18n(self.structure, "en-us"), "a")
    
    def test_with_all_wrong(self):
        self.assertEqual(i18n(self.structure, "en-us", "ja-jp"), None)
