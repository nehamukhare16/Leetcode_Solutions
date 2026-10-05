class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                # Start a new nested group
                stack.append(0)
            else:
                inner_score = stack.pop()

                if inner_score == 0:
                    # "()"
                    score = 1
                else:
                    # "(A)"
                    score = 2 * inner_score

                stack[-1] += score

        return stack[0]