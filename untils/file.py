import os
import json
from configs import base

def check_file_exit(path=base.FILE) -> bool:
    if os.path.exists(path):
        return True
    return False

def check_file_empty(path=base.FILE) -> bool:
    if os.path.getsize(path) <= 0:
        return True
    return False

def init_file(path=base.FILE, struct=base.BASE_STRUCT):
    with open(path, 'w') as file:
        json.dump(struct, file, indent=4)

def create_file(path=base.FILE, struct=base.BASE_STRUCT):
    if not check_file_exit(path) or check_file_empty(path):
        init_file(path, struct)