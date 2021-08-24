def calc(x):
  if '-' in x:
    nums = x.split('-')
    return int(nums[1]) - int(nums[0]) + 1
  else: return 1

problems = [calc(x) for x in input().split(';')]
print(sum(problems))
