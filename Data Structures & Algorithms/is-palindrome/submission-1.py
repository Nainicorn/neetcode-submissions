class Solution:
    def isPalindrome(self, s: str) -> bool:
        # need to have this shortcut down
        clean_str = "".join(c for c in s if c.isalnum()).lower()
        rev_str = clean_str[::-1]
        if clean_str == rev_str:
            return True
        return False
        
        