from cat import Cat

def test():
    b = Cat('KitKat', 1, 'tabby')
    c = Cat('Othello', 6, 'black')
    
    print(b)
    print(c)
    
    b.description()
    c.description()

    c.meow()
    b.sleep()
    c.hungry()
    b.eat()

if __name__ == '__main__':
    x = Cat('test')
    print(x)
    test()

