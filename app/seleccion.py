from flask import Flask, render_template, request
from os import replace
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, firestore

app = Flask(__name__)

cred = credentials.Certificate("app\database\leep-tree-firebase-adminsdk-6pg7t-6076089425.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://leep-tree-default-rtdb.firebaseio.com/'
})


@app.route('/', methods=['GET', 'POST'])

def index():
    print('hola')
    ref= db.reference('Usuario')
    Listas= ref.get('/')
    for titulo in Listas:
        print(Listas[titulo])
        if Listas[titulo]==False:
            if request.form.get('mycheckbox')=='1':
                ref.update({
                    Listas[titulo]:'act_evaluada'
                })
                return ('La actividad evaluada ' + request.form.get('nuevalista') + ' ha sido guardado con exito')

            elif request.form.get('mycheckbox')=='2':
                ref.update({
                    Listas[titulo]:'recordatorio'
                })
                return ('El recordatorio ' + request.form.get('nuevalista') + ' ha sido guardado con exito')