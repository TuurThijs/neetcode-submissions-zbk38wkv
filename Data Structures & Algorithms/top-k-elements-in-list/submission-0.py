class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for number in nums:
            if number in dict.keys():
                dict[number] += 1
            else:
                dict[number] = 1
        bucket = [[]for _ in range(len(nums) + 1)]
        for key, value in dict.items():
            bucket[value].append(key)
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result

#dict{
#    1:"1"
#    2:"2"
#    3:"3"
#}
