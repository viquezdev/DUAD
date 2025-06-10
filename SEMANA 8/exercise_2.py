import csv


def generate_data_dict(headers):
    game_data={}
    for item in headers:
        field_value=input(f'{item}: ')
        game_data[item]=field_value
    return game_data


def export_data_to_csv(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

def main():
    

    try:
        option=1
        videogame_headers=['name','genre','developer','esrb_rating']
        game_data=[]
        while(option==1):
            option=int(input("Enter 1 to add a game or 0 to finish:"))
            if(option==1):
                game_data.append(generate_data_dict(videogame_headers))
        export_data_to_csv('videogames.csv', game_data, videogame_headers)
    except Exception as error:
        print(f'An error has occurred: {error}')
        
	

if __name__ == '__main__':
	main()