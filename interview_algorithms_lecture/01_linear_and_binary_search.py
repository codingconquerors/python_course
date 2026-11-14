"""
ALGORITHM 1: Linear Search and Binary Search
============================================

HOW LINEAR SEARCH WORKS (in simple steps):
  1. Start at the first element.
  2. Check it — is it the target?
  3. If yes, you're done. If no, move to the next element.
  4. Repeat until you find the target or run out of elements.

  Think of it like finding a name in an unsorted stack of papers:
  you flip through them one by one.

  Time: O(n) — in the worst case you look at every element.

HOW BINARY SEARCH WORKS (only works on SORTED data):
  1. Look at the MIDDLE element.
  2. If it's the target — done!
  3. If the target is smaller, throw away the RIGHT half.
  4. If the target is bigger, throw away the LEFT half.
  5. Repeat on the remaining half until you find it or nothing is left.

  Think of opening a dictionary to the middle to find a word —
  each step cuts the search space in half.

  Time: O(log n) — much faster on big lists.
  RULE: the list MUST be sorted first.
"""

# ------------------ Linear Search ------------------

def linear_search(items, target):
    """Check every element one by one. Works on ANY list."""
    for index, value in enumerate(items):
        if value == target:
            return index          # found it — return where
    return -1                     # not found


# ------------------ Binary Search ------------------

def binary_search(sorted_items, target):
    """Halve the search space each step. List MUST be sorted."""
    left = 0
    right = len(sorted_items) - 1

    while left <= right:
        mid = (left + right) // 2     # index of the middle element
        if sorted_items[mid] == target:
            return mid                # found it
        elif sorted_items[mid] < target:
            left = mid + 1            # target is in the right half
        else:
            right = mid - 1           # target is in the left half

    return -1                         # not found


# ------------------ Demo with different data types ------------------

if __name__ == "__main__":
    # 1) Searching numbers
    numbers = [4, 9, 15, 22, 31, 47, 53, 68, 79]
    print("Numbers:", numbers)
    print("Linear search for 31 ->", linear_search(numbers, 31))
    print("Binary search for 31 ->", binary_search(numbers, 31))
    print("Binary search for 50 ->", binary_search(numbers, 50))  # -1: not there

    # 2) Searching strings (also works — strings compare alphabetically)
    names = ["amit", "divya", "karan", "neha", "priya", "rohan"]
    print("\nNames:", names)
    print("Binary search for 'neha' ->", binary_search(names, "neha"))

    # 3) Searching tuples (sorted by first element works fine)
    students = [(1, "Asha"), (3, "Bilal"), (7, "Chen"), (9, "Dana")]
    print("\nStudents:", students)
    print("Linear search for (7, 'Chen') ->", linear_search(students, (7, "Chen")))

    # Interview tip: if the list is NOT sorted, binary search gives wrong
    # answers — always check/mention sorting first.
