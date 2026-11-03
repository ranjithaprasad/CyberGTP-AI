import os
import requests
from flask import Flask, request, 
jsonify, render_template

app=Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return
render_template("index.html")
       
      
