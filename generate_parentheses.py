"""
    Given n pairs of parentheses, 
    write a function to generate all combinations of well-formed parentheses.
    Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    Example 2:

    Input: n = 1
    Output: ["()"]
 
"""

class Solution(object):
    def generateParenthesis(self, n):
        def generate(current, open_count, close_count):
            if len(current) == 2 * n:
                valid_combinations.append(current)
                return
            if open_count < n:
                generate(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                generate(current + ")", open_count, close_count + 1)

        if n == 0:
            return [""]
        valid_combinations = []
        generate("", 0, 0)
        return valid_combinations

def main():
    solution = Solution()
    n1 = 3
    result1 = solution.generateParenthesis(n1)
    expected1 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    print("Test Case 1:")
    print("Input:", n1)
    print("Output:", result1)
    print("Expected:", expected1)
    print("Pass? ", result1 == expected1)
    print()

    # Test case 2: n = 1
    n2 = 1
    result2 = solution.generateParenthesis(n2)
    expected2 = ["()"]
    print("Test Case 2:")
    print("Input:", n2)
    print("Output:", result2)
    print("Expected:", expected2)
    print("Pass? ", result2 == expected2)
    print()

    # Test case 3: n = 0 (edge case)
    n3 = 0
    result3 = solution.generateParenthesis(n3)
    expected3 = [""]
    print("Test Case 3:")
    print("Input:", n3)
    print("Output:", result3)
    print("Expected:", expected3)
    print("Pass? ", result3 == expected3)
    print()

    n4 = 4
    result4 = solution.generateParenthesis(n4)
    expected4 = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    print("Test Case 4:")
    print("Input:", n4)
    print("Output:", result4)
    print("Expected:", expected4)
    print(len(expected4),len(result4))
    print("Pass? ", result4 == expected4)
    print()
    
if __name__=='__main__':
    main()