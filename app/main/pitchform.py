from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField,RadioField
from wtforms.validators import Required,AnyOf



class PitchForm(FlaskForm):
    title = StringField('Pitch Title',validators=[Required()])
    pitchcontent =TextAreaField('Pitch Content',validators=[Required()])
    pitchcategory =RadioField('lease pick from the following categories',choices=[('pick_up','Pick-up lines'),('interview','Interview Pitches'),
        ('thought_full', 'Thoughtful life pitches'),
        ('adventure', 'Happy life/Motivational/adventure')],validators=[Required()])
    submit = SubmitField('Submit') 