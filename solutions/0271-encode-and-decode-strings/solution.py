class Codec:
    delimiter = "å"
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        return self.delimiter.join(strs)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        str_list = s.split(self.delimiter)
        return str_list
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
