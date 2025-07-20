#string data    to be used in the code

first = "Umar"
second = "Farooq"

# print(type(first))  # Check the type of first variable

# print(type(second) == str)  # Check the type of second variable


#Cosntant variable


pizza = str("Pepponi Pizza")  # String variable

# print(type(pizza))  # Print the pizza variable

# print("Pizza is a string:", type(pizza) == str)  # Check if pizza is a string
# # Print the pizza variable
# print("Pizza is a instance string:", isinstance(pizza, str) ) # Check if pizza is a string


fullname = first + " " + second  # Concatenate first and second with a space
print("Full name:", fullname)  # Print the full name

fullname += "!"  # Append an exclamation mark to the full name

print("Full name with exclamation:", fullname)  # Print the full name with exclamation


#CAsting a number tp string

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from " + decade + "s"
print(statement)  # Print the statement with the decade

multiline = """This is a multiline string.

I was just checking

how are youdoing?
I hope you are doing well.

                         This is the end of the multiline string.""" 

print(multiline)  # Print the multiline string

#Escape characters in strings

setence = "This is a sentence with a \"quote\" inside it."
print(setence)  # Print the sentence with escaped quote

print(first)  # Print first and second variables
print(first.lower())        # Print first variable in lowercase

print(first.upper())        # Print first variable in uppercase     
print(first.capitalize())   # Print first variable with the first letter capitalized            
print(first.title())        # Print first variable with each word capitalized       

print(first.count("a"))  # Count occurrences of 'a' in first variable


print(setence.replace("quote", "quotation"))  # Replace 'quote' with 'quotation' in the sentence
print(setence.find("quote"))  # Find the index of 'quote' in the sentence
print(setence.title())  # Find the index of 'quote' in the sentence (raises error if not found)
print(setence.capitalize())  # Find the index of 'quote' in the sentence (raises error if not found)

print(len(setence))  # Print the length of the sentence