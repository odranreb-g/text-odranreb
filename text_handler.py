import attr


@attr.s
class TextHandler:
    texts = attr.ib()

    @texts.validator
    def texts_check(self, attribute, value):

        if not isinstance(value, list):
            raise ValueError("the value must be list.")
