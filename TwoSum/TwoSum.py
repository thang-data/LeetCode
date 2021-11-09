"""
-----------------------Solution 1: O(N) -------------------
You can dict == dictionary == map( inother language )
dic = dict()
All num in nums
dic [n] = index
dic = [all num in question]
exp = [2, 7, 11, 15]
       0, 1, 2, 3
 for num in nums
    if x = target - num = 9 -2 = 7
      if have in dic => return index_num, dic[x]
-----------------------------------------------------------
enumrate(nums)
-----------------------Solution 2: O(N)-------------------
All num in nums
dic [n] = index
dic = [all num in question]
exp = [2, 7, 11, 15]
       0, 1, 2, 3
 with num in nums
    if x = target - num = 9 -2 = 7
        x = 9 - 7 = 2
      if have in dic => return index_num, dic[x] = >
      dic[n] = index_num
      dic[2] =0

"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List [int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i, num in enumerate(nums):  # enumerate: return index in array
            x = target - num
            if x in dic:
                return dic[x], i
            dic[num] = i

