#Напишите скрипт, который позволяет ввести с клавиатуры текст
#предложения и сформировать новую строку на основе исходной, в
#которой все слова, начинающиеся с большой буквы, приведены к
#верхнему регистру. Слова могут разделяться запятыми или пробелами.
#Например, если пользователь введет строку «город Донецк, река
#Кальмиус», результирующая строка должна выглядеть так: «город
#ДОНЕЦК, река КАЛЬМИУС»
# 1 способ
# print(" ".join([i.upper() if i.istitle() else i for i in("".join([" " if not i.isalnum() else i for i in input(
# "Введите текст: ")]).split())]))

# 2 способ
s = input("Введите текст: ")
lst = "".join([" " if not i.isalnum() else i for i in s]).split()
result = " ".join([i.upper() if i.istitle() else i for i in lst])
print(result)

# 3 способ
# s = input("Введите текст: ")
# lst = "".join([" " if not i.isalnum() else i for i in s]).split()
# for i in range(len(lst)):
#    if lst[i].istitle():
#        lst[i] = lst[i].upper()
# print(" ".join(lst))
