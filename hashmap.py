my_map={}
my_map["key"]="this is a value"
my_map[0]='zero'
my_map[1.3]='one.three'
print(my_map)
try:
    print(my_map[10])
except:
    print('key doesnt exist')


#Printing and defaulting if a key does not exist
# print(my_map)
# try:
#     print(my_map[10])
# except:
#     print("key does not exists")
# print(my_map[1.3])


#del my_map[0]
# print(my_map)


# if "key" in my_map:
#     print("key key is present")
# else:
#     print("key 0 is not present")