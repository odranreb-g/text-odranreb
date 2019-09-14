#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from text_handler import TextHandler


class TestTextHandler:
    # text_handler = None

    # @pytest.fixture(autouse=True)
    # def run_around_tests(self):
    #     yield
    #     self.text_handler = None

    def test_it_should_be_a_class(self):
        text_handler = TextHandler([""])
        assert isinstance(text_handler, TextHandler)

    def test_it_should_throw_exception_with_wrong_param(self):
        with pytest.raises(ValueError):
            TextHandler("bufalo bufalo bufalo")

    def test_it_should_receive_list_of_text_by_param(self):
        text_handler = TextHandler(["bufalo bufalo bufalo"])
        assert isinstance(text_handler.texts, list)

    def test_if_return_list_with_single_words_and_unique_items(self):
        text_handler = TextHandler(["bufalo bufalo bufalo"])
        assert text_handler.sw_vocabulary() == ["bufalo"]

    def test_if_return_list_with_single_words_in_order(self):
        text_handler = TextHandler(["bernardo gomes abreu"])
        assert text_handler.sw_vocabulary() == ["abreu", "bernardo", "gomes"]

    def test_if_return_list_with_ignored_punctuation(self):
        text_handler = TextHandler(
            ["bernardo gomes; abreu. a! a# a% a$ a' a& a) a( a, a; a: a< a? a> a@ a[ a] a` a{ a} "]
        )
        assert text_handler.sw_vocabulary() == ["a", "abreu", "bernardo", "gomes"]

    def test_if_return_list_with_ignored_case(self):
        text_handler = TextHandler(["bernardo GOMES; Abreu."])
        assert text_handler.sw_vocabulary() == ["abreu", "bernardo", "gomes"]

    def test_if_return_list_when_the_params_is_multiple_texts(self):
        text_handler = TextHandler(
            ["bernardo GOMES; Abreu.", "YASMINE", "Melo", "Costa", "Leonardo Gomes Abreu"]
        )
        assert text_handler.sw_vocabulary() == [
            "abreu",
            "bernardo",
            "costa",
            "gomes",
            "leonardo",
            "melo",
            "yasmine",
        ]
