from service import *

def controller_verify_login(json_obj):
    try:
        data = service_verify_login(json_obj)
        return data
    except Exception as e:
        print(e)
        return jsonify({"status": str(e)})

def controller_save_files(json_obj):
    try:
        data = service_save_files(json_obj)
        return data
    except Exception as e:
        print(e)
        return jsonify({"status": str(e)})
    
def controller_get_fs():
    try:
        data = service_get_fs()
        return data
    except Exception as e:
        print(e)
        return jsonify({"status": str(e)})