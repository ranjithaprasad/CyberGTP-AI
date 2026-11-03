import os
import requests
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template request, 
jsonify, 
app=Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return
render_template("index.html")
       
      
