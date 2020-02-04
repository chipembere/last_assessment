from app import app
from flask import render_template
from app import generator

@app.route('/')
def index():
    return render_template('index.html', activity='activity', people = 'people')

@app.route('/getIdea', methods=['get'])
def idea():
    # this doesn't match the signature of the actual method (activities, people)
    people, activity = generator.get_random_idea()

    return render_template('index.html', title='Home', activity=activity, people = people)
