
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real, self.imaginary * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        #return ComplexNumber((self.real + self.imaginary / other.real + other.imaginary) * (other.real + (other.imaginary * -1) / other.real + (other.imaginary * -1)))
        pass
    def __abs__(self):
        pass

    def conjugate(self):
        return ComplexNumber(self.real, self.imaginary * -1)

    def exp(self):
        pass
