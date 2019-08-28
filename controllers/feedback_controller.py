from flask import Blueprint, abort
from flask import request
from sqlalchemy.exc import IntegrityError

from middlewares.param_validator import validate_parameters_for_feedback_controller
from services.feedback_service import FeedbackService

feedback_blueprint = Blueprint('feedback', __name__)


@feedback_blueprint.route('/feedback', methods=['POST'])
@validate_parameters_for_feedback_controller
def vote():
    talk_id = request.json['talk_id']
    feedback_detail = request.get_json()['detail']
    feedback_service = FeedbackService()
    try:
        feedback_service.save_feedback(talk_id, feedback_detail)
        return "Thanks for your feedback! It is really important for us", 200
    except IntegrityError:
        abort(500, "The talk does not exist")
