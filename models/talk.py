from database.database import db
from utils.my_encoder import Serializer


class Talk(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return '<Code %r>' % self.id
