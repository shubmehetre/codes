def takeSecond(x):
    return x[1]

record = [('nik' , 88), ('Jacob' , 44), ('Clint' , 78), ('jay' , 66)]

record.sort(key=takeSecond)


print("Sorted : ", record)
