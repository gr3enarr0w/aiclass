# chapter 2 variables
message = "Hello Python world!"
print(message)

hipython = "Hello Python Crash Course world!"
print(message)

message = "Hello Python Crash Course reader!"
print(message)
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

print(f"Hello,{full_name.title()}!")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = (f"Hello, {full_name.title()}")
print(message)

print("Python")
print("\tPython")
# \t inside a parenthesis of a string before the word adds a tab to the output

print("Languages:\nPython\nC\nJavaScript")
# Adding a \n 

print("Language\tEnglish\t\nSpanish\nJapanese\tChinese")

# white space can be removed but it requires a method
favorite_language = 'python '
print(favorite_language)

# .rstrip() removes whitespace if space is on right side and .lstrip() if space is on left and .strip() for both
print(favorite_language.rstrip())

# To associate the strip permanently a new variable is needed
new_favorite = favorite_language.rstrip()

#prefixes can be removed .removeprefix('thing_to_remove) see example
my_website = 'https://clarkeverson.com'
my_website.removeprefix('https://')
print(my_website.removeprefix('https://'))
user_website = my_website.removeprefix('https://')

# Same can be done with suffixes
domain_no_end = user_website.removesuffix('.com')
print(domain_no_end)
#the original string is unchanged hence my new variable
print(my_website)


# integers allow for multiplication, addition, subtraction and division
# to the power of can be done with ** where as multiplication is *
# Python uses PEMDAS (order of operations)
print((2+2)*3+1-4+2**2)

#any number with a decimal point is called a float
print(3/2)
# 3 and 2 are integers and the output, 1.5 is a float
# sometimes you will get an arbitrary number of decimals
print(0.2+0.1)
# the output of this is 0.30000000000000004
# division is always output as a float
print(3/3)
# answer is 1.0 not 1
# also mixing a integer and a float gives a float as well
print(1+5.0)
# you get 6.0 not 6

# underscores work in integers to make them more easibly readable like , in english. this works for integers and floats
print(1_000_000_000)
# output is 1000000000

universe_age = 14_000_000_000
print(universe_age)

# can assign multiple variables at once
variable_a, variable_b, variable_c = 1,2,3
print(variable_a)

# python doesn't have a for sure way to guarentee a constant but programmers generally use ALL_CAPS to indicate such
MAX_CONNECTIONS = 5000
# MAX_CONNECTIONS would indicate to others reading my code to not change the value later as it's all caps
# comments are represented by hashes (#) they are ways to exclude code or make notes. They are ignored when code runs
