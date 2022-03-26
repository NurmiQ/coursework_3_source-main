from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str
    password = fields.Str
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    favorite_genre = fields.Str
    role = fields.Str