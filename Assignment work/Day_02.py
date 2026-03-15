# Q : 1 User se age input lo or check kro agr age 13 se kam hy to child agr 13 se 18 hy to teenager aur 18 se zyda hy to adult
'''age = int(input("enter your age :"))
if (age < 13):
  print("you are child....")
elif (age >=13 and age <=18):
  print("You are teenager...")
else:
  print("you are adult...")'''

# Q : 2 user se username or password lo input m or check kro agr sahi dala hy to login successfully agr nahi to check kro konsi galt dale hy username ya passsword

'''username = input("Enter your username :")
password = input("Enter your password :")

if( username == "admin" and password =="admin124"):
  print("Login Successfully...")
elif (username != "admin" and password =="admin124"):
  print("incorrect username...")
elif (username == "admin" and password !="admin124"):
  print("incorrect password...")
else:
  print("Both are incorrect...")'''

# Q : 3 :- Student ke marks input lo.Agar marks ≥ 50 ho, check karo marks ≥ 80, agar haan → "Grade A", warna → "Pass", Agar marks < 50 → "Fail"

'''marks = int(input("Enter your marks :"))
if(marks >=50):
  if(marks >=80):
    print("Grade A")
  else:
    print("Pass")
else:
  print("Fail")'''