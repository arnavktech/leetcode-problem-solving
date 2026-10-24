class Solution:
    def isPalindrome(self, text: str) -> bool:
        text = text.lower()
        text = "".join(filter(str.isalnum, text))
        #our two pointers
        i = 0
        j = len(text)-1
        # our loop
        while i < j:
            if text[i] == text[j]:
                i += 1
                j -= 1
            else:
                return False

        return True