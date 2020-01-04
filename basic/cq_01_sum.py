i = 0
result = 0

while i <= 100:
    # even number i % 2 == 0
    # uneven number i % 2 != 0
    if i % 2 == 0:
        result += i
    i += 1
print("sum of even number from 0~100 = {0}".format(result))