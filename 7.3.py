from faker import Faker
fake=Faker()


class BaseContact():
    def __init__(self, first_name, last_name, phone_nr, email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_nr=phone_nr
        self.__label=0


    @property
    def label_length(self):
        return self.__label
    @label_length.setter
    def label_length(self,value):
        self.__label=value
    def contact(self):
        return f'Wybieram nr {self.phone_nr} i dzwonię do {self.first_name} {self.last_name}'
        
     
class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone_nr,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.position=position
        self.company=company
        self.work_phone_nr=work_phone_nr

        self.__label=0

    @property
    def label_length(self):
        return self.__label
    @label_length.setter
    def label_length(self,value):
        self.__label=value

    def contact(self):
        return f"Wybieram nr {self.work_phone_nr} i dzwonię do {self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_nr}, {self.email}, {self.position}, {self.company}, {self.work_phone_nr}"
        
def contact_generator(type, amount):
    cards=[]
    if type == 1:
        for i in range(amount):
            cards.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_nr=fake.phone_number(), email=fake.email()))
    elif type == 2:
        for i in range(amount):
            cards.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_nr=fake.phone_number(), email=fake.email(),\
        position=fake.job(),company=fake.company(), work_phone_nr=fake.phone_number()))
    return cards

for i in contact_generator(2,10):
    if isinstance(i, BusinessContact)==True:
        BusinessContact.label_length=len(i.first_name)+len(i.last_name)+1
        print(f"{BaseContact.contact(i)}\n{BusinessContact.contact(i)} \n{i.label_length}")
    else:
        BaseContact.label_length=len(i.first_name)+len(i.last_name)+1
        print(f"{BaseContact.contact(i)}\n{i.label_length}")








