import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format(
            'postgres@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "question": "In which royal palace would you find the Hall of Mirrors?"}
        self.previous_questions = [
            {
                "answer": "Escher",
                "category": "2",
                "difficulty": 1,
                "id": 16,
                "question": "Which Dutch graphic artist 2013 initials M C was a creator of optical illusions?"

            }
        ]

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

    def test_405_if_get_categories_not_allowed(self):
        res = self.client().post('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEquals(data['message'], 'Method Not Allowed')

    def test_get_paginate_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_404_if_get_paginate_questions_not_found(self):
        res = self.client().get('/questions?page=100')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEquals(data['message'], 'Not found')

    def test_delete_question(self):
        res = self.client().delete('/questions/9')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 9).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 9)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEquals(question, None)

    def test_422_if_delete_question_unprocessable(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEquals(data['message'], 'unprocessable')

    def test_post_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_405_if_post_new_question_not_allowed(self):
        res = self.client().post('/questions/15', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEquals(data['message'], 'Method Not Allowed')

    def test_post_search_questions(self):
        res = self.client().post(
            '/questions/search',
            json={
                'search_term': 'palace'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_405_if_post_search_questions_not_allowed(self):
        res = self.client().get(
            '/questions/search',
            json={
                'search_term': 'palace'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEquals(data['message'], 'Method Not Allowed')

    def test_get_category_questions(self):
        res = self.client().get('/categories/4/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['current_category'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_404_if_get_category_questions_not_found(self):
        res = self.client().get('/categories/1/question')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEquals(data['message'], 'Not found')

    def test_post_quiz_questions(self):
        res = self.client().post(
            '/quizzes',
            json={
                'quiz_category': {
                    "type": "Art",
                    "id": "2"},
                'previous_questions': []})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    def test_422_if_get_paginate_questions_unprocessable(self):
        res = self.client().post(
            '/quizzes',
            json={
                'quiz_category': "2",
                'previous_questions': []})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEquals(data['message'], 'unprocessable')

    def test_500_server_error(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEquals(data['message'], 'Internal Server Error')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
