from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import yagmail
import os
import pymongo
from bson.objectid import ObjectId

email="juliethximenarendonsanchez.com"

contraseña = "Julieth2023"

yag = yagmail.SMTP(user=email, password=contraseña)

destinatario = ["cesarmcuellar@gmail.com"]
asunto = "Prueba yagmail"
mensaje= " Usuario Ingreso Exitosamente"

app = Flask(__name__)

conexion = MongoClient('mongodb://localhost:27017')

db = conexion['Trabajo_SS']

app.config["UPLOAD_FOLDER"]="./static/img"

usuarios = db['Usuarios']
productos = db["Productos"]
categoria = db["Categorias"]


@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        
        usuario = usuarios.find_one({'correo': correo})

        if usuario and usuario['contraseña'] == contraseña:
            yag.send(destinatario, asunto, mensaje)
            return redirect(url_for('home'))
        else:
            mensaje='Correo o contraseña incorrectos'

    return render_template('login.html',mensaje=mensaje)