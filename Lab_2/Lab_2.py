import numpy as np
import matplotlib.pyplot as plt

"""
f1: cos (x + 0.5) - y - 2 = 0
f2: sin y - 2x - 1 = 0
"""

zero = np.zeros(2)  # вектор нулей (0, 0)


"""Создаётся и возвращается система из двух функций в конкретной точке"""
def function(x):
    # x, y = x[0], x[1]
    return np.array([(np.cos(x[0] + 0.5) - x[1] - 2), (np.sin(x[1]) - 2 * x[0] - 1)])


def f1_dx(x):
    return -np.sin(x + 0.5)


def f1_dy(y):
    return -1


def f2_dx(x):
    return -2


def f2_dy(y):
    return np.cos(y)


def matrix_jacobi(x):
    # x, y = x[0], x[1]
    return np.array([[f1_dx(x[0]), f1_dy(x[1])], [f2_dx(x[0]), f2_dy(x[1])]])


def norm(x1, x2):
    return np.linalg.norm(x1 - x2)


def newton(x0, eps):
    i = 1
    x = x0
    x = x - np.linalg.inv(matrix_jacobi(x)).dot(function(x))
    while norm(x, x0) > eps:
        # dot - выполняет скаларное произведение двух массивов,
        # linalg.inv - Обратная матрица
        i += 1
        x0 = x
        x = x - np.linalg.inv(matrix_jacobi(x)).dot(function(x))
        if i > 400:
            print("Error: Number of iterations above the limit")
            print("!!Diverge!!")
            break

    print('||x_k - x_k1||:', norm(x, x0))
    print('||F(x_k) - F(x)||:', norm(function(x), zero))
    print('Point:', x[0], x[1])
    print('Iterations:', i)


def mod_newton(x_init, eps):
    i = 1
    x_prev = x_init
    x = x_init
    # dot - выполняет скаларное произведение двух массивов,
    # linalg.inv - Обратная матрица
    jacobi_in_x_init = np.linalg.inv(matrix_jacobi(x_init))
    x = x - jacobi_in_x_init.dot(function(x))
    while norm(x, x_prev) > eps:
        i += 1
        x_prev = x
        x = x - jacobi_in_x_init.dot(function(x))
        if i > 400:
            print("Error: Number of iterations above the limit")
            print("!!Diverge!!")
            break

    print('||x_k - x_k1||:', norm(x, x_prev))
    print('||F(x_k) - F(x)||:', norm(function(x), zero))
    print('Point:', x[0], x[1])
    print('Iterations:', i)


def display_graph():
    # Возвращение значений "у" через значения "х" для первого уравнения
    def f1(x):
        return np.cos(x + 0.5) - 2

    # Возвращение значений "х" через значения "у" для второго уравнения
    def f2(y):
        return (np.sin(y) - 1) / 2

    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)

    plt.plot(x, f1(x), c='g')  # Занесение графика для первого уравнения
    plt.plot(f2(y), y, c='r')  # Занесение графика для второго уравнения
    plt.grid()  # Добавление сетки
    plt.xlabel('Ось х')  # Подпись к оси
    plt.ylabel('Ось y')  # Подпись к оси
    plt.show()


if __name__ == '__main__':
    display_graph()

    x = float(input('Enter x: '))
    y = float(input('Enter y: '))
    eps = 0.00001
    x0 = np.array([x, y], dtype=np.float64)

    print('Newton')
    newton(x0, eps)

    print('---------------------------------------\nModified Newton')
    mod_newton(x0, eps)
