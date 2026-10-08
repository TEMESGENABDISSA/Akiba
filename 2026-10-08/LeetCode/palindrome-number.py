class Solution:
    def isPalindrome(self, x):
        number = str(x)
        reverse = number[::-1]

        if number == reverse:
            return True
        else:
            return False