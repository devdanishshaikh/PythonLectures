#Q1. Write a program that takes as input. Using conditional statements, 
#calculate the final tax rate based on these rules: 
'''If salary < 30,000 → 5% 
• If salary is 30,000–70,000 → 15% 
• If salary > 70,000 → 25% '''
#code part
'''salary =int(input("Enter your Salary: "))
if(salary < 30000):
    tax_rate = (5*salary)/100
    after_tax_salary = salary - tax_rate
elif(salary >=30000 and salary <=70000):
    tax_rate = (15*salary)/100
    after_tax_salary = salary - tax_rate
else:
    tax_rate = (25*salary)/100
    after_tax_salary = salary - tax_rate

print("Your tax rate is: ", tax_rate)
print("Your salary after tax is: ", after_tax_salary)'''

#Q2. Write a function that takes two integers and and prints all even 
#numbers between them (inclusive). 
'''def even(a,b):
  for i in range(a,b+1):
    if(i%2==0):
      print(i, end=" ")
a= int(input("ENter the first number: "))
b= int(input("ENter the second number: "))
even(a,b)'''

 
'''Q3. Write a function that prints the digits of a number, . 
For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them. 
 
 
[Hint - The right most digit of a number N is N%10. 
And to remove the right most digit from a number, we can do N = N / 10.] '''
  
'''def count_digit(n):
  if(n==0):
    return 1
  count =0
  while(n>0):
    n=n//10
    count+=1
  return count
n=int(input("Enter a number :"))
print("The number of digits in the number is: ", count_digit(n))'''


#Q5. Write a function to return the sum of digits of a number, . 
'''def sum_of_digits(n):
  sum=0
  while(n>0):
    r=n%10
    sum=sum+r
    n=n//10
  return sum
n=int(input("Enter a number :"))
print("The sum of digits in the number", n, "is :", sum_of_digits(n))'''

#.Write a program that print 1 to 100 divisible by 3 and 5

'''for i in range(1,100):
  if(i%3==0 and i%5==0):
    print(i, end=" ")'''

'''Design a program to continuously input a number from user & print if it is 
positive or negative until the user enters “Quit”.'''

'''message = (input("Enter a number or type 'Quit' to exit: "))
while(message!="Quit"):
  if(int(message)>0):
    print("The number is positive")
  elif(int(message)<0):
    print("The number is negative")
  else:
    print("The number is zero")
  message = (input("Enter a number or type 'Quit' to exit: "))'''

# create a simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division. The program should take two numbers and an operator as input from the
'''def calculator(num1, num2, operator):
  if(operator=="+"):
    return num1+num2
  elif(operator=="-"):
    return num1-num2
  elif(operator=="*"):
    return num1*num2
  elif(operator=="/"):
    if(num2!=0):
      return num1/num2
    else:
      return "Error: Division by zero is not allowed."
  else:    return "Error: Invalid operator. Please use +, -, *, or /."
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))  
operator = input("Enter the operator (+, -, *, /): ")
result = calculator(num1, num2, operator)
print("The result is:", result)'''

#Q10. Letʼs create a “Number Guessing Game”. Given a secret number (already 
#decided by you), write a program that asks the user to guess it and prints: 
#“Too low” if the userʼs guess is less than the secret number, 
#“Too high” if the userʼs guess is greater than the secret number, and  
#“Congratulations! You guessed the number.” if the userʼs guess is correct.
'''secret_number = 42
guess = int(input("Guess the secret number: "))
while guess != secret_number:
    if guess < secret_number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess the secret number: "))
print("Congratulations! You guessed the number.")'''

