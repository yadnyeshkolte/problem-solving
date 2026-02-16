---
title: "String Multiplication"
difficulty: "Easy"
topics: ["String", "Math", "Hash Map"]
category: "DSA"
date: 2026-02-16
source: "Raja Software Labs Question Test"
time_complexity: "O(n + m)"
space_complexity: "O(1)"
---

## Problem Description

Given two non-negative integers represented as strings, convert them to numbers and return their multiplication as a string.

**Example 1:**
```
Input: s1 = "2", s2 = "3"
Output: "6"
```

**Example 2:**
```
Input: s1 = "123", s2 = "456"
Output: "56088"
```

## Approach

Build a digit map from string digits (`"0"` to `"9"`) to integers. Convert each input string to its numeric value by traversing characters and updating value as `value * 10 + digit`.

Then multiply the two converted numbers and return the result as a string.

**Key Insights:**
1. A HashMap helps convert each character digit to integer
2. Parse the full string by place-value accumulation
3. Handle single-digit strings directly
4. Return multiplication as string

## Solution

```java
import java.util.HashMap;
class  Solution2{
    public static void main(String[] args){
        String s1 = "2";
        String s2 = "3";
        String s3 = "123";
        String s4 = "456";

        String result = returnMultiplication(s3,s4);
        System.out.println(result);
    }
    public static String returnMultiplication(String s1, String s2){
        HashMap<String, Integer> map = new HashMap<>();
        for(int i=0;i<=9;i++){
            String s =  i+"";
            map.put(s, i);
        }

        if(s1.length()==1 && s2.length()==1){
            return map.get(s1) * map.get(s2) + " ";
        }
        int len = s1.length();
        int number1 = map.get(s1.charAt(0)+"");
        int number2 = map.get(s2.charAt(0)+"");

        for(int i=1;i<len;i++){
            number1 = number1*10 + map.get(s1.charAt(i)+"");
            number2 = number2*10 + map.get(s2.charAt(i)+"");
        }

        System.out.println(number1+" "+number2);
        return number1*number2+" ";
    }
}
```

Time Complexity = `O(n + m)`
Space Complexity = `O(1)`
