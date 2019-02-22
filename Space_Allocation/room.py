class Room:
  def __init__(self,room_name=None,room_type=None,Max_capacity=None):
    self.name = room_name
    self.max_capacity = Max_capacity
    self.room_type = room_type  

class Office(Room):
  def __init__(self,room_name=None,Max_capacity=6):
    Room.__init__(self,room_name=room_name,Max_capacity=Max_capacity) 
    self.room_type = "OFFICE SPACE"

class LivingSpace(Room):
  def __init__(self,room_name=None,Max_capacity=4):
    Room.__init__(self,room_name=room_name,Max_capacity=Max_capacity)
    self.room_type = "LIVING SPACE"

    
