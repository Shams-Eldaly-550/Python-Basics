n1 = float (input ('Enter the first number : '))
Operator = input ('Please enter the operator : ')
n2 = float (input ('Enter the second number : '))


if Operator == '+':
    print ('summation = '+  str(n1 + n2))
elif Operator == '-':
    print ('intersection = '+ str(n1 - n2))
elif Operator == '*':
    print ('product = '+ str(n1 * n2))
elif Operator == '/' :
    if n2 != 0:
        print ('division = ' + str(n1 / n2))
    else:
        print ('cannot divide by 0')
else :
    print ('Operator not supported')
