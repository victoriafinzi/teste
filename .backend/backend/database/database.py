from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardsecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/replybetdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Login(db.Model):
    __tablename__ = 'login'
    idlogin = db.Column(db.Integer(4), primary_key = True)
    email = db.Column(db.String(45), primary_key = True)
    password = db.Column(db.String(45))
    iduser = db.Column(db.Integer, db.ForeignKey('users.iduser'))

class Users(db.Model):
    __tablename__ = 'users'
    iduser = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70))
    phone = db.Column(db.String(15))
    status = db.Column(db.String(2))

class Clients(db.Model):
    idclient = 