for number in range(4):
    print(f"Number attempted is {number}")

# for loops

for char in "hello":
    print(char)

# for else

successful = False
attempt = 0
for number in range(1,4):
    print("Attempt")
    attempt = number
    if successful:
        print("successfully process")
        break
else:
    print(f"Attempt not successful after {attempt}")

name = "rado"
# nested loop
for x in range(len(name)):
    for y in range(2):
        print(f"({x},{y})")

command = ""
# while loop
while command != "Q":
    command = input(f"ECHO : ")


# exercise
even_number = 0
for x in range(1,10):
    if x % 2 == 0:
        print(x)
        even_number +=1
print(f"We have {even_number} even number in the range")

