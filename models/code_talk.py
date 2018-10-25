from database.database import db
from models.code import Code
from models.talk import Talk

code_talk = db.Table('code_talk',
                     db.Column('code_id', db.String, db.ForeignKey(Code.id), primary_key=True),
                     db.Column('talk_id', db.Integer, db.ForeignKey(Talk.id), primary_key=True)
                     )

