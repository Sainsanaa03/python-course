"""
Loops::
Ямар нэгэн үйлдлийг олон дахин давтахдаа loop ашиглана.
    For loop
    While loop
"""

"""
For Loop
    For loop ашиглан list, tuple, string, set зэрэг iterator буюу гүйх боломжтой обьектуудаар эхнээс нь давтан хандаж болно.
"""
the_list = [ 1, 2, 3, 4 ]
the_tuple = ( 1, 2, 3, 4 )
the_set = { 1, 2, 3, 4 }
the_string = '1234'
the_dict = {
    'name': "Бат",
    'age': 20
}


for item in the_list:
    print("the_list: ", item)
# the_list:  1
# the_list:  2
# the_list:  3
# the_list:  4

for item in the_tuple:
    print("the_tuple: ", item)
# the_tuple:  1
# the_tuple:  2
# the_tuple:  3
# the_tuple:  4

for item in the_set:
    print("the_set: ", item)
# the_set:  1
# the_set:  2
# the_set:  3
# the_set:  4

for item in the_string:
    print("the_string: ", item)
# the_string:  1
# the_string:  2
# the_string:  3
# the_string:  4

for item in the_dict:
    print("the_dict: ", item)
# the_dict:  name
# the_dict:  age

for item in the_dict.keys():
    print("the_dict.keys: ", item)
# the_dict.keys:  name
# the_dict.keys:  age

for item in the_dict.values():
    print("the_dict.values: ", item)
# the_dict.values:  Бат
# the_dict.values:  20

# Тоон цуваагаар range() функц ашиглан гүйж болно.
print("-------- range(10) --------")
for item in range(10):
    print(item)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# range(10) нь 0 -с 9 хүртэлх утгийг авна, 10 орохгүй.

print("-------- range(1, 5) --------")
for item in range(1, 5):
    print(item)
# 1
# 2
# 3
# 4
# range(1, 5) нь 1 -с 4 хүртэлх утгийг авна, 5 орохгүй.


print("-------- range(0, 10, 2) --------")
for item in range(0, 10, 2):
    print(item)
# 0
# 2
# 4
# 6
# 8

print("-------- range(0, 12, 3) --------")
for item in range(0, 12, 3):
    print(item)
# 0
# 3
# 6
# 9

counter = 0
for n in range(1500, 2501):
    if n % 8 == 0 and n % 9 == 0:
        counter += 1
        print(n)
print(f"Нийт {counter} ширхэг байна.")

"""
1512
1584
1656
1728
1800
1872
1944
2016
2088
2160
2232
2304
2376
2448
Нийт 14 ширхэг байна.
"""


"""
Break, Continue Statement::
"""

# Давталтыг зогсоох буюу давталтаас гарахдаа 'break' ашиглана.
print("-------- Break Statement : for --------")
the_list = [ 0, 1, 2, 3, 4, 5 ]

for num in the_list:
    # 3 орж ирвэл давталтаас гарна
    if num == 3:
        break
    print(num)
# 0
# 1
# 2

# Давталт дундаас дараагийн давталтын ээлж рүү шууд шилжихдээ 'continue' ашиглана.
print("-------- Continue Statement : for --------")
the_list = [ 0, 1, 2, 3, 4, 5 ]

for num in the_list:
    # 3 орж ирвэл дараагийн давталт руу шууд үсэрнэ
    if num == 3:
        continue
    print(num)
# 0
# 1
# 2
# 4
# 5

"""
Else::
"""
print("------------ Else : for ------------")
for item in range(0, 5, 3):
    print("range: ", item)
else:
  print("Давталт дууслаа /range")
# 0
# 3
# Давталт дууслаа /range

the_list = [ "тэг", "нэг", "хоёр", "гурав" ]
for num in the_list:
    if num == "хоёр":
        break
    print("break: ", num)
else:
  print("Давталт дууслаа /break")
# тэг
# нэг

the_list = [ "тэг", "нэг", "хоёр", "гурав" ]
for num in the_list:
    if num == "хоёр":
        continue
    print("continue: ", num)
else:
  print("Давталт дууслаа /continue")
# тэг
# нэг
# гурав
# Давталт дууслаа /continue


"""
Nested Loops::
"""
print("------------ Nested Loops ------------")

listNum = ["нэг", "хоёр", "гурав"]
new_list = ["хонь", "үхэр", "ямаа"]

for x in listNum:
  for y in new_list:
    print(x, y)
# нэг хонь
# нэг үхэр
# нэг ямаа
# хоёр хонь
# хоёр үхэр
# хоёр ямаа
# гурав хонь
# гурав үхэр
# гурав ямаа

""" pass:: """
# loop давталт хоосон байж болохгүй, алдаа өгдөг 
# гэхдээ ямар нэгэн үйлдэл хийхгүй үед 'pass' ийг ашиглавал алдаа өгөхгүй
for x in [0, 1, 2]:
  pass


print("----------------------------- While Loop:: -----------------------------")
"""
While Loop::

Тухайн нөхцөл хангахгүй болтол давталтыг үргэлжлүүлэхдээ while loop-ийг ашиглана.
"""
temp = 1
while temp < 5:
  print(temp)
  temp += 1

# built-in module оруулж ирэх
import random
# 1-9 хооронд бүхэл тоон санамсаргүй утга авах
guess_number = random.randint(0, 10)
# Гараас авах утгыг хадгалах хувьсагч
input_number = 0
while guess_number != input_number:
    input_number = int(input("Тоо оруулна уу: "))

print(f"Баяр хүргэе. {guess_number} тоог амжилттай таалаа.")

# Тоо оруулна уу: 4
# Тоо оруулна уу: 6
# Тоо оруулна уу: 7
# Баяр хүргэе. 7 тоог амжилттай таалаа.

# Давталтыг зогсоох буюу давталтаас гарахдаа 'break' ашиглана.
print("-------- Break Statement : While --------")
counter = 0

while counter <= 5:
    # 3 орж ирвэл давталтаас гарна
    if counter == 3:
        break        
    print(counter)
    counter += 1
# 0
# 1
# 2

print("-------- Continue Statement : While --------")
counter = 0

while counter <= 5:
    counter += 1
    # 3 орж ирвэл дараагийн давталт руу шууд үсэрнэ
    if counter == 3:
        continue
    print(counter)
# 1
# 2
# 4
# 5
# 6

"""
Else::
"""
print("------------ Else : While ------------")
temp = 1
while temp < 5:
  print(temp)
  temp += 1
else:
  print("while давталт дууслаа.")

counter = 0
while counter <= 5:
    # 3 орж ирвэл давталтаас гарна
    if counter == 3:
        break        
    print("break", counter)
    counter += 1
else:
    print("while давталт дууслаа. /break")

counter = 0
while counter <= 5:
    counter += 1
    # 3 орж ирвэл дараагийн давталт руу шууд үсэрнэ
    if counter == 3:
        continue
    print("continue", counter)
else:
    print("while давталт дууслаа. /continue")

