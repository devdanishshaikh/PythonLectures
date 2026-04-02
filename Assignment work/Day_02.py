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

# Q : 4 :- While loop ka use krke 1 se 10 tak ke numbers print kro
'''num = 1
while (num <=10):
  print(num, end=" ")
  num+=1  '''
# Q : 4 :- While loop ka use krke 1 se 100 ke bech numbers even print krwo print kro
'''num = 1
while (num <= 100):
    if (num % 2 == 0):
        print(num, end=" ")
    num += 1'''

# Q : 5 :- While loop ka use krke mathematic table print krwo
'''while True:
  num = int(input("Enter a number to print its table :"))
  i = 1
  while (i<=10):
    print(f"{num} x {i} = {num*i}")
    i+=1'''


# Q : 6 :- While loop ka use krke 1 se 10 ke bech odd numbers print krwo print kro
'''num = 1
while (num <= 10):
  if (num % 2 == 0):
    num+=1
    continue
  print(num, end=" ")
  num+=1
  '''

# Q : 7 :- For Loop ka use krke 1 se 10 tak ke numbers print kro
'''for i in range(1,11):
  print(i, end=" ")'''


# Q : 8 :- for loop use krke string se vowel print kro
'''name = "Danish ALi Shaikh"
for i in name:
  if (i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i == "O" or i == "u" or i == "U"):
    print(i, end=" ")'''
# same but here only i ko find krke doond rhe hy
'''name = "Artificial Intelligence"
count = 0
for y in name:
  if y == "z" or y == "Z":
    count+=1
print(f"Total number of i in {name} is : {count}")
'''


# Q : 9 :- for loop use krke sum of N numbers find kro
num = int(input("Enter a number :"))
sum = 0
for i in range(1,num+1):
  sum+=i
print(f"Sum of first {num} numbers is : {sum}")


# Q : 10 :- Prime Number Check (For Loop)
# Title: User se number input lo aur check karo prime hai ya nahi
number = int(input("Enter a number to check prime: "))

if number <= 1:
  print("Not a prime number")
else:
  is_prime = True
  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      is_prime = False
      break

  if is_prime:
    print("Prime number")
  else:
    print("Not a prime number")