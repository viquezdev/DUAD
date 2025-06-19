#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

import json

class AuthenticationMixin:
    def login(self, email,password):
        if self.email==email and self.password==password:
            print(f"User {self.name} authenticaded succesfully")
        else:
            print("Authentication failed")


class StatisticsMixin:
    def view_statistics(self):
        print(f"User {self.name} has logged in 4 times this week")


class JsonExportMixin:
    def to_json(self):
        return json.dumps(self.__dict__,indent=4)
    

class BaseUser:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

    
    def show_profile(self):
        print(f"Name: {self.name}, Email: {self.email}")


class Admin(BaseUser,AuthenticationMixin,StatisticsMixin,JsonExportMixin):
    pass


class Client(BaseUser,AuthenticationMixin,JsonExportMixin):
    pass
    

admin=Admin("Luis","admin@mail.com","admin123")
client=Client("Pedro","pedro@mail.com","pass123")

admin.show_profile()
admin.login("admin@mail.com","admin123")
admin.view_statistics()
print(admin.to_json())

client.show_profile()
client.login("pedro@mail.com","pass123")
print(client.to_json())