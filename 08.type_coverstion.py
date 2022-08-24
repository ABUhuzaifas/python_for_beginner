# type of conversion function
x = 10               # type integer
y = 10.2             # type float
z = 'hello world'    # type string

# impilicit type conversion function
x = x+y # if you multiply any number with float it will always in form of float
print(x, 'the type of class',type(x)) # example: float

# explicit type conversion function
age = input('what is your age?  ') 
print(age, type(int(age))) # example of integer
age = int(age) # convert into any type(str,int,float)

# name
name = input('what is your name? ') 
print(name, type(str(name))) # example of string