def move_zeros(nums):
    pos_ins = 0

    for num in nums:
        if num != 0:
            nums[pos_ins] = num
            pos_ins += 1 


    while pos_ins < len(nums):
        nums[pos_ins] = 0
        pos_ins += 1

nums = [0,1,0,3,12]
move_zeros(nums)
print(nums)
