from repositories.code_talk_repository import CodeTalkRepository


class VoteService:

    @classmethod
    def register_votes(cls, code, votes: []):
        code_talk_repository = CodeTalkRepository()
        for vote in votes:
            code_talk_repository.insert_vote_for_talk(code, vote)

    @classmethod
    def get_talks_sorted_by_votes(cls):
        code_talk_repository = CodeTalkRepository()
        voted_talks = code_talk_repository.find_talks_and_votes()
        text_voted_talks = ''
        break_line = '\n'
        space = " "
        for name, votes in voted_talks:
            text_voted_talks += name
            text_voted_talks += space
            text_voted_talks += votes
            text_voted_talks += break_line
        return text_voted_talks
