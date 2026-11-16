class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

    
        if len(str1) < len(str2): 
            min_word = str1 
            max_word = str2 
            min_len = len(str1)
            max_len = len(str2)
        else: 
            min_word = str2 
            max_word = str1
            min_len = len(str2)
            max_len = len(str1)

        res = ""
        for i in range(min_len): 
            curr_len = i+1 

            if (min_len % curr_len == 0) and (max_len % curr_len == 0): 
                amnt1 = min_len // curr_len
                amnt2 = max_len // curr_len 
            
                sub = min_word[:curr_len]

                if sub * amnt1 == min_word and sub*amnt2 == max_word: 
                    res = sub




        return res