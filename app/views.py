from app import app, JsonParser
from flask import render_template, request, session,  url_for, redirect, jsonify, json


@app.route('/')
@app.route('/homepage')
def homepage():
    	return render_template('Homepage.html')
