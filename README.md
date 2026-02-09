# Two Sum II – Input Array Is Sorted

## 🧩 Problem Overview

You are given a **1-indexed** array of integers called `numbers` that is already sorted in **non-decreasing order**.

Your task is to find **two distinct elements** in the array such that their sum equals a given `target`.

### Requirements
- Return the **indices** of the two numbers as an array `[index1, index2]`
- Indices must satisfy:  
  `1 <= index1 < index2 <= numbers.length`
- You may not use the same element twice
- There is **exactly one valid solution**
- Your solution must use **constant extra space** (`O(1)`)

---

## ✅ Expected Output

Return an integer array of length `2` containing the indices (1-based) of the two numbers whose sum equals the target.

---

## 📌 Examples

### Example 1
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: 2 + 7 = 9


### Example 2
Input: numbers = [2, 3, 4], target = 6
Output: [1, 3]
Explanation: 2 + 4 = 6


### Example 3
Input: numbers = [-1, 0], target = -1
Output: [1, 2]
Explanation: -1 + 0 = -1


---

## 🔒 Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly **one solution**

---

## 🧠 Key Observations

- The array is already **sorted**
- Indices are **1-based**, not 0-based
- Only **constant extra space** is allowed
- The sorted nature of the array enables an efficient **two-pointer approach**

---

## 🎯 Goal

Implement an algorithm that:
- Runs efficiently
- Uses constant extra memory
- Correctly returns the two indices that sum to the target

---

## 🚀 Repository Purpose

This repository contains:
- A clean and optimal solution
- Logic that leverages the sorted array constraint
- An approach that satisfies all problem requirements
