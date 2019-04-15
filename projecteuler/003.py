from math import sqrt

def isprime(n):
    if n<2:
        return False
    for m in range(2, int(sqrt(n)+1)):
        if n%m==0:
            return False
    return True

def alg(n: int) -> int:
    if isprime(n):
        return n

    if n == 1:
        return 2
    if n % 2 == 0:
        return alg(n >> 1)
    else:
        for i in range(3, int(sqrt(n)+1), 2):
            if n % i == 0:
                return alg(int(n/i))

t = int(input().strip())
results = [0]*t
for a0 in range(t):
    n = int(input().strip())
    results[a0] = alg(n)

for result in results:
    print(result)
