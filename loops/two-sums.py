n = int(input())

left_sum = 0
for i in range(n):
    number = int(input())
    left_sum += number

right_sum = 0
for b in range(n):
    number = int(input())
    right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")