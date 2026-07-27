#Given a binary array nums, return the maximum number of consecutive 1's in the array.

#Example 1:
#Input: nums = [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

#Example 2:
#Input: nums = [1,0,1,1,0,1]

l=[]
n=int(input("Enter no of entries:"))
for i in range(n):
    num=int(input("Enter the numbers"))
    l.append(num)
print("List:",l)
maxStreak=0
count=0
for i in range(len(l)):
    if l[i]==1:
        count+=1
    else:
        count=0
    if count>maxStreak:
        maxStreak=count
print("maxStreak:",maxStreak)
        
        
    
