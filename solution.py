s = input()

summ = 0
counter = 0

for i in range(len(s)):
    if ord('0') <= ord(s[i]) <= ord('9'):
        print(s[i])
        summ += int(s[i])
        counter += 1

print(summ / counter)
