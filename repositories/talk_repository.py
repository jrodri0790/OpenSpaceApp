from models.talk import Talk


class TalkRepository:

    @classmethod
    def find_all(cls):
        return Talk.query.all()
