data_structure = [
  [1, 2, 3],# Список с числами
  {'a': 4, 'b': 5},# Словарь с ключами и значениями
  (6, {'cube': 7, 'drum': 8}),# Кортеж с числом и словарем
  "Hello",# Строка
  ((), [{(2, 'Urban', ('Urban2', 35))}])# Кортеж с вложенной структурой
]

def calculate_structure_sum(args):
  summa = 0
  # Прописываем условие при помощи цикла для подсчета чисел в списке
  if isinstance(args,list):
    for item in args:
      summa += calculate_structure_sum(item)
  # Прописываем условия при помощи цикла для подсчета ключей и значений
  elif isinstance(args, dict):
    for key, value in args.items():
      summa += calculate_structure_sum(key)
      summa += calculate_structure_sum(value)
  # Прописываем условия при помощи цикла для подсчета чисел в кортеже
  elif isinstance(args, tuple):
    for item in args:
      summa += calculate_structure_sum(item)
  # Прописываем условия при помощи цикла для множеств
  elif isinstance(args,set):
    for item in args:
      summa += calculate_structure_sum(item)
  # Прописываем условия для подсчета букв в слове с помощью метода len()
  elif isinstance(args, str):
      summa += len(args)
  # Прописываем условия определить тип данных методом isinstance из аргумента args и суммируем
  elif isinstance(args, (int, float)):
    summa += args
  return summa


result = calculate_structure_sum(data_structure)
print(result)


############################################################### ПЕРЕДЕЛКА ##############################################################################


data_structure = [
    [1, 2, 3],  # Список с числами
    {'a': 4, 'b': 5},  # Словарь с ключами и значениями
    (6, {'cube': 7, 'drum': 8}),  # Кортеж с числом и словарем
    "Hello",  # Строка
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # Кортеж с вложенной структурой
]


def calculate_structure_sum(args):
    total_sum = 0

    # Обработка списков и кортежей
    if isinstance(args, (list, tuple)):
        for item in args:
            total_sum += calculate_structure_sum(item)

    # Обработка словарей
    elif isinstance(args, dict):
        for key, value in args.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    # Обработка множеств
    elif isinstance(args, set):
        for item in args:
            total_sum += calculate_structure_sum(item)

    # Обработка строк
    elif isinstance(args, str):
        total_sum += len(args)

    # Обработка чисел
    elif isinstance(args, (int, float)):
        total_sum += args

    return total_sum


result = calculate_structure_sum(data_structure)
print(result)

# Рекурсивный подход
# Рекурсия позволяет функции вызывать саму себя для обработки вложенных структур.
#
# Списки: Если аргумент — это список, функция проходит по каждому элементу и вызывает саму себя для каждого элемента.
# Словари: Если аргумент — это словарь, функция проходит по ключам и значениям, вызывая саму себя для каждого
# ключа и значения.
# Кортежи и множества: Аналогично спискам, функция обрабатывает каждый элемент.
# Строки: Для строк функция просто добавляет их длину к сумме.
# Числа: Если аргумент — это число, оно добавляется к сумме.

# Объяснение изменений
# Объединение обработки списков и кортежей: Вместо того чтобы писать отдельные условия для 
# списков и кортежей, мы используем кортеж (list, tuple) в isinstance, что упрощает код.
# Переименование переменной: Переименовал summa в total_sum для большей ясности.
# Комментарии: Добавлены комментарии для лучшего понимания кода.

