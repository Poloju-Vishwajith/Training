# Rearrange Array Elements by Sign
nums = [2, 4, 5, -1, -3, -4]
neg=[]
pos=[]
for i in nums:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
res=[]
for i in range(len(pos)):
    res.append(pos[i])
    res.append(neg[i])
print(res)
# Time comp ; O(n)
# Space comp ; O(n)