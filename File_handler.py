import json


def load_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return False


def save_data(data, filename):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        return False
