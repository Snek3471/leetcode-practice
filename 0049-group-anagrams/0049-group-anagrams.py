class Solution(object):
    def groupAnagrams(self, strs):
        myhash = {}

        for s in strs:
            count = [0] * 26

            for c in s: 
                count[ord(c) - ord("a")] += 1

            if tuple(count) in myhash:
                myhash[tuple(count)].append(s)
            else:
                myhash[tuple(count)] = [s]

        return list(myhash.values())
        