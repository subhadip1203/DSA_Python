"""
Leetcode :  https://leetcode.com/problems/word-break/description/

Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""

#  youtube : https://www.youtube.com/watch?v=jiPwesyVw2w


class Solution:
    def wordBreak(self, s, wordDict):
        # Tracker will be used to determine if we have successfully created a string ending at tracker[index]
        # We initialize it to all False, then set the tracker[0] to True as a base case.
        dp = [True]+[False]*(len(s))

        wordDict = set(wordDict)

        # Outer loop will be ahead of inner loop at all times.
        for i in range(1, len(s)+1):

            # Inner loop will start at string[0] and increment up to 1 step less than i, 
            # checking each time to see if string[left:right] is in wordDict
            for j in range(i):
                word = s[j:i]
                if dp[j] and word in wordDict:
                    dp[i] = True
                    break
                
        return dp[-1]

s = "leetcode"
wordDict = ["leet","code"]
print(Solution().wordBreak(s,wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]
print(Solution().wordBreak(s,wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(Solution().wordBreak(s,wordDict))