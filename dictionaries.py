# dictionary
#create a new dictionary

dic = {"id":1, "name": "ted lanzo"}

dic2 = dict(id=1, name="ted lanzo")
print(dic)
print(dic2)

# add new item in the dictionary
dic["gender"] = "male"

# get an item with the id
print(dic.get('id',0))

# delete an item in a dictionary
print(dic)
del dic["name"]
print(dic)

# loop through a dictionary

for key , value in  dic.items():
    print(key,value)