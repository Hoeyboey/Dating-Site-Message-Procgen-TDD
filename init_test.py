import unittest
from init import init

class TestInitFucntion(unittest.TestCase):
	def test_given_source_messages_init(self):
		source_messages = ["Testing mark one", "Testing mark two", "Testing mark three"]
		expected_output = {"testing":3, "mark":3, "one":1, "two":1, "three":1}
		actual = init(source_messages)
		self.assertEqual(actual, expected_output)
