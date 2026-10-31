# Leaders in an Array
# Iteration met
nums = [1, 2, 5, 3, 1, 2]
res=[]
for i in range(len(nums)):
    a=0
    for j in range(i,len(nums)):
        if nums[i]<nums[j]:
            break
        if j==len(nums)-1:
            res.append(nums[i])
print(res)
# Time complexity : O(N^2)
# Space complexity : O(N)
