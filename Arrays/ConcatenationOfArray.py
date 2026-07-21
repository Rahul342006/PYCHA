#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#Specifically, ans is the concatenation of two nums arrays.
#Return the array ans.

#Example 1:
#Input: nums = [1,2,1]
#Output: [1,2,1,1,2,1]
#Explanation: The array ans is formed as follows:
#- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
#- ans = [1,2,1,1,2,1]

#Example 2:
#Input: nums = [1,3,2,1]
#Output: [1,3,2,1,1,3,2,1]
#Explanation: The array ans is formed as follows:
#- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
#- ans = [1,3,2,1,1,3,2,1]

orginal_list=[]
n=int(input("enter numbers to add in the list"))
for i in range(n):
    num=int(input("enter numbers"))
    orginal_list.append(num)
print("orginal list:",orginal_list)
temp=[]
for i in (orginal_list):
    temp.append(i)
new_list=orginal_list+temp
print("Concatenated list:",new_list)
    
