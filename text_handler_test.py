#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from text_handler import TextHandler


class TestTextHandler:
    text_handler = None

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        self.text_handler = TextHandler()
        yield
        self.text_handler = None

    def test_it_should_be_a_class(self):
        assert isinstance(self.text_handler, TextHandler)
