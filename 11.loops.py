# while and for loops
# while loops
from pyrsistent import b


x=0
while(x<=5):
    print(x)
    x=x+1

# for loops
for x in range(4,11):
    print(x)      

days = ['mon','tue','wed','thu','fri','sat','sund']


for d in days:
    # if (d=='fri'):break  # loops stop here
    if (d=='fri'):continue # loops skip here    
    print(d)
