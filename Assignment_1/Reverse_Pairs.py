# Reverse Pairs
nums = [6, 4, 1, 2, 7]
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>2*nums[j]:
            count+=1
print(count)
# Time comp : O(n^2)
# Space comp : O(1)