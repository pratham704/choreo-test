from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
from pymongo import MongoClient
import requests
from datetime import datetime
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
CORS(app)




@app.route("/")
def index():
    return "hi"

asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(asgi_app, host="0.0.0.0", port=8129)
