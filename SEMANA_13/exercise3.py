#3. Cree una clase de `User` que:
#   - Tenga un atributo de `date_of_birth`.
#   - Tenga un property de `age`.
    
#    Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class UnderAgeError(Exception):
    def __init__(self):
        super().__init__(f"You are under the required age.")

class User:
    def __init__(self,date_of_birth):
        self.date_of_birth=date_of_birth


    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

    


def check_age_requirement(func):
    def wrapper(user):
        if(user.age>=18):
            print("The user meets the required age")
            return func(user)
        else:
            raise UnderAgeError()
        
    return wrapper
        

@check_age_requirement
def allow_entry(user):
    return f"Welcome, you have {user.age} years."


user=User(date(2020, 5, 14))
print(allow_entry(user))