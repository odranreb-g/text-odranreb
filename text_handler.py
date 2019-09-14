import string
import attr

# from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize


# word_tokenize(text, language='english', preserve_line=False)


@attr.s
class TextHandler:
    """
        This class will handler the text.

        the sw is abreviation of single word.

        every word will be converted to lower case.
    """

    texts = attr.ib()

    @texts.validator
    def texts_check(self, attribute, value):

        if not isinstance(value, list):
            raise ValueError("the value must be list.")

    def sw_vocabulary(self):
        words = set(word_tokenize("".join(self.texts), language="portuguese"))

        words = words - set(string.punctuation)
        words = list(words)
        words = [word.lower() for word in words]
        words.sort()
        return words
        # return TreebankWordTokenizer().tokenize("".join(self.texts))
