# Algorithm 5: Recursion (Factorial & Fibonacci) — Explained Simply

## The idea in one line
A function that solves a problem by calling itself on a **smaller** version of the same problem.

## The two mandatory parts
Every recursive function needs both — missing either is a bug:

1. **Base case** — the smallest input, answered directly, which STOPS the chain.
2. **Recursive case** — call yourself on a smaller input that moves toward the base case.

## Analogy
Standing in a queue and asking "how many people are ahead of me?" Each person asks the person in front; the person at the front answers "zero" (base case), and the answers add up coming back.

## Example 1: Factorial

`factorial(n) = n × factorial(n-1)` with base case `factorial(0 or 1) = 1`.

Unrolling `factorial(4)`:

```
factorial(4) = 4 * factorial(3)
             = 4 * 3 * factorial(2)
             = 4 * 3 * 2 * factorial(1)
             = 4 * 3 * 2 * 1
             = 24
```

Calls go **down** the stack until the base case, then results multiply back **up**.

## Example 2: Fibonacci

Each number is the sum of the previous two: `0, 1, 1, 2, 3, 5, 8, 13, ...`

`fib(n) = fib(n-1) + fib(n-2)` with base cases `fib(0)=0`, `fib(1)=1`.

### The trap: naive recursion is exponential
`fib(5)` computes `fib(3)` twice, `fib(2)` three times... The call tree explodes → O(2ⁿ).

### Fix 1: Memoization
Store each computed `fib(k)` in a dict; never compute it twice → O(n).

### Fix 2: Iteration (best answer)
Two variables walking forward — O(n) time, O(1) space. Offer this after the recursive version.

## Complexity
| Version | Time | Space |
|---|---|---|
| Factorial recursion | O(n) | O(n) call stack |
| Fibonacci naive | O(2ⁿ) | O(n) stack depth |
| Fibonacci memoized | O(n) | O(n) dict + stack |
| Fibonacci iterative | O(n) | O(1) |

## Where recursion really shines
Math functions are just the teaching example — recursion is natural for:
- Trees (file folders, HTML DOM, org charts)
- Nested structures (flattening nested lists — see the code demo)
- Divide & conquer (binary search, merge sort)
- Backtracking (mazes, sudoku, permutations)

## Interview follow-ups to expect
- *"What happens without a base case?"* → infinite recursion → `RecursionError` (stack overflow).
- *"Why is naive fib slow?"* → draw the call tree; overlapping subproblems.
- *"How do you fix it?"* → memoization or iteration — this is the bridge to dynamic programming.
- *"Recursion vs iteration?"* → recursion is elegant but uses call-stack memory; iteration is cheaper.

## Common mistakes
- Base case that the input never reaches (e.g. wrong decrement).
- Modifying a default `memo={}` argument — works here, but explain it if asked (it's a shared mutable default — fine only because we always pass/keep it).
- Trying to recurse on huge n — Python's default recursion limit is ~1000.

**Code:** `05_recursion_fibonacci.py`
