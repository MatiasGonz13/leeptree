from flask import escape
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("app\database\leep-tree-firebase-adminsdk-6pg7t-6076089425.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://leep-tree-default-rtdb.firebaseio.com/'
})

ref= db.reference('Usuario')
Listas = (ref.get())

def RevListas(diccionario):
    dicc= {}
    for titulo in diccionario:
        if diccionario[titulo]==False:
            dicc[titulo]=diccionario[titulo]
    return (dicc)

def escribirhtml(lista, archivo):
    RevListas(lista)
    for title in lista:
        plant = '<input type="checkbox" value= {1} name="mycheckbox"> {2}\n'
        a = open(archivo, 'w')
        a.replace('{0}', plant)
        a.replace('{1}', str(lista.index(title)))
        a.replace('{2}', str(title))
        archivo.close()
    return archivo

print(RevListas(Listas))
escribirhtml(Listas, 'index.html')


