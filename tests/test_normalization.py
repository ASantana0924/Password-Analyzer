import unittest
from src.utils import normalization

class TestNormalization(unittest.TestCase):

    def test_lowercase_conversion(self):
        self.assertEqual(normalization.normalize("ABCdef"), "abcdef")
        self.assertEqual(normalization.normalize("PASSWORD"), "password")

    def test_leetspeak_conversion(self):
        self.assertEqual(normalization.normalize("H3LL0P@SSW0RD"), "hellopassword")        
        self.assertEqual(normalization.normalize("5up3r$tr1ng!"), "superstringi")
        self.assertEqual(normalization.normalize("4@8361!05$7+2"), "aabegiiossttz")

    def test_leetspeak_skipped(self):
        self.assertEqual(normalization.normalize("P@SSW0RD", leetspeak=False), "p@ssw0rd")
        self.assertEqual(normalization.normalize("4@8361!05$7+2", leetspeak=False), "4@8361!05$7+2")
        self.assertEqual(normalization.normalize("5up3r$tr1ng!", leetspeak=False), "5up3r$tr1ng!")

    def test_empty_and_non_string_inputs(self):
        self.assertEqual(normalization.normalize(""), "")
        self.assertEqual(normalization.normalize(None), "")
        self.assertEqual(normalization.normalize(12345), "")

if __name__ == "__main__":
    unittest.main()