"""
ALGORITHM 5: Recursion (Factorial & Fibonacci)
=============================================

WHAT IS RECURSION: a function that calls itself to solve a smaller
version of the same problem.

EVERY recursive function needs TWO parts:
  1. BASE CASE — when to STOP (otherwise it runs forever!).
  2. RECURSIVE CASE — call itself on a smaller input.

HOW FACTORIAL WORKS (in simple steps):
  factorial(5) = 5 * factorial(4)
               = 5 * 4 * factorial(3)
               = 5 * 4 * 3 * 2 * factorial(1)
               = 5 * 4 * 3 * 2 * 1        <- base case stops the chain

HOW FIBONACCI WORKS:
  Each number is the sum of the previous two:
  fib(n) = fib(n-1) + fib(n-2), with fib(0)=0, fib(1)=1 as base cases.
  Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...

  Naive recursion is O(2^n) — very slow! We fix it with MEMOIZATION
  (remembering answers we've already computed), which is another
  classic interview topic.
"""

# ------------------ Factorial ------------------

def factorial(n):
    """n! = n * (n-1) * ... * 1"""
    if n <= 1:                    # BASE CASE: 0! = 1! = 1
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE: smaller input


# ------------------ Fibonacci (naive) ------------------

def fib_naive(n):
    """Correct but slow — recomputes the same values over and over."""
    if n <= 1:                    # base cases: fib(0)=0, fib(1)=1
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ------------------ Fibonacci (memoized) ------------------

def fib_memo(n, memo={}):
    """Cache results in a dict so each fib(k) is computed only once."""
    if n in memo:                 # already computed? return the saved answer
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ------------------ Fibonacci (iterative — the best answer) ------------------

def fib_iterative(n):
    """No recursion at all: O(n) time, O(1) space. Interviewers love
    when you offer this after the recursive version."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ------------------ Demo with different data types ------------------

if __name__ == "__main__":
    # 1) Factorial of small ints
    print("factorial(5) =", factorial(5))
    print("factorial(0) =", factorial(0))

    # 2) Fibonacci sequence as a list
    print("\nFirst 10 fibs:", [fib_iterative(i) for i in range(10)])

    # 3) Speed difference: naive recursion vs memoized
    import time
    n = 30
    t = time.time(); fib_naive(n); print(f"\nfib_naive({n})  :", round(time.time() - t, 3), "s")
    t = time.time(); fib_memo(n);  print(f"fib_memo({n})   :", round(time.time() - t, 6), "s")

    # 4) Recursion on a different data type: flatten a nested list
    def flatten(nested):
        """Flatten arbitrarily nested lists -> shows recursion beyond math."""
        result = []
        for item in nested:
            if isinstance(item, list):
                result.extend(flatten(item))   # recurse into the sublist
            else:
                result.append(item)
        return result

    print("\nflatten([[1, [2, 3]], [4, [5, [6]]]]) ->",
          flatten([[1, [2, 3]], [4, [5, [6]]]]))

    # Interview tip: ALWAYS state the base case first. Then explain
    # the call stack briefly — that proves you understand what's happening.
