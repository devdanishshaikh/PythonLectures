# Q : 1   Sum of Two number take input from user
'''num1 = int(input("Enter the value of num1 :"))
num2 = int(input("Enter the value of num2 :"))
sum = num1 + num2
print("Sum of two numbers :", sum)'''

# Q : 2   Area of Rectange take input from user
'''length = float(input("Enter the length of rectangle :"))
width = float(input("Enter the width of rectangle :"))
area = length * width
print("Area of rectangle :", area)'''

# Q : 3 Find the simple interest take input from users prinicpal(original amount) ,rate(kitna percent per year hoga), time
'''principal = int(input("Enter the original amount :"))
rate  = float(input("Enter the interset percentage per year :"))
time = int(input("Enter the Time :"))
SI = (principal * rate * time) / 100
print("Principal :",principal)
print("Rate      :",rate,"%")
print("Time      :",time,"year")
print("Simple Interest :",SI)'''

# Q : 4 Even or Odd :- User se number lo aur check karo even hai ya odd.
'''num = int(input("Enter a number :"))
if (num % 2 ==0):
  if (num > 0):
    print(num,"is a positive Even number")
  else:
    print(num,"is a negative Even number")
else:
  if (num > 0):
    print(num," is a positive odd number")
  else:
    print(num, "is a negative odd number")'''

# Q : 5 User se 2 numbers lo aur batao kaunsa number bada hai.
'''num1 = int(input("Enter the value of num1 :"))
num2 = int(input("Enter the value of num2 :"))
if (num1 > num2):
  print(num1, " is bigger than ", num2)
elif (num2 > num1):
  print(num2, " is bigger than ", num1)
else:
  print("Both number are equal")
'''

# Q : 6  User se name aur age input lo aur print karo: Hello Ali, you will be 25 next year
name = input("Enter your name :")
age = int(input("Enter your age :"))
print("Hello", name + ", you will be", age + 1, "next year")

# Q : 7  User se number lo aur uska square print karo.
'''num = int(input("Enter a number :"))
square = num * num
print("Square of", num, "is :", square)'''

# Q : 8  User se temperature Celsius me lo aur Fahrenheit me convert karo.
'''celsius = float(input("Enter temperature in Celsius :"))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit :", fahrenheit)'''