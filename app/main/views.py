from flask import render_template,request,redirect,url_for
from . import main
from .pitchform import PitchForm
from ..models import Pitch
from .. import db

#views
@main.route('/')
def index():
    '''
    view  root page function that returns 
    the index page and its data
    '''
    return render_template('index.html')

@main.route('/newpitch' ,methods = ['GET','POST'])
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch = Pitch(title = form.title.data,pitchcontent = form.pitchcontent.data,pitchcategory = form.pitchcategory.data)

        pitch.save_pitch()
        # print('Your Pitch has been successfully saved!')
        return redirect(url_for('main.new_pitch'))
    return render_template('newpitch.html',pitch_form = form)

@main.route('/pickup',methods = ['GET'])
def pickup_lines():
    return render_template('pickup.html')

@main.route('/interview',methods = ['GET'])
def interview_pi():
    return render_template('interview.html')

@main.route('/thought',methods = ['GET'])
def thought_pi():
    return render_template('thought.html')

@main.route('/adventure',methods = ['GET'])
def adventure_pi():
    return render_template('adventure.html')

