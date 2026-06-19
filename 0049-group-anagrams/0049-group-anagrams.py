class Solution(object):
    def groupAnagrams(self, strs):
        myhash = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s: 
                count[ord(c) - ord("a")] += 1

            myhash[tuple(count)].append(s)

        return list(myhash.values())
        