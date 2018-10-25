from database.database import db
from models.code_talk import code_talk
from sqlalchemy import text


class CodeTalkRepository:

    @classmethod
    def find_talks_and_votes(cls):
        sql = text('select talk_id, count(*) as votes from code_talk group by talk_id order by votes desc')
        result = db.engine.execute(sql)
        code_talks = []
        for row in result:
            talk_vote = (row[0], row[1])
            code_talks.append(talk_vote)
        return code_talks

    @classmethod
    def insert_vote_for_talk(cls, code_id, talk_id):
        statement = code_talk.insert().values(code_id=code_id, talk_id=talk_id)
        db.session.execute(statement)
        db.session.commit()

    @classmethod
    def find_by_code(cls, code):
        return db.session.query(code_talk).filter(code_talk.c.code_id == code).first()

