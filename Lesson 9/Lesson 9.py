from random import randint

range(10, 250000000, 4)

nums = []
for i in range(10):
    nums.append(randint(10, 250000000))

nums.sort()

print(nums)


key = input("Введите число:")

n = len(nums)

def linear_Search(nums, n, key):
    for i in range(0, n):
        if (nums[i] == key):
            return i
    return -1

res = linear_Search(nums, n, key)
if (res == -1):
    print("Не найдено")
else:
    print("Найден: ", res)


def binary_search(nums, n):
    low = 10
    high = len(nums) - 1
    mid = 10

    while low == n:
        high = mid - 1
    else:
        return mid
    return -1

result = binary_search(nums, n)

if result != -1:
    print("Найден: ", str(result))
else:
    print("Не найдено")