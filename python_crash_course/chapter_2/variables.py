# chapter 2 variables
message = "Hello Python world!"
print(message)

hipython = "Hello Python Crash Course world!"
print(message)

print(mesage)

mesage = "Hello Python Crash Course reader!"
print(mesage)
# variables are labels
# variables can be changed

changes = "python is fun'who knew'"
print(changes)
# you can have quotes in quotes as long as you finish the quotes off

# anything after a . is a method, a method is an action python can do where as a variable is a label
# all methods end with () because it indicates the information it needs is also in parenthesis 


name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# .upper() and .lower() are methods that print in all upper case or all lower case lettersregardless of how the string is written
# .lower() is useful for storing info

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# between {} you need spaces if you want there to be a space between the two variables
# to combine variable put an f in front of the first quote and curly bracket
# f is for format and these are called f-strings
print(full_name.title())
# methods work on f-strings too