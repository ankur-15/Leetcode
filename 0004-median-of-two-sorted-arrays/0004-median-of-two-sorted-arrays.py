class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        # Ensure nums1 is the shorter array to optimize binary search range
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        low, high = 0, m  # Binary search range for partition point i in nums1
        total_len = m + n
        
        # half_len represents the total number of elements in the left partition
        # For odd total_len, left partition has (total_len // 2) + 1 elements,
        # and the median is the largest element in this partition.
        # For even total_len, left partition has (total_len // 2) elements.
        # (total_len + 1) // 2 correctly gives the count for the left partition
        # which can contain the median itself if total_len is odd.
        half_len = (total_len + 1) // 2 

        while low <= high:
            i = (low + high) // 2  # Partition point for nums1
            j = half_len - i       # Corresponding partition point for nums2

            # Define the four critical elements that form the boundaries of the partitions
            # L1: element just before cut 'i' in nums1
            # R1: element just after cut 'i' in nums1
            # L2: element just before cut 'j' in nums2
            # R2: element just after cut 'j' in nums2

            # Handle edge cases where i or j are 0 (no left element) or m/n (no right element)
            L1 = nums1[i-1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < m else float('inf')

            L2 = nums2[j-1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < n else float('inf')

            # Check if the partition is valid
            if L1 <= R2 and L2 <= R1:
                # Correct partition found!
                if total_len % 2 == 1:
                    # If total length is odd, the median is the maximum of the left partition
                    return float(max(L1, L2))
                else:
                    # If total length is even, the median is the average of
                    # the maximum of the left partition and the minimum of the right partition
                    return float((max(L1, L2) + min(R1, R2)) / 2.0)
            elif L1 > R2:
                # L1 is too large, meaning the partition in nums1 is too far to the right.
                # We need to shift the partition in nums1 to the left.
                high = i - 1
            else: # L2 > R1
                # L2 is too large, meaning the partition in nums1 is too far to the left.
                # We need to shift the partition in nums1 to the right.
                low = i + 1

        # This line should ideally not be reached if the input arrays are valid.
        # It's a fallback for type hinting completeness.
        return 0.0