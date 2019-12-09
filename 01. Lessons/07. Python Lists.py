"""
Lists

    Элемэнтүүдийн дарааллыг list гэнэ. 
    String - тэй төстэй боловч mutable буюу элемэнтийг сольж болдог шинж чанартай.
"""

# my_list нэртэй list үүсгэх
my_list = [1,2,3, 4]
print(my_list)
# [1, 2, 3, 4]

# Өөр өөр обьект буюу өгөгдлийн төрлүүдийг хадгалж болно.
my_list = ['A string', 23, 100.232 ,'o' ]
print(my_list)
# ['A string', 23, 100.232, 'o']

# List хэдэн элемэнттэйг харуулна.
len(my_list)
length = len(my_list)
print(length)
# 4

# list() ашиглан list үүсгэх, үүсгэхдээ 2 хаалтыг ашиглана 
other_list = list((11.2, "Хүснэгт", 2j))
print(other_list)
# [11.2, 'Хүснэгт', 2j]

"""
Indexing and Slicing
String төрлийн indexing - тэй адилхан байдлаар хэрэглэгдэнэ.
"""

my_list = ['нэг','хоёр','гурав',4,5]
# Эхний элемэнтэд хандах
temp = my_list[0]
print(temp)
# нэг

# Сүүлийн элемэнтэд хандах
temp = my_list[-1]
print(temp)
# 5

# Хоёр дахь элемэнтийг өөрчилөх
my_list[1] = 2
print(my_list)
# ['нэг', 2, 'гурав', 4, 5]

# Эхний элемэнтээс бусад элемэнтийг авах
temp = my_list[1:]
print(temp)
# [2, 'гурав', 4, 5]

# Эхний 3 элемэнтийг авах
temp = my_list[:3]
print(temp)
# ['нэг', 2, 'гурав']


"""
 2 list - ийг хооронд нь залгах.
"""
# 2 хүснэгтийг хооронд нь залгах хамгийн амархан арга нь + тэмдгийг ашиглах юм.

list1 = ["нэг", "хоёр" , "гурав"]
list2 = [2.5, "дундах элемэнт", 1j]
list3 = list1 + list2
print(list3)
# ['нэг', 'хоёр', 'гурав', 2.5, 'дундах элемэнт', 1j]

list2.extend(list1)
print(list2) 
# [2.5, 'дундах элемэнт', 1j, 'нэг', 'хоёр', 'гурав']

my_list += ['шинэ элемэнт']
print(my_list)
# ['нэг', 2, 'гурав', 4, 5, 'шинэ элемэнт']

"""
list - ийг өөрөөр нь үржүүлэх буюу олон дахин өөр дээр нь залгаж болно.
"""

# 2 дахин давтах
my_list *= 2
print(my_list)
# ['нэг', 2, 'гурав', 4, 5, 'шинэ элемэнт', 'нэг', 2, 'гурав', 4, 5, 'шинэ элемэнт']

# int ээс өөр төрлийн өгөдлөөр дээрх үйлдлийг хийж болохгүй,
"""
my_list *= "2aa"
print(my_list)
"""

"""
List функцууд

    Python хэлний list - д тодорхой хэмжээ гэж байхгүй. Хүссэн үедээ элемэнт нэмж болно.
"""

# Шинэ list үүсгэх
new_list = [1,2,3]

# Тухайн list - ийн төгсгөлд элемэнт нэмэх
new_list.append('нэмэгдсэн элемэнт')
print(new_list)
# [1, 2, 3, 'нэмэгдсэн элемэнт']

# pop функцийг ашиглан элемэнт сугалах буюу устгаж болно.
# Эхний элемэнтийг сугалах
new_list.pop(0)
print(new_list)
# [2, 3, 'нэмэгдсэн элемэнт']

# Сүүлийн элемэнтийг сугалах
popped_item = new_list.pop()
print(popped_item)
# нэмэгдсэн элемэнт

# Үлдсэн элемэнтүүд
print(new_list)
# [2, 3]

# Элемэнт нэмэх: insert()
new_list.insert(0, "нэг")
print(new_list)
# ['нэг', 2, 3]

# Элемэнт хасах: remove()
new_list.remove(2)
print(new_list)
# ['нэг', 3]

# Хүснэгтийг хоослох: clear()
new_list.clear()
print(new_list)
# []

# Хоосон хүснэгтэнд утга өгөх:
new_list = [1, 2, "гурав"]
print(new_list)
# [1, 2, 'гурав']

# Элемэнт устгах: del
del new_list[0]
print(new_list)
# [2, 'гурав']

# Хүснэгтийг устгах: del
del new_list
# print(new_list) # Алдаа заана, яагаад гэвэл ийм хүснэгт байхгүй устсан учраас,

# Хүснэгтийг хувилах: copy(), list()
new_list = ["1В", 0.28, "тоо"]
print(new_list)
# ['1В', 0.28, 'тоо']
copylist = new_list.copy()
print(copylist)
# ['1В', 0.28, 'тоо']
listList = list(copylist)
print(listList)
# ['1В', 0.28, 'тоо']

# Хүснэгтээс элемэнт тоолох: count()
count_list = [12, 2, 55, 2, 16, 2]
count = count_list.count(2)
print(count)
# 3

# Хүснэгтийн хэд дэхь элемэнт вэ: index()
index_list = ['нэг', 'хоёр', 'гурав']
index = index_list.index("гурав")
print(index)
# 2

# Хүснэгтийг сүүлээс нь эхлэл болгож байрлалыг нь өөрчлөх: reverse()
reverse_list = [0, 1, 2, 3, 4, 5]
reverse_list.reverse()
print(reverse_list)
# [5, 4, 3, 2, 1, 0]

# Хүснэгтийг дараалалд оруулах: sort()
sort_list = [16, 1, 22, 51, 38, 2.1]
sort_list.sort()
print(sort_list)
# [1, 2.1, 16, 22, 38, 51]
