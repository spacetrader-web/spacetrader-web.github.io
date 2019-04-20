from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired



class Player(FlaskForm):
	playerName = StringField('Player Name', validators=[DataRequired()])
	pilotSkill = IntegerField('Pilot Skill', validators=[DataRequired()])
	traderSkill = IntegerField('Trader Skill', validators=[DataRequired()])
	engineerSkill = IntegerField('Engineer Skill', validators=[DataRequired()])
	fighterSkill = IntegerField('Fighter Skill', validators=[DataRequired()])
	difficulty = StringField('Difficulty', validators=[DataRequired()])
	submit = SubmitField('Sign In')
