class Person:
    def __init__(self):
        self.street_addr = None
        self.city = None
        self.post_card = None

        self.company_name = None
        self.position = None
        self.income = None

class PersonBuilder:
    def __init__(self, person=Person()):
        self.person=person


    def build(self):
        return self.person
    
    @property
    def works(self):
        return PersonJobBuilder(self.job)

    @property
    def lives(self):
        return PersonAddrBuider(self.person)
    
class PersonJobBuilder:
    def __init__(self, person):
        super.__init__(person)

    def at(self,company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, income):
        self.person.income = income
        return self



class PersonAddrBuider:
    def __init__(self, person):
        super.__init__(person)

    def at(self, street_addr):
        self.street_addr - street_addr 
        return self








