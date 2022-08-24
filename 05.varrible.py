# varrible: object containing specific value 
from re import A, X

from numpy import number


x = 5 #numeric/integer value
print(x)

y = ('we are learning python with ammar') #string_value
print(y)

x = x+10 #or x=15
print(x)

# type/class of varriable
type(x)
print(type(y)) #print_type_class

# Rule to assign a varriable
# 1. The varriable should contain letter,number,underscore
# 2. Do not start with number / do not start with underscore
# 3. Spaces are not allowed 
# 4. Do not use keyword used in function(break,mean,text,try,etc)
# 5.Short and descriptive
# 6.Case sentivity(lowercase,upercase, letter lowercase letter should be used )
a_b = 1
print(a_b)

fruit_basket = 8
fruit_basket = 'Mangoes'
print(type(fruit_basket))
print(fruit_basket)
del fruit_basket # del is used to delete varriable