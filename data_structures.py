# Lists

list_sample = [1, 4, "ABC", 5, True]

print(list_sample[2])

# Dictionary
dictionary = {
    "name": "hello",
    "age": 30,
    "address": "USA"
}

print(dictionary["name"])

# Create a list
test = list("abcdefg")
print(test)
print(type(test))

# Add elements to the list
list_sample.append("DEF")
print(list_sample)

# Delete elements
del list_sample[1]
print(list_sample)


# Replace elements
list_sample[1] = 10
print(list_sample)

# Look for a value and return index
print(list_sample.index(10))
print(list_sample)

# extend method, add several values to the end of the list
list_sample.extend(["D", "E", "F"])
print(list_sample)

# concatenate lists
list_a = ['a', 'b', 'c']
list_b = ['d', 'e', 'f']

list_c = list_a + list_b
print(list_c)

# Sorting a list
list1 = ['H', 'e', 'l', 'l', 'o']
list1.sort()
print(list1)

list2 = ['H', 'e', 'l', 'l', 'o']
list2.sort(reverse=True)
print(list2)

# Insert an element at a specific index
list_sample.insert(3, "DEF")
print(list_sample)

# Delete an element at a specific index
list_sample.pop(1)
print(list_sample)

# Clear all elements in a list
anotherlist = [1, 2, 3, 'ABC', 5]
anotherlist.clear()
print(anotherlist)

# Get the lenght of a list
print(len(list_sample))

# Convert strings to list
test = "a,b,c"
list3 = test.split(",")
print(list3)

# Join mehtod
string = "/".join(list3)
print(string)

# Example program
def init():
    mylist = []
    while True:
        print("Please, enter a number between 1 and 5. Enter 6 to end this program")
        point = input()
        if (point.isdecimal()):
            point = int(point)
            
            if point == 6:
                print("All your comments here: ")
                print(mylist)
                break
            elif 1 <= point <= 6:
                print("Enter your comments: ")
                comment = input()
                
                print(f"Your comment: {comment}")
                print(f"Your point: {point}")
                
                mylist.append({point, comment})
                
        else:
            print("Please, enter a valid number")
                    
                    
                    
                    
# TUPLES elements cannot change, they are inmutable
tuple_test = "T01", "T02", "T03"
print(tuple_test)
print(type(tuple_test))

# Accessing elements
print(tuple_test[0])

# declaring two tuples
s, t = 100, 200
user_id1, user_id2, user_id3 = tuple_test
print(tuple_test)
print(user_id1)