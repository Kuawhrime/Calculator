#Calculator
number1 = int(input("Give me a number : "))

sigle = input("What type of operation do you want to do? ")

number2 = int(input("Give me a number : "))

#Which sign do you want to choose
if sigle == "+":
    print(number1 + number2)
       
elif sigle == "-":
    print(number1 - number2)
        
elif sigle == "*":
    print(number1 * number2)

#sign "division with zeroDivision Error Solved" 
elif sigle == "/":
    try:
        somme = number1 / number2
        print(somme)
    except ZeroDivisionError:
        print("You can't divide by 0")

#If "sigle" is unknown
else:
    print("Unknown operation")
