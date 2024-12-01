pairs = [map(int, x.split()) for x in open('input.txt').read().splitlines()]

left, right = zip(*pairs)
left, right = sorted(left), sorted(right)

answer = sum(abs(x - y) for x, y in zip(left, right))

print(answer)

answer2 = sum(x * right.count(x) for x in left)

print(answer2)
