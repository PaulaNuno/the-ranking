from src.app import app
from src.database import db
from flask import request
from bson.json_util import dumps
import numpy as np

@app.route('/') 
def welcome():
    return {
        'status': 'OK',
        'message': 'Hola, bienvenida a mi primera API'}

@app.route('/student/create/<name>')
def create_student(name):
    new_student = {
        'Usuario': f"{name}"}  
    result = db.pull.insert_one(new_student)
    return {'_id': str(result.inserted_id)}

@app.route('/student/all')
def allstudents():
    result = db.pull.distinct("Usuario")
    return dumps(result)



