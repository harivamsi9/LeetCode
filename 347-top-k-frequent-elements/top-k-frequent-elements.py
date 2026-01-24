class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        freq_map = defaultdict(list) # freq --> (unique) num mapping

        for ke,v in c.items():
            freq_map[v].append(ke)

        sorted_freq_map_keys = sorted(freq_map.keys(), reverse=True)
        
        # what we have conflicts i.e two or more nums have the same freq?
        # how do we return the top k here
        res = []
        for key in sorted_freq_map_keys:
            values = freq_map[key]
            print(f"values = {values}")
            
            if k-len(values) >= 0:
                res += values
                k = k-len(values)

            # if k>0:
            #     res += values[:k]

        return res



                


        