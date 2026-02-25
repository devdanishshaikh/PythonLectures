'''def greet():
  print("Hello, World!")
greet()'''


'''def add(a, b):
  return a + b
result = add(5, 3)
print(result)'''

'''def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))'''

#function using parameters and return value
'''def math(a,b):
  go=a+b
  return go
result=math(10,20)
print("sum :",result)'''


#1. make a function which take 3 input value and gives their average as output
'''def average(a,b,c):
  return (a+b+c)/3
a=input("Enter first number: ")
b=input("Enter second number: ")
c=input("Enter third number: ")

print(average(int(a),int(b),int(c)))'''

#2Lambda Function
'''square = lambda x : x*x
x=int(input("Enter a number: "))
print("Square of",x,"is",square(x))
'''
#3. make a function which find factorial of N number
'''def factorial(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact
n=int(input("ENter Number : "))
print("Factorial of ",n," is ",factorial(n))'''