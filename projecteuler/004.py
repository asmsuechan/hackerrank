from copy import deepcopy
import pdb

def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

def separate_2_three_digits_number(num: int) -> bool:
    result = False
    for i in range(100, 1000):
        if num % i == 0 and len(str(int(num / i))) == 3:
            result = True
            break
    return result

def check(num: int) -> int:
    result = 0
    for n in range(num - 1, 101100, -1):
        if is_palindrome(n):
            if separate_2_three_digits_number(n):
                result = deepcopy(n)
                break
    return result

t = int(input().strip())
results = [0]*t
for a0 in range(t):
    n = int(input().strip())
    results[a0] = check(n)

for result in results:
    print(result)
