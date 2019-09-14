from http import HTTPStatus
import json
from flask import url_for
import pytest

# from app import flaskr


# @pytest.fixture
# def client():
#     flaskr.app.config["TESTING"] = True

#     with flaskr.app.test_client() as client:
#         yield client


@pytest.mark.usefixtures("client_class")
class TestEndpointSendTextAPI:
    def test_endpoint_send_text_with_valid_data(self, client):
        data = {"text": "new text to server"}
        rv = client.post(url_for("api.send_text_api"), data=json.dumps(data))

        assert rv.status_code == HTTPStatus.CREATED
        assert rv.get_json()["text"] == data["text"]

        assert rv.get_json().get("id", None) is not None

    def test_endpoint_send_text_without_valid_data(self, client):
        data = {"otherfiled": "new text to server"}
        rv = client.post(url_for("api.send_text_api"), data=json.dumps(data))

        assert rv.status_code == HTTPStatus.BAD_REQUEST

        assert rv.get_json() == {"text": ["Missing data for required field."]}

