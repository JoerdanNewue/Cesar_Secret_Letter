bukvar = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
message = str(input("введите сообщение для шифрования"))
key = str(input("введите ключ для кодирования, слово из русских букв"))
key = key.lower()
key *= len(message) // len(key) + 1
print(key)
schet=0
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
    codeposition = position + endcount[schet]
    schet=schet+1
    if bukva in bukvar:
        strangeword = strangeword + bukvar[codeposition]
    else:
        print("вы ввели недопустимый символ")
print("теперь ваш текст не прочитать без ключа! выглядит он так:", strangeword)
