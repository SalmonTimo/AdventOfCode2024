def main():
    with open('input.txt') as f:
        s = f.read()
    lines = s.split('\n')
    cnt = 0
    for line in lines:
        nums = [int(x) for x in line.split()]
        diffs = [(nums[i] - nums[i-1]) for i in range(1, len(nums))]
        if all(x > 0 and x <= 3 for x in diffs) or all(x < 0 and x >= -3 for x in diffs):
            cnt += 1

    return cnt

print(main())