from repositories.feedback_repository import FeedbackRepository


class FeedbackService:

    @classmethod
    def save_feedback(cls, talk_id, feedback_detail):
        feedback_repository = FeedbackRepository()
        feedback_repository.insert_feedback_for_talk(talk_id, feedback_detail)
