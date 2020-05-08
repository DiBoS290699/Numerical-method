import numpy as np
import matplotlib.pyplot as plt


# Наша функция
def f(x):
    return np.pi * x / (10+x/2)


# Производная 4 порядка понадобится для вычисления шага
def derivative(x):
    return -(1152*np.pi)/(np.power(x+24, 5))


# Построение графика,
x = np.linspace(0, 10, 100)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, f(x), label="Функция")
plt.legend()
plt.show()


def lagrange(x, y, arg):
    L = 0
    for i in range(len(x)):
        mult = 1
        for j in range(len(x)):
            if i != j:
                mult *= (arg - x[j]) / (x[i] - x[j])
        L += y[i] * mult
    return L


arg = np.arange(0, 10, 0.001)
x = np.linspace(0, 10, 4)
y = f(x)
plt.plot(arg, lagrange(x, y, arg), c="black", label="Лагранж")
plt.grid()
plt.legend()
plt.show()


def newton(x, y, arg):
    result = y[0]
    h = x[1] - x[0]
    t = (arg - x[0])/h
    diff = [0]*4
    for i in range(len(y)):  # Скопировали массив значений
        diff[i] = y[i]
    # Одно значение уже использовали
    for i in range(len(x)-1):
        for j in range(len(x) - (i+1)):
            diff[j] = diff[j+1]-diff[j]  # Конечная разность j-1 порядка 1.
        temp = diff[0]
        # Факториал
        for j in range(0, i+1):
            temp *= (t-j)
            temp /= (j+1)
        result += temp
    return result


plt.plot(arg, newton(x, y, arg), c="red", label="Ньютон")
plt.grid()
plt.legend()
plt.show()


def omega(x, xs):
    val = 1
    for point in xs:
        val *= x - point  # (х-х0)(х-х1)...
    return val


# Оценка погрешности интерполяции в точке на отрезке
def error(x, xs):
    max_deriv = np.max(np.abs(derivative(x)))  # максимальное значение производной 4 порядка на отрезке,
    err_val = max_deriv * np.max(np.abs(omega(x, xs))) / np.math.factorial(len(xs))
    return np.abs(err_val)


def max_error_h(a, h):
    xs = np.array([a, a + h, a + 2*h, a + 3*h])
    x = np.linspace(a, a + 3*h, 100)
    return np.max(error(x, xs))


def compute_optimal_h(left_border, max_err):
    hs = np.linspace(10.0, 0, 100)  # размеры шагов, которые будем перебирать
    for h in hs:
        err = max_error_h(left_border, h)
        if err <= max_err:
            return h


h = compute_optimal_h(0, 0.0001)
print(f"Оптимальный шаг h = {h}")

a = 0
b = a + 3*h
X = np.linspace(a, b, 4)
Y = f(X)
arg = np.linspace(a, b, 30000)

lagrange_calculate, newton_calculate, lagrange_error, newton_error = [], [], [], []
for i in range(len(arg)):
    Lag = lagrange(X, Y, arg[i])
    Newt = newton(X, Y, arg[i])
    lagrange_calculate.append(Lag)
    newton_calculate.append(Newt)
    # (X, Y, arg[i]) - f(arg[i])) - разность между значением многочлена в точке и значением фун в точке
    lagrange_error.append(abs(Lag - f(arg[i])))
    newton_error.append(abs(Newt - f(arg[i])))

plt.title('Все графики')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.plot(arg, newton_calculate, c="red", linewidth=4, label="Ньютон")
plt.plot(arg, lagrange_calculate, c='black', linewidth=2, label='Лагранж')
plt.plot(X, f(X), c='blue', linewidth=1, label='Функция')
plt.legend()
plt.show()


plt.title("Абсолютная погрешность")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.plot(arg, lagrange_error, linewidth=3, label="Погрешность Лагранжа", c='black')
plt.plot(arg, newton_error, linewidth=1, label='Погрешность Ньютона', c='red')
plt.legend()
plt.show()


point = 1
print(f"Ньютон при аргументе: {point} равен: {newton(X, Y, point)}")
print(f"Лагранж при аргументе: {point} равен: {lagrange(X, Y, point)}")
