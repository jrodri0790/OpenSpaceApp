from flask import request, abort, current_app
import re

from repositories.code_repository import CodeRepository
from repositories.code_talk_repository import CodeTalkRepository


def validate_code(func):
    def validation(*args, **kwargs):
        code_received = request.json['code']
        ab = re.compile("XC[A-Z]{3}-[\d]{3}")
        is_valid_code = ab.match(code_received)
        if not is_valid_code:
            current_app.logger.error("Invalid code {}".format(code_received))
            abort(403)
        code_repository = CodeRepository()
        db_code = code_repository.find_code(code_received)
        if db_code is None:
            current_app.logger.error("Code is not in the database {}".format(code_received))
            abort(403)
        vote_repository = CodeTalkRepository()
        code_already_voted = vote_repository.find_by_code(code_received)
        if code_already_voted is not None:
            current_app.logger.error("Code already voted {}".format(code_received))
            abort(401, "You have already voted")
        return func(*args, **kwargs)
    return validation
