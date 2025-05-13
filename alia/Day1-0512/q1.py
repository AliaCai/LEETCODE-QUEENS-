class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=s.lower().replace(" ","")
        lr=""
        for char in word:
            if(char.isalnum()):
                lr+=char
        size=len(lr)
        for i in range(0, size//2):
            if(lr[i]!=lr[size-1-i]):
                return False
        return True
        