from gcd import gcd

class Fraction:
    def __init__(self, nominator, denominator):
        self.__normalize(nominator, denominator)
        
    def __eq__(self, other):
        return isinstance(other, Fraction) and self.nominator() == other.nominator() and self.denominator() == other.denominator()
    
    def nominator(self):
        return self.__nominator

    def denominator(self):
        return self.__denominator

    def __str__(self):
        return str(self.nominator()) + "\n-\n" + str(self.denominator())
    
    def __repr__(self):
        return str(self.nominator()) + "/" + str(self.denominator())

    def __normalize(self, nominator, denominator):
        self.__nominator = nominator // gcd(nominator,denominator)
        self.__denominator = denominator // gcd(nominator,denominator)