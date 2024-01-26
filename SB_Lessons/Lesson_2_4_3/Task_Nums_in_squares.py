# Каждое нечётное число от 0 до 10 возвести в квадрат, чётное - в куб.

squares_cubes = [(x**2 if x % 2 != 0 else x**3) for x in range(10)]

print(squares_cubes)