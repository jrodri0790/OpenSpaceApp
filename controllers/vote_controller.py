from flask import Blueprint, abort
from flask import request
from sqlalchemy.exc import IntegrityError

from middlewares.code_validator import validate_code
from services.vote_service import VoteService

vote_blueprint = Blueprint('vote', __name__)
results_blueprint = Blueprint('results', __name__)


@vote_blueprint.route('/vote', methods=['POST'])
@validate_code
def vote():
    code = request.json['code']
    votes = request.get_json()['talks']
    vote_service = VoteService()
    try:
        vote_service.register_votes(code, votes)
        return "Thanks for voting", 200
    except IntegrityError:
        abort(500, "The talk does not exist")


@results_blueprint.route('/results', methods=['GET'])
def get_results():
    vote_service = VoteService()
    return vote_service.get_talks_sorted_by_votes(), 200
