# LeetCode
> 
> Perform: **Nguyen Duc Thang**
> 
> Last update:**11/09/2021**
### Table of contents

[I. Description of the topic:](#I)  

[II. Solution:](#II) 

<a name = "I"></a>

# I. Description of the topic:
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

- You may assume that each input would have exactly one solution, and you may not use the same element twice.

- You can return the answer in any order.

<img src="Screenshot from 2021-11-09 17-33-15.png">

<a name = "II"></a>

# II. Solution:
## Solution 1:
------------------------Solution 1: O(N) -------------------
- You can dict == dictionary == map( inother language )
- dic = dict()
- All num in nums
- dic [n] = index
- dic = [all num in question]
- exp = [2, 7, 11, 15]
-        0, 1, 2, 3
- for num in nums
-     if x = target - num = 9 -2 = 7
-       if have in dic => return index_num, dic[x]
- First you will use dict (aka dictionary) to create dic (containing numbers from nums)
- The for loop will run num out of total nums
- For variable x = target - num value in the loop
- Then let the variable x run in the dict
- If variable x appears in dict we will return and return dict_num and index
-----------------------Solution 2: O(N)-------------------
- All num in nums
- dic [n] = index
- dic = [all num in question]
- exp = [2, 7, 11, 15]
-        0, 1, 2, 3
- with num in nums
-     if x = target - num = 9 -2 = 7
-         x = 9 - 7 = 2
-      if have in dic => return index_num, dic[x] = >
-      dic[n] = index_num
-      dic[2] =0
- The for loop will run num out of total nums
- For variable x = target - num value in the loop
- Then let the variable x run in the dict
- If we haven't created the original dic, we will start creating the dic and add the value nums which is the subtracted number in the variable x.
- Then we let the loop run again and continue to use x to compare.
- If variable x appears in dict we will return and return dict_num and index
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Summary
The above article only gives people based on the reference level, and the simulation is not highly accurate.

Surely the article has many shortcomings, hope you understand and send your comments to improve it.
My contact:

-Email: nguyenducthang.iy1908@gmail.com


Sincerely thank!


# LeetCode
