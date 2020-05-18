import numpy as np


# Определим функции
def f(x):
    return x*np.sin(3*x)


def second_deriv_f(x):
    return 3*(-3*x*np.sin(3*x) + 2*np.cos(3*x))


def newton_method():
    return np.sin(3)/9 - np.cos(3)/3


# Оптимальный шаг для трапеции
def find_optimal_h(a, b, eps=0.001):
    x = np.linspace(a, b, 100)
    M = np.max(np.abs(second_deriv_f(x)))
    # M * |b -a| * h^2 / 12 < eps
    h = np.sqrt(12 * eps / (M * abs(b-a)))
    n = int((b-a)/h)
    n += (4-(n % 4))
    return (b-a)/n, n


def trapez_method(a, b, h, n):
    x = np.linspace(a, b, n+1)
    f_x = f(x)
    return h*((f_x[0] + f_x[-1])/2 + np.sum(f_x[1:-1]))


def simpson_method(a, b, h, n):
    x = np.linspace(a, b, n+1)
    f_x = f(x)
    return (h/6) * (f_x[0] + f_x[-1] + 4*np.sum(f_x[1:-1]) - 1/2 + 2*np.sum(f_x[1:-2]))


a = 0
b = 1
h, n = find_optimal_h(a, b, 0.001)
print(f"Оптимальный h и n: h = {h}\nn = {n}")

# Интегрирование при h
t_m_with_h = trapez_method(a, b, h, n)
s_m_with_h = simpson_method(a, b, h, n)

# Интегрирование при 2h
t_m_with_2h = trapez_method(a, b, 2*h, n//2)
s_m_with_2h = simpson_method(a, b, 2*h, n//2)

# Расчет ошибки по методу Рунге для метода ТРАПЕЦИЙ
coef_Trapez = 1 / 3
error_t = coef_Trapez * (abs(t_m_with_h - t_m_with_2h))

# Расчет ошибки по методу Рунге для метода Симпсона
coef_Simpson = 1 / 15
error_s = coef_Simpson * (abs(s_m_with_h - s_m_with_2h))

print(f"Вычисление интеграла методом трапеций при h:    {t_m_with_h:.10f} +- {error_t:.10f}")
print(f"Вычисление интеграла методом Симпсона при h:    {s_m_with_h:.10f} +- {error_s:.10f}")

print(f"Вычисление интеграла методом трапеций при 2h:   {t_m_with_2h:.10f} +- {error_t:.10f}")
print(f"Вычисление интеграла методом Симпсона при 2h:   {s_m_with_2h:.10f} +- {error_s:.10f}")

# Вычисление Ньютона-Лейбница
print(f"Вычисление интеграла мметодом Ньютона-Лейбница: {newton_method():.10f}")