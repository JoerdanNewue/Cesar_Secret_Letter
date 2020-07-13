bukvar = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
numberal = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32]
message = str(input("введите сообщение для шифрования"))
key = str(input("введите ключ для кодирования, слово из русских букв"))
key = key.lower()
key *= len(message) // len(key) + 1
print(key)
ckount = []
endcount = []
strangeword = ""
for i, j in enumerate(key):
    print(i, j)
    ckount.append(j)
for litera in ckount:
    secret_pose = bukvar.find(litera)
    endcount.append(secret_pose)
for bukva in message:
    position = bukvar.find(bukva)
    p=0
    codeposition = position + endcount[p]
    for o in range(len(key)):
        p=p+1
    if bukva in bukvar:
        strangeword = strangeword + bukvar[codeposition]
    else:
        print("вы ввели недопустимый символ")
print("теперь ваш текст не прочитать без ключа! выглядит он так:", strangeword)
