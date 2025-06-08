import json

def read_json_file():
    try:
        with open('pokemon_data.json','r',encoding="utf-8") as file:
            data_from_json=json.load(file)
        return data_from_json
    except FileNotFoundError:
        print("File not found")


def register_pokemon():
    try:
        name=input("Pokemon name:")
        pokemon_type=input("Pokemon type(s), separated by commas: ").split(",")
        base = {}
        base["HP"] = int(input("HP: "))
        base["Attack"] = int(input("Attack: "))
        base["Defense"] = int(input("Defense: "))
        base["Sp. Attack"] = int(input("Sp. Attack: "))
        base["Sp. Defense"] = int(input("Sp. Defense: "))
        base["Speed"] = int(input("Speed: "))
        pokemon_info={
            "name": {
            "english": name
            },
            "type": pokemon_type,
            "base": base
            
        }
        return pokemon_info
    except ValueError as error:
        print(f'The number selected is invalid. Error: {error}')


def save_json_file(data_from_json):
    try:
        with open('pokemon_data.json','w',encoding="utf-8") as file:
            json.dump(data_from_json,file,indent=4)
    except PermissionError:
        print("You don't have the necessary permissions.")
    except TypeError:
        print("The data contains types that are not JSON serializable.")


def main():
    

    try:
        json_data=read_json_file()
        json_data.append(register_pokemon())
        save_json_file(json_data)
        
    except Exception as error:
        print(f'An error has occurred: {error}')
	

if __name__ == '__main__':
	main()
