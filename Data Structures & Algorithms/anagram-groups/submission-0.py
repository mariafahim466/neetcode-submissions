class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

                # wanna sort each word use that as the key 
        # if its there, we add the og word to the list 
        # else create a new list w just that word 

        track = {} 
        for word in strs: 
            new = "".join(sorted(word))

            if new in track: 
                track[new].append(word)
            else: 
                track[new] = [word]

        final = [] 
        for k, v in track.items(): 
            final.append(v)

        return final 
        