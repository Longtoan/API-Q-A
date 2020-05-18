from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, backref


class Question(db.Model):
    __tablename_ = "Table question"
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(100), nullable=False)
    date_create = Column(
        DateTime, default=datetime.utcnow(), nullable=False)
    answer = relationship('Answer', backref='question',
                          lazy=True, cascade="all,delete")
    tag_id = Column(Integer, ForeignKey(
        'tag.id'))

    usercreate = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return '<Question> {}'.format(self.id, self.question)

    def view(self):
        ans_id = [i.answer for i in self.answer]
        return {"id": self.id, "question": self.question, "date": self.date_create, "answer": ans_id}

    def saveDb(self):
        db.session.add(self)
        db.session.commit()


class Answer(db.Model):
    __tablename_ = "Table Answer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    answer = Column(Text, nullable=False)
    question_id = Column(Integer, ForeignKey(
        'question.id'), nullable=False)
    usercreate = Column(Integer, ForeignKey('user.id'))
    date_create = Column(
        DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return "<Answer> {}".format(self.id, self.question_id)

    def view(self):

        return {"id": self.id, "answer": self.answer, "date": self.date_create, "question_id": self.question_id}

    def saveDb(self):
        db.session.add(self)
        db.session.commit()


class Tag(db.Model):
    __tablename_ = "Table Tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tagname = Column(String(50))
    description = Column(Text)
    tagquestion = relationship(
        "Question", backref="tag", lazy=True, cascade="all,delete")

    def __repr__(self):
        return "<Tag> {}".format(self.id, self.question_id, self.tagname)

    def view(self):
        ques = [i.question for i in self.tagquestion]
        return {"id": self.id, "tag": self.tagname, "question": ques}

    def saveDb(self):
        db.session.add(self)
        db.session.commit()


class User(db.Model):
    __tablename_ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    email = Column(db.String(20))
    password = Column(db.String(30))

    userquestion = relationship("Question", backref="userquestion", lazy=True)
    useranswer = relationship("Answer", backref="useranswer", lazy=True)
