from app import app
from flask import request, jsonify, current_app
from functools import wraps
from controller import *


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '')

        invalid_msg = {
            'message': 'Invalid token. Registration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }
        invalid_usr = {
            'message': 'Invalid user. Need a valid user.',
            'authenticated': False
        }

        if len(auth_headers.split(".")) != 3:
            return jsonify(invalid_msg), 401

        try:
            data = jwt.decode(auth_headers, current_app.config['SECRET_KEY'], algorithms="HS256")
            user = os.environ.get("USER")
            if user != data['sub']:
                raise RuntimeError('User not found')
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except jwt.InvalidTokenError:
            return jsonify(invalid_msg), 401
        except RuntimeError:
            return jsonify(invalid_usr), 401

    return _verify

@app.route("/api/login", methods=["POST"])
def verify_login():
    data = controller_verify_login(request.get_json())
    return data

@app.route("/api/files/save", methods=["POST"])
def save_files():
    data = controller_save_files(request.files)
    return data

@app.route("/api/fs", methods=["GET"])
def get_fs():
    data = controller_get_fs()
    return data