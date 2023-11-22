
sample = {"test", "test2", "test3"}

# Adding elements
sample.add("test4")
print(sample)
print(type(sample))

sample |= {"test5", "test6"}
print(sample)

# deleting elements
sample.remove("test2")
print(sample)

sample.discard("test5")
print(sample)


# clear all values
print(sample.clear())