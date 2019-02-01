print('CALCULATOR')
a = float(input('Enter the number 1:'))
b = float(input('Enter the number 2:'))
print("Type 'add' for addition \n Type 'sub' for substration \n Type 'mul' for multiplication \n Type 'div' for divion \n")
c = str(input("Enter your Actions:"))
if c == 'add':
    print('The answer is', str(a + b))
elif c == 'sub':
    print('The answer is', str(a-b))
elif c == 'mul':
    print('The answer is', str(a*b))
elif c == 'div':
    print('The answer is', str(a//b))
    
