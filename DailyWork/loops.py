# 1. print numbers from 1 to 10
'''num = 1
while num <=10:
  print(num)
  num +=1'''

# 2. print any number table
'''num = 1
n=int(input("ENter the table "))
while num <=10:
  print(n, " x ",num, " = ",num*n)
  num +=1'''

# 3.Sum of Numbers
'''temp = 0
count = 1
num= int(input("Enter Number : "))
while count <=num:
  temp = temp + count
  count +=1
print("Sum of  number ", temp)'''

# 4. write code that print 10 9 8 7 ..... 1
'''i=10
while(i>=1):
  print(i, end=" ")
  i=i-1'''

# 5.using break statement which terminate loop when it prints 5
'''i =1
while (i<=10):
  print(i, end=" ")
  if(i==6):
   break
  i=i+1'''

# 6. use continue keyword to print only even numbers
'''
num=1
while(num<=10):
    num=num+1
    if num % 2 ==0:
       continue
    print(num, end=" ")'''

#.7 use for loop and print any name letter sperately
'''name="Danish"
for letter in name:
  print(letter,end="   ")'''

# 8.print all items for array
'''fruits=["Banana", "Orange", "Apple","Pineapple","Peach"]
for fruit in fruits:
  print(fruit, end="  ")'''

# 9. in is used to check presence
'''nam = "Abid"
letter =input("Enter any letter to check is it exist or not in word : ")
if letter in nam:
  print(letter,"this exist in abid")
else:
  print(letter," this Does not exist in abid")'''


# 10 . how to print numbers in sequnce 
'''num =100
for i in range(num):
  print(i, end=" ")
'''

# 11. check and conut the any letter in any word

'''name =input("Enter the word : ")
letter=input("Enter the letter to check how many time it exist in word : ")
count =0
for var in name:
  if letter in var:
    count +=1
  else:
    continue
print(count)'''


# 12. print vowel from a word using for loop

'''name =input("Enter the word : ")
count=0
for var in name:
  if var in "aeiou":
    print(var,end=" ",)
    count+=1

print("\nTotal vowl in word :",count)'''
count=0
for num in range(1,11):
  count+=num

print(count)

  