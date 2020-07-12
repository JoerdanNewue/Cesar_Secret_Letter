bukvar = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
message = str(input("введите сообщение для шифрования"))
key = int(input("введите ключ для кодирования"))
message = message.lower()
strangeword = ""
for bukva in message:
    position = bukvar.find(bukva)
    codeposition = position + key
    if bukva in bukvar:
        strangeword = strangeword + bukvar[codeposition]
    else:
        print("вы ввели недопустимый символ")
print("теперь ваш текст не прочитать без ключа! выглядит он так:", strangeword)
