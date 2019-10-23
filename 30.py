class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []

        reference, window = {},{}
        windowsize=0

        for word in words:
            reference[word] = reference.get(word,0)+1
            windowsize +=len(word)

        wordlen = len(words[0])
        start,end = 0, 0
        li = []
        counter = len(reference)
        if windowsize>len(s):
            return []

        for i in range(wordlen):
            start,end = i,i
            counter = len(reference)
            table = {}
            for word in words:
                table[word]=table.get(word,0)+1
            while end+wordlen-1 <len(s):
                cur = s[end:end+wordlen]
                if cur in table:
                    table[cur]-=1
                    if table[cur]==0:counter-=1
                end +=wordlen
                while counter==0:
                    if end-start == windowsize:
                        li.append(start)
                    first = s[start:start+wordlen]
                    if first in table:
                        table[first]+=1
                        if table[first]>0:counter+=1
                    start +=wordlen
        return li
                
