class Dunder:
    def __init__(self, Hubby, Wife):
        self.Hubby = Hubby
        self.Wife = Wife

    def __str__(self):
        return f'{self.Hubby} Loves {self.Wife}'

    def __add__(self, other):
        return f'{self.Hubby} Loves {other.Wife}'


couple1 = Dunder('Varya', 'Anusha')
couple2 = Dunder('Varya', 'Anuu')
print(couple1 + couple2)
