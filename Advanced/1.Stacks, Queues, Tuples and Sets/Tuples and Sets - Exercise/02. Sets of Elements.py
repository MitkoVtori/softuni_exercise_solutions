n, m = list(map(int, input().split()))

set_n, set_m = set(), set()

for first_set in range(n):
    num = int(input())
    set_n.add(num)

for second_set in range(m):
    num = int(input())
    set_m.add(num)

print('\n'.join([str(num) for num in set_n.intersection(set_m)]))




# n, m = list(map(int, input().split()))
# print('\n'.join([str(num) for num in set([int(input()) for num in range(n)]).intersection(set([int(input()) for num in range(m)]))]))
