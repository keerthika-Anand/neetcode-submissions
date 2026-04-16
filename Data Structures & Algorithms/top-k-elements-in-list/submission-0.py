class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # arr = []
        res = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            res.append(sorted_items[i][0])
        return res