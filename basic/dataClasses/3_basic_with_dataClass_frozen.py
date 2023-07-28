from dataclasses import dataclass , field


@dataclass
class Person:
    id: int
    name: str
    address:str = "fake address"
    active: bool = True


# frozen=True - means we could not change any property outside of datacalss
@dataclass(frozen=True)
class User:
    id: int
    name: str
    address:str = "fake address"
    active: bool = True

    


def main():
    person = Person( id=1, name= 'subhadip')
    print(person)
    person.name = "pahari"
    print(person)


    # user = User(id=2 , name="subhadip")
    # print(user)
    # # this line will give error , as User datacalss is frozen=True
    # # after initilizing , we couldnot chage the value out side of the datacalss
    # user.name = "pahari"
    # print(user)


main()