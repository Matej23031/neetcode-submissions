class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        left = 0 
        right = k
        if len(arr) < k:
            return -1 
        suma = sum(arr[left:right]) 
        if (suma//k) >= threshold:
            cnt += 1
        while right < len(arr):
            suma -= arr[left]
            suma += arr[right]
            left += 1 
            right += 1
            
            if (suma // k >= threshold):
                cnt += 1
        
        return cnt
            