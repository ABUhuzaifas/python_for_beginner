from asyncio import staggered


fruit_basket="Mangoes"
print(fruit_basket)

#input function
fruit_basket=input(str("what is your favriout fruit? \n"))
print(fruit_basket)

# input function of 2nd stage 
name = input(str("what's your name? \n"))
greetings = 'Hello'
print(greetings, name)

# another way of stage 2 input function 
name = input(str("what's your name? \n"))
print('Hellow', name)

# 3rd stage input function 

name = input(str("what's your name? \n"))
age = int(input("ahow old are you? \n"))
greetings = 'Hello'
print(greetings, name, "you are still young")
