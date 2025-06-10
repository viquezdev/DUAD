
def read_and_write_file(path):
    try:
        with open(path) as file:
            lines=file.readlines()
        lines.sort()
        with open('sorted_list.txt','w',encoding='utf-8') as file:
            file.writelines(lines)
    except FileNotFoundError:
        print("file not found")


def main():
    try:
        read_and_write_file('songs.txt')
        
    except Exception as error:
        print(f'An error has occurred: {error}')
	

if __name__ == '__main__':
	main()