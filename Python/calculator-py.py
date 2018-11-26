## FUNCTIONS ##
#add 2 numbers
def add(x,y):
    return x + y

#subtract 2 numbers
def subtract(x,y):
    return x - y

#multiply 2 numbers
def multiply(x,y):
    return x*y

#divide 2 numbers
def divide(x,y):
    return x/y

print('Choose your operation')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

#get user input
choice = input('Enter 1,2,3 or 4 to select')

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

if choice == '1':
    print(number1, '+', number2, '=', add(number1,number2))

elif choice =='2':
    print(number1, '-', number2, '=', subtract(number1,number2))

elif choice =='3':
    print(number1, 'x', number2, '=', multiply(number1,number2))

elif choice=='4':
    print(number1, '/', number2, '=', divide(number1,number2))

else:
    print('Invalid selection. Try again')
