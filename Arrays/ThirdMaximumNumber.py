#Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
#Example 1:
#Input: nums = [3,2,1]
#Output: 1
#Explanation:
#The first distinct maximum is 3.
#The second distinct maximum is 2.
#The third distinct maximum is 1.

#Example 2:
#Input: nums = [1,2]
#Output: 2
#Explanation:
#The first distinct maximum is 2.
#The second distinct maximum is 1.
#The third distinct maximum does not exist, so the maximum (2) is returned instead.

#Example 3:
#Input: nums = [2,2,3,1]
#Output: 1
#Explanation:
#The first distinct maximum is 3.
#The second distinct maximum is 2 (both 2's are counted together since they have the same value).
#The third distinct maximum is 1.
l = []
ln = []

n = int(input("Enter number of entries: "))

for i in range(n):
    num = int(input("Enter numbers: "))
    l.append(num)

for ele in l:
    if ele not in ln:
        ln.append(ele)

print("Unique list:", ln)

max1 = ln[0]
for e in ln:
    if e > max1:
        max1 = e

if len(ln) < 3:
    print("Answer:", max1)
else:
    max2 = None
    max3 = None

    for e in ln:
        if e != max1:
            if max2 is None or e > max2:
                max2 = e

    for e in ln:
        if e != max1 and e != max2:
            if max3 is None or e > max3:
                max3 = e

    print("Answer:", max3)

        
