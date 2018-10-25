from database.database import db
from models.code import Code


class CodeRepository:

    @classmethod
    def find_code(cls, code):
        return Code.query.filter_by(id=code).first()

    @classmethod
    def insert_code(cls, code_id):
        code = Code(code_id)
        db.session.add(code)
        db.session.commit()
