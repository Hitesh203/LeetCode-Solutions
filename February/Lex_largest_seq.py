#1718. Construct the Lexicographically Largest Valid Sequence Feb-16/2025
class Solution:
    def constructDistancedSequence(self, n):
        size = 2 * n - 1
        res = [0] * size
        # count[i] represents how many times we still need to place i.
        # For 1, we only need to place it once; for others, twice.
        count = {i: 2 for i in range(1, n + 1)}
        count[1] = 1

        def backtrack(idx):
            # If we've reached the end of the array, we found a solution.
            if idx == size:
                return True

            # If this position is already filled, move to the next.
            if res[idx] != 0:
                return backtrack(idx + 1)

            # Try placing numbers from n down to 1 to get lexicographically largest order.
            for num in range(n, 0, -1):
                if count[num] > 0:
                    # For number 1, place it in this position.
                    if num == 1:
                        res[idx] = 1
                        count[1] -= 1
                        if backtrack(idx + 1):
                            return True
                        # Backtrack if needed.
                        res[idx] = 0
                        count[1] += 1
                    else:
                        # For numbers greater than 1, we need to place them twice.
                        # The second occurrence must be exactly num positions ahead.
                        second_idx = idx + num
                        if second_idx < size and res[second_idx] == 0:
                            res[idx] = num
                            res[second_idx] = num
                            count[num] -= 2
                            if backtrack(idx + 1):
                                return True
                            # Backtrack: remove both occurrences.
                            res[idx] = 0
                            res[second_idx] = 0
                            count[num] += 2
            return False

        backtrack(0)
        return res
