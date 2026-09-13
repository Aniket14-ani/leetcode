
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        ones_img1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones_img2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        translation_counts = collections.defaultdict(int)
        
        for r1, c1 in ones_img1:
            for r2, c2 in ones_img2:

                translation_vec = (r2 - r1, c2 - c1)
                translation_counts[translation_vec] += 1
                
        return max(translation_counts.values()) if translation_counts else 0