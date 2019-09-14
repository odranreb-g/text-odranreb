import pytest
from marshmallow.exceptions import ValidationError
from app.api_v1.schemas import SendTextSchema


class TestSendText:
    def test_validate_should_throw_expectio_when_validate_wrong_data(self):
        with pytest.raises(ValidationError):
            data = {"country": "brazil"}
            schema = SendTextSchema()
            schema.load(data)

    def test_validate_should_create_a_json_when_is_passed_a_valide_data(self):
        data = {"text": "brazil is cool"}
        schema = SendTextSchema()
        new_data = schema.load(data)
        assert new_data == data

    def test_validate_should_create_a_json_when_is_passed_a_valide_field_and_invalid_field(self):
        data = {"text": "brazil is cool", "another": "cool"}
        schema = SendTextSchema()
        new_data = schema.load(data)
        del data["another"]
        assert new_data == data

    def test_dump_should_create_a_json_with_id_and_text(self):
        data = {"text": "brazil is cool", "id": 2}

        schema = SendTextSchema()
        new_data = schema.dump(data)
        assert data == new_data

    def test_dump_should_create_a_json_with_id_and_text_and_another_text(self):
        data = {"text": "brazil is cool", "id": 2, "another": "teste"}

        schema = SendTextSchema()
        new_data = schema.dump(data)
        del data["another"]
        assert data == new_data

