# Algorithm 2: Bubble Sort — Explained Simply

## The problem
Put a list in order (smallest → biggest).

## The idea in one line
Repeatedly compare neighbouring pairs and swap them if they're out of order — the biggest values "bubble up" to the end like air bubbles in water.

## Analogy
Lining students up by height: walk down the line, and whenever two neighbours are in the wrong order, swap them. After one pass, the tallest student is guaranteed to be at the end.

## Steps
1. **Pass 1:** compare elements at index 0 and 1; swap if the left is bigger. Then index 1 and 2, and so on to the end. → the largest element is now last.
2. **Pass 2:** repeat, but stop one earlier — the tail is already sorted. → second-largest lands in second-last.
3. Keep making passes. Each pass sorts one more element into the tail.
4. **Early exit:** if a whole pass makes zero swaps, the list is sorted — stop.

## Trace (small example)

`[5, 1, 4, 2]`

- Pass 1: `[1,5,4,2]` → `[1,4,5,2]` → `[1,4,2,5]` — **5** is fixed
- Pass 2: `[1,4,2,5]` → `[1,2,4,5]` — **4** is fixed
- Pass 3: no swaps → done

## Complexity
| | |
|---|---|
| Time (worst/average) | O(n²) |
| Time (best — already sorted) | O(n) thanks to the early exit |
| Space | O(1) — sorts in place |
| Stable? | Yes — equal elements keep their original order |

## Interview follow-ups to expect
- *"Why mention bubble sort at all?"* → it's the teaching baseline. Show you know the `swapped` flag optimization.
- *"What would you use for real data?"* → merge sort or quicksort: O(n log n). Python's built-in `sorted()` uses Timsort.
- *"When is O(n²) acceptable?"* → tiny lists, or nearly-sorted data (bubble sort's best case is good).

## Common mistakes
- Inner loop running to `n-1` every pass instead of `n-1-pass_num` (still correct, just wasted work).
- Forgetting the `swapped` early exit — interviewers specifically look for it.

**Code:** `02_bubble_sort.py`
