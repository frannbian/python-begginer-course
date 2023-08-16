#Dictionaries (Like Objects, Jsons)

dog = { "name": "Terry", "age": 8 }

# print with the index
dog["name"]  # return True
#changing value
dog["name"] = "Pedra"
#also getting value
dog.get("name") # return Pedra
dog.get("color", "red") # return red, because the index color does not exists, so the default value is red (second parameter)

dog.pop("name") # remove the index selected

dog.popitem("color") # remove and return the value removed

#check if exists items
"color" in dog

#get the keys
list(dog.keys());

#get the values
list(dog.values())

#get the whole items
list(dog.items())

len(dog)

#delete a value
del dog["color"]

#copy a dictionary
newDictionary = dog.copy()

