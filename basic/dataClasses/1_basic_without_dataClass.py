

class Person:

    # init calss
    def __init__(self, id , name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"id: {self.id} || name: {self.name}" 


def main():
    person = Person( id=1, name= 'subhadip')
    print(person)


main()