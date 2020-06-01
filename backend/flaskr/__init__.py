import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    print(page)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization')
        response.headers.add(
            'Access-Control-Allow-Methods',
            " GET, POST, PATCH, DELETE, OPTIONS")
        return response

    @app.route('/')
    def index():
        abort(500)

    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.all()
        formatted_categories = {
            category.id: category.type for category in categories}
        return jsonify({
            'success': True,
            'categories': formatted_categories
        }), 200

    @app.route('/questions',  methods=['GET','OPTIONS'])
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        categories = Category.query.all()
        current_categories = {
            category.id: category.type for category in categories}
        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'categories': current_categories,
            'total_questions': len(Question.query.all()),
            'current_category': None
        }), 200

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': current_questions,
                'total_questions': len(Question.query.all())
            }), 200
        except BaseException:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_question():

        if not request.method == 'POST':
            abort(405)

        body = request.get_json()

        question = body.get('question', None)
        answer = body.get('answer', None)
        category = body.get('category', None)
        difficulty = body.get('difficulty', None)
        try:
            question = Question(question, answer, category, difficulty)
            question.insert()

            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'success': True,
                'created': question.id,
                'questions': current_questions,
                'total_questions': len(Question.query.all())
            }), 200
        except BaseException:
            abort(422)

    @app.route('/questions/search', methods=['POST'])
    def search_questions():

        if not request.method == 'POST':
            abort(405)

        body = request.get_json()
        search_term = body.get('search_term')
        try:
            selection = Question.query.filter(
                Question.question.ilike(
                    '%{}%'.format(search_term))).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'success': True,
                'questions': current_questions,
                'current_category': None,
                'total_questions': len(selection)
            }), 200
        except BaseException:
            abort(422)

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_category_questions(category_id,):
        try:
            selection = Question.query.filter_by(
                category=str(category_id)).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'success': True,
                'questions': current_questions,
                'current_category': category_id,
                'total_questions': len(selection)
            }), 200
        except BaseException:
            abort(422)

    @app.route('/quizzes', methods=['POST'])
    def get_quiz_questions():
        if not request.method == 'POST':
            abort(405)
        body = request.get_json()
        category = body.get('quiz_category')
        previous_questions = body.get('previous_questions')
        try:
            if category['id'] == 0:
                current_questions = Question.query.filter(
                    Question.id.notin_(previous_questions)).all()
            else:
                current_questions = Question.query.filter_by(
                    category=category['id']).filter(
                    Question.id.notin_(previous_questions)).all()

            if len(current_questions) == 0:
                next_question = None
            else:
                next_question = random.choice(current_questions).format()

            return jsonify({
                'success': True,
                'previousQuestions': previous_questions,
                'question': next_question
            }), 200
        except BaseException:
            abort(422)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    return app
