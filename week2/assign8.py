def twoSum(nums, target):
    
    seen = {}  
    
    for i, num in enumerate(nums):
        needed = target - num
        
        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i

print(twoSum([2,7,11,15], 9))
