class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for i in range(len(strs)):
            output.append(f'{len(strs[i])}#'+strs[i])
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        j = 0
        while j < len(s):
            i = s.find('#', j)
            length = int(s[j:i])
            output.append(s[i+1 : i+1+length])
            j = i + 1 + length
        return output
