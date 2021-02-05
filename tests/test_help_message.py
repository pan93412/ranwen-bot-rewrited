from typing import cast
import unittest
from ranwen_bot import i18nstruct, i18n

class TestI18n(unittest.TestCase):
    structure: i18nstruct

    def setUp(self):
        self.structure = cast(i18nstruct, {
            "zh_CN": "a",
            "zh_TW": "A",
        })

    def test_with_correct_target(self):
        self.assertEqual(i18n(self.structure, "zh_TW"), "A")

    def test_with_correct_default(self):
        self.assertEqual(i18n(self.structure, "en_US"), "a")
    
    def test_with_all_wrong(self):
        self.assertEqual(i18n(self.structure, "en_US", "ja_JP"), None)
