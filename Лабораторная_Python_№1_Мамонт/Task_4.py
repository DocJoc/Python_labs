#Напишите скрипт, который разделяет введенный с клавиатуры текст на
#слова и выводит сначала те слова, длина которых превосходит 7
#символов, затем слова размером от 4 до 7 символов, затем – все
#остальные
# [print(i) for i in [print(i) if i is not None and 4 <= len(i) <= 7 else i for i in
#                   [print(i) if len(i) > 6 else i for i in input("Введите текст: ").split()]] if
# i is not None and len(i) < 4]
lst = input("Введите текст: ").replace(",", " ").split()
large = [i for i in lst if len(i) > 7]
medium = [i for i in lst if 4 <= len(i) <= 7]
small = [i for i in lst if len(i) < 4]
print("{}\n{}\n{}".format(", ".join(large), ", ".join(medium), ", ".join(small)))
