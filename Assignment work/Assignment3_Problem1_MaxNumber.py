# ==================================
# List Example - Problem 1
# ==================================
# Find maximum number in a list

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num

print("max_num:", max_num)
