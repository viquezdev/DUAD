class Head():
    def __init__(self):
	    pass


class Torso():
    def __init__(self,head,left_arm,right_arm):
        self.head=head
        self.left_arm=left_arm
        self.right_arm=right_arm




class Arm():
    def __init__(self,hand):
        self.hand=hand
	


class Hand():
    def __init__(self):
	    pass


class Leg():
    def __init__(self,feet):
	    self.feet=feet


class Feet():
    def __init__(self):
	    pass


class Human():
    def __init__(self,torso,left_leg,right_leg):
        self.torso=torso
        self.left_leg=left_leg
        self.right_leg=right_leg


head=Head()
right_hand = Hand()
left_hand=Hand()
left_arm=Arm(left_hand)
right_arm=Arm(right_hand)
torso = Torso(head, right_arm, left_arm)
left_feet=Feet()
right_feet=Feet()
left_leg=Leg(left_feet)
right_leg=Leg(right_feet)
human=Human(torso,left_leg,right_leg)
