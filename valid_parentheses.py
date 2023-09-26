class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_mapping = {')': '(', ']': '[', '}': '{'}
        for br in s:
            if br in bracket_mapping:
                top_element = stack.pop() if stack else '#'
                if bracket_mapping[br] != top_element:
                    return False
            else:
                stack.append(br)
        return not stack
    
def main():
    s = Solution()
    print(s.isValid('){'))

if __name__=='__main__':
    main()
        