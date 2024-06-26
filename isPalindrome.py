class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        

        return x == reverted_number or x == reverted_number // 10


solution = Solution()


print(solution.isPalindrome(121))  
print(solution.isPalindrome(-121)) 
print(solution.isPalindrome(10))   
print(solution.isPalindrome(12321)) 
print(solution.isPalindrome(0))    
