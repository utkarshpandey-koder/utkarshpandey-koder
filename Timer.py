import time
x=int(input("Enter the Time in Seconds :"))
for i in range(x , 0 ,-1):
  seconds=i%60
  minutes=int(i/60)%60
  hours=int(i/3600)
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)
print("Time Up !")