f = open('1/input.txt', 'r')
input = f.readlines()

total_score = 0
left_nums, right_nums = [], []

for line in input:
    left, right = line.split('   ')
    left_nums.append(int(left))
    right_nums.append(int(right))

total_score = sum(num * right_nums.count(num) for num in left_nums)

print(total_score)