def sum_n(n):
    return n * (n + 1)//2
print("sum of the first n number s (n=5):", sum_n(5))

def array_sum(a):
    total=0
    for i in a :
        total +=i
    return total
a=[12,3,4,15]
print("array sum:",array_sum(a))


def summ(n):
    if n <= 0:
        return 0
    return 0 + summ(n - 1)
print("recursive sum (n=5):",summ(5))