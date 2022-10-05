from Validacion_Email_BD.configuracion.mysqlconnection import connectToMySQL
from flask import flash

import re	# el módulo regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Clientes:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email= data['email']
        self.crado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    #Validación de informacion
    @staticmethod
    def validar_informacion(cliente):
        is_valid = True # asumimos que esto es true
        if len(cliente['nombre']) < 4:
            flash("Nombre debe al menos 3 caracteres.")
            is_valid = False
        if not EMAIL_REGEX.match(cliente['email']): 
            flash("Dirección de Email Incorrecta")
            is_valid = False 
        query = "SELECT * FROM clientes where email = %(email)s;"
        resultado = connectToMySQL('clientes').query_db(query, cliente)
        print (resultado)
        if resultado:
            flash("Dirección de Email ya Existente")
            is_valid = False 
        return is_valid 

    @classmethod
    def clientes(cls):
        query = "SELECT * FROM clientes;"
        resultado = connectToMySQL('clientes').query_db(query)
        return resultado

    @classmethod
    def crear_cliente(cls, data):
        query = "INSERT INTO clientes (nombre, email) VALUES (%(nombre)s, %(email)s);"
        resultado = connectToMySQL('Clientes').query_db(query, data)
        return resultado
