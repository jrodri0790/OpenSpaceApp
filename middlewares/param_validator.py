from flask import request, abort, current_app
import re

from repositories.code_repository import CodeRepository
from repositories.code_talk_repository import CodeTalkRepository


def validate_parameters_for_feedback_controller(func):
    def validation(*args, **kwargs):
        talk_id_received = request.json['talk_id']
        detail_received = request.json['detail']
        if not talk_id_received:
            abort(403, "Talk id must be present")
        if not detail_received.strip():
            abort(403, "Feedback could not be empty")
        try:
            int(talk_id_received)
        except ValueError:
            print("Talk id is not a number")
        return func(*args, **kwargs)

    return validation
