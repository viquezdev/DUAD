import json

def read_json_file():
    filename = 'task_data.json'
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return []


def save_json_file(data_from_json):
    try:
        with open('task_data.json','w',encoding="utf-8") as file:
            json.dump(data_from_json,file,indent=4)
    except PermissionError:
        print("You don't have the necessary permissions.")
    except TypeError:
        print("The data contains types that are not JSON serializable.")