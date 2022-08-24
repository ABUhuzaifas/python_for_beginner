# logical operator are either "true or false" or "yes or no" or "0 or 1".
# equal to operator               ==
# not equal to operator           !=
# less than operator              <
# greater than operator           >
# less than or equal to operator  <=
#greater than or equal to operator>=
# is 4 equal to 4?
from ast import operator

from numpy import int0, logical_and


print(4==4) # equal to operator
print(4!=4) # not equal to operator
print(4>3) # less than
print(3>6) # less than
print(3<=5) # less than or equal to operator
print(5>=4) # greater than or equal to operator

# application of logical operatore
huzaifa_age=4
age_at_school=5
print(huzaifa_age==age_at_school) # equal to example

# input operator and logical
age_at_school=5
huzaifa_age=int(input("How old are you? \n"))
print(huzaifa_age>=age_at_school)