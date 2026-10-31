# Maximum Subarray Sum
nums = [2, 3, 5, -2, 7, -4]
maxi=nums[0]
l=0
r=l+1
while l<len(nums):
    s=0
    for i in range(l,r):
        s+=nums[i]
    if s>maxi:
        maxi=s
    r+=1
    if r>len(nums):
        l+=1
        r=l+1
print(maxi)