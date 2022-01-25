class Prvek:
    def __init__(self, data, dalsi=None):
        self.data = data
        self.dalsi = dalsi

class LinSeznam:
    def __init__(self):
        self.head = None
    
    def vytiskni_ls(self, prvek):
        if self.head is None:
            self.head = prvek

        if self.head is not None:
            puk = self.head
            while puk is not None:
                print(puk.data)
                puk = puk.dalsi
    
    def push(self, new_data):
        new_node = Prvek(new_data)
        new_node.next = self.head
        self.head = new_node
        print("")


if __name__ == '__main__':
    p = Prvek(100)
    p.dalsi = Prvek(200)
    p.dalsi.dalsi = Prvek(300)
    p.dalsi.dalsi.dalsi = Prvek(400)

    ls = LinSeznam()
    ls.vytiskni_ls(p)
    ls.push(111)