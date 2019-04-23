from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from universe import Universe



class Player(FlaskForm):
	playerName = StringField('Player Name', validators=[DataRequired(message=('Player Name'))])
	pilotSkill = IntegerField('Pilot Skill', validators=[DataRequired()])
	traderSkill = IntegerField('Trader Skill', validators=[DataRequired()])
	engineerSkill = IntegerField('Engineer Skill', validators=[DataRequired()])
	fighterSkill = IntegerField('Fighter Skill', validators=[DataRequired()])
	difficulty = SelectField('Difficulty',validators=[('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')])
	submit = SubmitField('Submit')
	spaceship = ''
	credits = 0
	universe = []


	def setPlayer(self, playerName, pilotSkill, traderSkill, engineerSkill, fighterSkill, difficulty, spaceship, credits, universe):
		self.playerName = playerName
		self.pilotSkill = pilotSkill
		self.fighterSkill = fighterSkill
		self.traderSkill = traderSkill
		self.engineerSkill = engineerSkill
		self.difficulty = difficulty
		self.spaceship = spaceship
		self.credits = credits
		self.universe = universe



	# def __init__(self, playerName, pilotSkill, traderSkill, engineerSkill, fighterSkill, difficulty, spaceship, credits):
		# self.playerName = playerName
		# self.pilotSkill = pilotSkill
		# self.fighterSkill = fighterSkill
		# self.traderSkill = traderSkill
		# self.engineerSkill = engineerSkill
		# self.difficulty = difficulty
		# self.spaceship = spaceship
		# self.credits = credits
	#
	# def validateSkills(form, pilotSkill, traderSkill, engineerSkill, fighterSkill):
	# 	sum = pilotSkill.data + traderSkill.data + engineerSkill.data + fighterSkill.data
	# 	if sum != 16:
	# 		raise ValidationError("Skills must be equal to 16")
