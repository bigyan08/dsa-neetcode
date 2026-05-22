class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            if (''.join(sorted(word))) in hashmap.keys():
                hashmap[(''.join(sorted(word)))].append(word)
            else:
                hashmap.setdefault(''.join(sorted(word)),[word])
        output = []
        for key in hashmap.keys():
            output.append(hashmap[key])
        return output




        