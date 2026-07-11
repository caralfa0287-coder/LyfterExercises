class Head:
    def __init__(self, eyes_color, hair_color):
        self.eyes_color = eyes_color
        self.hair_color = hair_color

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Feet:
    def __init__(self):
        pass

class Human:
    def __init__(self, name, torso):
        self.name = name
        self.torso = torso

head = Head(eyes_color="Blue", hair_color="Blonde")

left_hand = Hand()
right_hand = Hand()

left_arm = Arm(hand=left_hand)
right_arm = Arm(hand=right_hand)    

left_feet = Feet()
right_feet = Feet()         

left_leg = Leg(feet=left_feet)
right_leg = Leg(feet=right_feet)    

torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

person = Human(name="John", torso=torso)

print(f"Name: {person.name}")   
print(f"Eye Color: {person.torso.head.eyes_color}")
print(f"Hair Color: {person.torso.head.hair_color}")