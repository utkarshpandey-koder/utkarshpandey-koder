a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
print('''Choose the Operation :
1.Addition
2.Substract
3.Multilpy
4.Divide
5.Modulus''')
operation=int(input("Enter Operation No."))
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
if operation==1 :
  print("Addition of both Numbers is : ",c)
elif operation ==2 :
  print("Substraction of Both numbers is : ",d)
elif operation ==3:
  print("Multiplication of both Numbers is :",e)
elif operation==4:
  print("Division of both Numbers is :",f)
else:
  print("Modulus of Given Numbers are :",g)
