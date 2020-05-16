from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, backref


class Question(db.Model):
    __tablename_ = "Table question"
    id = Column(Integer, primary_key=True)
    question = Column(String(100), nullable=False)
    datepost = Column(
        DateTime, default=datetime.utcnow(), nullable=False)
    answer = relationship('Answer', backref='question', lazy=True)

    def __repr__(self):
        return '<Question> {}'.format(self.id, self.question)

    def view(self):
        return {"id": self.id, "title": self.question, "date": self.datepost, "answer": self.answer}


class Answer(db.Model):
    __tablename_ = "Table Answer"
    id = Column(Integer, primary_key=True)
    answer = Column(Text, nullable=False)
    question_id = Column(Integer, ForeignKey(
        'question.id'), nullable=False)

    def __repr__(self):
        return "<Answer> {}".format(self.id, self.question_id)


# class Tag(db.Model):
#     __tablename_ = "Table Tag"
#     id = Column(Integer, primary_key=True)
#     tagname = Column(String(50))
#     tagquestion = relationship("Question", backref="tagQuestion", lazy=True)

#     def __repr__(self):
#         return "<Tag> {}".format(self.id, self.question_id, self.tagname)
