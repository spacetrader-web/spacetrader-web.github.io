import pymongo
from flask import Flask, request, jsonify, json, render_template, flash, redirect, url_for
from pymongo import MongoClient
# from app import app
from player_form import Player


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
client = MongoClient("mongodb://admin:space123@ds145356.mlab.com:45356/spacetrader")
db = client["spacetrader"]
db.authenticate("admin","space123");



print(db.users.find_one({}))



@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login"""
    form = Player()
    # print(form)
    # # if form.validate_on_submit():
    # if request.method == 'POST':
    #     if form.validate():
    #         flash('Login requested for user {}'.format(
    #             form.playerName.data, form.pilotSkill.data, form.traderSkill.data, form.engineerSkill.data, form.fighterSkill.data))
    #         db.insert_one ({
    #             '_id' : 1,
    #             'name': form.playerName.data,
    #             'pilot': form.pilotSkill.data,
    #             'trader': form.traderSkill.data,
    #             'engineer': form.engineerSkill.data,
    #             'fighter': form.fighterSkill.data
    #         })
    #         print("player insert")
    #         return render_template('main.html', form = form)
    # print(db)
    #dump()
    return render_template('base.html', form = form )


    # return render_template('base.html',  title='Sign In', form=form)
@app.route('/add_player', methods=['POST'])
def add_player():
    print(request.form.to_dict())
    db.users.insert_one(request.form.to_dict())
    return "Success!"
    #dump()

if __name__ == "__main__":
    app.run(debug=True)


#rahulrajus
#teamformation
