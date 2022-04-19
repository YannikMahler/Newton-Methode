import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


print(""" 
         _               _                __  __      _   _               _ 
    | \ | |             | |              |  \/  |    | | | |             | |
    |  \| | _____      _| |_ ___  _ __   | \  / | ___| |_| |__   ___   __| |
    |     |/ _ \ \ /\ / / __/ _ \|  _ \  | |\/| |/ _ \ __|  _ \ / _ \ / _  |
    | |\  |  __/\ V  V /| || (_) | | | | | |  | |  __/ |_| | | | (_) | (_| |
    |_| \_|\___| \_/\_/  \__\___/|_| |_| |_|  |_|\___|\__|_| |_|\___/ \__,_|
""")

x = symbols("x")

function = parse_expr(input("Funktion: f(x)= "))
fderivative = function.diff(x)
print(f'Ableitung: f`(x)= {fderivative}')

# 5*x**3+8*x**2-1
xn = float(input("Startwert: x_0= "))
max_iter = int(input("Anzahl an Iterationen:"))

print('\n')
print('{0:<3} {1:>4} {2:>10}'.format('Iter', 'x_n', 'f(x_n)'))
print('―' * 30)
for i in range(max_iter):
    xn = xn - float(function.evalf(subs= {x: xn})) / float(fderivative.evalf(subs= {x: xn}))
    print(f'{i+1}     {xn:.2}     {float(function.evalf(subs= {x:xn})):.2}')
