# test_logic.py
# Write tests to make sure your logic works as expected.

import unittest
from game.logic import check_guess

class TestGameLogic(unittest.TestCase):
    
    def test_correct_guess(self):
        guess_result = check_guess(10, 10)
        expected_result = "correct"
        assert expected_result == guess_result

    def test_too_low(self):
        guess_result = check_guess(10, 5)
        expected_result = "low"
        assert expected_result == guess_result

    def test_too_high(self):
        guess_result = check_guess(5, 10)
        expected_result = "high"
        assert expected_result == guess_result

if __name__ == "__main__":
    unittest.main()
