
def input_number():
    try:
        number1 =int(input("Please enter a number from 1 - 20: "))
    except:
        print("Not and integer")
        return -1
    while number1 < 1  or number1 > 20:
        print("value out of range")
        input_number()
def input_numberx():
    try:
        number2 =int(input("Please enter a number from 1 - 20: "))
    except:
        print("Not and integer")
        return -1
    while number2 < 1  or number2 > 20:
        print("value out of range")
        input_numberx()

        
value = input_number()

while value == -1:
    value = int(input_number())
        

valuex = input_numberx()

while valuex == -1:
    valuex = int(input_number())




x = 1
for x in range(1, valuex+1):
    anw = value * x;
    x = x + 1;
    print(anw);

    
    

