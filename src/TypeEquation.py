class TypeEquation:
    def __init__(self, S, T):
        self.S = S
        self.T = T

    def __repr__(self):
        return f"{self.S} .= {self.T}"