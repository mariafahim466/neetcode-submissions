class Solution:

    def encode(self, strs: List[str]) -> str:
        # go thru the list of strings 
        # for each string, get its length 
        final_string = ""
        char = '#'
        for string in strs: 
            length = len(string)
            length = str(length)
            final_string += length 
            final_string += char
            final_string += string
        
        # print(final_string)
        return final_string




    def decode(self, s: str) -> List[str]:
        # go thru the string, char by char 
        # first char tells us the length to grab
        # skip a char (#) and get the next length 

        # then read the next one for the length, and repeat 
        final_list = [] 
        i = 0 

        while i < len(s): 
            # first we wanna find where the # is and save the index

            # then grab everything before the # index we jsut saved 

            # so from i to j 

            j = s.index('#', i)
            # j is where our # lives, starting from index i 
            length_to_grab = int(s[i:j])
            # i to j cuz i is where we're at, then stop at 
            # where the # is (not inclusive)
            # in case the number is more than 1 digit 
            to_add = s[j+1: j+1+length_to_grab]

            final_list.append(to_add)
            i = length_to_grab + 1 + j
          

        print(final_list)
        return final_list









