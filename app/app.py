import pymongo
from flask import Flask, request, jsonify, json, render_template, flash, redirect, url_for
from pymongo import MongoClient
# from app import app
from app.player_form import Player


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

client = pymongo.MongoClient("mongodb://admin:st@spacetrader-cluster-shard-00-00-yik2d.gcp.mongodb.net:27017,spacetrader-cluster-shard-00-01-yik2d.gcp.mongodb.net:27017,spacetrader-cluster-shard-00-02-yik2d.gcp.mongodb.net:27017/test?ssl=true&replicaSet=spacetrader-cluster-shard-0&authSource=admin&retryWrites=true")
db = client.test
print(db)



@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Player()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.playerName.data, form.pilotSkill.data, form.traderSkill.data, form.engineerSkill.data, form.fighterSkill.data))
        return redirect(url_for('base'))
    return render_template('base.html',  title='Sign In', form=form)
