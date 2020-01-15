# Add comments to file

class Solution:
    def reverse(self, x):
        y = 0
        if x >= 0:
            flag = 1
            y = int(str(x)[::-1]) * flag
        else:
            flag = -1
            y = int(str(abs(x))[::-1]) * flag

        if y > 2 ** 31 - 1 or y < -2 ** 31:
            return 0
        else:
            return y

    def PracticeNewBranch(self):
        pass

if __name__ =="__main__":
    x = 123
    y = Solution().reverse(x)
    print(y)
