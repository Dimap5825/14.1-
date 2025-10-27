from config import DATA_PATH
import json

def json_to_py_dict(path = DATA_PATH)->dict|list:
    """

    :param path:
    :return:
    """
    with open(DATA_PATH,'r') as f:
        return json.load(f)
# print(json_to_py_dict())