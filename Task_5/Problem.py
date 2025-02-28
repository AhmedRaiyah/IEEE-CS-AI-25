
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]: # this error is because I solved on Leetcode then copied to this file  
        minimum = 255
        maximum = 0
        mean = 0
        num_of_elements = 0 
        median = 0
        mode = 0
        max_count = 0
        
        for k in range(256):
            if count[k] > 0:
                minimum = min(minimum, k)
                maximum = max(maximum, k)
                mean += count[k] * k
                num_of_elements += count[k]
                if count[k] > max_count:
                    max_count = count[k]
                    mode = k
        
        mean /= num_of_elements

        if num_of_elements % 2:
            mid_idx = num_of_elements // 2 + 1
            temp = 0
            for x in range(256):
                temp += count[x]
                if temp >= mid_idx:
                    median = x
                    break
        else:
            mid_idx = num_of_elements // 2
            temp1 = 0
            temp2 = 0
            for x in range(256):
                temp1 += count[x]
                if temp1 == mid_idx and count[x] > 0:
                    temp2 = x
                elif temp1 > mid_idx:
                    if temp2 == 0:
                        temp2 = x
                    median = (temp2 + x) / 2
                    break
        
        return [minimum, maximum, mean, median, mode]
