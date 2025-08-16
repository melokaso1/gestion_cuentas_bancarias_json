import os
import json
from typing import Optional


RUTA = 'data/db.json'

def read_json(file_path : str):
    try:
        with open(file_path, 'r') as db:
            return json.load(db)
    except FileNotFoundError:
        return {}
    
def write_json(file_path : str, data : dict):
    with open(file_path, 'w', encoding= 'utf-8') as db:
        json.dump(data, db, indent=4)

def rewrite_json(file_path : str, data : dict, path: Optional[list[str]] = None) -> None:
    actual_data = read_json(file_path)
    
    if not path:
        actual_data.update(data)
    else:
        current = actual_data
        for key in path[:-1]:
            current = current.setdefault(key, {})
        current[path[-1]] = data
    
    write_json(file_path, actual_data)

def delete_data_json(file_path : str,  path: list[str]) -> bool: # type: ignore
    data1 = read_json(file_path)
    data = data1
    for key in path[:-1]:
        if key not in data:
            return False
        data = data[key]
        if path and path[-1] in data:
            del data[path[-1]]
            write_json(file_path, data1)
            return True
    return False

def initialize_json(file_path : str, initial_structure : dict) -> None:
    if not os.path.exists(file_path):
        write_json(file_path, initial_structure)
    else:
        actual_data = read_json(file_path)
        for key, value in initial_structure.items():
            if key not in actual_data:
                actual_data[key] = value
        write_json(file_path, actual_data)