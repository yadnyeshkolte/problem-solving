# DSA Tracker

A personal documentation site for Data Structures & Algorithms, built with Jekyll.

## Features
- **Dashboard**: Progress stats and contribution activity.
- **Problems List**: Searchable and filterable table of solved problems.
- **Dark Mode**: Built-in theme toggle.
- **Categories**: Filter by difficulty and topics.

## How to Add a New Problem

1. Create a new file in `_problems/` with the format `YYYY-MM-DD-problem-slug.md`.
2. Add the following frontmatter:

```yaml
---
title: "Problem Title"
problem_url: "https://leetcode.com/problems/..."
platform: "LeetCode" # LeetCode, HackerRank, NeetCode
difficulty: "Easy" # or Medium, Hard
topics: ["Array", "Two Pointers"]
date: 2026-01-23
time_complexity: "O(n)"
space_complexity: "O(1)"
---
```

`leetcode_url` is still supported for older entries, but new problems should use `problem_url`.

3. Add your content below (Description, Approach, Code).

## Local Development

1. Install Ruby and Jekyll.
2. Run `bundle install`.
3. Run `bundle exec jekyll serve`.
4. Open `http://localhost:4000`.

## Structure

- `_problems/`: Your problem documentation files.
- `_layouts/`: HTML templates.
- `assets/css/`: Styles.
- `assets/js/`: Logic for search and theme toggle.
