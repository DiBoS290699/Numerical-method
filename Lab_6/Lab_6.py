import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl


# Нахождение экспоненциальной показательной функции
def exponential_func(x, n):
    Eulers_const = 0.5772156649
    result = Eulers_const + np.log(abs(x))
    for i in range(1, n+1):
        result += np.power(x, i) / (np.math.factorial(i) * i)
    return result


# Общее решение диф-ого уравнения
def y(x):
    C = 1 + exponential_func(-1, 15)
    E_x = exponential_func(-x, 15)
    return np.sqrt(1/(np.exp(-x)*(1 - x) + np.power(x, 2)*(-E_x + C)))


# y' = f(x,y)
def f(x, y):
    return (np.power(y, 3)*np.exp(-x) - y) / x


# Нахождение шага h
def find_h(x_0, y_0, eps):
    h_list = np.linspace(1, 0, 1000)
    for h in h_list:
        # Отбрасываем значение х, перенеся его в переменную _
        _, y_1 = runge_kutta_method(x_0, y_0, h, 2)
        _, y_2 = runge_kutta_method(x_0, y_0, 2 * h, 1)
        if np.abs(y_1[-1] - y_2[-1]) < eps:
            return h


def find_n(a, b, h):
    n = np.ceil((b - a) / h)    # Округление к большему
    n = int(n + n % 2)
    h = (b - a) / n
    return n, h


# Решение диф. уравнения методом Рунге-Кутта 4 порядка
def runge_kutta_method(x, y, h, n):
    x_list = [x]
    y_list = [y]
    for i in range(n):
        K_1 = h * f(x, y)
        K_2 = h * f(x + h / 2, y + K_1 / 2)
        K_3 = h * f(x + h / 2, y + K_2 / 2)
        K_4 = h * f(x + h, y + K_3)
        y = y + K_1/6 + K_2/3 + K_3/3 + K_4/6
        x = x + h
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list


# Решение диф. уравнения методом Эйлера
def euler_method(x, y, h, n):
    x_list = [x]
    y_list = [y]
    for i in range(n):
        y += h * f(x, y)
        x += h
        y_list.append(y)
        x_list.append(x)
    return x_list, y_list


# Создание таблицы с данными
def create_table(data, path):
    data_frame = pd.DataFrame(data)
    data_frame.to_excel(path)


a = 1
b = 2
x_0 = 1
y_0 = 1
eps = 1e-4
optimal_h = find_h(x_0, y_0, eps)
n, h = find_n(a, b, optimal_h)
print(f"Оптимальный шаг h = {optimal_h}")
print(f'Оптимальный шаг с условием четности n, h = {h}')
print(f'Количество отрезков n = {n}')
print(f'Уточненное значение погрешности (по правилу Рунге) =\n'
      f'{np.abs(runge_kutta_method(x_0, y_0, h*2, 1)[1][-1] - runge_kutta_method(x_0, y_0, h, 2)[1][-1]) / 15}')

runge_x_list, runge_y_list = runge_kutta_method(x_0, y_0, h, n)
euler_x_list, euler_y_list = euler_method(x_0, y_0, h, n)
analitycal_x_list = np.linspace(a, b, 100)
analitycal_y_list = y(analitycal_x_list)

new_y_list = y(np.array(runge_x_list))

runge_error = np.abs(runge_y_list - new_y_list)
euler_error = np.abs(euler_y_list - new_y_list)
runge_error_max = np.max(runge_error)
euler_error_max = np.max(euler_error)
print(f'Максимум модуля отклонений (для метода Рунге) = {runge_error_max}')
print(f'Максимум модуля отклонений (для метода Эйлера) = {euler_error_max}')

data = {'Точное решение': new_y_list, 'Метод Рунге': runge_y_list, 'Отклонение для Рунге': runge_error,
        'Макс. откл. для Рунге': [runge_error_max for i in range(len(runge_x_list))],
        'Метод Эйлера': euler_y_list, 'Отклонение для Эйлера': euler_error,
        'Макс. откл. для Эйлера': [euler_error_max for i in range(len(runge_x_list))]}
create_table(data, 'Table with the results.xlsx')

plt.figure(figsize=(10, 10))
plt.plot(runge_x_list,  runge_y_list, label='Рунге')
plt.plot(euler_x_list,  euler_y_list, label='Эйлер')
plt.plot(analitycal_x_list, analitycal_y_list, label="Точное решение")
plt.title('Сравнение методов Рунге, Эйлера и точного решения')
plt.legend()
plt.grid()
plt.show()
