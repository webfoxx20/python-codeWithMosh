# conditional statement
from pyexpat.errors import messages

temperature = 26

if temperature > 30:
    print("the weather is hot")
elif temperature > 25:
    print("the weather is warm")
else:
    print("the weather is cold")
print("done checking the weather.")


# tenary operator

age = 25
message = "eligible" if age >= 18 else "uneligible"
print(message)

# chaining comparism operator
if 20 <= age < 40:
    print(" you're eligble to pertake in the drill.")
else:
    print("you're not eligible to pertake in the drill")


print("bag" > "apple")


