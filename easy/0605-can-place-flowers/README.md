# Can Place Flowers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 
Constraints:


	1 <= flowerbed.length <= 2 * 104
	flowerbed[i] is 0 or 1.
	There are no two adjacent flowers in flowerbed.
	0 <= n <= flowerbed.length

## Solution

**Language:** Python  
**Runtime:** 6 ms (beats 83.39%)  
**Memory:** 19.8 MB (beats 10.26%)  
**Submitted:** 2026-06-29T15:49:19.886Z  

```py
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) -1 ):
            if f[i-1] == 0 and  f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n-=1
        return n <= 0      
```

---

[View on LeetCode](https://leetcode.com/problems/can-place-flowers/)