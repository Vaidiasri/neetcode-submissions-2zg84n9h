class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for c in s1:
            if c in s1_count:
                s1_count[c] += 1
            else:
                s1_count[c] = 1

        window = {}
        left = 0

        for right in range(len(s2)):
            
            if s2[right] in window:
                window[s2[right]] += 1
            else:
                window[s2[right]] = 1

            
            if right - left + 1 > len(s1):
                if window[s2[left]] == 1:
                    del window[s2[left]]
                else:
                    window[s2[left]] -= 1
                left += 1

            
            if window == s1_count:
                return True

        return False