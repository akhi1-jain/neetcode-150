from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) ensures that if a key doesn't exist, 
        # it automatically creates an empty list [] for us.
        res = defaultdict(list)
        
        for s in strs:
            # Create a frequency array for characters 'a' through 'z'
            count = [0] * 26
            
            for c in s:
                # ord(c) - ord('a') maps 'a'->0, 'b'->1, ..., 'z'->25
                count[ord(c) - ord('a')] += 1
            
            # Convert list to tuple because lists cannot be dictionary keys (they are mutable)
            # Tuples are immutable and hashable, making them perfect keys.
            res[tuple(count)].append(s)
            
        return list(res.values())

# --- Local Testing ---
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {test_strs}")
    
    result = solution.groupAnagrams(test_strs)
    print(f"Output: {result}")