from repositories.talk_repository import TalkRepository


class TalkService:

    @classmethod
    def get_all_talks(cls):
        code_talk_repository = TalkRepository()
        return code_talk_repository.find_all()
