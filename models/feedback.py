from datetime import datetime
from database.database import db
from models.talk import Talk
from utils.my_encoder import Serializer


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    detail = db.Column(db.String, nullable=False)
    posted_at = db.Column(db.DateTime, default=datetime.now())
    talk_id = db.Column(db.Integer, db.ForeignKey(Talk.id), nullable=False)
    talks = db.relationship('Talk', lazy='select',
                            backref=db.backref('feedback_list', lazy='dynamic'))

    def __init__(self, detail, talk_id):
        self.detail = detail
        self.talk_id = talk_id

    def __repr__(self):
        return '<detail %r>' % self.detail
