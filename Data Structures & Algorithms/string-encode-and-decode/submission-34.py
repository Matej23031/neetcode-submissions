class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:

            lens = len(s)
            ans += str(lens) + "#" + s

        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        start = 1     
        add = True
        num = ""
        l = 0
        while l < len(s):
            if s[l] != "#":
                num += s[l]
                l += 1
            else:
                #print(num)
                num = int(num)
                member = s[l + 1:l + num + 1]
                print(member)
                l += num + 1
                num = ""
                
                ans.append(member)
                print("a")

        return ans