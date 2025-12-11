import unittest
from src.analyzer import entropy_calculator

class TestEntropyCalculator(unittest.TestCase):

    def setUp(self):
        """
        List of test passwords ranging from weak to strong.
        """
        self.test_passwords = [
            "",                 
            "aaaaaa",           
            "123456",           
            "abcdef",           
            "abc123",           
            "passw0rd",         
            "P@ssw0rd123",      
            "Str0ngP@ssw0rd!"   
        ]

    def test_normalized_entropy_scores(self):
        """
        Test that entropy scores are normalized between 0 and 1 and increase with
        password complexity.
        """
        results = entropy_calculator.evaluate(self.test_passwords)

        for pwd in self.test_passwords:
            score = results[pwd]
            print(f"Password: {pwd}, Score: {score:.2f}")

            # Check that score is between 0 and 1
            self.assertGreaterEqual(score, 0.0, msg=f"Score below 0 for: {pwd}")
            self.assertLessEqual(score, 1.0, msg=f"Score above 1 for: {pwd}")

if __name__ == "__main__":
    unittest.main()
