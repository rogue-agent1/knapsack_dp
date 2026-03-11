#!/usr/bin/env python3
"""0/1 Knapsack — dynamic programming with item recovery."""
import sys

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
    # Recover items
    items = []; w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i-1); w -= weights[i-1]
    return dp[n][capacity], items[::-1]

if __name__ == "__main__":
    items = [("gold", 10, 60), ("silver", 20, 100), ("bronze", 30, 120), ("diamond", 5, 50), ("ruby", 15, 80)]
    names = [i[0] for i in items]
    weights = [i[1] for i in items]
    values = [i[2] for i in items]
    capacity = 50
    max_val, selected = knapsack(weights, values, capacity)
    print(f"Capacity: {capacity}")
    print(f"Items: {[(n, f'w={w}, v={v}') for n, w, v in items]}")
    print(f"\nSelected: {[names[i] for i in selected]}")
    print(f"Total weight: {sum(weights[i] for i in selected)}")
    print(f"Total value: {max_val}")
