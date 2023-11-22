# Open a file

# with open('data.txt', 'r') as file_r:

file_r = open('data.txt', 'r')
print(file_r.read())

# write to file
file = open('data.txt', 'a')
file.write("Python world")



file_r.close()