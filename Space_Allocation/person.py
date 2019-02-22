

class Person:
  def __init__(self,name=None,role=None,wants_accomodation=None):
    self.name = name
    self.role = role
    self.wants_accomodation = wants_accomodation

class Staff(Person):
  def __init__(self,name=None,wants_accomodation=None):
    Person.__init__(self,name=name,wants_accomodation=wants_accomodation)
    self.role = "STAFF"  

class Fellow(Person):
  def __init__(self,name=None,wants_accomodation=None):
    Person.__init__(self,name=name,wants_accomodation=wants_accomodation)
    self.role = "FELLOW"