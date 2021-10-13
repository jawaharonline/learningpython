
b = set()
print(type(b))

# adding values to an empty set
b.add(34) #adding repetative doesnt change sets
b.add((3, 4, 40))
# b.add({4:5}) U cant add dict or list in set
b.add("hello")
print(b)

#Length of set
print(len(b)) #sets length

#REmoveal of elements
b.remove(34) #removes the element
print(b)

print(b.pop()) #deletes randomly 
# print(b.clear()) #clear the sets


print(b.union())