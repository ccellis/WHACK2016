from flask.ext.wtf import Form
from wtforms import StringField, RadioField, SelectField
from wtforms.validators import DataRequired


class ReviewForm(Form):
    review = StringField('review', validators=[DataRequired()])
    rating = SelectField('rating', choices=[(str(x),str(x)) for x in range(1,6)])