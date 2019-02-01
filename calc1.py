print('CALCULATOR')
a = float(input('Enter the number 1:'))
b = float(input('Enter the number 2:'))
print("Type '1' for addition \n Type '2' for substration \n Type '3' for multiplication \n Type 4 'div' for divion \n")
c = str(input("Enter your Actions:"))
if c == 'add':
    print('The answer is', str(a + b))
elif c == 'sub':
    print('The answer is', str(a-b))
elif c == 'mul':
    print('The answer is', str(a*b))
elif c == 'div':
    print('The answer is', str(a//b))
