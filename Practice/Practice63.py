# finding roots of a quadratic equation
import math


def quadratic(a, b, c):

    # find d = b^2 -4ac

    d = b*b - 4*a*c
    sq_val = math.sqrt(abs(d))

    if d == 0:
        print('the roots are real and same')
        print(-b/2*a, 'r1 and r2')

    if d > 0:
        print('roots are real and distinct')
        print(-b + sq_val/(2*a), 'root1')
        print(-b - sq_val/(2*a), 'root2')

    if d < 0:
        print('roots are imaginary')
        print(-b/(2*a), '+i', sq_val)
        print(-b/(2*a), '-i', sq_val)


quadratic(1, -4, 4)
