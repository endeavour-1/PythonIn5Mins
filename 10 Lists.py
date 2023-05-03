#Represent a list of Objects or List of Names.


name = ["John", "Jayesh", "Jerry", "James"]

print(name)
# Output = ['John', 'Jayesh', 'Jerry', 'James']


# If we have to print only John we will write number corresponding to it.
print(name[0])
# Output = John


# Python supports negative index.
print(name[-1])
# Output = James


# If we have to replace John with Jon ; We type number corresponding to it and then equals new value.
# name [0]= "Jon"
# print(name)
# Output = ['Jon', 'Jayesh', 'Jerry', 'James']


# We can also select a range of value. Here we are printing first three Words in List.
print(name[0:3])
# Output = ['John', 'Jayesh', 'Jerry']