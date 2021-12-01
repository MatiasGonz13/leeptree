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
    nombre_lista=request.form.get('nuevalista')
    ref= db.reference('Usuario') 
    #Si existe algun cambio en la pagina:
    if request.method == 'POST':
        #Si el input para nuevas listas esta vacio o si las casillas no fueron marcadas
        # se analizaran las listas marcadas       
        if (nombre_lista == '' or nombre_lista == None) and (request.form.getlist('seleccion')!= '1' or request.form.getlist('seleccion')!= '2'):
            return render_template('index.html')
            #Falta implementar la conexion de firebase a html (pregunta para la profe)
        
            
        else:
            #A partir de aqui es tu parte
            hopper_ref=db.reference('Usuario')
            #Si se marca actividad evaluada
            if request.form.getlist('seleccion')== ['1']:
                ref.update({
                    nombre_lista:'act_evaluada'
                })
                return ('La actividad evaluada ' + request.form.get('nuevalista') + ' ha sido guardado con exito')
                #La actividad evaluada Tarea 6 - FIS110 ha sido guardado con éxito

            #Si se marca recordatorio
            elif request.form.getlist('seleccion')== ['2']:
                ref.update({
                    nombre_lista:'recordatorio'
                    })
                return ('El recordatorio ' + request.form.get('nuevalista') + ' ha sido guardado con éxito')
                #El recordatorio Estudiar - FIS110 ha sido guardado con éxito
    else:
        return render_template('index.html')


 #Funcion para que la app comience a correr
if __name__=='__main__':
    app.run(debug=True,port=5000)