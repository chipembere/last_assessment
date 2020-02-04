from app import app
from flask import render_template
import generator

@app.route('/')
def index():

    render_template('index.html', activity='activity', people = 'people')

@app.route('/getIdea', methods=['POST'])
def idea():

    people, activity = generator.getRandomIdea()

    return render_template('index.html', title='Home', activity=activity, people = people)
