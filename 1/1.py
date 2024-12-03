f = open('1/input.txt', 'r')
input = f.readlines()

distance = 0
left_nums, right_nums = [], []

for line in input:
    left, right = line.split('   ')
    left_nums.append(int(left))
    right_nums.append(int(right))

left_nums, right_nums = sorted(left_nums), sorted(right_nums)

for i in range(len(left_nums)):
    distance += abs(left_nums[i] - right_nums[i])


print(distance)