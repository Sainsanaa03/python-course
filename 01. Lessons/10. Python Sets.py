"""
Sets::
Ялгаатай элемэнтүүдээс бүрдсэн олонлогийг set гэнэ.
"""

# Шинэ set үүсгэх
x = set()
print(x)
# set()

# Элемэнт нэмэх
x.add(1)
print(x)
# {1}

# index, order гэсэн ойлголт байхгүй,
# print(x[0])
# TypeError: 'set' object is not subscriptable


"""
Аливаа элемэнт зөвхөн нэг удаа байна.
"""
# add() - Элемэнт нэмэх
x.add(2)
print(x)
# {1, 2}

# Адилхан элемэнт нэмэх гэж оролдох
x.add(1)
print(x)
# {1, 2}

# update() - Элемэнт нэмэх
mySet = {"0", 1, 2}
print("mySet: ", mySet) 
mySet.update([0, "one", "two"])
print("mySet update: ", mySet) 
# {0, 1, 2, 'one', '0', 'two'}

# Адилхан элемэнт нэмэх гэж оролдох
mySet.update([0, 0, 0])
print("mySet another update: ", mySet) 
# {0, 1, 2, 'two', '0', 'one'}
# print(mySet[1]) - # TypeError: 'set' object is not subscriptable

# len()
len_mySet = len(mySet)
print(len_mySet) 
# 6

# in 
mySet = {"this", "is", "my", "set"}
in_mySet = "my" in mySet
print("in:", in_mySet)
# true
in_mySet = "are" in mySet
print("in:", in_mySet)
# false

# not in
in_mySet = "my" not in mySet
print("not in:", in_mySet)
# false
in_mySet = "are" not in mySet
print("not in:", in_mySet)
# true

"""
Устгах::
"""
# remove()
removeSet = {"zero", "one", "two"}
print("remove:", removeSet) 
# {'zero', 'two', 'one'}
removeSet.remove("one")
print("remove:", removeSet) 
# {'zero', 'two'}

# remove() - Байхгүй утгийг устгах гэвэл алдаа заана
# removeSet.remove("one")
# print("remove:", removeSet) 
# removeSet.remove("one")   KeyError: 'one

# discard()
discardSet = {1, 2, 3}
print("discard:", discardSet) 
# {1, 2, 3}
discardSet.discard(3)
print("discard:", discardSet) 
# {1, 2}
# discard() - Байхгүй утгийг устгах гэвэл алдаа заахгүй
discardSet.discard(3)
print("discard:", discardSet) 
# {1, 2}

# pop () - функц сүүлийн элемэнтийг устгана, 
# гэхдээ Sets -д order, index гэж байхгүй учираас аль ч элемэнтийг устгаж магадгүй!

popSet = {"zero", "one", "two", "three"}
popItem = popSet.pop()
print("popItem:", popItem)
print("popSet:", popSet)  

# clear()
clearSet = {1, 2, 3, 4}
print("clearSet before clear():", clearSet)
# {1, 2, 3, 4}
clearSet.clear()
print("clearSet after clear():", clearSet)
# set()

# del
delSet = {"one", "two", "three"}
del delSet
# print(delSet) 
# NameError: name 'delSet' is not defined

"""
2 Sets -г нэмэх
"""
# union()
set1 = {"one", "two", "three"}
print("set1: ", set1)
# {'one', 'three', 'two'}
set2 = {1, 2, 3}
print("set2: ", set2)
# {1, 2, 3}
set3 = set1.union(set2)
print("union set3: ", set3) 
# {1, 2, 3, 'one', 'three', 'two'}

# update()
set1 = {"one", "two", "three"}
print("set1: ", set1)
# {'one', 'three', 'two'} 
set2 = {1, 2, 3}
print("set2: ", set2)
# {1, 2, 3}
set1.update(set2)
print("update set1: ", set1) 
# {1, 'two', 2, 3, 'one', 'three'}

# Давхардсан элемэнттэй үед::
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.union(set2)
print("union: ", set3)
# {1, 2, 3, 4, 5, 6}
set1.update(set2)
print("update: ", set1)
# {1, 2, 3, 4, 5, 6}


# set() -р set үүсгэх::
set_set = set(("one", "two", "three")) 
print("set(): ", set_set) 
#  {'one', 'three', 'two'}

"""
List - ийг set болгон хөрвүүлж болно.
"""
# Давтагдсан элемэнтүүдтэй list
list1 = [1,1,2,2,3,4,5,6,1,1]
print(list1)
# [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]

# Set болгон хөрвүүлэх
print(type(list1))
# <class 'list'>
newSet =  set(list1)
print(type(newSet))
# <class 'set'>
print(newSet)
# {1, 2, 3, 4, 5, 6}


"""
Бусад функцууд::
"""
# copy():: - хуулах
new_set = {1, 2, 3, 4}
copy_set = new_set.copy()
print("copy(): ", copy_set)
# {1, 2, 3, 4}


# difference():: - set дотор байгаа ялгаатай элемэнтүүдийг буцаана
set1 = {"zero", "one", "two"}
set2 = {"two", "three", "five"}
diffSet = set1.difference(set2)
print("difference(): ", diffSet) 
# {'zero', 'one'}

diffSet = set2.difference(set1)
print("difference(): ", diffSet)
# {'three', 'five'}


# difference_update():: - 2 дахь set дотор эхний set -тэй адилхан элемэнт байвал эхний set -с устгана 
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
set1.difference_update(set2)
print("difference_update(): ", set1) 
# {1, 2, 3}

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
set2.difference_update(set1)
print("difference_update(): ", set2) 
# {5, 6, 7}


# discard():: - яг тухайн утгийг устгана, 
mySet = {"zero", "one", "two"}
mySet.discard("two")
print("discard(): ", mySet) 
# {'one', 'zero'}


# intersection():: - бүх set дотор байгаа ижил элемэнтүүдийг буцаана,
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
set3 = set1.intersection(set2)
print("intersection(): ", set3) 
# {4}

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
set3 = {3, 4, 6, 7}
set4 = set1.intersection(set2, set3)
print("intersection(): ", set4) 
# {4}


# intersection_update():: - set1, set2, - бүх set -д байхгүй элемэнтүүдийг устгана,
set1 = {"zero", "one", "two"}
set2 = {"two", "three", "four"}
set1.intersection_update(set2)
print("intersection_update(): ", set1)
# {'two'}

set1 = {"zero", "one", "two", "three"}
set2 = {"two", "three", "four", "five"}
set3 = {"three", "four", "five", "six"}
set1.intersection_update(set2, set3)
print("intersection_update(): ", set1)
# {'three'}


# isdisjoint():: - Адилхан элемэнт байхгүй байна, тийм үү?
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
set3 = set1.isdisjoint(set2)
print("isdisjoint(): ", set3) 
# True

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
set3 = set1.isdisjoint(set2)
print("isdisjoint(): ", set3) 
# False


# issubset():: - set2 дотор set1 ийн бүх элемэнт агуулагдаж байна уу? 
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = set1.issubset(set2)
print("issubset(): ", set3) 
# True

set1 = {1, 2, 3, 4, "тав"}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}
set3 = set1.issubset(set2)
print("issubset(): ", set3) 
# False


# issuperset():: set1 дотор set2 ийн бүх элемэнт агуулагдаж байна уу?
set1 = {8, 7, 6, 5, 4, 3, 2, 1}
set2 = {1, 2, 3, 4}
set3 = set1.issuperset(set2)
print("issuperset(): ", set3) 
# True

set1 = {8, 7, 6, 5, 4, 3, 2, 1}
set2 = {1, 2, 3, 4, "тав"}
set3 = set1.issuperset(set2)
print("issuperset(): ", set3) 
# False


# symmetric_difference():: set дотор байгаа ижил элемэтээс бусад элемэнтүүдийг буцаана,
# давхцаагүй элемэтүүдийг буцаана
set1 = {"zero", "one", "two", "three"}
set2 = {"two", "three", "four", "five"}
set3 = set1.symmetric_difference(set2)

print("symmetric_difference(): ", set3) 
# {'four', 'one', 'five', 'zero'}


# symmetric_difference_update():: set1 -д set1 болон2 дотор байгаа ижил элемэтээс бусад элемэнтүүдийг өгнө,
set1 = {"zero", "one", "two", "three"}
set2 = {"two", "three", "four", "five"}
set1.symmetric_difference_update(set2)
print("symmetric_difference_update():", set1) 
# {'four', 'five', 'zero', 'one'}