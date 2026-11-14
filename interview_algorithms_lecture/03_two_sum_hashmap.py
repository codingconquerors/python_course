"""
ALGORITHM 3: Two Sum (using a Hash Map)
=======================================

PROBLEM: Given a list of numbers and a target, find two numbers that
add up to the target. Return their indexes.

HOW IT WORKS (in simple steps):
  1. Walk through the list once.
  2. For each number, ask: "what number do I NEED to pair with this one
     to reach the target?"  needed = target - current
  3. Check a dictionary (hash map): have I already SEEN that needed number?
     - YES -> return its index and the current index. Done!
     - NO  -> store the current number and its index in the dictionary,
              then keep walking.

  A dictionary lookup is O(1) — that's the whole trick. Instead of
  checking every pair (O(n^2)), we remember what we've seen.

  Time: O(n) — one pass through the list.
  Space: O(n) — the dictionary can hold up to n entries.
"""

def two_sum(numbers, target):
    """Return indexes of two numbers that add to target, or None."""
    seen = {}                                # number -> index where we saw it

    for index, num in enumerate(numbers):
        needed = target - num                # the partner we're looking for
        if needed in seen:
            return (seen[needed], index)     # found the pair!
        seen[num] = index                    # remember this number

    return None                              # no pair exists


# Bonus: the naive O(n^2) version interviewers ask about FIRST

def two_sum_brute_force(numbers, target):
    """Check every pair — slow but simple. Always mention this first,
    then improve to the hash map version."""
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None


# ------------------ Demo with different data types ------------------

if __name__ == "__main__":
    # 1) Positive integers
    nums = [2, 7, 11, 15]
    print("nums:", nums, "| target 9 ->", two_sum(nums, 9))   # (0, 1)

    # 2) Negatives and zero work the same way
    nums2 = [-3, 4, 0, 8, -1]
    print("nums:", nums2, "| target 7 ->", two_sum(nums2, 7)) # (3, 4): 8 + -1

    # 3) Floats
    prices = [1.5, 2.25, 0.75, 3.0]
    print("prices:", prices, "| target 3.75 ->", two_sum(prices, 3.75))

    # 4) No solution
    print("target 100 ->", two_sum([1, 2, 3], 100))           # None

    # Compare with brute force on a bigger list
    big = list(range(10000))
    import time
    t = time.time(); two_sum_brute_force(big, 19997); print("\nBrute force:", round(time.time() - t, 3), "s")
    t = time.time(); two_sum(big, 19997);             print("Hash map:   ", round(time.time() - t, 6), "s")
