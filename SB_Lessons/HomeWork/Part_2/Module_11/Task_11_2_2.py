# Задача 2. Однотипные объекты
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть
# четыре характеристики: название производителя, матрица, разрешение и частота обновления
# экрана. Все четыре монитора отличаются только частотой.
# У наушников три характеристики: название производителя, чувствительность и наличие
# микрофона. Отличие только в наличии микрофона.
#
# Для внесения в базу программист начал писать такой код:
# monitor_name_1 = 'Samsung'
# monitor_matrix_1 = 'VA'
# monitor_res_1 = 'WQHD'
# monitor_freq_1 = 60
# monitor_name_2 = 'Samsung'
# monitor_matrix_2 = 'VA'
# monitor_res_2 = 'WQHD'
# monitor_freq_2 = 144
# monitor_name_3 = 'Samsung'
# monitor_matrix_3 = 'VA'
# monitor_res_3 = 'WQHD'
# monitor_freq_3 = 70
# monitor_name_4 = 'Samsung'
# monitor_matrix_4 = 'VA'
# monitor_res_4 = 'WQHD'
# monitor_freq_4 = 60
#
# headphones_name_1 = 'Sony'
# headphones_sensitivity_1 = 108
# headphones_micro_1 = False
# headphones_name_2 = 'Sony'
# headphones_sensitivity_2 = 108
# headphones_micro_2 = True
# headphones_name_3 = 'Sony'
# headphones_sensitivity_3 = 108
# headphones_micro_3 = True
#
# Поправьте программиста: перепишите код, используя классы и экземпляры классов.

class Monitor:
    def __init__(self, name, matrix, res, freq):
        self.name = name
        self.matrix = matrix
        self.res = res
        self.freq = freq

    def print_info(self):
        print(f'TV\n'
              f'model: {self.name}\n'
              f'matrix: {self.matrix}\n'
              f'resolution: {self.res}\n'
              f'frequency: {self.freq}\n')


class Headphones:
    def __init__(self, name, sensitivity, micro):
        self.name = name
        self.sensitivity = sensitivity
        self.micro = micro

    def print_info(self):
        print(f'Headphones\n'
              f'model: {self.name}\n'
              f'sensitivity: {self.sensitivity}\n'
              f'microphone: {self.micro}\n')


monitor_1 = Monitor('Samsung', 'VA', 'WQHD', 60)
monitor_2 = Monitor('Samsung', 'VA', 'WQHD', 144)
monitor_3 = Monitor('Samsung', 'VA', 'WQHD', 70)
monitor_4 = Monitor('Samsung', 'VA', 'WQHD', 60)

headphones_1 = Headphones('Sony', 108, False)
headphones_2 = Headphones('Sony', 108, True)
headphones_3 = Headphones('Sony', 108, True)

monitor_1.print_info()
monitor_2.print_info()
monitor_3.print_info()
monitor_4.print_info()

headphones_1.print_info()
headphones_2.print_info()
headphones_3.print_info()
