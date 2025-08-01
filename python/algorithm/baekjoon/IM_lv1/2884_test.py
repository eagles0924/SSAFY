# import sys

# input = sys.stdin.readline
n = list(map(int, input().split()))

hour = n[0]
minute = n[-1]

if hour != 0:
    if (minute-45) >= 0:
        print(f"{hour} {minute-45}")
    elif (minute-45) < 0:
        print(f"{hour-1} {minute+15}")
elif hour == 0:
    if (minute-45) >= 0:
        print(f"{hour} {minute-45}")
    elif (minute-45) < 0:
        print(f"{hour+23} {minute+15}")
