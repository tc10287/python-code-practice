#write a function named add_dots that takes a string an adds a dot in be between each word in the string\
#below the add_dots function, write another function named remove_dots that removes all the dots from the string.
# if both the functions are correct, calling remove_dots(add_dots(string)) should return the original string

def add_dots(str):      
    d="."
    str1=d.join(str)      #join function takes a string and returns a string with all the dots in between each word in the string
    return(str1)

def remove_dots(str):
    str1=str.replace(".","")   #replace function takes a string and returns a string with all the dots in between each word in
    return(str1)

print(add_dots("hello"))
print(remove_dots(add_dots("tenzin")))