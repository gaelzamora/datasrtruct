def TwoSum(nums, target):
    if nums == None or len(nums) < 2: return None
    # [4,5,6,2,1,4] # 10
    hashMap = {}
    
    for i, n in enumerate(nums): #2 6
        diff = target - n #10-6 = 4
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i
        # 4 = 0
        # 5 = 1


print(TwoSum([4,5,6,2,1,4], 10))