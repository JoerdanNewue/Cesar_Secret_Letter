bukvar = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
numberal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33]
message = str(input("введите сообщение для шифрования"))
key = str(input("введите ключ для кодирования, слово из русских букв"))
key = key.lower()
ckount= []
strangeword = ""
for i, j in enumerate(key):
    print(i, j)
    for g in bukvar:
        pos_keya = bukvar.find(g)
        if j==g:
            for 
