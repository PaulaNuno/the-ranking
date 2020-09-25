from src.app import app
from src.database import db
from flask import request
from bson.json_util import dumps

@app.route('/lab/create/<name>')
def create_lab(name):
    new_labt = {
    'Title': name}
    result = db.pulls.insert_one(new_lab)
    return {'_id':str(result.inserted_id)}


#@app.route("/lab/<Title>/meme")
#def random_meme(Title):
    #result = random.choice(db.pull_request.find({"Title":lab},{'Url':1}))
    #return result