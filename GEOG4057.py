import sys

class ComplexNumber:
    """
    This is a class for mathematical operation on complex numbers.

    Attributes:
        real (int): The real part of the complex number.
        imag (int): The imaginary part of the complex number.

    """
    def __init__(self, real, imag):
        """
        The constructor for ComplexNumber class.
        Parameters:
            real (int): The real part of the complex number.
            imag (int): The imaginary part of the complex number.
        """
        self.real = real
        self.imag = imag
    def add(self, num):
        """
        The function to add two Complex Numbers.
        parameters:
            num (ComplexNumber)
        """
        re = self.real + num.real
        im = self.imag + num.imag
        return ComplexNumber(re, im)

def main():
    """
    This is a main function
    I can write multiple lines

    """
    #this is for main function
    c_1 = ComplexNumber(2,1)
    print(c_1.imag)
    c_2 = ComplexNumber(3,4)
    c_3 = c_1.add(c_2)
    print(f"c_3:{c_3.real}+{c_3.imag}i")
    pass

if __name__== "__main__":
    main()