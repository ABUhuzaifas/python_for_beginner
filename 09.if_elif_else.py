required_age_at_school = 5
huzaifa_age = int(input("Please enter your age! "))

# 01:question 
# can huzaifa go to school?
if huzaifa_age == required_age_at_school:
    print("cngradulations!huzaifa can join the school")
elif huzaifa_age > required_age_at_school:
    print("huzaifa should go to higher secondary  school")
elif huzaifa_age == 2:
    print("you should take care of huzaifa, he is still a baby!")  
else:
    print("huzaifa can't go to school")