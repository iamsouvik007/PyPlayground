
# a = True 
# print(a=False)
# # Error

a = True
print(a := False) # Warlus operator
# Output: False

# The warlus operator (:=) is used to assign a value to a variable as part of an expression. In this case, it assigns False to the variable a and then prints the value of a, which is now False.

print(x:=10)



n = len("Python")
print(n) # Output: 6

print(n:= len("Python")) 




text = "Hello, World!"
n = len(text)
if n > 5:
    print(n)

text = "Hello, World!"
if (n:= len(text)) > 5:
    print(n) 


    

name = input("Enter name: ")

while name != "quit":
    print("Hello", name)
    name = input("Enter name: ")


while (name := input("Enter name: ")) != "quit":
    print("Hello", name)





