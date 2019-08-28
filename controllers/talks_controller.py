from flask import Blueprint, abort, jsonify
from sqlalchemy.exc import IntegrityError

from schemas.feedback_schema import talks_schema, talk_schema, feedback_list_schema
from services.talk_service import TalkService

talks_blueprint = Blueprint('talks', __name__)
talk_by_id_blueprint = Blueprint('talk_by_id', __name__)


@talks_blueprint.route('/talks/', methods=['GET'])
def get_talks():
    talks_service = TalkService()
    try:
        talks = talks_service.get_all_talks()
        result = talks_schema.dump(talks)
        return jsonify(result), 200
    except IntegrityError:
        abort(404, "Talks not found") @ talks_blueprint.route('/talks/', methods=['GET'])


@talk_by_id_blueprint.route('/talk/<int:code>', methods=['GET'])
def get_talk_by_id(code):
    talks_service = TalkService()
    try:
        talk = talks_service.get_talk_by_id(code)
        talk_result = talk_schema.dump(talk)
        feedback_result = feedback_list_schema.dump(talk.feedback_list.all())
        return jsonify({"talk": talk_result, "feedback": feedback_result}), 200
    except IntegrityError:
        abort(404, "Talk not found")
