---
title: "Design URL Shortener"
leetcode_url: "https://leetcode.com/discuss/interview-question/system-design/124658/Design-a-URL-Shortener"
difficulty: "Medium"
topics: ["System Design", "Scalability"]
category: "System Design"
date: 2026-01-24
---

## Problem Description
Design a URL shortening service like bit.ly or goo.gl.

## Requirements
*   Given a long URL, return a unique short URL.
*   When a user accesses the short URL, redirect them to the original long URL.
*   Users can optionally pick a custom alias for their URL.
*   Links expire after a standard default timespan (e.g., 5 years).

## High-Level Design

1.  **API Endpoints**:
    *   `POST /api/v1/data/shorten`: Takes `longUrl`, returns `shortUrl`.
    *   `GET /{shortUrl}`: Redirects to `longUrl`.

2.  **Database Schema**:
    *   **URLMapping Table**:
        *   `Hash` (PK): varchar(6-7)
        *   `OriginalURL`: varchar(2048)
        *   `CreationDate`: datetime
        *   `ExpirationDate`: datetime
        *   `UserID`: int (optional)

3.  **URL Encoding**:
    *   Use Base62 encoding ([a-z, A-Z, 0-9]) for the hash.
    *   A 7-character Base62 string offers ~3.5 trillion combinations ($62^7$).

4.  **Key Generation Service (KGS)**:
    *   To avoid collision checks on every insertion, pre-generate keys and store them in a separate DB or use a standalone service (KGS) to hand out unique keys.
