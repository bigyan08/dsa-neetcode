class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower()
        for ch in new_s:
            if not (ch.isalnum()):
                new_s = new_s.replace(ch,'')
        pal = new_s[::-1]
        return True if new_s==pal else False

        