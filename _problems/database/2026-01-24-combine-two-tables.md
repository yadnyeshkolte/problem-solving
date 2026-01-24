---
title: "Combine Two Tables"
leetcode_url: "https://leetcode.com/problems/combine-two-tables/"
difficulty: "Easy"
topics: ["Database", "SQL"]
category: "Database"
date: 2026-01-24
---

## Problem Description
Table: `Person`
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key column for this table.
```

Table: `Address`
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key column for this table.
```

Write a solution to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `PersonId` is not present in the `Address` table, report `null` instead.

## Solution

```sql
SELECT 
    firstName, 
    lastName, 
    city, 
    state
FROM Person
LEFT JOIN Address 
    ON Person.personId = Address.personId;
```
