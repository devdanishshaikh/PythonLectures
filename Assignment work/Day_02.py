# Q : 1 User se age input lo or check kro agr age 13 se kam hy to child agr 13 se 18 hy to teenager aur 18 se zyda hy to adult
age = int(input("enter your age :"))
if (age < 13):
  print("you are child....")
elif (age >=13 and age <=18):
  print("You are teenager...")
else:
  print("you are adult...")