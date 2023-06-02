import os, jwt
from datetime import datetime, timedelta
from flask import current_app, jsonify
from werkzeug.utils import secure_filename
from utils import get_fs

def service_verify_login(data):
    if data["password"] != os.environ.get("PASSWORD"):
        raise Exception("Wrong Password.")
    else:
        token = jwt.encode({
            "sub": os.environ.get("USER"),
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }, current_app.config['SECRET_KEY'])
        json_data = {
            "token": token
        }
        return jsonify(json_data)
       

def service_save_files(data):
    if "file" not in data:
        return jsonify({"status": 1, "message": "No Files Found"})
    files = data.getlist("file")
    filenames = []
    for file in files:
        filename = secure_filename(file.filename)
        file.save(os.path.join("/home/russ/Temp/file_upload", filename))
        filenames.append(filename)
    
    return jsonify({"status": 0, "message": f"{len(filenames)} file(s) successfully saved."})

def service_get_fs():
    root = {
        "name": "root",
        "type": "directory",
        "contents": get_fs("fs/")
    }
    return jsonify({"status": 0, "fs": root})
