# Algorithm 3: Two Sum — Explained Simply

## The problem (asked constantly in fresher interviews)
Given a list of numbers and a target, return the **indexes** of two numbers that add up to the target.

Example: `[2, 7, 11, 15]`, target `9` → indexes `(0, 1)` because `2 + 7 = 9`.

## The brute-force idea (mention this FIRST in interviews)
Check every pair: for each element, loop over all elements after it.
- Time: O(n²) — fine for small lists, terrible for big ones.
- Space: O(1).

## The hash-map idea (the answer they're waiting for)
**One line:** instead of searching for a partner, *remember* every number you've seen — then finding the partner is an instant dictionary lookup.

## Analogy
A coat-check ticket. When you meet each number, you note "if I ever need `target − this`, it lives at this index." One walk-through is enough.

## Steps
1. Create an empty dict: `seen = {}` (maps a number → the index where you saw it).
2. For each `num` at `index`:
   - Compute `needed = target − num`.
   - Is `needed` already in `seen`? → **yes**: return `(seen[needed], index)`. Done!
   - **No**: store `seen[num] = index` and continue.
3. Finish the loop with no match → no pair exists.

## Trace

`nums = [2, 7, 11, 15]`, target `9`

| index | num | needed | seen so far | action |
|---|---|---|---|---|
| 0 | 2 | 7 | {} | store `{2: 0}` |
| 1 | 7 | 2 | {2:0} | **2 is in seen → return (0, 1)** |

## Complexity
| | |
|---|---|
| Time | O(n) — one pass, O(1) dict lookups |
| Space | O(n) — the dict |

## Interview follow-ups to expect
- *"Return the values, not indexes?"* → same technique, store values in a set instead.
- *"Duplicates?"* → storing indexes handles `[3, 3]` target `6` correctly.
- *"Multiple pairs?"* → collect them instead of returning the first.
- *"What if you can't use extra memory?"* → sort + two pointers: O(n log n) time, O(1) space — but you lose original indexes.

## Why a dict?
`needed in seen` is O(1) for a dict/set but O(n) for a list — that single difference turns O(n²) into O(n).

**Code:** `03_two_sum_hashmap.py`
