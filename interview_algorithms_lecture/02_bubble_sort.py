"""
ALGORITHM 2: Bubble Sort
========================

HOW IT WORKS (in simple steps):
  1. Compare the first two elements.
  2. If the left one is bigger than the right one, SWAP them.
  3. Move one step right and repeat until the end of the list.
     After one full pass, the BIGGEST element has "bubbled up" to the end.
  4. Repeat passes over the list (each pass can ignore the already-sorted tail).
  5. Stop early if a full pass makes no swaps — the list is already sorted.

  Picture air bubbles rising in water: the biggest values slowly
  float to the top (end of the list).

  Time: O(n^2) — slow for big lists, but easy to understand.
  Space: O(1) — sorts in place, no extra memory.
"""

def bubble_sort(items):
    """Sort a list in place using the bubble sort algorithm."""
    n = len(items)

    for pass_num in range(n - 1):
        swapped = False                      # optimization: early exit

        # After each pass the last `pass_num` items are already sorted,
        # so we stop the inner loop earlier each time.
        for i in range(n - 1 - pass_num):
            if items[i] > items[i + 1]:      # out of order?
                items[i], items[i + 1] = items[i + 1], items[i]  # swap
                swapped = True

        if not swapped:                      # nothing moved -> sorted
            break

    return items


# ------------------ Demo with different data types ------------------

if __name__ == "__main__":
    # 1) Numbers
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("Before:", nums)
    print("After: ", bubble_sort(nums[:]))   # [:] passes a copy

    # 2) Strings (alphabetical order)
    fruits = ["mango", "apple", "banana", "cherry"]
    print("\nBefore:", fruits)
    print("After: ", bubble_sort(fruits[:]))

    # 3) Characters
    letters = list("devin")
    print("\nBefore:", letters)
    print("After: ", bubble_sort(letters[:]))

    # 4) Already sorted input — shows the early-exit optimization
    done = [1, 2, 3, 4, 5]
    print("\nAlready sorted:", bubble_sort(done[:]))

    # Interview tip: mention the `swapped` flag — it shows you thought
    # about optimization. Then mention merge sort / quicksort as O(n log n)
    # alternatives for large data.
