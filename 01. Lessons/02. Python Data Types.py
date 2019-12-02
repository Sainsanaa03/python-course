x = 5
print(x)
# 5
print(type(x))
# <class 'int'>


y = "Сайн байна уу"
print(y)
# Сайн байна уу
print(type(y))
# <class 'str'>


x = 1.8
print(x)
# 1.8
print(type(x)) 
# <class 'float'>


x = 8j
print(x)
# 8j
print(type(x)) 
# <class 'complex'>


x = ["Bat", "Dorj", "Bold"]
print(x)
# ["Bat", "Dorj", "Bold"]
print(type(x)) 
# <class 'list'>


x = ("Bat", "Dorj", "Bold")
print(x)
# ("Bat", "Dorj", "Bold")
print(type(x)) 
# <class 'tuple'>


x = range(8)
print(x)
# range(0, 8)
print(type(x)) 
# <class 'range'>


x = {"key1" : "value1", "key2" : "value2"}
print(x)
# {'key1': 'value1', 'key2': 'value2'}
print(type(x)) 
# <class 'dict'>


x = {"Bat", "Dorj", "Bold"}
print(x)
# {'Dorj', 'Bat', 'Bold'}
print(type(x)) 
# <class 'set'>


x = frozenset({"Bat", "Dorj", "Bold"})
print(x)
# frozenset({'Bold', 'Bat', 'Dorj'})
print(type(x)) 
# <class 'frozenset'>

x = True
print(x)
# True
print(type(x)) 
# <class 'bool'>


x = b"python"
print(x)
# b'python'
print(type(x)) 
# <class 'bytes'>


x = bytearray(3)
print(x)
# bytearray(b'\x00\x00\x00')
print(type(x)) 
# <class 'bytearray'>


x = memoryview(bytes(2))
print(x)
# <memory at 0x01871388>
print(type(x)) 
# <class 'memoryview'>


print("----------Төрөл хувиргах----------")
x = 8 # int төрөл
print(type(x))
# <class 'int'>
y = 5.1 # float  төрөл
print(type(y))
# <class 'float'>
z = 3j # complex  төрөл
print(type(z))
# <class 'complex'>


# int төрлийг float төрөл болгох:
a = float(x)
print(a)
# 8.0
print(type(a))
# <class 'float'>


# float төрлийг int төрөл болгох:
b = int(y)
print(b)
# 5
print(type(b))
# <class 'int'>


# int төрлийг complex төрөл болгох:
c = complex(x)
print(c)
# (8+0j)
print(type(c))
# <class 'complex'>


# string төрлийг int төрөл болгох:
age = "18"
print(type(age))
# <class 'str'>
age_int = int(age)
print(type(age_int))
# <class 'int'>
print(age_int + 5)
# 23


# int төрлийг string төрөл болгох:
age_string = str(age_int)
print(type(age_string))
# <class 'str'>
print(age_string)
# 18
print(age_string + "python3")
# 18python3


# list төрлийг string төрөл болгох:
list = ['1', '2', '3']
print(type(list))
# <class 'list'>
str1 = ''.join(list)
print(type(str1))
# <class 'str'>
print(str1)

list = [1, 2, 3]
print(type(list))
# <class 'list'>
str1 = ''.join(str(e) for e in list)
print(type(str1))
# <class 'str'>
print(str1)


