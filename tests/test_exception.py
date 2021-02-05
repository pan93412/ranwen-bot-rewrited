import unittest
from ranwen_bot.exceptions import DeveloperError


class TestExceptions(unittest.TestCase):
    def test_developer_error_with_only_message(self):
        exc = DeveloperError("test_msg")
        self.assertEqual(str(exc), "in somewhere: test_msg")
    
    def test_developer_error_with_message_and_location(self):
        exc = DeveloperError("test_msg", "test_where()")
        self.assertEqual(str(exc), "in test_where(): test_msg")
