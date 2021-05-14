class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        data = []
        j = 0
        if len(nums) ==1:
            g = nums[0]
            k = 0
            if g !=0:
                while g>=1:
                    k+=1
                    g //=10  
                print(g)
            if k%2==0:
                return 1
            else:
                return 0
        else:
            for i in nums:
                k = 0
                if i !=0:
                    while i>=1:
                        k+=1
                        i=i/10  
                    data.append(k)
            for i in data:
                if i%2==0:
                    j+=1     
            return j 
