import unittest
from src.analyzer import frequency_checker

class TestFrequencyChecker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Ensure frequency lists are loaded before tests
        frequency_checker.load_frequency_lists()

    def test_top1k_password(self):
        """Test a password that exists in the top 1k blacklist"""
        pw = "123456"  # common password, should exist in top1k
        result = frequency_checker.check_frequency(pw)
        self.assertEqual(result["matched_list"], "top_10k")
        self.assertEqual(result["frequency_score"], 1.0)

    def test_rockyou_password(self):
        """Test a password that exists in RockYou but not top 1k"""
        pw = "letmein"  # example RockYou password not in top 1k
        result = frequency_checker.check_frequency(pw)
        self.assertEqual(result["matched_list"], "rockyou")
        self.assertEqual(result["frequency_score"], 0.8)

    def test_password_not_in_lists(self):
        """Test a password that is not in any blacklist"""
        pw = "UncommonPassword123!"
        result = frequency_checker.check_frequency(pw)
        self.assertIsNone(result["matched_list"])
        self.assertEqual(result["frequency_score"], 0.0)

    def test_normalization_applied(self):
        """Passwords with leetspeak should match after normalization"""
        pw = "p@ssw0rd"  # should normalize to 'password'
        result = frequency_checker.check_frequency(pw)
        # 'password' is a top1k password
        self.assertEqual(result["matched_list"], "top_10k")
        self.assertEqual(result["frequency_score"], 1.0)

    def test_evaluate_multiple_passwords(self):
        """Test evaluate function for multiple passwords"""
        passwords = ["123456", "letmein", "UncommonPassword123!", "p@ssw0rd"]
        results = frequency_checker.evaluate(passwords)
        expected_matches = ["top_10k", "rockyou", None, "top_10k"]
        expected_scores = [1.0, 0.8, 0.0, 1.0]

        for i, res in enumerate(results):
            self.assertEqual(res["matched_list"], expected_matches[i])
            self.assertEqual(res["frequency_score"], expected_scores[i])

if __name__ == "__main__":
    unittest.main()
