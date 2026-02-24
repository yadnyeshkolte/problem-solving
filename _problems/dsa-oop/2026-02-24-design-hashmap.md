---
title: "Design HashMap"
difficulty: "Easy"
topics: ["Design", "Array", "Hash Table", "OOP"]
category: "DSA & OOP"
date: 2026-02-24
time_complexity: "O(1) average"
space_complexity: "O(n)"
---

## Problem Description

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

*   `MyHashMap()` initializes the object with an empty map.
*   `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
*   `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
*   `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

## Approach

We can use an array of linked lists (chaining) to handle collisions. The OOP aspect focuses on creating standard node and bucket classes to separate concerns.

## Solution

```java
// Add your implementation here...
class MyHashMap {
    
    public MyHashMap() {
        
    }
    
    public void put(int key, int value) {
        
    }
    
    public int get(int key) {
        return -1;
    }
    
    public void remove(int key) {
        
    }
}
```
