# Majority Element I
# 1) By sorting
nums=[7, 0, 0, 1, 7, 7, 2, 7, 7]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
print(nums[len(nums)//2])

# Time complexity : O(n^2)
# Space complexity : O(1)

# 2) Using Dictionary 
nums2=[7, 0, 0, 1, 7, 7, 2, 7, 7]

d={}
for i in range(len(nums)):
    d[nums[i]]=1+d.get(nums[i],0)
max_value=0
max_key=nums[0]
for key,values in d.items():
    if values>max_value:
        max_key=key
        max_value=values
print(max_key)

# Time complexity ; O(n)
# Space complexity ; O(n)

