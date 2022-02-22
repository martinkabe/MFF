class Cat:
    name = ''
    age = ''
    color = ''

    def __init__(self, name, age=0, color='white') -> None:
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')
    
    def meow(self):
        print(f'{self.name} meow')
    
    def sleep(self):
        print(f'{self.name} zzz')
    
    def hungry(self):
        for x in range(5):
            self.meow()
    
    def eat(self):
        print(f'{self.name} nom nom nom')
    
    def description(self):
        print(f'{self.name} is a {self.color} cat, who is {self.age} years old')

class Feline:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> None:
        return(f"Creating a feline with name of {self.name}")
    
    def meow(self):
        print(f'{self.name} meow')
    
    def setName(self, name):
        print(f'{self} setting name: {name}')
        self.name = name

class Lion(Feline):
    def __repr__(self) -> None:
        return(f'{self.name} roar')


class Tiger(Feline):
    def __init__(self, name):
        super().__init__(name)
    
    def __repr__(self) -> None:
        return(f"Creating a tiger with name of {self.name}")


c = Feline('Kitty')
print(c)
c.meow()

l = Lion('Leo')
print(l)
l.meow()

t = Tiger('Hans')
print(t)