from flask import current_app as app
from .model import db, Question, Answer, Tag
from flask import jsonify, request, make_response
from sqlalchemy import exc


# Create new question
@app.route("/question/new", methods=["POST"])
def createQuestion():
    if not request.json:
        abort(400)
    question = request.json['question']
    tag_id = request.json['tag_id']
    data = Question(question=question, tag_id=tag_id)
    try:
        data.saveDb()
    except exc.SQLAlchemyError:
        db.session.rollback()

    return jsonify({"message": "successfully"}), 200

# get all question
@app.route("/question", methods=["GET"])
def question():
    return jsonify({"question": list(map(lambda data: data.view(), Question.query.all()))})
# delete question
@app.route("/question/<int:question_id>/delete", methods=["DELETE"])
def deleteQuestion(question_id):
    question_id = Question.query.get_or_404(question_id)

    if question_id and request.method == "DELETE":
        db.session.delete(question_id)
        db.session.commit()

        return jsonify({"message": "delete successfully"})

# update question
# @app.route("question/<int:question_id>/update", methods=["PUT"])
# def updateQuestion(question_id):
#     question_id = Question.query.get_or_404(question_id)

#     question = request.json['question'] or None
#     tag_id = request.json['tag_id'] or None
#     data = Question(question_id=question_id, question=question, tag_id=tag_id)
#     if request.method == "PUT":
#         question.saveDb(data)
#         return jsonify({"update successfully"})
# get question id
@app.route("/question/<int:question_id>", methods=["GET"])
def question_id(question_id):
    ques = Question.query.get_or_404(question_id)
    if not ques:
        return jsonify({"message": "Question is not exits"})
    return jsonify({"question": ques.view()})


# create new answer
@app.route("/answer/new", methods=["POST"])
def newAnswer():
    if request.json:
        answer = request.json['answer']
        question_id = request.json['question_id']
        data = Answer(answer=answer, question_id=question_id)
        try:
            data.saveDb()
        except exc.SQLAlchemyError:
            db.session.rollback()

        return jsonify({"message": "successfully"})

# create tag
@app.route("/tag/new", methods=["POST"])
def newTag():
    if request.json:
        tagname = request.json['tagname']
        des = request.json['description']
        data = Tag(tagname=tagname, description=des)
        try:
            db.session.add(data)
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()

        return jsonify({"message": "successfully"})

# Get all tag
@app.route("/tag", methods=["GET"])
def getTag():
    return jsonify({"Tag": list(map(lambda data: data.view(), Tag.query.all()))})

# get tag id
@app.route("/tag/<int:tag_id>", methods=["GET"])
def tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    if not tag:
        return jsonify({"tag is not exits"})
    return jsonify({"Tag": tag.view()})

# deteletag
@app.route("/tag/<int:tag_id>/delete", methods=["DELETE"])
def deleteTag(tag_id):
    tag = Tag.query.get_or_404(tag_id)

    if request.method == "DELETE":

        db.session.delete(tag)
        db.session.commit()
        return jsonify({"message": "successfully delete id {}".format(tag_id)})
