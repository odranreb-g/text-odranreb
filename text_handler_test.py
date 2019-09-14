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

