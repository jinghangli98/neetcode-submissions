class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        tmp = [0] * (m+n)
        for idx in range(m+n-1, -1, -1):
            # print(idx)
            # print(tmp)
            if m-1 < 0:
                tmp[idx] = nums2[n-1]
                n -= 1
            elif n-1 < 0:
                tmp[idx] = nums1[m-1]
                m -= 1

            elif nums2[n-1] < nums1[m-1]:
                tmp[idx] = nums1[m-1]
                m -= 1
            else:
                tmp[idx] = nums2[n-1]
                n -= 1
        
        nums1[:] = tmp

        