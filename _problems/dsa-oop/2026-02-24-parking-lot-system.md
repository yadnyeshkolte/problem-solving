---
title: "Design a Parking Lot System"
difficulty: "Medium"
topics: ["Design", "OOP", "System Design"]
category: "DSA & OOP"
date: 2026-02-24
---

## Problem Description

Design an Object-Oriented system for a Parking Lot. 

Requirements:
1. The parking lot should have multiple levels.
2. Each level has a certain number of spots.
3. The parking lot can park different types of vehicles (Motorcycles, Cars, and Buses).
4. The parking lot has motorcycle spots, compact spots, and large spots.
5. A motorcycle can park in any spot.
6. A car can park in either a single compact spot or a single large spot.
7. A bus can park in five large spots that are consecutive and within the same row.

## Approach

This is a pure Object-Oriented Design problem. Core classes will include `Vehicle` (abstract), `Motorcycle`, `Car`, `Bus`, `ParkingSpot`, `Level`, and `ParkingLot`. Use Enums for `VehicleSize`.

## Solution

```java
// Add your implementation here...

public enum VehicleSize {
    Motorcycle,
    Compact,
    Large
}

public abstract class Vehicle {
    protected int spotsNeeded;
    protected VehicleSize size;
    protected String licensePlate;
    
    public int getSpotsNeeded() { return spotsNeeded; }
    public VehicleSize getSize() { return size; }
}

public class ParkingLot {
    // Implement levels and parking logic
}
```
