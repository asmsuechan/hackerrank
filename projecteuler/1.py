import sys

def calc_multiplied_sum(number: int) -> int:
    num = number - 1
    number_of_3 = int(num / 3)
    number_of_5 = int(num / 5)
    number_of_15 = int(num / 15)

    S_n3 = number_of_3 * (2*3 + (number_of_3-1)*3) >> 1 if number_of_3 > 0 else 0
    S_n5 = number_of_5 * (2*5 + (number_of_5-1)*5) >> 1 if number_of_5 > 0 else 0
    S_n15 = number_of_15 * (2*15 + (number_of_15-1)*15) >> 1 if number_of_15 > 0 else 0

    return S_n3 + S_n5 - S_n15

t = int(input().strip())
results = [None] * t
for a0 in range(t):
    n = int(input().strip())
    results[a0] = calc_multiplied_sum(n)

for result in results:
    print(result)
