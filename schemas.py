from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    author = fields.Str(required=True)
    status = fields.Str(required=True) 