import os

def get_fs(path):
    results = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            results.append({
                'name': item,
                'type': 'file',
            })
        elif os.path.isdir(item_path):
            results.append({
                'name': item,
                'type': 'directory',
                'contents': get_fs(item_path)
            })
    return results

