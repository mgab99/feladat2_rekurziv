#https://cses.fi/problemset/task/1637/
#2. feladat: rekurzio - Removing Digits
#minden tesztesetre mukodik

import sys

input_data = sys.stdin.read().splitlines()
value = int(input_data[0])

def removing_digits(n):
    if n < 1 or n > 10**6:
        return -1
    if len(str(n)) == 1:
        return 1
    else:
        legnagyobb = int()

        for i in str(n):
            if int(i) > legnagyobb:
                legnagyobb = int(i)

        n -= legnagyobb

        return removing_digits(n)+1

print(removing_digits(value))