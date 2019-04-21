from typing import List
from math import sqrt

def isprime(n):
    if n<2:
        return False
    for m in range(2, int(sqrt(n)+1)):
        if n%m==0:
            return False
    return True

def prime_numbers(number: int) -> List[int]:
    _prime_numbers = []
    for i in range(number + 1):
        if isprime(i):
            _prime_numbers.append(i)
    return _prime_numbers

def smallest_multiple(number: int) -> int:
    mul = 1
    _prime_numbers = prime_numbers(number)
    for prime in _prime_numbers:
        mul *= prime

        # 2^5 = 32 < 40
        for i in range(1, 5):
            pow = prime**(i+1)
            if pow <= number:
                mul *= prime

    return mul

t = int(input().strip())
results = [0]*t
for a0 in range(t):
    n = int(input().strip())
    results[a0] = smallest_multiple(n)

for result in results:
    print(result)
