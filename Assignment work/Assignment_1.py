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
def even(a,b):
  for i in range(a,b+1):
    if(i%2==0):
      print(i)
a= int(input("ENter the first number: "))
b= int(input("ENter the second number: "))
even(a,b)