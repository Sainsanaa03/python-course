"""
Variable Assignment
Хувьсагчид нэр оноох дүрмүүд¶

    Хувьсагчийн нэр тоогоор эхлэхгүй
    Хувьсагчийн нэр дундаа хоосон зайг агуулахгүй
    Дараах тэмдэгтүүдийг агуулахгүй: :'",<>/?|\!@#%^&*~-+
    Хувьсагчийн нэрийг жижиг үсгээр эхэлж бичих нь зохимжтой. (PEP8)
    Python хэлэнд тусгай зориулалтаар ашигладаг үгсийг ашиглахгүй. Жишээ нь: list, str

Dynamic Typing vs Static Typing
    Dynamic: Аливаа хувьсагчид олон төрлийн өгөгдлийг дурын үед оноож болно.
    Static: Аливаа хувьсагчид програмын туршид зөвхөн анх зарласан өгөгдлийн төрлийн утгуудыг оноож болно.
"""

my_friends = 3
print(my_friends)
# 3

my_friends = ['Сараа', 'Нараа', 'Навчаа']
print(my_friends)
# ['Сараа', 'Нараа', 'Навчаа']

"""
Хувьсагчид утга оноох:    
name = object, = нь утга оноох оператор юм.
"""

a = 5
print(a)
# 5
print(a + a)
# 10

y = "BOLD"
print(y)
# BOLD

z = 10
print(z)
# 10

z = "BAT"
print(z)
# BAT

# Хувьсагч зарлах үед жижиг болон том үсгүүд өөр өөр хувьсагчийг илэрхийлнэ.

AGE = 1
AGe = 2
aGe = 3
AgE = 4

print(AGE)
# 1
print(AGe)
# 2
print(aGe)
# 3
print(AgE)
# 4

name, nAme, naMe = "Dolgor", "Bataa", "Naraa"
print(name)
# Dolgor
print(nAme)
# Bataa
print(naMe)
# Naraa

x = y = z = 1.2
print(x)
# 1.2
print(y)
# 1.2
print(z)
# 1.2

x = "байна уу"
print("Сайн " + x)
# Сайн байна уу

y = x
x = "Сайн "
z =  x + y
print(z)
# Сайн байна уу

x = 5
y = 10
print ( "five + ten =", x + y)
# 15
print ( "five - ten =", x - y)
# -5


""" 
# Global Variables
"""

x = "байна уу"
def func01():
    print("Сайн " + x)
    # Сайн байна уу
func01()


def func02():
  x = "уу :)"
  print("Сайн " + x)
  # Сайн уу :)
func02()
print("Сайн " + x)
# Сайн байна уу


def func03():
  global x
  x = "байна уу"
func03()
print("Сайн " + x)
# Сайн байна уу


x = "байна уу"
def func04():
  global x
  x = "уу :)"
func04()
print("Сайн " + x)
# Сайн уу :)
