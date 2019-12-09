"""
Tuples::

List төрөлтэй төстэй боловч элемэнтийг өөрчилж болдоггүйгээрээ ялгаатай. 
Ямар нэгэн өөрчилж болдоггүй утгыг хадгалахдаа tuple - ийг ашиглана.
"""

# tuple үүсгэх
t = (1, 2, 3)
print(t)
# (1, 2, 3)

# Ямарч өгөгдлийн төрөлтэй элемэнтүүдээс бүрдэж болно.
t = ('нэг', 2)
print(t)
# ('нэг', 2)

# Тухайн элемэнтэд хандах
temp = t[0]
print(temp)
# нэг

# Сүүлийн элемэнтэд хандах
temp = t[-1]
print(temp)
# 2

"""
Tuple функцууд::

Цөөхөн хэдэн гишүүн функцуудтэй.
"""
# Элемэнтийн тоог авах
len_t = len(t)
print(len_t)
# 3

# Тухайн элемэнтийн дугаарыг авах
index_t = t.index('нэг')
print(index_t)
# 0

# Тухайн элемэнт tuple - д хэд байгааг олох
count_t = t.count('нэг')
print(count_t)
# 1

# in
new_tuples = (0, 1, 2, 3) 
t_in = 0 in new_tuples
print(t_in)
# true

t_in = "0" in new_tuples
print(t_in)
# false

# not in
t_in = 0 not in new_tuples
print(t_in)
# false

t_in = "0" not in new_tuples
print(t_in)
# true

"""
Immutability буюу гишүүн элемэнтийг өөрчилж болохгүй
"""

# t[0] = 'change value'
# TypeError: 'tuple' object does not support item assignment

# t[2] = 'new value'
# TypeError: 'tuple' object does not support item assignment

# t.append('nope')
# AttributeError: 'tuple' object has no attribute 'append'


"""
Tuples утга өөрчилөх
"""
tuple_temp = ("тэг", 1, "two", "3")
print("Tuple:", tuple_temp)
# ('тэг', 1, 'two', '3')

list_temp = list(tuple_temp)
print("List before change:", list_temp)
# ['тэг', 1, 'two', '3']
list_temp[0] = "zero"
print("List after change:", list_temp)
# ['zero', 1, 'two', '3']
tuple_temp = tuple(list_temp)
print("Tuple:", tuple_temp)
# ('zero', 1, 'two', '3')


# 1 утгатай Tuple үүгэхдээ сүүлд нь , нэмж өгөх хэрэгтэй
oneTuple = ("Tuple",)
print(type(oneTuple))
# <class 'tuple'>
# oneTuple[0] = "tuples"
# TypeError: 'tuple' object does not support item assignment

# Tuple биш,
oneTuple = ("Tuple")
print(type(oneTuple)) 
# <class 'str'>

# Устгах::
del_tuple = ("Delete",)
del del_tuple
# print(del_tuple)
# NameError: name 'del_tuple' is not defined

# 2 Tuple-г нэмэх:: 
tuple1 = ("zero", 1 , "two")
tuple2 = (0, "one", 2)

tuple3 = tuple1 + tuple2
print(tuple3) 

# Tuple(), Tuple үүсгэх
newTuple = tuple(("create", "new", "tuple")) 
print(newTuple)
# ('create', 'new', 'tuple')
print(type(newTuple)) 
# <class 'tuple'>