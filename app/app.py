import pymongo
from flask import Flask, request, jsonify, json, render_template, flash, redirect, url_for
from pymongo import MongoClient
# from app import app
from player import Player
from universe import Universe, Planet, Location

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
    return render_template('base.html', form = form)

@app.route('/get_player', methods=['GET'])

def get_player():
    playerDict = db.users.find_one({})
    p = Player()
    p.setPlayer(playerDict['name'], playerDict['pilot'], playerDict['fighter'], playerDict['trader'], playerDict['engineer'], playerDict['difficulty'], playerDict['spaceship'], playerDict['credits'], playerDict['universe'])
    print(p)

    return render_template("main.html", player = p)


    # return render_template('base.html',  title='Sign In', form=form)
@app.route('/add_player', methods=['POST'])
def add_player():
    print(request.form.to_dict())
    playerDict = request.form.to_dict();
    isValid = True
    sum = 0;
    for key,value in playerDict.items():
        print(sum)

        if value == '':
            flash('Name is empty')
            isValid = False



        if key == 'pilot':
            sum += int(value)

        elif key == 'fighter':
            sum += int(value)

        elif key == 'trader':
            sum += int(value)

        elif key == 'engineer':
            sum += int(value)

    if sum != 16:
        flash('Skills must add to 16')
        isValid = False



    #print(playerDict)

    if isValid is True:
        playerDict['spaceship'] = 'gnat'
        playerDict['credits'] = 1000
        u = Universe()
        universe = u.makeUniverse()
        playerDict['universe'] = universe

        db.users.insert_one(playerDict)
        # p = db.users.find_one({})
        player = Player()

        print(universe)
        player.setPlayer(playerDict['name'], playerDict['pilot'], playerDict['fighter'], playerDict['trader'], playerDict['engineer'], playerDict['difficulty'], playerDict['spaceship'], playerDict['credits'], playerDict['universe'])

        return "Success!"
    else:
        return "Try again!"






    #dump()

if __name__ == "__main__":
    app.run(debug=True)


#rahulrajus
#teamformation
