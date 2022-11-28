class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ws, we = 0, 1
        nw_set = set()
        nw_set.add(nums[ws])
        while(we < len(nums)):
            if(nums[we] in nw_set):
                if(we - ws <= k):
                    return True
                else:
                    we +=1
                    ws +=1
            else:
                nw_set.add(nums[we])
                if(we - ws >= k):
                    nw_set.remove(nums[ws])
                    ws += 1
                we += 1
        return False
                    
                    
                