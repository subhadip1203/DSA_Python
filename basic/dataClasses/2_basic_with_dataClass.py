from dataclasses import dataclass , field
import random
import string

def random_val():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


@dataclass
class Person:
    id: int
    name: str
    address:str = "fake address"
    active: bool = True

    # any list is reference type , so for all objects , the array/lost will be same
    # default factory is always a function
    email_list: list[str] = field(default_factory=list)
    phone_list: list[str] = field(default_factory=lambda: ['1234567890', '1234567891'])

    # call function as default value
    # default factory is always a function
    # init = False , means we not allaw this property will not be a part on initilization
    random_id:str = field(init=False, default_factory=random_val)


    # __post_init__ : insert value into a property after creataion of object from class
    # although we are not calling __init__ , as @dataclass do it from us
    search:str = field(init=False)
    def __post_init__(self):
        self.search = f"{self.id}, {self.name}"

    # private field by repr= False
    _password:str = field(init=False, repr= False, default= "test password") 


def main():
    person = Person( id=1, name= 'subhadip')
    print(person)


    # TypeError: Person.__init__() got an unexpected keyword argument 'random_val'
    #  as random_val is made by : init=False
    # person2 = Person( id=1, name= 'subhadip', random_val="AW3WI8")
    # print(person2)


main()