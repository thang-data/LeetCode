# LeetCode
> 
> Perform: **Nguyen Duc Thang**
> 
> Last update:**11/12/2021**
### Table of contents

[I. Description of the topic:](#I)  

[II. Solution:](#II) 

<a name = "I"></a>

# I. Description of the topic:
- Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

- Return k after placing the final result in the first k slots of nums.

 - Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

- Custom Judge:

- The judge will test your solution with the following code:
[ int[] nums = [...]; // Input array
  int[] expectedNums = [...]; // The expected answer with correct length

  int k = removeDuplicates(nums); // Calls your implementation

  assert k == expectedNums.length;
  for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
} ]
- If all assertions pass, then your solution will be accepted.

- Example 1:

[ Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores). ]

- Example 2:
[ Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores). ]

- Constraints:

[]
<a name = "II"></a>

# II. Solution:
- We will review the first element in the array.
- If the array has that element, they use the "Remove" function in Python to remove that element and push the last element up.
- This happens continuously until the threshold i is no longer less than the length of the array.
- Finally we will return the reduced array.
## Summary
The above article only gives people based on the reference level, and the simulation is not highly accurate.

Surely the article has many shortcomings, hope you understand and send your comments to improve it.
My contact:

-Email: nguyenducthang.iy1908@gmail.com