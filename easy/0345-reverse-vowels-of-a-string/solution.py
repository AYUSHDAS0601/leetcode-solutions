class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u'}
        s.lower()
        l, r = 0 , len(s)-1
        while l>r:
            if s[l] not in vowels:
                left += 1
            elif s[r] not in vowels:
                right += 1
            else :
                s[l], s[r] = s[r], s[l]
                right += 1
                left += 1
        return ' '.join(s)
