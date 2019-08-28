from models.feedback import Feedback
from database.database import db


class FeedbackRepository:

    @classmethod
    def find_all(cls):
        return Feedback.query.all()

    @classmethod
    def insert_feedback_for_talk(cls, talk_id, detail):
        feedback = Feedback(detail, talk_id)
        db.session.add(feedback)
        db.session.commit()
