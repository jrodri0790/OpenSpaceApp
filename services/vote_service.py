from repositories.code_talk_repository import CodeTalkRepository


class VoteService:

    @classmethod
    def register_votes(cls, code, votes: []):
        code_talk_repository = CodeTalkRepository()
        for vote in votes:
            code_talk_repository.insert_vote_for_talk(code, vote)
