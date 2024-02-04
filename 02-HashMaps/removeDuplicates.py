def removeDuplicates(nums):
        # [0,0,1,1,1,2,2,3,3,4]
        # [0, 1, 2, 3, 4]
        mapHash = {}
        # 0 0 / 1 0 / 1
        for i, num in enumerate(nums):
            
            if not num in mapHash:
                # 0 0 / 1 2 
                mapHash[num] = i
            # 0 1 1 1 2 2 3 3 4
            else:
                nums.pop(num)
        
        return nums

print(removeDuplicates([1,2,2,3,4,5,5]))

