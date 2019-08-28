from database.database import db


class Talk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    speakers = db.Column(db.String)

    def __repr__(self):
        return '<Code %r>' % self.id
