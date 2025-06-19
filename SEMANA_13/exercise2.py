#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


def check_params(func):
    def wrapper(*args,**kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Invalid parameter: {arg} is not a number.")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Invalid keyword parameter: {key}={value} is not a number.")
        return func(*args, **kwargs)
    return wrapper


@check_params
def print_all_params(*args,**kwargs):
    print(f"args: {args} kwargs: {kwargs}")
    


print_all_params(1,2,3,6,56,name=78,age=35)