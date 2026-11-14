"""
ALGORITHM 4: Palindrome Check (Two Pointers)
============================================

PROBLEM: Is a string the same forwards and backwards?
"madam" -> True, "hello" -> False.

HOW IT WORKS (in simple steps):
  1. Put one pointer (LEFT) at the start of the string.
  2. Put another pointer (RIGHT) at the end.
  3. Compare the two characters.
     - Different? Not a palindrome. Stop.
     - Same? Move LEFT one step right and RIGHT one step left.
  4. When the pointers meet or cross, every pair matched -> palindrome.

  Imagine two people reading a book from opposite ends — if every
  letter they read is the same, it's a palindrome.

  Time: O(n) — each character is visited at most once.
  Space: O(1) — no extra memory (better than reversing the string!).

THE TWO-POINTER TECHNIQUE also solves:
  - reversing a list in place
  - finding pairs in sorted arrays
  - removing duplicates
"""

def is_palindrome(text):
    """Two-pointer palindrome check on a string."""
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False                     # mismatch found
        left += 1                            # move inward
        right -= 1

    return True                              # all pairs matched


def is_palindrome_ignore_case(text):
    """Same idea, but skip spaces/punctuation and ignore letter case —
    a very common interview follow-up ('A man, a plan, a canal: Panama')."""
    left = 0
    right = len(text) - 1

    while left < right:
        while left < right and not text[left].isalnum():
            left += 1                        # skip non-letters on the left
        while left < right and not text[right].isalnum():
            right -= 1                       # skip non-letters on the right

        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1

    return True


# ------------------ Demo with different data types ------------------

if __name__ == "__main__":
    # 1) Strings
    for word in ["madam", "racecar", "hello", "a"]:
        print(f"{word!r:12} palindrome? {is_palindrome(word)}")

    # 2) Sentence with spaces and punctuation
    print("\n'A man, a plan, a canal: Panama' ->",
          is_palindrome_ignore_case("A man, a plan, a canal: Panama"))

    # 3) The same idea on a list of numbers
    def list_palindrome(lst):
        left, right = 0, len(lst) - 1
        while left < right:
            if lst[left] != lst[right]:
                return False
            left += 1
            right -= 1
        return True

    print("\n[1, 2, 3, 2, 1] ->", list_palindrome([1, 2, 3, 2, 1]))
    print("[1, 2, 3, 4, 5] ->", list_palindrome([1, 2, 3, 4, 5]))

    # Interview tip: the one-liner `text == text[::-1]` works in Python,
    # but interviewers want the two-pointer version — it shows technique.
