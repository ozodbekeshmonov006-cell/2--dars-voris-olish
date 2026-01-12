class Animal:
    def __init__(self,name):
        self.name=name
        
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound="Woof"
        
d1=Dog("buynoq")
print(f"{d1.name} {d1.sound} dedi")        
    