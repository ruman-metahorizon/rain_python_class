first_number = float(input("Enter your first number : "))
second_number = float(input("Enter your second number : "))

user_choice = input("""
           Please choose you option
                + for Addition
                - for Subtraction         
                    
                    """)
if user_choice == "+":
    print("Addition = ", first_number + second_number)
elif user_choice == "-":
    print("Subtraction = ", first_number - second_number)
else:
    print("Invalid option")

