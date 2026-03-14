# 1. check username and password
'''username = input("Enter username :")
password = input("Enter your password :")

if username == "admin" and password == "pass":
  print("Successfully login")
elif username != "admin":
  print("invalid username")
else:
  print("invalid password")'''


# 2. check multiple of 5
'''num =int(input("Enter the number"))
if num % 5==0:
  print(num," is the multiple of 5")
else:
  print(num," is not multiple of 5 ")
'''
# 3. check whether number is even or odd
'''num = int(input("Enter number :"))
if num % 2==0:
  print(num, "is even")
else:
  print(num, " is odd")'''

# 4.check username and password using nested if else statement
'''username = input("Enter username : ")
password = input("Enter password : ")

if username == "admin" and password =="pass":
  print("LOGIN SUCCESSFULLY")
else:
  if username !="admin":
    print("Invalid Username....!")
  else:
    print("Invalid Password....!")
'''
# 5. check week day
'''day = int(input("Enter the Number of Day : "))
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Invalid number....!")'''

# 6. Take 2 numbers and an operator from user (+, -, *, /) Use match-case to perform calculation
'''print("=============SIMPLE CALCULATOR============")
num_1 = int(input("Enter the num1 value : "))
num_2 = int(input("Enter the num2 value : "))
op = input("Enter operator (+, -, *, /): ")

match op:
  case "+":
    print("=============Result============")
    print("Sum :", num_1 + num_2)
    print("===============================")
  case "-":
    print("=============Result============")
    print("Subtraction : ", num_1 - num_2)
    print("===============================")
  case "*":
    print("=============Result============")
    print("Multiplication : ", num_1 * num_2)
    print("================================")
  case "/":
    print("=============Result============")
    print("Division : ", num_1 / num_2)
    print("===============================")
  case "%":
    print("=============Result============")
    print("Remainder : ", num_1 % num_2)
    print("===============================")
  case "**":
    print("=============Result============")
    print("Exponential :", num_1  ** num_2)
    print("===============================")
  case _:
    print("Invalid operator")'''

# 7. check the marks and show the grade
'''marks = int(input("Enter your marks : "))

match marks//10:
  case 10|9:
    print("Your Grade is A+")
  case 8:
    print("Your Grade is A")
  case 7:
    print("Your Grade is B")
  case 6:
    print("Your Grade is C")
  case _:
    print("Fail")'''
 
 # 8.Menu Program
'''
1. Tea
2. Coffee
3. Juice
4. Water
'''
'''customer_name =input("Enter Customer name :")
table_no =int(input("Enter customer's table number :"))
order = input("Enter your order :").title()

match order:
  case "Tea":
   size = input("Full or Half? ").title()
   match size:
        case "Full":
            print("Full chai 70 rupees")
        case "Half":
            print("Half chai 40 rupees")
        case _:
            print("Invalid size")
  case "Coffee":
      size = input("Cafechino or normal? ").title()
      match size:
        case "Cafechino":
            print("Cafechino coffee is 700 rupees")
        case "normal":
            print("normal coffee 400 rupees")
        case _:
            print("Not available")
  case "Juice":
    print("Slice Juice is 60 rupees")
    print("Pak_ola Juice is 100 rupees")
    print("Fruit Juice is 300 rupees")
  case "Water":
    print("Aqua_fina half-litre 60 and 1.5 litre 150")
    print("Nestle half 70 and full 180")
  case _:
    print("Invalid Order....Not available")

print("\--- Customer Details ---")
print("Customer Name    : ",customer_name)
print("Customer's Tabel : ",table_no)
print("Order Type       : ", order)
print("Chai Size        :",size)
'''


