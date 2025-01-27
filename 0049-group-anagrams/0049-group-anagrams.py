def createCounterDict(eachStr):
        tmp = dict()
        for e in tmp:
            if e not in tmp.keys():
                tmp[e] = 1
            else:
                tmp[e]+=1
        return tmp

class Solution:
    # def createCounterDict(eachStr):
    #     tmp = {}
    #     for e in tmp:
    #         if e not in tmp.keys():
    #             tmp[e] = 1
    #         else:
    #             tmp[e]+=1
    #     return tmp

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        def createCounterDict(eachStr):
            tmp = dict()
            # print()
            for e in eachStr:
                if e not in tmp.keys():
                    tmp[e] = 1
                else:
                    tmp[e]+=1
            # print(tmp, 'j')
            return tmp
        count_dict = []

        for eachStr in strs:
            count_eS = createCounterDict(eachStr)
            # print(count_eS)
            flag = 0
            for i in count_dict:
                # print(i)
                if i[0] == count_eS:
                    i[1].append(eachStr)
                    flag = 1
            if flag == 0 :
                count_dict.append( ([count_eS, [eachStr]]) )
        ans = []
        # return count_dict
        for i in count_dict:
            ans.append(i[1])
        return ans


