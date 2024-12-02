from itertools import pairwise

reports = [
    list(map(int, x.split()))
    for x in open('input.txt').read().splitlines()
]

def check_report(report):
    pairs = pairwise(report)
    diffs = [x - y for x, y in pairs]

    if all(x > 0 and x <= 3 for x in diffs):
        return 1
    if all(x < 0 and x >= -3 for x in diffs):
        return 1

    return 0


# Part 1
print(sum(check_report(r) for r in reports))

# Part 2
def check_report_options(report):
    options = [
      report[:i] + report[i+1:]
      for i in range(len(report))
    ]

    return any(check_report(option) for option in options)

print(sum(1 if check_report_options(r) else 0 for r in reports))
