import math, re

text = open("input.txt").read()


# Part 1
matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)
result = sum(
    math.prod(map(int, x[4:-1].split(",")))
    for x in matches
)

print(result)


# Part 2
matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\))", text)

result = 0
counting = True
for m in matches:
    if m == "don't()":
        counting = False
    elif m == "do()":
        counting = True
    elif counting:
        result += math.prod(map(int, m[4:-1].split(",")))

print(result)
