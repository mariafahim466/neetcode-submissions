class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {} 
        t_dict = {} 
        def add_to_dict(myDict: dict, s:str) -> dict: 
            for i in range(len(s)): 
                if s[i] in myDict: 
                    myDict[s[i]] += 1 
                else: 
                    myDict[s[i]] = 1 
            return myDict
        # for i in range(len(s)): 
        #     if s[i] in s_dict: 
        #         s_dict[s[i]] += 1 
        #     else: 
        #         s_dict[s[i]] = 1 
        
        # for i in range(len(t)): 
        #     if t[i] in t_dict: 
        #         t_dict[t[i]] += 1 
        #     else: 
        #         t_dict[t[i]] = 1 
        s_dict = add_to_dict(s_dict, s)
        t_dict = add_to_dict(t_dict, t)
        return s_dict == t_dict 
        

        
