class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ''
        for char in s:
            if char.isalnum():
                newStr += char

        if newStr.lower() == newStr[::-1].lower():
            return True


        return False

        