class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            len_ = 1;
            flag = 1;
        else:
            len_ = 0;
            flag = 0;
        while flag:
            if len(nums)>len_:
                if nums[len_]==nums[len_-1]:
                    nums.pop(len_);
                else:
                    len_ += 1;
            else:
                flag = 0;

        return len_
        