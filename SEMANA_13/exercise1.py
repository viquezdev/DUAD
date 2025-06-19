#Cree un decorador que haga print de los parámetros y retorno de la función que decore.


def print_args(func):
    def wrapper(*args,**kwargs):
        print(f"Calling to {func.__name__} with args: {args} and kwargs: {kwargs} ")
        value=func(*args,**kwargs)
        print(f"{func.__name__} result: {value}")
        return value
    return wrapper


@print_args
def print_all_params(*args,**kwargs):
    print(f"args: {args} kwargs: {kwargs}")
    return "completed"


print_all_params(1,2,3,"hello",[12,56,78],name="Daniel",age=35)