# ==================================
# List Example - Problem 4
# ==================================
# Find even numbers from a list

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

print("Even numbers:", even_nums)
