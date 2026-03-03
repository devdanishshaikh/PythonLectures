'''marks =[10,99,23,45,67,89,90]
marks.append(100)
marks.insert(2, 50)
marks.remove(45)
marks.pop(0)
marks.reverse()
print(len(marks))
print(marks[2:6])'''


'''# =============================================
# Problem: Find the Second Largest Element in a List
# =============================================

def find_second_largest(numbers):
    """
    Find the second largest element in a list of numbers.
    Returns None if the list has fewer than 2 unique elements.
    """
    if len(numbers) < 2:
        return None

    unique_numbers = list(set(numbers))  # Remove duplicates

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)
    return unique_numbers[1]


# --- Test Cases ---
if __name__ == "__main__":
    test1 = [10, 99, 23, 45, 67, 89, 90]
    print(f"List: {test1}")
    print(f"Second Largest: {find_second_largest(test1)}")  # Expected: 90

    test2 = [5, 5, 5, 5]
    print(f"\nList: {test2}")
    print(f"Second Largest: {find_second_largest(test2)}")  # Expected: None

    test3 = [3, 1]
    print(f"\nList: {test3}")
    print(f"Second Largest: {find_second_largest(test3)}")  # Expected: 1

    test4 = [12, 35, 1, 10, 34, 1]
    print(f"\nList: {test4}")
    print(f"Second Largest: {find_second_largest(test4)}")  # Expected: 34'''

'''    # =============================================
    # Problem: Slicing a list
my_list = [10, 20, 30, 40, 50, 60, 70]
sliced_list = my_list[1:4]  # This will include elements at index 2, 3, and 4
print(sliced_list)  # Output: [30, 40, 50]'''



# =============================================
# All list Methods
# =============================================
'''marks=[10,20,30,40,50,60,70]
print(marks)
marks.append(80)
print(marks)
marks.insert(0,7)
print(marks)
marks.remove(20)
print(marks)
marks.pop(3)
print(marks)
marks.reverse()
print(marks)
print(len(marks))
print(marks[2:6])'''

'''marks=[10,20,30,40]
x=int(input("Enter the element to search: "))
index=0
for val in marks:
  if val==x:
    print(f"Element {x} found at index {index}")
    break
  index+=1'''

'''tup=(1,2,3,4,5,6,7,8,9,10)
sum=0
for val in tup:
  if val%2==0:
    sum+=val
print(f"Sum of elements in tuple: {sum}")'''