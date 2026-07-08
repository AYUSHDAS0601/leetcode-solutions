# Reverse Vowels of a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:


Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".


Example 2:


Input: s = "leetcode"

Output: "leotcede"


 
Constraints:


	1 <= s.length <= 3 * 105
	s consist of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-07-08T17:17:38.217Z  

```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u', 'A', 'E', 
        l, r = 0 , len(s)-1
        while l<r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else :
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        'I', 'O', 'U'}
        s = list(s)
        return ''.join(s)

```

---

[View on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)