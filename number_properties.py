# Number properties Checker

user_number = int(input("Enter number"))

if user_number % 2 == 0:
    print(f"{user_number} is even")
else:
    print(f"{user_number} is odd")

# check prime number

for i in range(2, user_number):
    if user_number % i == 0:
        print(f"{user_number} is not prime")
        break
else:
    print(f"{user_number} is prime")

# check number is a square number

for i in range(1, user_number):
    if i * i == user_number:
        print(f"{user_number} is a square number")
        break
else:
    print(f"{user_number} is not a square number")

