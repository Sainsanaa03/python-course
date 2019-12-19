
"""
01. Хэрэглэгчээс орж ирсэн тэмдэгт мөрийг урвуугаар хөрвүүлэх код бичнэ үү!
"""

var = input('Гараас утга оруулна уу: ')
txt = var[::-1]
print(txt)


"""
02. Өгөгдсөн тоонуудад сондгой болон тэгш тоо хэд байгааг тоолох код бичнэ үү!
    Жишээ оролт: (1, 2, 3, 4, 5, 6, 7, 8, 9)
    Жишээ гаралт: Сондгой тоо 5, Тэгш тоо 4
"""
# 02::
var = [1, 2, 3, 4, 5, 6, 7, 8, 9]

oddNum = 0
evenNum = 0

for n in var:
    if n % 2 == 0:
        evenNum += 1
    else:
        oddNum += 1

print(f'Тэгш тоо: {evenNum}, Сондгой тоо: {oddNum}')

"""
03. 0-6 хүртэлх тоон цуваанаас 2 болон 5-аас бусад тоог хэвлэх код бичнэ үү!
"""
# 03::
var = '123456'

for n in var:
    if n == '2' or n == '5':
        pass
    else:
        print(n)
        
"""
04. Хэрэглэгчээс авсан текст дундаас тоон тэмдэгт хэдэн удаа орсон, үсэг хэдэн удаа орсонг олох код бичнэ үү!

    Жишээ оролт: Books 6.7
    Жишээ гаралт: Тоо 2, Үсэг 5
"""
# 04::
var = "Books 6.7"
strNum = 0
intNum = 0

for n in var:
    if n.isdigit():
        intNum += 1
    elif n.isalpha():
        strNum += 1

print(f'string = {strNum}, int = {intNum}')

"""
05. Loop ашиглан дараах хэлбэрээр * тэмдэгтийг хэвлэнэ үү!

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""

# 05 for::

for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(5, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

# 05 while::
y = 1
x = '* '
while y < 6:
    print(x * y)
    y += 1
while y > 0:
    print(x * y)
    y -= 1
