import unittest
from unittest.mock import patch
import lab1_part1


class TestGenerateNumber(unittest.TestCase):

    def test_generate_number(self):
        ulimit = 10
        num = lab1_part1.generate_number(ulimit)
        # test generated number is greater than 0
        self.assertGreaterEqual(num, 0)

        # test generated number less than ulimit
        self.assertLessEqual(num, ulimit)

    # test that input is less than max, greater than min, is integer
    @patch('builtins.input', side_effect=['a', 11, 1, -1, 3.3])
    @patch('builtins.print')
    def test_user_input(self, mock_print, mock_input):
        max = 10

        # mock_input = a
        lab1_part1.get_input(max)
        mock_print.assert_called_with("Was that a number?")

        # mock_input = 11
        # if this is greater than max return false
        self.assertEqual(lab1_part1.get_input(max), False)

        # mock_input = 1
        self.assertEqual(lab1_part1.get_input(max), 1)

        # mock_input = -1
        self.assertEqual(lab1_part1.get_input(max), False)

        # mock_input = 3.3
        self.assertEqual(lab1_part1.get_input(max), 3)
