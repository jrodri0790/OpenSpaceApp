from database.database import db


class Code(db.Model):
    id = db.Column(db.String, primary_key=True)

    def __init__(self, code):
        self.id = code

    def __repr__(self):
        return '<Code %r>' % self.code
