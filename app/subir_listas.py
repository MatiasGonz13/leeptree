import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, render_template, request
cred = credentials.Certificate("app\database\leep-tree-firebase-adminsdk-6pg7t-6076089425.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://leep-tree-default-rtdb.firebaseio.com/'
})


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def index1():
    if request.method == 'POST':
        if request.form.getlist('mycheckbox')==['1']:
            print(request.form.getlist('mycheckbox'))
            return render_template('lista-1.html')

        elif request.form.getlist('mycheckbox')==['2']:
            print(request.form.getlist('mycheckbox'))
            return render_template('lista-2.html')
        
        elif request.form.getlist('mycheckbox')==['3']:
            print(request.form.getlist('mycheckbox'))
            return render_template('lista-3.html')
        
        else:
            print(request.form.get('nuevalista'))
            if request.form.get('nuevalista') == '':
                 return render_template('index.html')
            else:
                nombre = request.form.get('nuevalista')
    
    print(request.form.get('mycheckbox'))
    return render_template('index.html')



ref= db.reference('/')
ref.set({

    'Usuario':{ 
        'Lista1':True
    }

})

