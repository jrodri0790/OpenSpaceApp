from marshmallow import Schema, fields, ValidationError


class TalkSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(load_only=True)
    speakers = fields.Str(load_only=True)
    formatted_name = fields.Method("format_name", dump_only=True)

    @classmethod
    def format_name(cls, talk):
        return "{} por {}".format(talk.name, talk.speakers)


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")
