'''
解説
inputで与えられた複数の数のうちで最大のものだけに関して、その数までのフィボナッチ数の配列を求める。この配列を使って他の結果も求める。
メモ化再帰のフィボナッチ数列はここを参照。https://qiita.com/takey/items/4b1767af0f0652ef8764
'''

import sys
from typing import List

#def fibo(num: int) -> int:
#    if (num == 0): return 0
#    if (num == 1): return 2
#    return 4*fibo(num - 1) + fibo(num - 2)

def even_fibo_memo(n):
    memo = [0]*(n+1)

    def _fib(n):
        if n == 0: return 0
        if n == 1: return 2
        if memo[n] != 0:
            return memo[n]
        memo[n] = 4*_fib(n-1) + _fib(n-2)
        return memo[n]

    return _fib(n)

#for i in range(10):
#    print(even_fibo_memo(i))

def fibo_array(n: int) -> List[int]:
    results = []
    for i in range(n):
        fibo = even_fibo_memo(i)
        if fibo > n: break
        results.append(even_fibo_memo(i))
    return results

def even_fibo_sum(nums: List[int]) -> int:
    max_num = max(nums)
    fibo_sequence = fibo_array(max_num)
    results = [0]*len(nums)
    for i in range(len(nums)):
        for fibo in fibo_sequence:
            if fibo > nums[i]: break
            results[i] += fibo

    return results

    #fibo_sequence = []
    #sum = 0
    #for i in range(n+1):
    #    f = even_fibo_memo(i)
    #    if f > n: break
    #    if f % 2 == 0: sum += f
    #return sum

t = int(input().strip())
numbers = [0]*t
for a0 in range(t):
    n = int(input().strip())
    numbers[a0] = n

for result in even_fibo_sum(numbers):
    print(result)
