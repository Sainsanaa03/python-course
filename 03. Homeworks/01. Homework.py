"""
01. Loop ашиглан дараах хэлбэрээр тоонуудыг хэвлэнэ үү!
   A.
        1
        2 2
        3 3 3
        4 4 4 4
        5 5 5 5 5

    B.
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
"""
# 01 - A::
lastNumber = 5
for row in range(1, lastNumber):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")


# 01 - B::
lastNumber = 5
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

"""
02. Өгөгдсөн 2 List ийг нэгтгэх. Нэгтгэхдээ эхний List - ээс зөвхөн тэгш тоог, 2 дахь List -ээс сондгой тоог нь авна.

   List01 = [1, 2, 5, 15, 6]
    List02 = [3, 4, 7, 11, 18]
    mergedList = [2, 6, 3, 7, 11]
"""
# 02::
List01 = [1, 2, 5, 15, 6]
List02 = [3, 4, 7, 11, 18]
# mergedList = [2, 6, 3, 7, 11]
mergedList = []

for n in List01:
    if n % 2 == 0:
        mergedList.append(n)

for n in List02:
    if n % 2 == 0:
        pass
    else:
        mergedList.append(n)

print(mergedList)

"""
03. 1-50 хүртэлх тоон цувааг эхнээс нь хэвлэнэ. Ингэхдээ 5-д хуваагддаг тоонуудын оронд 'FIVE', 3-д хуваагддаг тоонуудын оронд 'THREE' гэж бичнэ.
"""

# 03::
for n in range(1, 51):
    if n % 5 == 0 and n % 3 == 0:
        print('Five and Three')
    elif n % 5 == 0:
        print('Five')
    elif n % 3 == 0:
        print('Three')
    else:
        print(n)
