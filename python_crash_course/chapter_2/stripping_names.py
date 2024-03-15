# 2.7 exercise, stripping names

# variable for person's name with whitespace with first and last on separate lines
name = " Don\t\nJulio "

# print the original name
print(name)

# print the name with leading whitespace removed
print(name.lstrip())

# print the name with trailing whitespace removed
print(name.rstrip())

# print the name with leading and trailing whitespace removed
print(name.strip())