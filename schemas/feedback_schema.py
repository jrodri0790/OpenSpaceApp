from marshmallow import Schema, fields

from schemas.talk_schema import TalkSchema, must_not_be_blank


class FeedbackSchema(Schema):
    id = fields.Int(dump_only=True, load_only=True)
    talk = fields.Nested(TalkSchema, validate=must_not_be_blank)
    detail = fields.Str(required=True, validate=must_not_be_blank)
    posted_at = fields.DateTime(dump_only=True)


talk_schema = TalkSchema()
talks_schema = TalkSchema(many=True)
feedback_schema = FeedbackSchema()
feedback_list_schema = FeedbackSchema(many=True, only=("id", "detail"))
