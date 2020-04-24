import numpy as np
from sympy import Integral, integrate
from sympy import *
from sympy.plotting import plot
from sympy import Symbol
from sympy.plotting import plot

x = Symbol('x')

i = float(input('Ingrese el limite inferior: '))
j = float(input('Ingrese el limite superior: '))


f = input('Ingrese la primera expresión: ')
f = sympify(f)
pprint(f)

d1 = np.pi * Integral(f**2,(x,i,j)).doit()

g = input('Ingrese la segunda expresión: ')
g = sympify(g)
pprint(g)

p = plot(f, g, legend=True, show=False)
p[0].line_color = 'b'
p[1].line_color = 'r'
p.show()

d2 = np.pi * Integral(g**2,(x,i,j)).doit()

print("El valor de la volumen entre {} y {} es : {}".format(i,j,d1-d2))
