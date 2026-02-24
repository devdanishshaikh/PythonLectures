def greet():
  print("Hello, World!")
greet()


def add(a, b):
  return a + b
result = add(5, 3)
print(result)

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))