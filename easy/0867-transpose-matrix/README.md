# Transpose Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.



 
Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]


Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


 
Constraints:


	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 1000
	1 <= m * n <= 105
	-109 <= matrix[i][j] <= 109

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.9 MB (beats 45.01%)  
**Submitted:** 2026-06-29T16:43:27.967Z  

```py
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0]* ROWS for _ in range (COLS)]
        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/transpose-matrix/)