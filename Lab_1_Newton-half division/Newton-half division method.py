def absol(val):
    return -val if val < 0 else val


def equation(eq, val):
    return eq[0] + eq[1] * val + eq[2] * val ** 2 + eq[3] * val ** 3


def comp_equat_with_zero(eq, val, inaccuracy=0):
    sol_e = equation(eq, val)
    return absol(sol_e) <= inaccuracy


def derivative(eq, val):
    deriv = (eq[1], 2 * eq[2], 3 * eq[3])
    return deriv[0] + deriv[1] * val + deriv[2] * val ** 2


def comp_deriv_with_zero(eq, val, inaccuracy=0):
    sol_d = derivative(eq, val)
    return absol(sol_d) <= inaccuracy


def Newton_half_div(eq, a, b, x0, eps=0.001, inaccuracy=0):
    k = 0
    x_k = x0
    sol_d = derivative(eq, x_k)
    xx_k = x_k - equation(eq, x_k)/sol_d
