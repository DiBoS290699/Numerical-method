import matplotlib.pyplot as plt
import numpy as np


def equation(eq, val):
    return eq[0] + eq[1] * val + eq[2] * val ** 2 + eq[3] * val ** 3


def comp_equat_with_zero(eq, val, inaccuracy=0):
    sol_e = equation(eq, val)
    return abs(sol_e) <= inaccuracy


def derivative(eq, val):
    deriv = (eq[1], 2 * eq[2], 3 * eq[3])
    return deriv[0] + deriv[1] * val + deriv[2] * val ** 2


def comp_deriv_with_zero(eq, val, inaccuracy=0):
    sol_d = derivative(eq, val)
    return abs(sol_d) <= inaccuracy


def dichotomy(eq, a, b, eps=0.001):
    f_a = equation(eq, a)
    k = 0
    for k in range(1, 10000):
        c = 0.5 * (a + b)
        f_c = equation(eq, c)
        if abs(b - a) < 2*eps:
            return 'Completed', c, k, f_c
        else:
            if f_a*f_c < 0:
                b = c
            else:
                a = c
                f_a = f_c
    return 'Error: the solution of the equation was not found', c


def newton_half_div(eq, a, b, x0, eps=0.001):
    if x0 <= b and x0 >= a:
        x_k = x0
    else:
        return 'Error: x0 does not belong to the segment [a,b]', x0
    for k in range(1, 10000):
        sol_d = derivative(eq, x_k)
        xx_k = x_k - equation(eq, x_k)/sol_d
        while True:
            f_xx_k = equation(eq, xx_k)
            if abs(f_xx_k) < abs(equation(eq, x_k)):
                break
            else:
                xx_k = 0.5*(x_k + xx_k)
        if abs(xx_k - x_k) < eps:
            return 'Completed', xx_k, k, f_xx_k
        else:
            x_k = xx_k
    return 'Error: the solution of the equation was not found', x_k


def visualization(eq):
    plt.figure(figsize=(10, 10))
    plt.title("The graph of function: x^3 - 0.8*x^2 - 6.8*x + 0.7")

    x = np.linspace(-5, 5, 100)

    plt.axis([-5, 5, -10, 10])
    plt.grid()
    plt.plot(x, equation(eq, x))

    plt.gca().spines['bottom'].set_position(('data', 0))
    plt.gca().spines['left'].set_position(('data', 0))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.xticks(np.linspace(-5, 5, 11))
    plt.yticks(np.linspace(-10, 10, 21))
    plt.show()
    pass


if __name__ == '__main__':
    eq = (0.7, -6.8, -0.8, 1)
    visualization(eq)
    while True:
        a = float(input('Enter the left border of the segment: '))
        b = float(input('Enter the right border of the segment: '))
        f_a = equation(eq, a)
        f_b = equation(eq, b)
        if f_a == 0:
            print('The solution of the equation is at the point a! Enter the segment boundaries again.')
            continue
        if f_b == 0:
            print('The solution of the equation is at the point b! Enter the segment boundaries again.')
            continue
        if f_a * f_b < 0:
            break
        else:
            print('Incorrect segment boundaries! Enter the segment boundaries again.')
    x0 = float(input('Enter an arbitrary value that belongs to the segment: '))
    n_h_d = newton_half_div(eq, a, b, x0)
    d_method = dichotomy(eq, a, b)
    if n_h_d[0] != 'Completed':
        print(n_h_d[0])
        print(f'Value: {n_h_d[1]}')
    else:
        if n_h_d[1] < a or n_h_d[1] > b:
            print('WARNING! The solution was found outside the segment!')
        print(f'The hybrid method: {n_h_d[1]}.')
        print(f'The number of iterations of the calculation is {n_h_d[2]}.')
        print(f'The value of the function at this point: {n_h_d[3]} \n')
    if d_method[0] != 'Completed':
        print(d_method[0])
        print(f'Value: {d_method[1]}')
    else:
        print(f'The method of dichotomy: {d_method[1]}.')
        print(f'The number of iterations of the calculation is {d_method[2]}')
        print(f'The value of the function at this point: {d_method[3]}')
