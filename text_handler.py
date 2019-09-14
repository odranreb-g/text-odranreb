from collections import OrderedDict
import string

import attr

from text_handler_utils import stop_words_portuguese

# from nltk.tokenize import TreebankWordTokenizer
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# word_tokenize(text, language='english', preserve_line=False)


@attr.s
class TextHandler:
    """
        This class will handler the text.

        the sw is abbreviation of single word.

        the ng is abbreviation of number of gram.

        every word will be converted to lower case.
    """

    texts = attr.ib()

    @texts.validator
    def texts_check(self, attribute, value):

        if not isinstance(value, list):
            raise ValueError("the value must be list.")

        if not all([isinstance(v, str) for v in value]):
            raise ValueError("Every item inside the list must me string.")

    def _remove_stop_words(self, words):
        return [word for word in words if word not in stop_words_portuguese]

    def _word_tokenize_texts(self):
        return word_tokenize(" ".join(self.texts), language="portuguese")

    def _transform_to_lower_each_word(self, words):
        return [word.lower() for word in words]

    def _remove_punctuation(self, words):
        return [word for word in words if word not in string.punctuation]

    def _remove_duplicated_without_lost_order(self, words):
        return OrderedDict.fromkeys(words)

    def _calcule_frequence(self, words):
        return FreqDist(words)

    def sw_vocabulary(self):
        words = self._word_tokenize_texts()
        words = self._remove_stop_words(words)
        words = self._transform_to_lower_each_word(words)
        words = self._remove_punctuation(words)
        words = OrderedDict.fromkeys(words)
        words = list(words)

        return words

    def sw_frequency_distribution(self):
        words = self._word_tokenize_texts()
        words = self._remove_stop_words(words)
        words = self._transform_to_lower_each_word(words)
        words = self._remove_punctuation(words)

        freq_dist = self._calcule_frequence(words)

        words = self._remove_duplicated_without_lost_order(words)

        return [freq_dist[key] for key in words]

    def ng_vocabulary(self, num_gram=2):
        words = self._word_tokenize_texts()
        words = self._remove_stop_words(words)
        words = self._transform_to_lower_each_word(words)
        words = self._remove_punctuation(words)
        words = ngrams(words, num_gram)
        words = self._remove_duplicated_without_lost_order(words)
        words = list(words)
        return words

    def ng_frequency_distribution(self, num_gram=2):

        words = self._word_tokenize_texts()
        words = self._remove_stop_words(words)
        words = self._transform_to_lower_each_word(words)
        words = self._remove_punctuation(words)
        words = list(ngrams(words, num_gram))

        freq_dist = self._calcule_frequence(words)

        words = self._remove_duplicated_without_lost_order(words)

        return [freq_dist[key] for key in words]
