import pytest
from marshmallow import Schema
from marshmallow.exceptions import ValidationError
from app.api_v1.schemas import SendTextSchema, VocabularySchema


class TestSendTextSchema:
    @pytest.fixture(autouse=True)
    def setUpAndTearDown(self):
        self.schema = SendTextSchema()

    def test_validate_should_throw_expectio_when_validate_wrong_data(self):
        with pytest.raises(ValidationError):
            data = {"country": "brazil"}
            self.schema.load(data)

    def test_validate_should_create_a_json_when_is_passed_a_valide_data(self):
        data = {"text": "brazil is cool"}
        new_data = self.schema.load(data)
        assert new_data == data

    def test_validate_should_create_a_json_when_is_passed_a_valide_field_and_invalid_field(self):
        data = {"text": "brazil is cool", "another": "cool"}
        new_data = self.schema.load(data)
        del data["another"]
        assert new_data == data

    def test_dump_should_create_a_json_with_id_and_text(self):
        data = {"text": "brazil is cool", "id": 2}
        new_data = self.schema.dump(data)
        assert data == new_data

    def test_dump_should_create_a_json_with_id_and_text_and_another_text(self):
        data = {"text": "brazil is cool", "id": 2, "another": "teste"}
        new_data = self.schema.dump(data)
        del data["another"]
        assert data == new_data


class TestVocabularySchema:
    @pytest.fixture(autouse=True)
    def setUpAndTearDown(self):
        self.schema = VocabularySchema()

    def test_should_be_instace_of_schema(self):
        assert isinstance(self.schema, Schema)

    def test_validate_should_throw_expectio_when_validate_wrong_data(self):
        with pytest.raises(ValidationError):
            data = {"country": "brazil"}
            self.schema.load(data)

    def test_dump_should_create_a_json_with_id_and_text(self):
        data = {"vocabulary": ["aab", "bab", "aa", "ab"]}
        new_data = self.schema.load(data)
        assert data == new_data

    def test_dump_should_create_a_json_with_only_field_represented_in_schema(self):
        data = {"vocabulary": ["aab", "bab", "aa", "ab"], "another": [1, 2, 3, 4]}

        new_data = self.schema.load(data)
        del data["another"]
        assert data == new_data
