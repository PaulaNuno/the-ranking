from src.app import app
from database import db
from flask import request, Response
from bson.json_util import dumps

@app.route('/') 
def welcome():
    return {
        'status': 'OK',
        'message': 'Hola, bienvenida a mi primera API'}
        
@app.route('/student/create/<name>')
def create_student(name):
    new_student = {
        'Usuario': name}
    result = db.pull.insert_one(new_student)
    return {'_id': str(result.inserted_id)}

@app.route('/student/all')
def allstudents():
    result = db.pull.distinct("Usuario")
    return dumps(result)



