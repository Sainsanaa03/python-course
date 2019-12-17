"""
IF, ELIF, ELSE Condition
"""

# IF
x = 5
y = 8
print("x = ", x)
print("y = ", y)
if y > x:
    print("y нь x ээс их")
if y >= x:
    print("y нь x ээс их эсвэл тэнцүү")

# ELIF
a = 8
b = 8
if b > a:
  print("b нь a ээс их")
elif a == b:
  print("a болон b тэнцүү утгатай")

# ELSE
x = 100
if x % 3 == 0:
    print("3-т хуваагддаг тоо")
elif x % 3 == 1:
    print("3-т хуваахад 1 үлддэг тоо")
else:   
    print("3-т хуваахад 2 үлддэг тоо")

x = 101
if x % 3 == 0:
    print("3-т хуваагддаг тоо")
elif x % 3 == 1:
    print("3-т хуваахад 1 үлддэг тоо")
else:   
    print("3-т хуваахад 2 үлддэг тоо")

x = 7
if x % 2 == 0:
    print("2-т хуваагддаг тоо")
else:   
    print("2-т хуваахад 1 үлддэг тоо")

x = 101
if x % 3 == 0:
    print("3-т хуваагддаг тоо")
elif x % 3 == 1:
    print("3-т хуваахад 1 үлддэг тоо")
elif x % 3 == 2:   
    print("3-т хуваахад 2 үлддэг тоо")

# Short Hand IF, ELSE
x = 5
y = 8
if y > x: print("y нь x ээс их") 
"""
if y > x:
    print("y нь x ээс их")
"""

x = 7
print("2-т хуваагддаг тоо") if x % 2 == 0 else print("2-т хуваахад 1 үлддэг тоо") 
"""
x = 7
if x % 2 == 0:
    print("2-т хуваагддаг тоо")
else:   
    print("2-т хуваахад 1 үлддэг тоо")
"""

a = 8
b = 8
print("a > b") if a > b else print("a == b") if a == b else print("a < b") 
"""
if a > b:
    print("a > b")
else:
    if a == b:
        print("a == b")
    else:
        print("a < b")
"""


# IndentationError: expected an indented block
"""
if x % 3 == 0:
print("3-т хуваагддаг тоо")
elif x % 3 == 1:
print("3-т хуваахад 1 үлддэг тоо")
else:   
print("3-т хуваахад 2 үлддэг тоо")
"""    

# AND
a = 18
b = 5
c = 20
print(f"a = {a}, b = {b}, c = {c}")
if a > b and c > a:
  print("'a' нь 'b' ээс их мөн 'c' нь 'a' аас их")

# OR
a = 21
b = 8
c = 35
print(f"a = {a}, b = {b}, c = {c}")
if a > b or c < a:
  print("'a' нь 'b' ээс их эсвэл 'a' нь 'c' аас их")

# Nested If
x = 20

if x < 0:
    print("Сөрөг тоо")
    if x % 2 == 0:
        print("Тэгш тоо")
    else:
        print("Сондгой тоо")
else:
    print("Эерэг тоо")
    if x % 2 == 0:
        print("Тэгш тоо")
    else:
        print("Сондгой тоо")

y = -21

if y < 0:
    print("Сөрөг тоо")
    if y % 2 == 0:
        print("Тэгш тоо")
    else:
        print("Сондгой тоо")
else:
    print("Эерэг тоо")
    if y % 2 == 0:
        print("Тэгш тоо")
    else:
        print("Сондгой тоо")

# PASS
x = 8
y = 10

if y > x:
  pass
