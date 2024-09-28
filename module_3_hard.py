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



