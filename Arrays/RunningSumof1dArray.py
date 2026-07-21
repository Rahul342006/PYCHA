#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.
#Example 1:
#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

#Example 2:
#Input: nums = [1,1,1,1,1]
#Output: [1,2,3,4,5]
#Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

#Example 3:
#Input: nums = [3,1,2,10,1]
#Output: [3,4,6,16,17]

l=[]
n=int(input("enter numbers to add in list:"))
for i in range(n):
    num=int(input("enter num to add:"))
    l.append(num)
print("List:",l)
result=[]
summ=0
for i in l:
    summ+=i
    result.append(summ)
print("answer:",result)
    
