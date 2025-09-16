count = 0

for i in range(1, 10001):
    divisible_by_3 = (i % 3 == 0)
    divisible_by_5 = (i % 5 == 0)

    if divisible_by_3 and divisible_by_5:
        pass
    elif divisible_by_3 or divisible_by_5:
        count += 1

print(count)
