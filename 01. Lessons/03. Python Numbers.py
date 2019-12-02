"""
Numbers буюу тоон өгөгдөл

Тоон өгөгдлийн төрлүүд
Үндсэн 2 тоон төрөл байна.

    Integers буюу бүхэл тоон төрөл. Жишээ: 2, -2, 100, 0, 10.
    Floating point буюу бутархай тоон төрөл. Жишээ: 2.0, -2.1.
"""

# Нэмэх
print(1+2) 
# 3

# Хасах
print(10-8) 
# 2

# Үржих
print(5*6)
# 30

# Хуваах
print(5/2)
# 2.5

# Бүхлээр хуваах - Floor division
print(5//2)
# 2

# Хуваасан үлдэгдэл - Division reminder
print(5%2)
# 1

# Тоон зэрэг - Powers
print(2**3)
# 8 

# Язгуур олох 
print(4**0.5)
#2

# Үйлдлийн дараалал
print(2 + 10*10 + 3)
#105

# Хаалт хэрэглэх
print((2 + 10)*(10 + 3))
#156


# Python -д random() гэдэг функц байдаггүй бөгөөд random гэдэг модуль ийг ашигладаг
import random
# 1 ээс 10 хооронд санамсаргүй тоо сонгох
print("1 ээс 10 хооронд санамсаргүй тоо сонгох:", random.randrange(1,10))