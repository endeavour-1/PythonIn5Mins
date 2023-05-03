# Range Function in Python.

numbers = range(5)
#prints numbers from 0 to 4
for number in numbers:

    print(number)
# Output =
# 0
# 1
# 2
# 3
# 4


numbers = range(5, 10)
# Prints numbers from 5 to 10 - (Starting Number , Ending Number) Note: It excludes Ending Number.
for number in numbers:

    print(number)
# Output =
# 5
# 6
# 7
# 8
# 9


numbers = range(5, 10, 2)
# Prints numbers from 5 to 10 - (Starting Number , Ending Number, Step) Note: It excludes Ending Number.
# Step = Number of elements we want to Jump.
for number in numbers:

    print(number)
# Output =
# 5
# 7
# 9


for number in range(5):

    print(number)
# Output =
# 0
# 1
# 2
# 3
# 4