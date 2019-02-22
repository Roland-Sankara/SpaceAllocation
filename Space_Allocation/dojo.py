from person import Person,Staff,Fellow
from room import Room,Office,LivingSpace

class Dojo(Room,Person):
    def __init__(self):
        self.rooms = []
        self.persons = []
    def create_room(self,room_name,room_type):
        if room_type.upper() == "OFFICE":
            room = Office(str(room_name.upper()))
            self.rooms.append(room_name)
            print("An {} called {} has been created successfully".format(room_type,room_name))
        if room_type.upper() == "LIVINGSPACE":
            room = LivingSpace(str(room_name.upper()))
            self.rooms.append(room_name)
            print("A {} called {} has been created successfully".format(room_type,room_name))
    
    def add_person(self,name,role):
        if role.upper() == "FELLOW":
                person = Fellow(name)
                self.persons.append(name)
                print("Fellow {} has been successfully added".format(name))
        
        if role.upper() == "STAFF":
            person = Staff(name)
            self.persons.append(name)
            print("Staff {} has been successfully added ".format(name))                           

room1 = Dojo()
room1.create_room('Newyork','Office') 
room1.add_person('Sankara','fellow')
print(room1.persons)
room2 = Dojo()
room2.create_room('Mexico','LivingSpace')              