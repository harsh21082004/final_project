import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench_bonjour(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        result = englishToFrench(english_text)
        self.assertEqual(result, expected_french_text)

    def test_frenchToEnglish_bonjour(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"
        result = frenchToEnglish(french_text)
        self.assertEqual(result, expected_english_text)

    def test_frenchToEnglish_hello(self):
        french_text = "Hello"
        expected_english_text = "Bonjour"
        result = frenchToEnglish(french_text)
        self.assertEqual(result, expected_english_text)

if __name__ == "__main__":
    unittest.main()
