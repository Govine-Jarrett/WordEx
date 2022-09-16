# Letting python know where to look for the module which we are testing
import sys
sys.path.append(r'C:/Users/devgo/OneDrive/Desktop/Local_Projects/Word-Extractor/lib/')


import unittest
from word_extractor import WordExtractor

# TODO: - Write test for French and Spanish characters

class TestEnglishWords(unittest.TestCase):
    
    def setUp(self) -> None:
        self.word_extractor = WordExtractor()
    
    
    def test_white_space_char(self):
        """
         Extraction test with only white space character in sentence.
        """
        self.assertEqual(
            self.word_extractor.extract_words("Hello world my name is Python"),
            ['Hello', 'world', 'my', 'name', 'is', 'Python'])
 
 
    def test_punctuation_marks(self):
        """
         Extraction test with a few punctuation marks in sentence.
        """
        self.assertEqual(
            self.word_extractor.extract_words("Hello world!!, my name is Python."),
            ['Hello', 'world', 'my', 'name', 'is', 'Python'])
        
        
    def test_apostrophe_mark(self):
        """
         Extraction test with apostrophe mark in sentence.
        """
        self.assertEqual(
            self.word_extractor.extract_words("You're not supposed to be here."),
            ["You're", 'not', 'supposed', 'to', 'be', 'here'])
    
    
    def test_numbers(self):
        """
         Extraction test with digits in sentence.
        """
        self.assertEqual(
            self.word_extractor.extract_words("A quirky, quick way to make an excellent point. It reminded me of CASIOSpk - when we used to type in 771077345 or more commonly 58008 into our calculators and turn them upside down to reveal the 'hilarious' results."),
            
            ['A', 'quirky', 'quick', 'way', 'to', 'make', 'an', 'excellent', 'point', 'It', 'reminded', 'me', 'of', 'CASIOSpk', 'when', 'we', 'used', 'to', 'type', 'in', 'or', 'more', 'commonly', 'into', 'our', 'calculators', 'and', 'turn', 'them', 'upside', 'down', 'to', 'reveal', 'the', "'hilarious'", 'results'])





if __name__ == '__main__':
    unittest.main()