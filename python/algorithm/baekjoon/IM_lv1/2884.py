# import sys

# input = sys.stdin.readline
# n = int(input().strip())

# for _ in range(n):
#     line = input().strip()
#     input_value = list(map(int, line.split()))
#     hour = input_value[0]
#     minute = input_value[-1]

#     if hour+1 <= 23:
#         if (minute-45) >= 0:
#             print(f"{hour} {minute-45}")
#         elif (minute-45) < 0:
#             print(f"{hour} {minute+15}")
#     elif (hour+1) == 24:
#         if (minute-45) >= 0:
#             print(f"{hour-24} {minute-45}")
#         elif (minute-45) < 0:
#             print(f"{hour-24} {minute+15}")

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
