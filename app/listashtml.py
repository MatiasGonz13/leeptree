from flask import Flask, render_template, request


mensaje = """
<form method="POST" action="/">
        <p><input type='text' name='nuevalista' placeholder="Ingrese nueva lista"><p>
        <p><input type="checkbox" value='1' name="mycheckbox"> Comprar pan<p>
        <p><input type="checkbox" value='2' name="mycheckbox"> Estudiar MAT022<p>
        <p><input type="checkbox" value='3' name="mycheckbox"> Entrega de HRW132</p>
    <input type="submit" title='send'>
"""

def escribir(archivo):
    f = open(archivo,'w')
    f.write(mensaje)
    f.close()
    return render_template(archivo)

escribir('indexinsert.html')

