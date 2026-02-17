---
title: "String Encode and Decode"
leetcode_url: "https://neetcode.io/problems/string-encode-and-decode/question"
difficulty: "Medium"
topics: ["String", "Design", "Array"]
category: "DSA"
date: 2026-02-17
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```cpp
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```

Machine 2 (receiver) has the function:

```cpp
vector<string> decode(string s) {
  //... your code
  return strs;
}
```

So Machine 1 does:

`string encoded_string = encode(strs);`

and Machine 2 does:

`vector<string> strs2 = decode(encoded_string);`

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: `dummy_input = ["Hello","World"]`

Output: `["Hello","World"]`

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:

Input: `dummy_input = [""]`

Output: `[""]`

Constraints:

*   0 <= strs.length < 100
*   0 <= strs[i].length < 200
*   strs[i] contains any possible characters out of 256 valid ASCII characters.

Follow up: Could you write a generalized algorithm to work on any possible set of characters?

## Approach

The approach uses a length-prefix encoding. For each string in the list, we append its length, followed by a delimiter (here, `#`), and then the string itself. When decoding, we read the characters until we encounter the delimiter `#`. The number preceding the delimiter tells us exactly how many characters to read for the current string. This method handles all edge cases, including strings that contain the delimiter itself, because we rely on the length prefix to know where the string ends.

## Solution

```java
class Solution {

    public String encode(List<String> strs) {
        StringBuilder str = new StringBuilder();
        for(String s: strs){
            str.append(s.length());
            str.append("#");
            str.append(s);
        }
        return str.toString();

    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();
        int i=0;

        while(i<str.length()){
            int j = i;
            while(str.charAt(j)!='#'){
                j++;
            }
            String strlength = str.substring(i,j);

            int length = Integer.parseInt(strlength);
            String word = str.substring(j+1,j+1+length);
            list.add(word);
            i = j+1+length;
        }
        return list;
    }
}
```
