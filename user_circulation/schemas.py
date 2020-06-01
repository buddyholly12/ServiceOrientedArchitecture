from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    gender = fields.Number(required=True)
    status = fields.Str(required=True) 