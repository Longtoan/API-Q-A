from flask import current_app as app
from .model import db, Question, Answer
from flask import jsonify, request
from sqlalchemy import exc


@app.route("/question", methods=["POST"])
def create():
    if not request.json and method == "POST":
        abort(400)
    question = request.json['question']
    data = Question(question=question)
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        db.session.flush()
    return jsonify({"message": "successfully"}), 200


@app.route("/question", methods=["GET"])
def view():
    return jsonify({"question": list(map(lambda data: data.view(), Question.query.all()))})


@app.route("/question/<int:id>", methods=["POST"])
def create():
    if not request.json and method == "POST":
        abort(400)
    answer = request.json['answer']
    data = Answer(answer=answer)
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        db.session.flush()
    return jsonify({"message": "successfully"}), 400
