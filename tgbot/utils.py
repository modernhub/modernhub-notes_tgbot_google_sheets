import json

def parse_json(path):
    with open(path, 'r') as file:
        structure = json.load(file)
    return structure

def get_token_from_json(path):
    structure = parse_json(path)
    token = structure['token']
    return token
