# tests/test_pattern_detector.py
import unittest
from src.analyzer import pattern_detector

class TestPatternDetector(unittest.TestCase):

    def test_detect_patterns_basic(self):
        """Test detection of basic patterns (sequential, repeated, dates)"""
        passwords = [
            "123abc",       # sequential numbers + letters
            "qwerty123",    # keyboard pattern + sequential numbers
            "aaa123",       # repeated chars + sequential numbers
            "123123123123", # repeated substring + sequential numbers
            "01012020",     # numeric date
            "jan20",        # alphanumeric date
            "strongPass"    # no patterns
        ]

        expected_patterns = [
            ["sequential_numbers", "sequential_letters"],
            ["sequential_numbers", "keyboard_pattern"],
            ["sequential_numbers", "repeated_chars"],
            ["sequential_numbers", "repeated_substring"],
            ["date_numeric", "sequential_numbers", "repeated_substring"],
            ["date_alphanumeric"],
            []
        ]

        expected_scores = [
            2.0,    # seq numbers + seq letters
            1.8,    # seq numbers + keyboard
            1.5,    # seq numbers + repeated chars
            1.5,    # seq numbers + repeated substring
            2.2,    # numeric date + seq numbers + repeated substring
            0.7,    # alphanumeric date 
            0.0     # no patterns
        ]

        results = pattern_detector.evaluate(passwords)

        for i, res in enumerate(results):
            # Check that all expected patterns are detected
            for pattern in expected_patterns[i]:
                self.assertIn(pattern, res["patterns"], f"{pattern} not detected in '{res['password']}'")
            # Check the score is correct
            self.assertAlmostEqual(res["pattern_score"], expected_scores[i], places=2, 
                                   msg=f"Score mismatch for '{res['password']}'")

    def test_empty_password(self):
        """Empty password should detect no patterns"""
        res = pattern_detector.evaluate([""])[0]
        self.assertEqual(res["patterns"], [])
        self.assertEqual(res["pattern_score"], 0.0)

    def test_multiple_patterns(self):
        """Password with multiple overlapping patterns"""
        pw = "qwerty123aaa01012020jan20"
        res = pattern_detector.evaluate([pw])[0]
        # Should detect all pattern types
        self.assertIn("sequential_numbers", res["patterns"])
        self.assertIn("sequential_letters", res["patterns"])
        self.assertIn("keyboard_pattern", res["patterns"])
        self.assertIn("repeated_chars", res["patterns"])
        self.assertIn("date_numeric", res["patterns"])
        self.assertIn("date_alphanumeric", res["patterns"])
        # Pattern score should sum all weights
        expected_score = (
            pattern_detector.PATTERN_WEIGHTS["sequential_numbers"] +
            pattern_detector.PATTERN_WEIGHTS["sequential_letters"] +
            pattern_detector.PATTERN_WEIGHTS["keyboard_pattern"] +
            pattern_detector.PATTERN_WEIGHTS["repeated_chars"] +
            pattern_detector.PATTERN_WEIGHTS["date_numeric"] +
            pattern_detector.PATTERN_WEIGHTS["date_alphanumeric"]
        )
        self.assertAlmostEqual(res["pattern_score"], expected_score, places=2)

if __name__ == "__main__":
    unittest.main()