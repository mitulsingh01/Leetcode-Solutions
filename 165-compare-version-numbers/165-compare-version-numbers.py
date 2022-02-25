class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            val1, val2 = 0, 0
            
            if i < len(v1):
                val1 = int(v1[i])
            else:
                val1 = 0
            
            if j < len(v2):
                val2 = int(v2[j])
            else:
                val2 = 0
                
            if val1 > val2:
                return 1
            elif  val1 < val2:
                return -1
            
            i += 1
            j += 1
            
        return 0