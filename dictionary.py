dictionary = {
    'name': 'John',
    'age': 20
}

print(dictionary)

# no se puede almacenar dos veces la misma clave
dictionary = {
    "name": "Lady",
    "name": "Hello"
}

print(dictionary)

# Añadir elementos
dictionary["role"] = "CEO"
dictionary["address"] = "123 street"
print(dictionary)

# Delete elements
del dictionary["address"]
print(dictionary)

# Methods

# keys
print(dictionary.keys())

# values
print(dictionary.values)

# in not in
print("name" in dictionary)
print("age" not in dictionary)
print("role" not in dictionary)

# check if a value is in dictionary
print("Hello" in dictionary.values())
print("Jake" not in dictionary.values())

# items. get the key value items
print(dictionary.items())

# get the number of elements of the dictionary
print(len(dictionary))

mydict = {
    "name": "Jake",
    "age": 30
}

point_list = [100, 200]
address = {
    "prefecture": "Tokyo",
    "city": "Shibuya-ku"
}
dictionary["point"] = point_list
dictionary["address"] = address
print(dictionary)


# Convert to type dictionary using dict and zip function
sample_a = ["name", "age", "address"]
sample_b = ["Jake", 20, "Washington"]
person = dict(zip(sample_a, sample_b))
print(person)