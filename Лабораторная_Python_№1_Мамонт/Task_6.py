#Напишите программу, позволяющую ввести с клавиатуры текст
#предложения и вывести на консоль все символы, которые входят в этот
#текст ровно по одному разу.
text = input("Введите текст: ")
for i in text:
    if text.count(i) == 1:
        print(i)

# chars = {}
# for char in text:
#    chars[char] = chars.get(char, 0) + 1
# for key, value in chars.items():
#     if value == 1:
#         print(key)
