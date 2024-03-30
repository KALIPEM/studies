
firstname = input("Enter your firstname: ")  #here firstname is declared as a variable and input is used to get input from the user, same is for lastname, age and occupation.
lastname = input("Enter your lastname: ")
age= int(input("Enter your age: "))
occupation = input("Enter your occupation: ")
print(firstname + " " + lastname + " is " + str(age) + " years old and works as a " + occupation)

#This can also be printed as:
print(f"{firstname} {lastname} is {age} years old and works as a {occupation}.") #try running this code and see if you get the same results as above.

#given below is the way you will be able to write a multiple lined comment just like this one whereas this is a single lined comment .
"""_
This is a multiple lined comment!!
"""
#keywords

name = "Ankit"
print("m" in name) #this will print True if m is present in name and False if it is not. You can use this to check if a character is present in a string.


print(name.find("kit")) #this will print the index of the character kit in the string name and if it doesn't find it will print -1.
print(name.replace("k", "j")) #this will replace the character k with K in the string name.
print(name.upper()) #this will convert all the characters in the string name to uppercase.
print(name.lower()) #this will convert all the characters in the string name to lowercase.
print(name.title()) #this will convert the first character of each word in the string name to uppercase.
print(name.capitalize()) #this will convert the first character of the string name to uppercase.


#operators in python
num1 = 5
num2 = 10

sum = num1 + num2
product = num1 * num2
remainder = num1 % num2
division = num1 / num2
divisioninteger = num1 // num2
power = num1 ** num2
print(sum, product, remainder, division, divisioninteger, power)