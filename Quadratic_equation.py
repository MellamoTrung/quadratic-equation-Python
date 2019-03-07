print('---------------------------------------------------\n')
print('Formation of the quadratic equation:')
print('aX^2 + bX + c = 0 \n')

#Insert a, b, c
a = input('Insert a = ')
b = input('Insert b = ')
c = input('Insert c = ')

#Calculate delta
A = float(a)
B = float(b)
C = float(c)
delta = B*B - 4*A*C

#Set out the solutions
if delta < 0:
    print('\n No solution.')
elif delta == 0:
    print('\n One real solution x = ', (-B/(2*A)))
else:
    import math
    sqrt_delta = math.sqrt(delta)
    print('2 real solutions: \n')
    print('x1 = ', ((-B+sqrt_delta)/(2*A)))
    print('x2 = ', ((-B-sqrt_delta)/(2*A)))
