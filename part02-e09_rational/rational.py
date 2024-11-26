#!/usr/bin/env python3
class Rational(object):
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __mul__(self, second):
        new_n = self.n * second.n
        new_d = self.d * second.d
        return Rational(new_n, new_d)
    
    def __truediv__(self, second):
        new_n = self.n * second.d
        new_d = self.d * second.n
        return Rational(new_n, new_d)

    def __add__(self, second):
        new_n = (self.n * second.d) + (self.d * second.n)
        new_d = self.d * second.d
        return Rational(new_n, new_d)
    
    def __sub__(self, second):
        new_n = (self.n * second.d) - (self.d * second.n)
        new_d = self.d * second.d
        return Rational(new_n, new_d)
    
    def __eq__(self, second):
        return self.n == second.n and self.d == second.d
    
    def __gt__(self, second):
        return self.n/self.d > second.n/second.d
    
    def __lt__(self, second):
        return self.n/self.d < second.n/second.d

    def __str__(self):
        return f"{self.n}/{self.d}"

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()