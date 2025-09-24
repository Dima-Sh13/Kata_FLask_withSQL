from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date

class MOvementsForm(FlaskForm):
    date = DateField("date", validators=[ DataRequired() ])
    concept = StringField("concept", validators=[ DataRequired(), Length(min=4, message="Debe tener mas de 4 caracteres") ])
    amount = FloatField("amount", validators=[ DataRequired("The amount cant be 0") ])
    submit = SubmitField("Save")


    def validate_date(form, field):
        if field.data > date.today():
            raise ValidationError("La fecha no puede ser en el futuro")