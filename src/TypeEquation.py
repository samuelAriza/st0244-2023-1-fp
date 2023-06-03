class TypeEquation:

    # Initializes a TypeEquation object with the given S and T types
    def __init__(self, S, T):
        self.S = S
        self.T = T

    # Returns a string representation of the type equation in the form "S = T"
    def __str__(self):
        return f'{self.S} = {self.T}'

    # Returns a string representation of the type equation based on the specified number
    def __repr__(self, number):
        if(number == 1):
            return self.S
        else:
            return self.T
        
    # Returns an abbreviated string representation of the type equation based on the specified number    
    def __acc__(self, number):
        if(number == 1):
            return f'{self.S}'
        else:
            return f'{self.T}'
