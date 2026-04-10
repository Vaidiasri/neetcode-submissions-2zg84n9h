class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for  num in nums:
            if num in dict:
                dict[num]=dict[num]+1
            else:
                dict[num]=1

        sorted_keys = sorted(dict, key=lambda x: dict[x], reverse=True)
        return sorted_keys[:k]