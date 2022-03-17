{% include navigation.html %}



# Create Task Project

## Runtime
[Link to runtime](https://nastyawakened.cf/quizcrud/quizDB/)

## Idea
* Create a system of taking a quiz where you can see if you are correct or incorrect, move to next question, and get a score.
* Also have a database so that quiz questions can be created and stored server side. 
* [Issue with commits](https://github.com/NastyAwakened/NastyAwakened/issues/136)
* [Jump to my video and written responses](https://github.com/NastyAwakened/NastyAwakened/wiki/Sahil-Create-Task-Page#my-video)
* PBL Feature: This is implemented as PBL and can be found under the "Classes tab" and is called "Quiz Page".

## Snippets
## How my project meets the program requirements
* Input from user on which answer is selected, also next question and submit button

Code for one of the answer choice inputs: 
```html
<div id='block-11' style='padding: 10px;'>
            <label for='option1' style=' padding: 5px; font-size: 2.5rem;'>
                <input type='radio' name='option' value='' id='option1' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' />
                <span id='choicetext-1'></span>
                <div class="incorrect"></div>
            </label>
            <span id='result-11'></span>
        </div>
```
Code for choosing which question to see at end input box:
```html
<div id="show" style="display: none">
        <input type="text" id="chosenQuestion">
        <button id="chosenButton" onclick="specificQuestion()"> Choose which question to see</button>
    </div>
```
Code for button to go to next question, calling newQuestion function:
```html
 <button id = "newQuestionButton", onclick="newQuestion()">New Question</button>
```

* SQL Database has stored data of the quiz questions and answers

Code:
```python 
class Quiz(db.Model):
    # define the Users schema
    questionID = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), unique=False, nullable=False)
    answer1 = db.Column(db.String(255), unique=True, nullable=False)
    answer2 = db.Column(db.String(255), unique=False, nullable=False)
    answer3 = db.Column(db.String(255), unique=False, nullable=False)
    answer4 = db.Column(db.String(255), unique=False, nullable=False)
    correctAnswer = db.Column(db.String(255), unique=False, nullable=False)

# constructor of a User object, initializes of instance variables within object
    def __init__(self, question, answer1, answer2, answer3, answer4, correctAnswer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correctAnswer = correctAnswer


# CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "questionID": self.questionID,
            "question": self.question,
            "answer1": self.answer1,
            "answer2": self.answer2,
            "answer3": self.answer3,
            "answer4": self.answer4,
            "correctAnswer": self.correctAnswer
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, question="", answer1="", answer2="", answer3="", answer4="", correctAnswer=""):
        """only updates values with length"""
        if len(question) > 0:
            self.question = question
        if len(answer1) > 0:
            self.answer1 = answer1
        if len(answer2) > 0:
            self.answer2 = answer2
        if len(answer3) > 0:
            self.answer3 = answer3
        if len(answer4) > 0:
            self.answer4 = answer4
        if len(correctAnswer) > 0:
            self.correctAnswer = correctAnswer
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
```
```python
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests
from __init__ import db

# Import the new class from model
from crud2.model import Quiz

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
# Blueprint is important; in the navbar, to reference a page from the render templates in this python file,
# you must use the syntax href={{ url_for('blueprintName.functionName') }}
# functionName is just the name of the function with the render template for that page
app_crud_quiz = Blueprint('quizcrud', __name__,
                     url_prefix='/quizcrud',
                     template_folder='templates/crud2/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud_quiz)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# Same process here of changing everything to your new class and variables
def quiz_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Quiz.query.all()]


def quiz_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Quiz.query.filter((Quiz.question.ilike(term)) | (Quiz.answer1.ilike(term)) | (Quiz.answer2.ilike(term)) | (Quiz.answer3.ilike(term)) | (Quiz.answer4.ilike(term)) | (Quiz.correctAnswer.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def quiz_by_id(questionID):
    """finds User in table matching userid """
    x = Quiz.query.filter_by(questionID=questionID).first()
    print(x)
    return Quiz.query.filter_by(questionID=questionID).first()

def quiz_by_question(question):
    """finds User in table matching email """
    return Quiz.query.filter_by(question=question).first()


# Default URL
# Default URL
@app_crud_quiz.route('/')
def crudQuiz():
    """obtains all Users from table and loads Admin Form"""
    # table = quiz_all passes in the entire data table
    return render_template("crudQuiz.html", table=quiz_all())

@app_crud_quiz.route('/quizDB/')
def quizDB():
    """obtains all Users from table and loads Admin Form"""
    # table = quiz_all passes in the entire data table
    return render_template("quizDB.html", table=quiz_all())


# CRUD create/add
@app_crud_quiz.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Quiz(
            request.form.get("question"),
            request.form.get("answer1"),
            request.form.get("answer2"),
            request.form.get("answer3"),
            request.form.get("answer4"),
            request.form.get("correctAnswer")
        )
        po.create()
    # Utilizing the function from model
    return redirect(url_for('quizcrud.crudQuiz'))


# CRUD read
@app_crud_quiz.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        questionID = request.form.get("questionID")
        po = quiz_by_id(questionID)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("quizDB.html", table=table)


# CRUD update
@app_crud_quiz.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        questionID = request.form.get("questionID")
        question = request.form.get("question")
        answer1 = request.form.get("answer1")
        answer2 = request.form.get("answer2")
        answer3 = request.form.get("answer3")
        request.form.get("answer4")
        request.form.get("correctAnswer")
        po = quiz_by_id(questionID)
        if po is not None:
            po.update(answer1)
            po.update(answer2)
            po.update(answer3)
    return redirect(url_for('quizcrud.crudQuiz'))


# CRUD delete
@app_crud_quiz.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        questionID = request.form.get("questionID")
        po = quiz_by_id(questionID)
        if po is not None:
            po.delete()
    return redirect(url_for('quizcrud.crudQuiz'))
```

* Procedure for displayQuestion has parameter of chosen question so it knows which question to display. The return type is just string in changing the DOM.

Code:
```javascript 
 {# Function with parameters, showing a specific question. Called in newQuestion. #}
        function displayQuestion(chosenQuestion) {
            document.getElementById('showQuestion').innerHTML = allData[chosenQuestion-1]['question'];
            document.getElementById('choicetext-1').innerHTML = allData[chosenQuestion-1]['answer1'];
            document.getElementById('choicetext-2').innerHTML = allData[chosenQuestion-1]['answer2'];
            document.getElementById('choicetext-3').innerHTML = allData[chosenQuestion-1]['answer3'];
            document.getElementById('choicetext-4').innerHTML = allData[chosenQuestion-1]['answer4'];
        }
```
* Sequence through if/else statement with question number
* Selection by displaying the specific questions based on the index (which is determined by question number)

Code for both sequence and selection: 
```javascript 
           if ((questionNumber+1 >= allData.length)) {
                document.getElementById('newQuestionButton').innerHTML = 'End Quiz'
                end+=1
                console.log(end)
                if (end==2) {
                    document.getElementById('done').innerHTML = 'Good job! You got ' + score + '/' + (allData.length).toString()
                    {# Calling the function to show the input box to look at a specific question #}
                    show_last();
                }
            }
            else {
                document.getElementById('newQuestionButton').innerHTML = 'Next Question';
                questionNumber +=1
            }
```
* Iteration in the answer checking system

Code:
```javascript 
for (let i = 1; i < 5; i++) {
                if (document.getElementById('option' + i).checked) {
                    if (correct ==  allData[answerindex]['answer' + i.toString()]) {
                        var x = allData[answerindex]['answer' + i.toString()];
                        console.log(x)
                        document.getElementById('block-1' + i.toString()).style.border = '3px solid limegreen'
                        document.getElementById('result-1' + i.toString()).style.color = 'limegreen'
                        document.getElementById('result-1' + i.toString()).innerHTML = 'Correct!'
                        score = score + 1
                    }
                    else {
                        document.getElementById('block-1' + i.toString()).style.border = '3px solid red'
                        document.getElementById('result-1' + i.toString()).style.color = 'red'
                        document.getElementById('result-1' + i.toString()).innerHTML = 'Incorrect!'
                    }
                }
            }
```
* Procedure is called by the button

Code:
```html 
<button id = "newQuestionButton", onclick="newQuestion()">New Question</button>
```
```javascript
 if (end==2) {
                    document.getElementById('done').innerHTML = 'Good job! You got ' + score + '/' + (allData.length).toString()
                    {# Calling the function to show the input box to look at a specific question #}
                    show_last();
                }
```
* Instructions for output through comments in the code.

# My Video

* [Sahil Create Task Video](https://www.youtube.com/watch?v=B9sHHwXYmSk)

# Written Responses

* 3a-3d responses should not be more than 750 words, not including code.

## 3a. Provide a written response that does all three of the following:

### Describes the overall purpose of the program

* The purpose of the program is for a user to be able to make questions and answers and store them on a database. Then, they can be presented in a quiz format that gives insight into correct answers and also provides a score. 

### Describes what functionality of the program is demonstrated in the video

* The functionality of the program shown is to be able to take a quiz and get a score, as well as a final result. Each time you answer a question, the program will tell you if you are correct or wrong. Previous questions can be viewed again upon finishing the quiz.

### Describes the input and output of the program demonstrated in the video

* Input of the program is shown through being able to select an answer choice as well as pressing the buttons for next question and submit. Output is shown through correct/incorrect upon answering as well as a score and the display of the question and answer choices. Input is also there for the text box to show score, output is to show or hide score. Finally, input is there for textbox to show questions and answers and output is the display through changing the DOM(Document Object Model). 

## 3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.

###  The first program code segment must show how data have been stored in the list. 

```python 
class Quiz(db.Model):
    # define the Users schema
    questionID = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), unique=False, nullable=False)
    answer1 = db.Column(db.String(255), unique=True, nullable=False)
    answer2 = db.Column(db.String(255), unique=False, nullable=False)
    answer3 = db.Column(db.String(255), unique=False, nullable=False)
    answer4 = db.Column(db.String(255), unique=False, nullable=False)
    correctAnswer = db.Column(db.String(255), unique=False, nullable=False)

# constructor of a User object, initializes of instance variables within object
    def __init__(self, question, answer1, answer2, answer3, answer4, correctAnswer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correctAnswer = correctAnswer


# CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "questionID": self.questionID,
            "question": self.question,
            "answer1": self.answer1,
            "answer2": self.answer2,
            "answer3": self.answer3,
            "answer4": self.answer4,
            "correctAnswer": self.correctAnswer
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, question="", answer1="", answer2="", answer3="", answer4="", correctAnswer=""):
        """only updates values with length"""
        if len(question) > 0:
            self.question = question
        if len(answer1) > 0:
            self.answer1 = answer1
        if len(answer2) > 0:
            self.answer2 = answer2
        if len(answer3) > 0:
            self.answer3 = answer3
        if len(answer4) > 0:
            self.answer4 = answer4
        if len(correctAnswer) > 0:
            self.correctAnswer = correctAnswer
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
```

```python
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests
from __init__ import db

# Import the new class from model
from crud2.model import Quiz

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
# Blueprint is important; in the navbar, to reference a page from the render templates in this python file,
# you must use the syntax href={{ url_for('blueprintName.functionName') }}
# functionName is just the name of the function with the render template for that page
app_crud_quiz = Blueprint('quizcrud', __name__,
                     url_prefix='/quizcrud',
                     template_folder='templates/crud2/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud_quiz)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# Same process here of changing everything to your new class and variables
def quiz_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Quiz.query.all()]

@app_crud_quiz.route('/quizDB/')
def quizDB():
    """obtains all Users from table and loads Admin Form"""
    # table = quiz_all passes in the entire data table
    return render_template("quizDB.html", table=quiz_all())
```

### The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. 

```javascript
  {# Passing in the data table from jinja to javascript; now it can be used easily in javascript#}
        var allData = {{ allData | safe}};
   {# Function with parameters, showing a specific question. Called in newQuestion. #}
        function displayQuestion(chosenQuestion) {
            if (chosenQuestion-1 > -1 && chosenQuestion < allData.length) {
                document.getElementById("all").style.display = 'inline';
                document.getElementById('showQuestion').innerHTML = allData[chosenQuestion-1]['question'];
                document.getElementById('choice1').innerHTML = allData[chosenQuestion-1]['answer1'];
                document.getElementById('choice2').innerHTML = allData[chosenQuestion-1]['answer2'];
                document.getElementById('choice3').innerHTML = allData[chosenQuestion-1]['answer3'];
                document.getElementById('choice4').innerHTML = allData[chosenQuestion-1]['answer4'];
            }
            else {
                var displayed = Math.floor(Math.random() * (allData.length))
                document.getElementById("all").style.display = 'inline';
                document.getElementById('showQuestion').innerHTML = allData[displayed]['question'];
                document.getElementById('choice1').innerHTML = allData[displayed]['answer1'];
                document.getElementById('choice2').innerHTML = allData[displayed]['answer2'];
                document.getElementById('choice3').innerHTML = allData[displayed]['answer3'];
                document.getElementById('choice4').innerHTML = allData[displayed]['answer4'];
            }
        }
 {# This function is called by the button for begin quiz/next question/endquiz; it determines what questions and answers to display based on the value of question number. #}
        {# Question number is also updated through this procedure #}
        function newQuestion() {
            if (questionNumber > -1) {
                document.getElementById("all").style.display = 'inline';
            }
            document.getElementById('showQuestion').innerHTML = allData[questionNumber]['question'];
            document.getElementById('choice1').innerHTML = allData[questionNumber]['answer1'];
            document.getElementById('choice2').innerHTML = allData[questionNumber]['answer2'];
            document.getElementById('choice3').innerHTML = allData[questionNumber]['answer3'];
            document.getElementById('choice4').innerHTML = allData[questionNumber]['answer4'];
```

### Identifies the name of the list being used in this response

* In python, the list is generated by the function quiz_all(). It is then passed in as 'table' to jinja through the render template, and in javascript the name of the list that is referenced is 'allData'. 

### Describes what the data contained in the list represent in your program

* The list gets its data through user input on a UI through CRUD features on an SQL database. The data that it contains is in a table format, where each entry has a question, 4 answer choices, and a correct answer; a questionID is automatically assigned. 

### Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list.

* Without a list, it would not be possible for the user to enter in new questions and answers to be used in the quiz without hardcoding them. Without using a list, rather than using loops and updating questionNumber and simply indexing the list, each question would have to be separately hard coded resulting in n times the amount of code where n is the number of questions. 

## 3c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure. 

### The first program code segment must be a student-developed procedure that:

1. Defines the procedure’s name and return type (if necessary)
2. Contains and uses one or more parameters that have an effect
on the functionality of the procedure
3. Implements an algorithm that includes sequencing, selection,
and iteration 

```javascript
function evaluation(view) {
            var correct = allData[answerindex]['correctAnswer'].toString()
            document.getElementById('block1').style.border = '3px'
            document.getElementById('result1').style.color = 'white'
            document.getElementById('result1').innerHTML = ''
            document.getElementById('block2').style.border = '3px'
            document.getElementById('result2').style.color = 'white'
            document.getElementById('result2').innerHTML = ''
            document.getElementById('block3').style.border = '3px'
            document.getElementById('result3').style.color = 'white'
            document.getElementById('result3').innerHTML = ''
            document.getElementById('block4').style.border = '3px'
            document.getElementById('result4').style.color = 'white'
            document.getElementById('result4').innerHTML = ''
            for (let i = 1; i < 5; i++) {
                if (document.getElementById('option' + i).checked) {
                    if (correct ==  allData[answerindex]['answer' + i.toString()]) {
                        var x = allData[answerindex]['answer' + i.toString()];
                        console.log(x)
                        document.getElementById('block' + i.toString()).style.border = '3px solid limegreen'
                        document.getElementById('result' + i.toString()).style.color = 'limegreen'
                        document.getElementById('result' + i.toString()).innerHTML = 'Correct!'
                        if (view != "Yes" && view != "No") {
                            score = score + 1
                        }
                    }
                    else {
                        document.getElementById('block' + i.toString()).style.border = '3px solid red'
                        document.getElementById('result' + i.toString()).style.color = 'red'
                        document.getElementById('result' + i.toString()).innerHTML = 'Incorrect!'
                    }
                }
            }
            document.getElementById('score').innerHTML = "Score:" + score;

            if(view == "Yes") {
                document.getElementById("score").style.display = 'block';
            }
            else if(view == "No") {
                document.getElementById("score").style.display = 'none';
            }
            else {
                document.getElementById("score").style.display = 'none';
            }
        }
```

### The second program code segment must show where your student-developed procedure is being called in your program.


```html
    <button id="submit" type='button' onclick='evaluation()'>Submit</button>
```

```javascript
        function showScore() {
            var chosen = document.getElementById('scoreView').value;
            evaluation(chosen);
        }
```

### Describes in general what the identified procedure does and how it contributes to the overall functionality of the program

* The procedure checks the submitted answer and displays whether it was correct or incorrect. It also implements the scoring feature based on if the answer was right or wrong. Finally, it determines whether the score is displayed or not. 

###  Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.

* The list which contains the questions and answers also has the correct answer for each question. At the index of the current question, which is answerindex as determined by a separate procedure, correctAnswer is then indexed for that question and converted to a string and stored in a variable to be compared with as the correct answer. The question and answer blocks are then styled. A for loop is used with 4 iterations to check each answer choice and change the surrounding styling to green and display correct if the answer is right or change it to red and display incorrect if the answer is wrong. Additionally, score is increased by 1 for a correct answer but it stays the same if the answer is incorrect. The difference in styling is done through an if statement that checks if that answer matches the variable correct previously established. The parameter 'view' is passed in by an input box and through if else statements, if it is yes then the score element DOM(Document Object Model) is shown but otherwise it is not shown. 

## 3d. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.

### First call: 

If the evaluation function is called with the argument "Yes" by typing that into the input box, then the segment of code will execute to display the score. 

### Second call: 

If the evaluation function is called with the argument "No" or anything else but "Yes", then the segment of code will execute to hide the score. 

### Describes what condition(s) is being tested by each call to the procedure. Condition(s) tested by the first call: 

The condition tested is if the argument is equal to the string "Yes".

### Condition(s) tested by the second call: 

The condition tested is if the argument is equal to the string "No".

### Identifies the result of each call. Result of the first call: 

The DOM(Document Object Model) of the score text will be shown; in other words, the score will be visible. 

### Result of the second call: 

The DOM of the score text will not be shown, so the score will not be visible. 
