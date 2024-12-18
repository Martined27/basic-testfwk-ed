# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

# Write your first_three_multiples function here
def first_three_multiples(num):
    print(num)
    print(num * 2)
    print(num * 3)
    return num * 3

first_three_multiples(10)


# Create a function called tip() that has two parameters named total and percentage.# Write your tip function here:
def tip(total, percentage):
    return (total * percentage) / 100

# Uncomment these function calls to test your tip function:
print(tip(10, 25))


#Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.# Write your introduction function here:
def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))


# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"

# Write your dog_years function here:
def dog_years(name, age):
    dog_age = age * 7
    return f"{name}, you are {dog_age} years old in dog years"

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))


# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print c minus d.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo a.

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
    first = a + b
    second = c - d
    third = first * second
    print(first)
    print(second)
    print(third)
    return third % a

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
