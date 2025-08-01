import sys

input = sys.stdin.readline
n = int(input().strip())

for _ in range(n):
    line = input().strip()
    parts = list(map(int, line.split()))
    N = parts[0]
    scores = parts[1:]

    avg_score = sum(scores) / N
    above_avg = 0
    for score in scores:
        if score > avg_score:
            above_avg += 1
    print(f"{round(above_avg/N*100, 3)}%")
