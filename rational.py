class Rational(object):
    def __init__(self, numer, denom):
        self._numer = numer
        self._denom = denom
        self._reduce()

    def numerator(self):
        return self._numer

    def denominator(self):
        return self._denom

    def __str__(self):
        return str(self._numer) + "/" + str(self._denom)

    def _reduce(self):
        divisor = self._gcd(self._numer, self._denom)
        self._numer = self._numer // divisor
        self._denom = self._denom // divisor

    def _gcd(self, a, b):
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    def __add__(self, other):
        newNumer = self._numer * other._denom + other._numer * self._denom
        newDenom = self._denom * other._denom
        return Rational(newNumer,newDenom)

    def __lt__(self, other):
        extremes = self._numer * other._denom
        means = other._numer * self._denom
        return extremes < means

    def __eq__(self,  other):
        if self is other:
            return True
        elif type(self) !=  type(other):
            return False
        else:
            return self._numer  ==  other._numer and  self._denom  ==  other._denom

