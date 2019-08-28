from models.talk import Talk


class TalkRepository:

    @classmethod
    def find_all(cls):
        return Talk.query.all()

    @classmethod
    def find_by_id(cls, code):
        return Talk.query.get(code)
