# Algorithm 4: Palindrome Check (Two Pointers) — Explained Simply

## The problem
Does a string read the same forwards and backwards? `"madam"` → yes, `"hello"` → no.

## The idea in one line
Put one pointer at each end and walk them toward the middle, comparing characters as you go.

## Analogy
Two people proofreading a page — one reads left-to-right, the other right-to-left. If every letter matches, it's a palindrome.

## Steps
1. `left = 0`, `right = len(text) - 1`.
2. While `left < right`:
   - If `text[left] != text[right]` → **not** a palindrome, return False.
   - Otherwise move inward: `left += 1`, `right -= 1`.
3. Loop ends → every pair matched → return True.

## Trace

`"madam"`: `(m,m)` ✓ → `(a,a)` ✓ → pointers cross → **True**
`"hello"`: `(h,o)` ✗ → **False** immediately

## Why two pointers (and not `text == text[::-1]`)?
The slice works in Python — say so! — but it copies the string: O(n) extra space. Two pointers use O(1) space and it's a reusable technique.

## Complexity
| | |
|---|---|
| Time | O(n) — each character visited at most once |
| Space | O(1) |

## The two-pointer technique (this is the real lesson)
Same pattern solves many interview problems:
- Reverse a list in place
- Remove duplicates from a sorted list
- Find pairs in a **sorted** array that sum to a target
- Move all zeros to the end

## Common follow-ups
- *"Ignore spaces, punctuation, and case?"* → skip non-alphanumeric characters and compare `.lower()` versions. (`"A man, a plan, a canal: Panama"` → True.) This is the most-asked variation.
- *"Empty string / single char?"* → both are palindromes; the loop simply never runs.
- *"Longest palindromic substring?"* → different problem: expand around centers, or dynamic programming. Know it exists even if you don't write it.

## Common mistakes
- Loop condition `left <= right` vs `left < right` — for palindrome both work, but `<=` does one redundant middle comparison.
- Forgetting to handle the ignore-case variation's pointer skipping inside the while loop (keep `left < right` checks inside the skip loops).

**Code:** `04_palindrome_two_pointers.py`
