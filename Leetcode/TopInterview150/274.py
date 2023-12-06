# 274. H-Index - Medium
# It's referred another code.
# I didn't get it even though searched about h-index a lot.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        idx = 0

        for idx, citation in enumerate(citations, start=1):
            if citation < idx:
                return idx - 1
        
        return idx