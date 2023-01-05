import inflect
def stars(n=100):
  for i in range(100):
    print("*",end="")
print( "\n               Welcome To My Quiz Game !    ")
stars()
print("\nTotal Winning Amount of This Game is 20 Cr.")
stars()
start=input("\nPress Enter to Start the QUIZ Game :")
stars()
name=input("\nPlease Enter Your Name:")
stars()
print(f"\nWelcome {name},Lets Start the Game !!")
stars()
prize=0
print("\nQuestion No.1(For 1 Lakh Rs.):")
print("1.What is the output of the following code? print(type({}))\na.<class 'list'>     b.<class 'set'>\nc.<class 'tuple'>    d.<class 'dict'>")
a1=input("Enter the Correct Option: \n")
if a1== "d" or a1=="D":
  prize=+100000
  print(f"You are correct ,\nYour Total Prize ={prize}")
else:
  prize+=0
  print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
print("\nQuestion 2(For 500000 Rs.):")
print("Which of the following operators is used to add elements at the end of list?\na.add()       b.join()\nc.attach()    d.append()")
 
a2=input("Enter the Correct Option:\n")
if a2=="d" or a2=="D":
  prize+=500000
  print(f"You are Correct ,\nYour Total Prize = {prize}")
else:
  prize+=0
  print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
print("\nQuestion 3(For 14 Lakh Rs.):")
print("3.Which of the following cannot be a Python variable name?\na.Int_1     b.true\nc.var-2     d.name3\nEnter the Correct Option:")
a3=input()
if a3=="c"or a3=="C":
  prize+=1400000
  print(f"You are Correct ,\nYour Total Prize = {prize}")
else:
  prize+=0
  print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
print("\nQuestion 4(For 30 Lakh Rs.):")
print("4.Which of the following is not a Python Data Type?\na.int     b.string\nc.char    d.set\nEnter the Correct Option:")
a4=input()
if a4=="c"or a4=="C":
  prize+=3000000
  print(f"You are Correct ,\nYour Total Prize = {prize}")
else:
  prize+=0
  print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
print("\nQuestion 5(For 50 Lakh Rs.).\nnum=4+0j\nprint(type(num))\na.int       b.float\nc.complex   d.real")
a5=input()
if a5=="c"or a5=="C":
  prize+=5000000
  print(f"You are Correct ,\nYour Total Prize = {prize}")
else:
  prize+=0
  print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
print("\nQuestion 6(For 1 Cr. Rs.).\nWhich of the following statements is used to create an empty set in Python?\na) ( )     b) [ ]\nc) { }      d) set()")
a6=input()
if a6=="d"or a6=="D":
  prize+=10000000
  print(f"You are Correct ,\nYour Total Prize = {prize}")
else:
  prize+=0
  print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
print("\nQuestion 7(For 1 Cr. Rs.).\nWhat will be the output of the following Python code?\n>>>list1 = [1, 3]\n>>>list2 = list1\n>>>list1[0] = 4\n>>>print(list2)\na) [1, 4]      b) [1, 3, 4]\nc) [4, 3]     d) [1, 3]")
a7=input()
if a7=="c"or a7=="C":
  prize+=10000000
  print(f"You are Correct ,\nYour Total Prize = {prize}")
else:
  prize+=0
  if prize<10000000:
    print(f"Wrong answer ,\nYour Total Prize = {prize}")
  if prize==10000000:
    print(f"Wrong answer ,\nYour Total Prize = {prize}/1 Cr.")
  if prize==20000000:
    print(f"Wrong answer ,\nYour Total Prize = {prize}/2 Cr.")
stars()
print("\nQuestion 8(For 2 Cr. Rs.).\nWhat will be the output of the following Python program?\ni = 0\nwhile i < 5:\n  print(i)\n  i += 1\nif i == 3:         \n  break\nelse:\n  print(0)\na) error    b) 0 1 2 0\nc) 0 1 2    d) none of the mentioned")
a8=input()
if a8=="d"or a8=="D":
  prize+=20000000
  print(f"You are Correct ,\nYour Total Prize = {prize}")
else:
  prize+=0
  print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
print('''\nQuestion 9(For 5 Cr. Rs.).\n What will be the output of the following Python code?
i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2
a) 2 4 6 8 10 …
b) 2 4
c) 2 3
d) error''')
a9=input()
if a9=="b"or a9=="B":
  prize+=50000000
  print(f"You are Correct ,\nYour Total Prize = {prize}")
else:
  prize+=0
  print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
print("\nQuestion 10(For 10 Cr. Rs.).\n_________,I'm a Good Person.\nEnter the Correct Option:\na)Yes \nb)Maybe\nc)ofcourse\nd)No")
a10=input()
match a10:
  case "a":
    prize+=100000000
    print(f"You are Correct ,\nYour Total Prize = {prize}")
  case "b":
    prize+=100000000
    print(f"You are Correct ,\nYour Total Prize = {prize}")
  case "c":
    prize+=100000000
    print(f"You are Correct ,\nYour Total Prize = {prize}")
  case "d":
    prize+=100000000
    print(f"You are Correct ,\nYour Total Prize = {prize}")
  case "A":
    prize+=100000000
    print(f"You are Correct ,\nYour Total Prize = {prize}")
  case "B":
    prize+=100000000
    print(f"You are Correct ,\nYour Total Prize = {prize}")
  case "C":
    prize+=100000000
    print(f"You are Correct ,\nYour Total Prize = {prize}")
  case "D":
    prize+=100000000
    print(f"You are Correct ,\nYour Total Prize = {prize}")
  case _:
    prize+=0
    print(f"Wrong answer ,\nYour Total Prize = {prize}")
stars()
stars()
p=inflect.engine()
p=p.number_to_words(prize)
print(f"\nCongratulations,{name}! You completed the Game ,\nYour Total Winning Amount is {prize}\nIn Words: {p}\nThanks For Participating !")


  











