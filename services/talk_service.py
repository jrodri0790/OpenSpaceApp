from repositories.talk_repository import TalkRepository


class TalkService:

    @classmethod
    def get_all_talks(cls):
        talk_repository = TalkRepository()
        return talk_repository.find_all()

    @classmethod
    def get_talk_by_id(cls, code):
        talk_repository = TalkRepository()
        return talk_repository.find_by_id(code)
