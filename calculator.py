print("~~~~~~~~~~Mini Calculator~~~~~~~~~")

num1 = float(input("Enter a first number here: "))
num2 = float(input("Enter a second number here: "))

print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")

choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    print("The addition of the number is", num1+num2)
elif choice == 2:
    print("The substraction of the number is", num1-num2)
elif choice == 3:
    print("The multiplication of the number is", num1*num2)
elif choice == 4:
    print("The division of the number is", num1/num2)
else:
    print("Invalid input")








