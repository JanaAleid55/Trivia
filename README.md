# Full Stack Trivia API

This project is a Trivia App for everyone who look for the since of fun and changing.
By playing Trivia you are going to prove how smart you are,learn something new while having fun.
As a part of the key features in Trivia App the user is able to display questions both all questions and by category, Delete questions, add questions,Search for questions based on search term and play the quiz game, randomizing either all questions or within a specific category. 

All backend code follows [`PEP8 style guidlines`](https://www.python.org/dev/peps/pep-0008/)


#  Guidelines
Hello everyone! You can use this base in various workspaces and change or improve any stage, also notice that you can apply any change in the frontend section and should referene those sections for formatting your endpoints and responses, and update the frontend to match the endpoints you choose and the programmed behavior.

You should feel free to expand on the project in any way you can dream up to extend your skills. For instance, you could add additional question information to each entry or create individual question views including more information about the question, your thoughts or when you completed it.

# Getting Started
## Pre-requisites and Local Development
Developers using this project should already have Python3, pip and node installed on their local machines.

## Backend

From the backend folder run [pip install requirements.txt](). All required packages are included in the requirements file.
To run the application run the following commands:
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
These commands put the application in development and directs our application to use the __init__.py file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [`Flask documentation`](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration.

## Frontend
From the frontend folder, run the following commands to start the client:
```bash
npm install // only once to install dependencies
npm start 
```
By default, the frontend will run on localhost:3000.

## Tests
In order to run tests navigate to the backend folder and run the following commands:
```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
The first time you run the tests, omit the dropdb command.

All tests are kept in that file and should be maintained as updates are made to app functionality.

# API Reference
## Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

## Error Handling

Errors are returned as JSON objects in the following format:
```bash
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Server Error
## Endpoints

### GET/categories
- General:
Returns a list of all available categories and success value
- Sample: 
curl http://127.0.0.1:5000/categories
```bash
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```
### GET/questions
- General:
Returns a list of question objects, all categories, current_category, success value, and total number of questions
Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: 
curl http://127.0.0.1:5000/questions or curl 'http://127.0.0.1:5000/questions?page=1'
```bash
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": "2", 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": "2", 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": "1", 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": "1", 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": "4", 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 8
}
```
### POST/questions
- General:
Creates a new question using the submitted question, answer, category and difficulty. Returns the id of the created question, success value, total questions, and questions list based on current page number to update the frontend.
- Sample:
curl -X POST -H "Content-Type: application/json" -d '{"question":"What movie genre is The Rocker?","answer":"Comedy","category":"5","difficulty":"2"}' 'http://127.0.0.1:5000/questions?page=1'
```bash
{
  "created": 24, 
  "questions": [
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": "2", 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": "2", 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": "1", 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": "1", 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": "4", 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Comedy", 
      "category": "5", 
      "difficulty": 2, 
      "id": 24, 
      "question": "What movie genre is The Rocker?"
    }
  ], 
  "success": true, 
  "total_questions": 9
}
```
### DELETE/questions/{question_id}
- General:
Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total questions, and questions list based on current page number to update the frontend.
- Sample: 
curl -X DELETE 'http://127.0.0.1:5000/questions/24?page=1'
```bash
{
  "deleted": 24, 
  "questions": [
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": "2", 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": "2", 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": "1", 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": "1", 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": "4", 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 8
}
```
### POST/questions/search
- General:
Search about the question of the given search term if it exists. Returns the current_category, success value, total questions, and questions list based on search term.
- Sample:
 curl -X POST -H "Content-Type: application/json" -d '{"search_term":"was"}' http://127.0.0.1:5000/questions/search
```bash
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Scarab", 
      "category": "4", 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 1
}
```
### GET/categories/{category_id}/questions
- General:
Returns a list of category questions,current_category, success value, and total number of questions
- Sample:
curl http://127.0.0.1:5000/categories/1/questions
```bash
{
  "current_category": 1, 
  "questions": [
    {
      "answer": "Alexander Fleming", 
      "category": "1", 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": "1", 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}
```
### POST/quizzes
- General:
Returns a random question within the given category, if provided, and that is not one of the previous questions, previousQuestions list,success value. 
- Sample:
curl -X POST -H "Content-Type:application/json" -d '{"quiz_category": {"type": "Art", "id": "2"},"previous_questions":[]}' http://127.0.0.1:5000/quizzes
```bash
{
  "previousQuestions": [], 
  "question": {
    "answer": "Mona Lisa", 
    "category": "2", 
    "difficulty": 3, 
    "id": 17, 
    "question": "La Giaconda is better known as what?"
  }, 
  "success": true
}
```

# Deployment N/A

# Authors
Udacity team, Jana

# Acknowledgements
Special thanks to Udacity team and all of my teachers as well as the helpful monitors who gave me the golden opportunity to do this wonderful project, I am really thankful to them.
