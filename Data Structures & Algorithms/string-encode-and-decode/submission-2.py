class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ""
        strings = ""
        for i in range(0,len(strs)):
            lengths += f"{len(strs[i])}"
            if i != len(strs) -1:
                lengths += ","
            strings += strs[i]
        
        new_word = "{" + lengths + "}"

        final = new_word + strings
        
        return final

    def decode(self, s: str) -> List[str]:
        last_index = s.find("}")
        metadata = s[1:last_index]
        if metadata == "":
            word_lengths = []
        else:
            word_lengths = metadata.split(",")

        remaining = s[last_index+1:]
        final_list = []
        print(word_lengths)
        for word_length in word_lengths:
            final_list.append(remaining[0:int(word_length)])
            remaining = remaining[int(word_length):]

        return final_list

