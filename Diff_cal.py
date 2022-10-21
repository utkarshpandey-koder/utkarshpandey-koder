print("1.Square  2.Rectangle 3.Circle")
s=int(input("Choose one of the above : "))
if s>=4:
  print("Enter a Valid Number for above recommendations , Try again !")
#for square
if s==1:
  print('''Choose one of the following : 
  1.Area of Square
  2.Perimeter of Square''')
  os=int(input("Enter the operation you want :"))
  if os>=3:
    print("Enter a valid operation Number !")
  if os==1:
    side=int(input("Enter Side of Square :"))
    print("Area of Square with Side ",side," units is ",(side*side))
  else:
    side2=int(input("Enter side of Square : "))
    print("Perimeter of Square with side ",side2," units is ",(4*side2))
#for rectangle
if s==2:
  print('''Choose one of the following :
  1.Area of Rectangle 
  2.Perimeter of Rectangle''')
  oR=int(input("Enter the Operation you want with Rectangle :"))
  if oR>=3:
    print("Enter a valid operation Number !")
  if oR==1:
    length=int(input("Enter Length of Rectangle :"))
    breadth=int(input("Enter Breadth of Rectangle :"))
    print("Area of Rectangle with Length ",length ,"and Breadth ",breadth , " is ",(length*breadth))
  else:
    l=int(input("Enter Length of Rectangle :"))
    b=int(input("Enter Breadth of Rectangle :"))
    print("Perimeter of Rectangle with Length",l ,"and Breadth", b, "is ",(2*(l+b)))
#for circle
if s==3:
  print('''Choose one of the Following :
  1.Area of Circle
  2.Circumference of Circle''')
  oc=int(input("Enter the Operation you want :"))
  if oc>=3:
    print("Enter a valid operation Number !")
  pi=3.14
  if oc==1:
    r=int(input("Enter Radius of Circle :"))
    print("Area of Circle with Radius ",r," is ",(pi*(r*r)))
  else:
    r2=int(input("Enter Radius of Circle :"))
    print("Circumference of Circle  with Radius ",r2," is ",(2*pi*r2))
