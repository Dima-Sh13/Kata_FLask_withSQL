from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired

class MOvementsForm(FlaskForm):
    date = DateField("date", validators=[ DataRequired() ])
    concept = StringField("concept", validators=[ DataRequired() ])
    amount = FloatField("amount", validators=[ DataRequired() ])
    submit = SubmitField("Save")
