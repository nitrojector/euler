# 67

import os


def addLarge():
    for row in range(len(nums) - 1, 0, -1):
        for col in range(len(nums[row - 1])):
            nums[row - 1][col] += max(nums[row][col], nums[row][col + 1])

f = open(os.path.join(os.path.dirname(__file__), 'p067.in'))
nums = []

for line in f.readlines():
    nums += [[int(x) for x in line.split()]]

addLarge()
print(nums[0][0])
