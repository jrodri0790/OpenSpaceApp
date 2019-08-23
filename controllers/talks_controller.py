import json

from flask import Blueprint, abort
from sqlalchemy.exc import IntegrityError
from models.talk import Talk
from services.talk_service import TalkService

talks_blueprint = Blueprint('talks', __name__)


@talks_blueprint.route('/talks', methods=['GET'])
def get_talks():
    talks_service = TalkService()
    try:
        talks = talks_service.get_all_talks()
        return json.dumps(Talk.serialize_list(talks)), 200
    except IntegrityError:
        abort(404, "Talks not found")
