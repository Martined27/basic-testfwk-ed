letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
    # List of all uppercase and lowercase English letters
  
    # Initialize a counter for unique letters
    unique_count = 0
    # Loop through each letter in the alphabet
    for letter in letters:
        # Check if the letter is in the word
        if letter in word:
            unique_count += 1
    return unique_count

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4


### Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

# Write your count_char_x function here:# Write your count_char_x function here:
def count_char_x(word, x):
    # Initialize a counter for occurrences of x
    count = 0
    # Loop through each character in the word
    for char in word:
        # Check if the character is equal to x
        if char == x:
            count += 1
    return count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
    # Split the word by the substring x
    splits = word.split(x)
    # The number of occurrences is one less than the number of splits
    return len(splits) - 1

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
#print(count_multi_char_x("apple", "pp"))
# should print 1


# Write your check_for_name function here:
def check_for_name(sentence, name):
    # Convert both sentence and name to lowercase
    sentence_lower = sentence.lower()
    name_lower = name.lower()
    # Check if name is in sentence
    return name_lower in sentence_lower

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# Write your every_other_letter function here:
def every_other_letter(word):
    result = ""
    for i in range(0, len(word), 2):
        result += word[i]
    return result

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))


# Write your reverse_string function here:
def reverse_string(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))


# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
   
    first_char_word1 = word1[0]
    first_char_word2 = word2[0]
 
    rest_word1 = word1[1:]
    rest_word2 = word2[1:]
    
    new_word1 = first_char_word2 + rest_word1
    new_word2 = first_char_word1 + rest_word2
    
    result = new_word1 + " " + new_word2

    return result

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))

def add_exclamation(word):
    # Step 2: Loop while the length of word is less than 20
    while len(word) < 20:
        # Step 3: Append an exclamation mark
        word += "!"
    
    # Step 4: Return the result
    return word


