def main():
    with open('input.txt') as f:
        s = f.read()
    lines = s.split('\n')
    cnt = 0
    for line in lines:
        base_nums = [int(x) for x in line.split()]
        nums = base_nums
        for i in range(-1, len(base_nums)):
            if i > -1:
                nums = base_nums[:i] + base_nums[i+1:]
            diffs = [(nums[i] - nums[i-1]) for i in range(1, len(nums))]
            if all(x > 0 and x <= 3 for x in diffs) or all(x < 0 and x >= -3 for x in diffs):
                cnt += 1
                break

    return cnt

print(main())