"""
Dictionaries
Dictionary нь түлхүүр үг (key) түүнд харгалзах утга (value) - аас бүрдэнэ.
"""

# Dictionary үүсгэх
my_dict = { 'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict)
# { 'key1':'value1', 'key2':'value2', 'key3':'value3'}

# Key - ээр дамжуулж утгыг авах
key2 = my_dict['key2']
print(key2)
# value2

# get() ашиглах
key3 = my_dict.get("key3")
print(key3)
# value3

# Dictionary урт
print("length of my_dict:", len(my_dict)) 
# 3

# Key - д харгалзах утга нь ямар ч өгөгдлийн төрөл байж болно.
my_dict = {'key1':123, 'key2':[12,23,33], 'key3':['item0','item1','item2']}
key2 = my_dict['key2']
print(key2)
# [12, 23, 33]
key3 = my_dict['key3']
print(key3)
# ['item0', 'item1', 'item2']
key3_0 = my_dict['key3'][0]
print(key3_0)
# item0
key3_0 = my_dict['key3'][0].upper()
print(key3_0)
# ITEM0

# Тухайн key - д харгалзах утгыг өөрчилж болдог.
print("my_dict['key1']:", my_dict['key1'])
# 123
my_dict['key1'] = my_dict['key1'] - 123
print("my_dict['key1']:", my_dict['key1'])
# 0

my_dict['key3'] = "value3"
print("my_dict['key3']:", my_dict['key3'])
# value3

print("my_dict['key2']:", my_dict['key2'])
# [12, 23, 33]
print("type of my_dict['key2']:", type(my_dict['key2']))
# <class 'list'>
my_dict['key2'] += ['шинэ элемэнт']
print("my_dict['key2']:", my_dict['key2'])
# [12, 23, 33, 'шинэ элемэнт']

temp = my_dict['key2']
# my_dict['key2'].remove(0)
temp.remove(12)
print("temp:", temp)
# [23, 33, 'шинэ элемэнт']
print("my_dict['key2']: ", my_dict['key2']) 


# Нэмэх
student =	{
  "firstName": "BOLD",
  "lastName": "BAT",
  "DOB": "1990"
}
print("student: ", student)
# {'firstName': 'BOLD', 'lastName': 'BAT', 'DOB': '1990'}
student["school"] = "MUIS"
print("student: ", student)
# {'firstName': 'BOLD', 'lastName': 'BAT', 'DOB': '1990', 'school': 'MUIS'}

# Keyword -р элемэнтийг устгах (1) : pop()
student.pop("DOB")
print("student: ", student)
# {'firstName': 'BOLD', 'lastName': 'BAT', 'school': 'MUIS'}

# Сүүлийн элемэнтийг устгах: popitem()
student.popitem()
print("student: ", student)
# {'firstName': 'BOLD', 'lastName': 'BAT'}

# Keyword -р элемэнтийг устгах (2): del
del student["firstName"]
print("student: ", student)
# {'lastName': 'BAT'}

# Мөн Dictionary -ийг бүхэлд нь устгах: del
del student
# print(student) # Алдаа заана, яагаад гэвэл student гэдэг Dictionary байхгүй болсон учираас,

# Dictionary -ийг хоослох: clear()
person =	{
  "firstName": "Navchaa",
  "lastName": "Solongo",
  "DOB": "1985"
}
print("before clear: ", person) 
# {'firstName': 'Navchaa', 'lastName': 'Solongo', 'DOB': '1985'}
person.clear()
print("after clear: ", person) 
# {}

# Dictionary -ийг хуулах, хувилах: copy(), dict()
copy_dic_1 =	{
  "A": "1",
  "B": "2",
  "C": 3
}
print("copy_dic_1: ", copy_dic_1)
# {'A': '1', 'B': '2', 'C': 3}
copy_dic_2 = copy_dic_1.copy()
print("copy_dic_2: ", copy_dic_2)
# {'A': '1', 'B': '2', 'C': 3}
copy_dic_3 = dict(copy_dic_2)
print("copy_dic_3: ", copy_dic_3)
# {'A': '1', 'B': '2', 'C': 3}

# Dictionary бусад функцууд

d = {'key1':1,'key2':2,'key3':3}

# Бүх key - ийг авах
dict_k = d.keys()
print(dict_k)
# dict_keys(['key1', 'key2', 'key3'])

# Бүх утгыг авах
dict_val = d.values()
print(dict_val)
# dict_values([1, 2, 3])

# Бүх элемэнтийг tuple байдлаар авах
dict_t = d.items()
print(dict_t)
# dict_items([('key1', 1), ('key2', 2), ('key3', 3)])


# Шинэ dictionary үүсгэх
new_dict = {}
# Шинэ утга нэмэх
new_dict['animal'] = 'Dog'
# Шинэ утга нэмэх
new_dict['age'] = 2.5
print(new_dict)
# {'animal': 'Dog', 'age': 2.5}

# dict -р шинэ dictionary үүсгэх 
new_dict = dict( key1 = "1", key2 = 2, key3 = "Value3")
print(new_dict)
# {'key1': '1', 'key2': 2, 'key3': 'Value3'}


""" Dictionary дотор dictionary хадгалах """ 

d = {'key1': {'nestkey': {'subnestkey':'value'} } }
print(d)
# {'key1': {'nestkey': {'subnestkey': 'value'}}}
print(d['key1']['nestkey']['subnestkey'])
# value

nested_dict_1 = { 
    'dictA': {'key_1-1': 'value_1-1'},
    'dictB': {'key_1-2': 'value_1-2'},
    'dictc': {'key_1-3': 'value_1-3'},
}
print("nested_dict_1:", nested_dict_1)
#  {'dictA': {'key_1-1': 'value_1-1'}, 'dictB': {'key_1-2': 'value_1-2'}, 'dictc': {'key_1-3': 'value_1-3'}}

nested_dict_2 = { 
    'dictA': {'key_2-1': 'value_2-1'},
    'dictB': {'key_2-2': 'value_2-2'},
    'dictc': {'key_2-3': 'value_2-3'},
}
print("nested_dict_2:", nested_dict_2)
# {'dictA': {'key_2-1': 'value_2-1'}, 'dictB': {'key_2-2': 'value_2-2'}, 'dictc': {'key_2-3': 'value_2-3'}}

nested_dict_3 = { 
    'dictA': {'key_3-1': 'value_3-1'},
    'dictB': {'key_3-2': 'value_3-2'},
    'dictc': {'key_3-3': 'value_3-3'},
}
print("nested_dict_3:", nested_dict_3)
#  {'dictA': {'key_3-1': 'value_3-1'}, 'dictB': {'key_3-2': 'value_3-2'}, 'dictc': {'key_3-3': 'value_3-3'}}

nested_dict = {
  "nested_dict_1" : nested_dict_1,
  "nested_dict_2" : nested_dict_2,
  "nested_dict_3" : nested_dict_3
} 
print("nested_dict: ", nested_dict)
# nested_dict: {
# 'nested_dict_1': {
#                   'dictA': {'key_1-1': 'value_1-1'}, 
#                   'dictB': {'key_1-2': 'value_1-2'}, 
#                   'dictc': {'key_1-3': 'value_1-3'}
#                   }, 
# 'nested_dict_2': {
#                   'dictA': {'key_2-1': 'value_2-1'}, 
#                   'dictB': {'key_2-2': 'value_2-2'}, 
#                   'dictc': {'key_2-3': 'value_2-3'}
#                   }, 
# 'nested_dict_3': {
#                   'dictA': {'key_3-1': 'value_3-1'}, 
#                   'dictB': {'key_3-2': 'value_3-2'}, 
#                   'dictc': {'key_3-3': 'value_3-3'}
#                   }
# }



