# Big-O Notation: How We Measure Algorithm Performance — Explained Simply

## The problem Big-O solves

"How fast is my code?" is a bad question — it depends on the computer, the
programming language, and the input. Big-O answers a better question:

> **"As the input grows, how does the work grow?"**

Big-O describes the *shape* of the growth, not exact seconds. It ignores
constants and small terms — `2n + 5` is just **O(n)**.

## The two things we measure

1. **Time complexity** — how many steps (operations) as input `n` grows.
2. **Space complexity** — how much extra memory the algorithm needs as `n` grows.

Both are written in Big-O.

## The common complexities, fastest to slowest

| Notation | Name | Grows like | Example from this lecture |
|---|---|---|---|
| **O(1)** | Constant | stays flat | dict/set lookup (`needed in seen` in Two Sum) |
| **O(log n)** | Logarithmic | halves each step | Binary Search |
| **O(n)** | Linear | one pass per item | Linear Search, palindrome two-pointers |
| **O(n log n)** | Linearithmic | efficient sorting | Merge sort, Python's `sorted()` |
| **O(n²)** | Quadratic | a loop inside a loop | Bubble Sort, brute-force Two Sum |
| **O(2ⁿ)** | Exponential | doubles each step | naive recursive Fibonacci |
| **O(n!)** | Factorial | permutations | brute-force traveling salesman |

## Analogy: how much work per new input

- **O(1)** — looking up a word in a dictionary by its page number: same effort no matter how thick the book.
- **O(log n)** — guessing a number between 1–100 by halving: ~7 guesses no matter what.
- **O(n)** — reading a book cover to cover: twice as many pages, twice as long.
- **O(n²)** — comparing every student with every other student: add one student, and you add n more comparisons.

## How big n matters

For `n = 1,000,000` items:

| Complexity | Rough steps |
|---|---|
| O(1) | 1 |
| O(log n) | ~20 |
| O(n) | 1,000,000 |
| O(n log n) | ~20,000,000 |
| O(n²) | 1,000,000,000,000 — **hours** |
| O(2ⁿ) | more than atoms in the universe — **never finishes** |

This is why "it works on my small test" proves nothing — always state the Big-O.

## How to figure out Big-O of your code

1. **Single loop over the data** → O(n)
2. **Loop inside a loop over the same data** → O(n²)
3. **Halving the data each step** → O(log n)
4. **Sequential pieces** → add them, keep only the biggest: O(n) + O(n²) = O(n²)
5. **Dict/set operations** (insert, lookup) → O(1) each
6. **Drop constants and lower terms**: O(3n + 10) → O(n); O(n² + n) → O(n²)

## Best / average / worst case

Interviewers usually want **worst case** unless they say otherwise:

- Linear search: worst O(n) — target is last or absent.
- Bubble sort: worst O(n²), but best O(n) with the early-exit flag.
- QuickSort: average O(n log n), worst O(n²) on bad pivots.

## Space complexity — the forgotten half

Extra memory the algorithm allocates:

| Algorithm | Space | Why |
|---|---|---|
| Bubble sort | O(1) | sorts in place |
| Two pointers | O(1) | just two index variables |
| Two Sum hash map | O(n) | the dict can hold n items |
| Recursive factorial | O(n) | n frames on the call stack |
| `text[::-1]` palindrome trick | O(n) | copies the whole string |

**Classic interview trade-off:** hash maps trade memory for speed (Two Sum: O(n) space buys O(n) time instead of O(n²)).

## Common interview questions on this topic

- *"What's the time complexity?"* — always be ready to answer for anything you write.
- *"Can you do it in better time if you allow more memory?"* → hash map pattern.
- *"Can you do it in O(1) space?"* → usually means: two pointers, sort in place, or iterate.
- *"Why not just measure with a stopwatch?"* → results depend on hardware and input; Big-O compares algorithms fairly.

## One-line summary for students

> **Time complexity = how the number of steps grows. Space complexity = how the extra memory grows. Big-O = the growth shape, worst case, constants dropped.**
