class TypeEquation:
    def __init__(self, S, T):
        self.S = S
        self.T = T

    def __str__(self):
        return f'{self.S} = {self.T}'

    def __repr__(self, number):
        if(number == 1):
            return self.S
        else:
            return self.T
    def __acc__(self, number):
        if(number == 1):
            return f'{self.S}'
        else:
            return f'{self.T}'