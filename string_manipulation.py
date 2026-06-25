string = str(input("Enter a string: "))
print(string)
result = string.upper()
print(result)
reverse = string[::-1]
print(reverse)
modified_string = string.replace(" ", "-")
print(modified_string)
number_of_vowels1 = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
print(number_of_vowels1)

#number_of_vowels = sum(1 for char in string if char.lower() in 'aeiou')
#print(number_of_vowels)
