# git demo
# add code to the file

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 12, 5]
    target = 9
    answer = Solution().twoSum(nums, target)
    print(answer)