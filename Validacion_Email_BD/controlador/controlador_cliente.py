from Validacion_Email_BD import app
from flask import render_template, request, redirect
from flask import render_template, request, redirect,session
from Validacion_Email_BD.modelo.modelo_cliente import Clientes

app.secret_key = 'keep it secret, keep it safe' # establece una clave secretas

@app.route('/')
def email():
    return render_template("clientes.html")

@app.route('/exito')
def exito():
    resultado = Clientes.clientes()
    return render_template('exito_email.html', emails = resultado)

@app.route('/process',methods=['POST'])
def process():
    if not Clientes.validar_informacion(request.form):
        return redirect('/')
    Clientes.crear_cliente(request.form)
    return redirect('/exito')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404