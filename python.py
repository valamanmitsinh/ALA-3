str = "Hello World"
count = 0

for c in str:
    if c in "aeiouAEIOU":
        count += 1

print("Vowels =", count)