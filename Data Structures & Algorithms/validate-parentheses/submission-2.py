class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        mapping = {')': '(', '}': '{', ']': '['}

        STACK = []

        for char in s :
            if char in mapping.values() :
                STACK.append(char)

            elif char in mapping :
                if not STACK or STACK[-1] != mapping[char] :
                    return False

                STACK.pop()

        return len(STACK) == 0
