from string import  punctuation



# NOTE:
#  For some weird reason I can't get the last word without adding a extra char at the end of sentence.
#  Think its the index.


class WordExtractor:
    """
    Takes a sentence loop over each character then ignore all punctuation and numbers.
    
    Returns a list of words that was extracted from the given sentence.

    """
    def __init__(self) -> None:
        illegal_punctuation = "\"“”!#$%&()*+,./:;<=>?@[\]^_—`{|}~…¿¡«»€"
        self.space_char = ' '
        self.not_allowed_chars = '0123456789' + illegal_punctuation + self.space_char

            
    
    
    # Create a method the extract English Spanish and French words
    def extract_words(self, sentence:str) -> list:
        """
        Extract all English Spanish and French  word(s) from the given sentence. 

        Returns:
            list: all the list of word(s) that was extracted.
        """
        words = [] # Word(s) that was found in sentence
        chars = '' # Character(s) that was collected from the loops
        # Looping ove the sentence
        for char in sentence + self.space_char:
            # Checking for punctuations and numbers
            if char not in self.not_allowed_chars:
                # add char to chars
                chars += char
            # Else in not allowed characters 
            else:
                # Check if chars is not empty
                if len(chars) != 0:
                    # add the word to the words list
                    words.append(chars)
                    # reset the chars to empty then continue to search for the next word.
                    chars = ''
        # Return the results once the sentence loop as ended
        return words