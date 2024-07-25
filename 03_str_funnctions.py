name =  "harry are"

print(len(name))               #It gives the length of a string

print(name.endswith("ry"))     # it tells ending  of the string
print(name.startswith("ha"))   # it tells starting  of the string

print(name.capitalize())       #It capitalize the strings first word

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World" It concatenate the Strings
print(result)

result1 = str1 * 3  # "HelloHelloHello" It prints the strings three times 
print(result1)

num = 123
str_num = str(num)  # "123" It converts a value to a string
print(str_num)

lower_str = str1.lower()  # "hello" It converts the string to the lower case letter
print(lower_str)
upper_str = str1.upper()  # "HELLO" It converts the string to the upper case letter
print(upper_str)

str3 = " Hello "
stripped = str3.strip()  # "Hello"  It removes the white spaces at both ends of the string
print(stripped)
lstripped = str3.lstrip()  # "Hello  " It removes the white spaces at the left end of the string
print(lstripped)
rstripped = str3.rstrip()  # "  Hello" It removes the white spaces at the right end of the string
print(rstripped)

str4 = "Hello World"
words = str4.split()  # ['Hello', 'World'] It splits the string by comma
str5 = "-".join(words)  # "Hello-World"  It joins the string by the character
print(words,str5)

str6 = "Hello World"
new_str = str6.replace("World", "Python")  # "Hello Python" It replaces the word from a string
print(new_str)

pos = str2.find("World")  # 6   Find the first and last occurrence of a substring
print(pos)
rpos = str1.rfind("o")  # 7     Find the first and last occurrence of a substring
print(rpos)

st1 = "12345"
is_digit = st1.isdigit()  # True Tells whether the string is numerical or not
print(is_digit)
st2 = "Hello"
is_alpha = st2.isalpha()  # True  Tells whether the string is alphabatical or not
print(is_alpha)
st3 = "Hello123"
is_alnum = st3.isalnum()  # True  Tells whether the string is alphanumeric or not
print(is_alnum)
st4 = "   "
is_space = st4.isspace()  # True  Tells whether the string is only whitespace or not
print(is_space)

title_str = name.title()  # "Harry Are"  It capitalize the first alphabet of all thw words in the strings
print(title_str)
swapcase_str = name.swapcase()  # "HARRY ARE"  It capitalize all  the alphabets present in the string
print(swapcase_str)

s = "Welcome to python!"
print(len(s))
print(len(s.center(50)))       # Print the world at the center of the line

print(s.count("o"))        #Count the letter or world in the string

s = "Welcome to python"
print(s.swapcase())     #Convert uppercase characters to lowercase and lowercase characters to uppercase.

