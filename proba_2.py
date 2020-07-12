print("введите сообщение из МАКСИМАЛЬНО 5-ти слов, примечание: ввиду способа реализации в алфавите НЕ ПОДДЕРЖИВАЕТСЯ буква 'Ё' ")
message1 = str(input("введите сообщение1 для шифрования на русском"))
message1 = message1.lower()
message2 = str(input("введите сообщение2 для шифрования на русском"))
message2 = message2.lower()
message3 = str(input("введите сообщение3 для шифрования на русском"))
message3 = message3.lower()
message4 = str(input("введите сообщение4 для шифрования на русском"))
message4 = message4.lower()
message5 = str(input("введите сообщение5 для шифрования на русском"))
message5 = message5.lower()
key = str(input("введите ключ для кодирования, слово из русских букв"))
key= key.lower()
key *= (len(message1)+len(message2)+len(message3)+len(message4)+len(message5)) // len(key) + 1
strangeword1 = ""
for i, j in enumerate(message1):
    num = (ord(j) + ord(key[i]))
    print(ord(j), ord(key[i]), num, num%32)
    strangeword1 += chr(num % 32 + 1073)
strangeword2 = ""
for i, j in enumerate(message2):
    num = (ord(j) + ord(key[i]))
    print(ord(j), ord(key[i]), num, num%32)
    strangeword2 += chr(num % 32 + 1073)
strangeword3 = ""
for i, j in enumerate(message3):
    num = (ord(j) + ord(key[i]))
    print(ord(j), ord(key[i]), num, num%32)
    strangeword3 += chr(num % 32 + 1073)
for i, j in enumerate(message4):
    num = (ord(j) + ord(key[i]))
    print(ord(j), ord(key[i]), num, num%32)
    strangeword4 += chr(num % 32 + 1073)
for i, j in enumerate(message5):
    num = (ord(j) + ord(key[i]))
    print(ord(j), ord(key[i]), num, num%32)
    strangeword5 += chr(num % 32 + 1073)
print("закодирование собщение " + str(strangeword1)+)



print("введите одно слово, примечание: ввиду способа реализации в алфавите НЕ ПОДДЕРЖИВАЕТСЯ буква 'Ё' ")
message1 = str(input("введите сообщение1 для шифрования на русском"))
message1 = message1.lower()
key = str(input("введите ключ для кодирования, слово из русских букв"))
key= key.lower()
key *= (len(message1)) // len(key) + 1
strangeword1 = ""
for i, j in enumerate(message1):
    num = (ord(j) + ord(key[i]))
    print(ord(j), ord(key[i]), num, num%32)
    strangeword1 += chr(num % 32 + 1073)
print("закодирование собщение " + str(strangeword1))

