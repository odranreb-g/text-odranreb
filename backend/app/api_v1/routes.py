from flask import request
from flask_restplus import Resource, Api
from marshmallow.exceptions import ValidationError
from app.api_v1.schemas import SendTextSchema
from app.models import Text
from app.extensions import db
from . import api_bp_v1

api_restfull = Api(api_bp_v1)


@api_restfull.route("/send-text")
class SendTextAPI(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        schema = SendTextSchema()

        try:

            data = schema.load(json_data)

            text = Text()
            text.text = data.get("text")

            db.session.add(text)
            db.session.commit()

            data.update({"id": text.id})

            return schema.dump(data), 201

        except ValidationError as error:
            return error.messages, 400

