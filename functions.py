# init a function
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"



name = full_name("Ted", "cruz")
print(name)

# default parameter values
def increment(number, increment_value=3):
    return number + increment_value

print(increment(5))

# multiple number of params
def multiply(*numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply(2,4,6,8,10))

# multiple number of params using **

def user_details(**user):
    return print(user)

user_details(id=1,name="Ted Cruz" , gender= "male")

# exercise

def fizz_buzz(input):
    if input % 3 == 0  and input % 5 == 0:
        print("fizzBuzz")
    elif input % 3 == 0:
        print("fizz")
    elif input % 5 == 0:
        print("buzz")
    else:
        print(input)


fizz_buzz(25)