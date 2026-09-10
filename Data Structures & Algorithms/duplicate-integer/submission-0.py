class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        for num in nums:
            if num not in count:
                count[num]=0
            count[num]+=1

        max=0
        for num in nums:
            if max == 0 and count[num]==count[max]:
                return True
        return False
