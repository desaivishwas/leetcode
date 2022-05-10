class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(b) < len(a):
            a,b = b, a
            
        left, right = 0, len(a) - 1
        while True:
            idx = (left + right) // 2
            jdx = half - idx - 2
            
            a_left = a[idx] if idx >=0 else float("-infinity")
            b_left = b[jdx] if jdx >=0 else float("-infinity")
            a_right = a[idx + 1] if (idx + 1) < len(a) else float("infinity")
            b_right = b[jdx + 1] if (jdx + 1) < len(b) else float("infinity")
            
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                
            elif a_left > b_right:
                right = idx - 1
            else:
                left = idx + 1
                
        