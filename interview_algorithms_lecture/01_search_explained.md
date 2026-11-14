# Algorithm 1: Linear Search & Binary Search — Explained Simply

## The problem
You have a collection of items and a target. Is the target in the collection, and where?

## Linear Search

**The idea in one line:** check every item, one by one, until you find it.

**Analogy:** looking for a specific card in a shuffled deck — you flip cards one at a time.

### Steps
1. Start at index 0.
2. Compare the item to the target.
3. Match → return the index. No match → move to the next index.
4. Reach the end without a match → return "not found" (−1).

### Complexity
| | |
|---|---|
| Time | O(n) — worst case looks at all n items |
| Space | O(1) |
| Requires sorted data? | **No** — works on anything |

## Binary Search

**The idea in one line:** on a *sorted* list, always look at the middle and throw away the half that can't contain the answer.

**Analogy:** a phone book. To find "Priya" you open it near the middle — "Priya" is after "Mehta", so you ignore the left half completely.

### Steps
1. Set `left = 0`, `right = last index`.
2. Find the middle: `mid = (left + right) // 2`.
3. Compare `items[mid]` to the target:
   - Equal → done, return `mid`.
   - Target bigger → discard left half (`left = mid + 1`).
   - Target smaller → discard right half (`right = mid - 1`).
4. Repeat while `left <= right`. If the window closes → not found.

### Why it's fast
Each step **halves** the search space:
- 1,000 items → at most ~10 checks
- 1,000,000 items → at most ~20 checks

### Complexity
| | |
|---|---|
| Time | O(log n) |
| Space | O(1) iterative |
| Requires sorted data? | **YES — this is the catch** |

## Interview follow-ups to expect
- *"What if the list isn't sorted?"* → You must sort first (O(n log n)), which may erase the benefit — or just use linear search.
- *"Find the first/last occurrence with duplicates"* → keep searching the appropriate half after a match.
- *"What is `left <= right` vs `left < right`?"* → the `=` is required: a one-element window is still a candidate.

## Common mistakes
- Forgetting the data must be sorted.
- Infinite loop: updating `left = mid` instead of `mid + 1`.
- Integer overflow in other languages (`(left + right)` can overflow in C/Java — safe in Python).

**Code:** `01_linear_and_binary_search.py`
