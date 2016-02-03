# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
from math import sqrt

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n<0:
        raise ValueError
    
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    rho=b*b-4*a*c
    if rho >0:
        return ((-b-sqrt(rho))/(2*a),(-b+sqrt(rho))/(2*a))
    elif rho == 0:
        return ((-b)/(2*a))
    else:
        return ()
def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    pas=0.0001
    integrale=0
    numvalue = int((upper-lower)//pas)
    for i in range(numvalue):
        x=lower+i*pas
        integrale+=(eval(function)*pas)
    return integrale

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 2,-15))
    print(integrate('x**2-1', -1, 1))
    
