from flask import Flask, request, jsonify, current_app
from functools import wraps
from dotenv import load_dotenv
import jwt, os
load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = os.environ.get("SECRET_TOKEN")

from app import routes
