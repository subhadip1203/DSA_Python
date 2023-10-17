
class Person :
    
    def __init__(self,x,y):
        self.name = x
        self.age = y
        self.details = x+ ' -> '+str(y)
    
    def full_details(self):
        return self.name+ ' -> '+str(self.age)
    

a = Person('subhadip pahari',30)
print(a.name ,a.age)
print(a.details)
# print(a.full_details())


# b = Person('shammi',25)
# print(b.full_details())