def add_numbers(current_number):
    try:
        number=float(input("Enter a number: "))
        current_number+=number
        print(current_number)
        return current_number

    except ValueError as error:
        print(f'The number selected is invalid. Error: {error}')


def subtract_numbers(current_number):
    try:
        number=float(input("Enter a number: "))
        current_number-=number
        print(current_number)
        return current_number

    except ValueError as error:
        print(f'The number selected is invalid. Error: {error}')


def divide_numbers(current_number):
    try:
        number=float(input("Enter a number: "))
        current_number=current_number/number
        print(current_number)
        return current_number

    except ValueError as error:
        print(f'The number selected is invalid. Error: {error}')
    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: Division by zero is not allowed. Details: {e}")


def multiply_numbers(current_number):
    try:
        number=float(input("Enter a number: "))
        current_number*=number
        print(current_number)
        return current_number

    except ValueError as error:
        print(f'The number selected is invalid. Error: {error}')


def clear_result(current_number):
    current_number=0
    print(current_number)
    return current_number


def choose_option(current_number):
    try:
        new_value=0
        option=int(input("Choose an option to continue: "))
        if (option> 6):
            raise ValueError()
        elif(option==1):
            print(current_number)
            new_value=add_numbers(current_number)
            return new_value
            
        elif(option==2):
            print(current_number)
            new_value=subtract_numbers(current_number)
            return new_value
            
        elif(option==3):
            print(current_number)
            new_value=multiply_numbers(current_number) 
            return new_value
        
        elif(option==4):
            print(current_number)
            new_value=divide_numbers(current_number)
            return new_value
            
        elif(option==5):
            new_value=clear_result(current_number)
            return new_value
        elif(option==6):
            exit()
            
        else:
            return option
    except ValueError as error:
        print(f'The number selected is invalid. Error: {error}')
        raise error
        

def show_menu():
    menu_list=["1-Sum","2-Subtract","3-Multiply","4-Divide","5-Clear result","6-exit"]
    try:
        for element in menu_list:
            print(element + "/n")
    except IndexError as error:
        print(f'Index out of range. Error: {error}')


def main():
    option=0
    current_number=0

    try:
        while(option!=6):
            show_menu()
            current_number=choose_option(current_number)
        
    except Exception as error:
        print(f'An error has occurred: {error}')
	

if __name__ == '__main__':
	main()