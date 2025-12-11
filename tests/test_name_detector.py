import unittest
import tempfile
import os
from src.analyzer.name_detector import NameDetector


class TestNameDetector(unittest.TestCase):

    def setUp(self):
        # Create a temporary names file for controlled testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")
        self.temp_file.write("Alice\nBob\nMaria\nAlex\nJohn\n")
        self.temp_file.close()

        self.detector = NameDetector(name_file_path=self.temp_file.name)

    def tearDown(self):
        os.remove(self.temp_file.name)

    # ----------------------------------------------------------
    # 1. Test single name match
    # ----------------------------------------------------------
    def test_single_name_match(self):
        result = self.detector.analyze("helloAlice123")
        self.assertTrue(result["contains_name"])
        self.assertIn("alice", result["matched_names"])
        self.assertEqual(result["name_score"], 1)

    # ----------------------------------------------------------
    # 2. Test multiple name matches
    # ----------------------------------------------------------
    def test_multiple_name_matches(self):
        result = self.detector.analyze("alexmaria2024")
        self.assertTrue(result["contains_name"])
        self.assertIn("alex", result["matched_names"])
        self.assertIn("maria", result["matched_names"])
        self.assertEqual(result["name_score"], 2)

    # ----------------------------------------------------------
    # 3. Case insensitivity test
    # ----------------------------------------------------------
    def test_case_insensitivity(self):
        result = self.detector.analyze("JOHN123bob321")
        self.assertTrue(result["contains_name"])
        self.assertIn("john", result["matched_names"])
        self.assertIn("bob", result["matched_names"])
        self.assertEqual(result["name_score"], 2)

    # ----------------------------------------------------------
    # 4. No match test
    # ----------------------------------------------------------
    def test_no_names(self):
        result = self.detector.analyze("abcxyz123")
        self.assertFalse(result["contains_name"])
        self.assertEqual(len(result["matched_names"]), 0)
        self.assertEqual(result["name_score"], 0)

    # ----------------------------------------------------------
    # 5. evaluate() should process list of passwords
    # ----------------------------------------------------------
    def test_evaluate_multiple_passwords(self):
        pw_list = ["alex2020", "nothinghere", "MARIA99"]
        results = self.detector.evaluate(pw_list)

        self.assertEqual(len(results), 3)

        self.assertTrue(results[0]["contains_name"])   # alex
        self.assertFalse(results[1]["contains_name"])  # no names
        self.assertTrue(results[2]["contains_name"])   # maria

        self.assertIn("alex", results[0]["matched_names"])
        self.assertIn("maria", results[2]["matched_names"])

    # ----------------------------------------------------------
    # 6. Overlapping names shouldn't duplicate score
    # e.g. 'alexalex' should match alex ONCE
    # ----------------------------------------------------------
    def test_no_duplicate_matches(self):
        result = self.detector.analyze("alexalex")
        self.assertEqual(result["name_score"], 1)   # only count unique names
        self.assertEqual(len(result["matched_names"]), 1)


if __name__ == "__main__":
    unittest.main()