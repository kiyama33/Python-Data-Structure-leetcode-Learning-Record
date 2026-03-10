from typing import List
class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        if arrayA==[]:
            return []
        res=[]
        tmp=1
        for item in arrayA[1:]:
            tmp=tmp*item
        res.append(tmp)
        for index in range(1,len(arrayA),1):
            if arrayA[index]==0:
                tmp2=1
                for i in range(len(arrayA)):
                    if i!=index:
                        tmp2=tmp2*arrayA[i]
                res.append(tmp2)
            else:
                tmp = tmp*arrayA[index-1]//arrayA[index]
                res.append(tmp)
        return res
