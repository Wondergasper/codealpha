class FB ():
    def __init__(self) :
        self.n2 = 1
        self.n3 = 1
    def __iter__(self) :
        return self
    def __next__ (self):
        self.n1 = self.n2
        self.n2 = self.n3
        self.n3 = self.n1 + self.n2
        return self.n1
a = FB()    
i = iter(a)
for k in range( 10 ):
    print(next(i), end = " " )

    