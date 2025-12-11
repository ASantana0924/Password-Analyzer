import unittest
from src.analyzer import length_checker

class TestLengthChecker(unittest.TestCase):

    def test_evaluate_multiple_passwords(self):
        """Test evaluate function returns correct dictionary of scores"""
        passwords = ["", "1", "oh", "hey", "four", "55555", "xoxoxo", "passwrd", "password", "uhhohhuhh", "h3ll0Kitty", "str0ngP@ss3", "abcdefghijkl", "StrongPasswrd"]
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.5, 0.75, 1, 1]
        results = length_checker.evaluate(passwords)
        
        for i, pwd in enumerate(passwords):
            self.assertEqual(results[pwd], expected[i], msg=f"Failed for password: {pwd}")

if __name__ == "__main__":
    unittest.main()