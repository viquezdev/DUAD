class Person():
	def __init__(self, name,age):
		self.name = name
		self.age = 0


class Bus():
	def __init__(self,max_passengers):
		self.max_passengers=max_passengers
		self.passengers=[]
	
	
	def add_passenger(self,person):
		if(len(self.passengers)<self.max_passengers):
			self.passengers.append(person)
			print("New passenger on board.")
		else:
			print("the bus is full...")

	def remove_passenger(self,person):
		if self.passengers:
			self.passengers.remove(person)
			print("The passenger has left the bus.")


daniel=Person('Daniel',35)
andrey=Person('Andrey',30)
fernando=Person('Fernando',30)
maria=Person('maria',30)
bus=Bus(3)
bus.add_passenger(daniel)
bus.add_passenger(andrey)
bus.add_passenger(fernando)
bus.add_passenger(maria)

bus.remove_passenger(andrey)