class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in "!.',;:?": 
            paragraph = paragraph.replace(i, ' ')
            
        dic, ans, ansCount = defaultdict(int), '', 0
        for word in paragraph.lower().split():
            if word in banned:
                continue
            dic[word] += 1
            if dic[word] > ansCount:
                ansCount = dic[word]
                res = word
        return res