from models.talk import Talk


class TalkRepository:

    @classmethod
    def find_talk_by_id(cls, talk_id):
        return Talk.query.filter_by(id=talk_id).first()
