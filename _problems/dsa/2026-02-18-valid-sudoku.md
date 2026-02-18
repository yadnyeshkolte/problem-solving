---
title: "Valid Sudoku"
leetcode_url: "https://neetcode.io/problems/valid-sudoku/question"
difficulty: "Medium"
topics: ["Array", "Hash Table", "Matrix"]
category: "DSA"
date: 2026-02-18
time_complexity: "O(n^2)"
space_complexity: "O(n^2)"
---

## Problem Description

You are given a `9 x 9` Sudoku board `board`. A Sudoku board is valid if the following rules are followed:

1.  Each row must contain the digits `1-9` without duplicates.
2.  Each column must contain the digits `1-9` without duplicates.
3.  Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without duplicates.

Return `true` if the Sudoku board is valid, otherwise return `false`.

Note: A board does not need to be full or be solvable to be valid.

**Example 1:**

```
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
```

**Example 2:**

```
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.
```

**Constraints:**

*   `board.length == 9`
*   `board[i].length == 9`
*   `board[i][j]` is a digit `1-9` or `'.'`.

## Approach

The approach involves validating the Sudoku board by checking three conditions:
1.  **Row Validation**: Ensure no digit `1-9` repeats in any row.
2.  **Column Validation**: Ensure no digit `1-9` repeats in any column.
3.  **Sub-box Validation**: Ensure no digit `1-9` repeats in any of the nine `3x3` sub-grids.

We can use `HashSet` to keep track of seen numbers for each row, column, and sub-box. If a duplicate is found, the board is invalid.

## Solution

```java
import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        int i=0;
        while(i<9){
            ArrayList<Character> arr = new ArrayList<>();
            HashSet<Character> ht = new HashSet<>();
            int j=0;
            while(j<9){
                if(board[i][j]!='.'){
                    arr.add(board[i][j]);
                    ht.add(board[i][j]);
                }
                j++;
            }
            if(arr.size()!=ht.size()){
                return false;
            }
            arr = new ArrayList<>();
            ht = new HashSet<>();
            int k=0;
            while(k<9){
                if(board[k][i]!='.'){
                    arr.add(board[k][i]);
                    ht.add(board[k][i]);
                }
                k++;
            }
            if(arr.size()!=ht.size()){
                return false;
            }
            i++;
        }
        for(i=0;i<9;i=i+3){
            for(int j=0;j<9;j=j+3){
                HashSet<Character> ht = new HashSet<>();
                for(int k=i;k<i+3;k++){
                    for(int m=j;m<j+3;m++){
                        if(board[k][m]!='.'){
                            if(!ht.add(board[k][m])){
                                return false;
                            }

                        }
                    }
                }
            }
        }
        return true;
    }
}
```
