'''marks =[10,99,23,45,67,89,90]
marks.append(100)
marks.insert(2, 50)
marks.remove(45)
marks.pop(0)
marks.reverse()
print(len(marks))
print(marks[2:6])'''


# =============================================
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
    print(f"Second Largest: {find_second_largest(test4)}")  # Expected: 34