# Booleans нь дараах 2 утгийн нэгийг нь буцаана, илтгэнэ : True or False.

print("5 > 1 ::", 5 > 1)
# True
print("5 == 1 ::", 5 == 1)
# False
print("5 < 1 ::", 5 < 1) 
# False
print("Сайн уу" == "1") 
# False
print("Сайн байна уу" == "Сайн байна уу")
# True

print("Сайн уу ::", bool("Сайн уу"))
# True
print("18 ::", bool(18))
# True

x = "Сайн уу"
y = 18
print(f"x = {x}, y = {y}")
print("x ::", bool(x))
print("y ::", bool(y))

# TRUE::

print("bool('abc'):", bool("abc")) 
print("bool('123'):", bool(123)) 
print("bool(['apple', 'cherry', 'banana']):", bool(["apple", "cherry", "banana"]))

# FALSE::

print("bool(False):", bool(False))
print("bool(None):", bool(None))
print("bool(0):", bool(0))
print("bool(""):", bool(""))
print("bool(()):", bool(()))
print("bool([]):", bool([]))
print("bool({}):", bool({}))


x = 10
print("x ийн төрөл", isinstance(x, int))
x = "10"
print("x ийн төрөл", isinstance(x, int))
print("x ийн төрөл", isinstance(x, str))


