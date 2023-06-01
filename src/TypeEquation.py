class TypeEquation:
    def __init__(self, S, T):
        self.S = S
        self.T = T

    def __repr__(self, number):
        if(number == 1):
            return self.S
        else:
            return self.T
    