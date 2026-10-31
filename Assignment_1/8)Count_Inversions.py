# Count Inversions

nums = [2, 3, 7, 1, 3, 5]
count=0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]>nums[j]:
            count+=1
print(count)
