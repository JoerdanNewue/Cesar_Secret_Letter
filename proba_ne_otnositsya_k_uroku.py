bukvar = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
endcount=[]
for litera in bukvar:
    secret_pose = bukvar.find(litera)
    endcount.append(secret_pose)
print(endcount)