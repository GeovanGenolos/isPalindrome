# isPalindrome
This is my code in solving a problem in LeetCode.

<sub> 

    class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative, it is not a palindrome.
        # If x is not zero but ends in 0, it is not a palindrome (e.g., 10, 100).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        
        # When the length is an odd number, we can get rid of the middle digit by reverted_number // 10
        # For example when the input is 12321, at the end of the while loop we get x = 12, reverted_number = 123,
        # since the middle digit doesn't matter in palindrome (it will always equal to itself), we can simply get rid of it.
        return x == reverted_number or x == reverted_number // 10

        # Creating an instance of the Solution class
        solution = Solution()

        # Testing the isPalindrome method
        print(solution.isPalindrome(121))  # Output: True
        print(solution.isPalindrome(-121)) # Output: False
        print(solution.isPalindrome(10))   # Output: False
        prit(solution.isPalindrome(12321)) # Output: True
        print(solution.isPalindrome(0))    # Output: True
        
</sub>
