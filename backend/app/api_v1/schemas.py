from marshmallow import Schema, fields, EXCLUDE


class SendTextSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str(required=True)

    class Meta:
        unknown = EXCLUDE


class VocabularySchema(Schema):
    vocabulary = fields.List(fields.String(), required=True)

    class Meta:
        unknown = EXCLUDE
